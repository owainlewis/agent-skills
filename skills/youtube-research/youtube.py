#!/usr/bin/env python3
# /// script
# dependencies = [
#   "google-api-python-client>=2.150.0",
#   "python-dotenv>=1.0.0",
# ]
# ///
"""
YouTube Research Tool - Search videos and analyze creators.

Usage:
    uv run youtube.py search "AI agents" --max 10
    uv run youtube.py search "AI agents" --max 10 --days 30
    uv run youtube.py search "AI agents" --order view_count
    uv run youtube.py creator @mkbhd --days 90
    uv run youtube.py creator @mkbhd --max 20

Environment:
    YOUTUBE_API_KEY - Required. Get one at https://console.cloud.google.com
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Video:
    video_id: str
    title: str
    url: str
    channel_name: str
    published_at: str
    view_count: int
    like_count: int
    comment_count: int
    engagement_rate: float
    views_per_day: float
    outlier_score: float | None = None
    tags: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# YouTube client
# ---------------------------------------------------------------------------

class YouTube:
    def __init__(self, api_key: str):
        self.yt = build("youtube", "v3", developerKey=api_key)

    # -- public methods -----------------------------------------------------

    def search(
        self,
        query: str,
        max_results: int = 10,
        days_back: int | None = None,
        order_by: str = "relevance",
    ) -> dict:
        """Search for videos on a topic. Returns videos with stats."""
        order_map = {
            "relevance": "relevance",
            "view_count": "viewCount",
            "date": "date",
        }
        params: dict = {
            "part": "id",
            "q": query,
            "type": "video",
            "order": order_map.get(order_by, "relevance"),
            "maxResults": min(max_results, 50),
        }
        if days_back is not None:
            after = datetime.now(timezone.utc) - timedelta(days=days_back)
            params["publishedAfter"] = after.isoformat()

        resp = self.yt.search().list(**params).execute()
        video_ids = [item["id"]["videoId"] for item in resp.get("items", [])]

        if not video_ids:
            return {"query": query, "total": 0, "videos": []}

        videos = self._get_video_details(video_ids)
        avg_views = statistics.mean([v.view_count for v in videos]) if videos else 0

        return {
            "query": query,
            "total": len(videos),
            "avg_views": round(avg_views),
            "videos": [asdict(v) for v in videos],
        }

    def creator(
        self,
        handle: str,
        max_results: int = 15,
        days_back: int = 90,
    ) -> dict:
        """Get a creator's recent videos with outlier analysis."""
        channel_id = self._resolve_handle(handle)
        if channel_id is None:
            return {"error": f"Channel not found: {handle}"}

        # Get channel info
        ch = self.yt.channels().list(part="snippet,statistics", id=channel_id).execute()
        if not ch.get("items"):
            return {"error": f"Channel not found: {handle}"}

        ch_item = ch["items"][0]
        channel_name = ch_item["snippet"]["title"]
        subs = int(ch_item["statistics"].get("subscriberCount", 0))

        # Get recent videos
        after = datetime.now(timezone.utc) - timedelta(days=days_back)
        search_resp = (
            self.yt.search()
            .list(
                part="id",
                channelId=channel_id,
                type="video",
                order="date",
                publishedAfter=after.isoformat(),
                maxResults=min(max_results, 50),
            )
            .execute()
        )
        video_ids = [item["id"]["videoId"] for item in search_resp.get("items", [])]

        if not video_ids:
            return {
                "channel": channel_name,
                "subscribers": subs,
                "period_days": days_back,
                "total": 0,
                "videos": [],
            }

        videos = self._get_video_details(video_ids)
        view_counts = [v.view_count for v in videos]
        avg = statistics.mean(view_counts)
        std = statistics.stdev(view_counts) if len(view_counts) > 1 else 0

        for v in videos:
            v.outlier_score = round((v.view_count - avg) / std, 2) if std > 0 else 0.0

        videos.sort(key=lambda v: v.outlier_score or 0, reverse=True)

        return {
            "channel": channel_name,
            "subscribers": subs,
            "period_days": days_back,
            "total": len(videos),
            "avg_views": round(avg),
            "videos": [asdict(v) for v in videos],
        }

    # -- private helpers ----------------------------------------------------

    def _resolve_handle(self, handle: str) -> str | None:
        """Turn a @handle into a channel ID."""
        if not handle.startswith("@"):
            handle = f"@{handle}"
        resp = (
            self.yt.search()
            .list(part="snippet", q=handle, type="channel", maxResults=1)
            .execute()
        )
        items = resp.get("items", [])
        return items[0]["snippet"]["channelId"] if items else None

    def _get_video_details(self, video_ids: list[str]) -> list[Video]:
        """Fetch full stats for a list of video IDs."""
        resp = (
            self.yt.videos()
            .list(part="snippet,statistics", id=",".join(video_ids))
            .execute()
        )
        now = datetime.now(timezone.utc)
        videos = []

        for item in resp.get("items", []):
            snippet = item["snippet"]
            stats = item["statistics"]

            views = int(stats.get("viewCount", 0))
            likes = int(stats.get("likeCount", 0))
            comments = int(stats.get("commentCount", 0))

            published = datetime.fromisoformat(
                snippet["publishedAt"].replace("Z", "+00:00")
            )
            days_live = max((now - published).days, 1)
            engagement = round((likes + comments) / views * 100, 2) if views > 0 else 0

            videos.append(
                Video(
                    video_id=item["id"],
                    title=snippet["title"],
                    url=f"https://youtube.com/watch?v={item['id']}",
                    channel_name=snippet["channelTitle"],
                    published_at=snippet["publishedAt"],
                    view_count=views,
                    like_count=likes,
                    comment_count=comments,
                    engagement_rate=engagement,
                    views_per_day=round(views / days_live, 1),
                    tags=snippet.get("tags", []),
                )
            )

        return videos


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("Error: YOUTUBE_API_KEY environment variable is required.", file=sys.stderr)
        print("Get one at https://console.cloud.google.com", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description="YouTube Research Tool")
    sub = parser.add_subparsers(dest="command", required=True)

    # search command
    p_search = sub.add_parser("search", help="Search for videos on a topic")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--max", type=int, default=10, help="Max results (default: 10)")
    p_search.add_argument("--days", type=int, default=None, help="Only videos from last N days")
    p_search.add_argument(
        "--order", choices=["relevance", "view_count", "date"], default="relevance"
    )

    # creator command
    p_creator = sub.add_parser("creator", help="Get a creator's recent videos")
    p_creator.add_argument("handle", help="Channel @handle (e.g. @mkbhd)")
    p_creator.add_argument("--max", type=int, default=15, help="Max results (default: 15)")
    p_creator.add_argument("--days", type=int, default=90, help="Look back N days (default: 90)")

    args = parser.parse_args()
    yt = YouTube(api_key)

    if args.command == "search":
        result = yt.search(args.query, max_results=args.max, days_back=args.days, order_by=args.order)
    elif args.command == "creator":
        result = yt.creator(args.handle, max_results=args.max, days_back=args.days)
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
