# Advanced Veo 3.1 Workflows

This reference covers advanced techniques for complex video generation scenarios.

## Workflow 1: First and Last Frame Transitions

Create controlled camera movements or transformations between two distinct viewpoints.

**Use Cases:**
- 180-degree arc shots
- Reveal shots (close-up → wide shot)
- POV transitions
- Time transitions (day → night)

**Process:**
1. Generate or identify your starting frame image
2. Generate or identify your ending frame image
3. Use Veo 3.1's "First and Last Frame" feature
4. Describe the transition and audio in your prompt

**Example Prompt Structure:**
```
The camera performs a smooth [CAMERA MOVEMENT], starting with [DESCRIBE START] and [TRANSITION TYPE] to end on [DESCRIBE END]. [AUDIO DETAILS]
```

**Practical Example:**
Starting frame: Singer facing camera on dark stage
Ending frame: POV from behind singer looking at crowd
Prompt: `The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage. The singer sings "when you look me in the eyes, I can see a million stars."`

## Workflow 2: Ingredients to Video (Character Consistency)

Maintain consistent characters, objects, or styles across multiple shots using reference images.

**Use Cases:**
- Multi-shot dialogue scenes
- Character-driven narratives
- Brand consistency
- Location continuity

**Process:**
1. Generate reference images for:
   - Characters (consistent faces, clothing, appearance)
   - Settings (locations, environments)
   - Objects (props, vehicles, items)
   - Style references (aesthetic, mood)
2. Use "Ingredients to Video" feature with relevant references
3. Craft prompts that reference "the provided images"

**Prompt Template:**
```
Using the provided images for [CHARACTER/OBJECT/SETTING], create a [SHOT TYPE] of [SUBJECT] [ACTION]. [DIALOGUE/AUDIO]. [MOOD/STYLE]
```

**Example - Dialogue Scene:**
Reference images: Detective character, woman character, office setting

Shot 1: `Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, "Of all the offices in this town, you had to walk into mine."`

Shot 2: `Using the provided images for the detective, the woman, and the office setting, create a shot focusing on the woman. A slight, mysterious smile plays on her lips as she replies, "You were highly recommended."`

## Workflow 3: Timestamp Prompting (Multi-Shot Sequences)

Direct complete multi-shot sequences with precise cinematic pacing in a single generation.

**Use Cases:**
- Short scenes with multiple beats
- Action sequences
- Montages
- Reveal sequences

**Format:**
```
[START_TIME-END_TIME] [CINEMATOGRAPHY] [SUBJECT] [ACTION] [CONTEXT]. [AUDIO]. [EMOTION/STYLE]
```

**Time Segments:**
- 4-second videos: Use 1-2 second segments (e.g., [00:00-00:02], [00:02-00:04])
- 6-second videos: Use 2-second segments or mix (e.g., [00:00-00:02], [00:02-00:04], [00:04-00:06])
- 8-second videos: Use 2-second segments (e.g., [00:00-00:02], [00:02-00:04], [00:04-00:06], [00:06-00:08])

**Example - Adventure Discovery:**
```
[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a hidden path.
[00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of dense leaves, distant exotic bird calls.
[00:04-00:06] Tracking shot following the explorer as she steps into the clearing and runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and reverence.
[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in the center of the vast, forgotten temple complex, half-swallowed by the jungle. SFX: A swelling, gentle orchestral score begins to play.
```

## Workflow 4: Add/Remove Object

Modify generated videos by introducing new objects or removing existing ones.

**Important Notes:**
- Currently uses Veo 2 model (not Veo 3.1)
- Does NOT generate audio
- Best for object-level modifications, not major scene changes

**Use Cases:**
- Adding props to scenes
- Removing unwanted elements
- Product placement
- Scene refinement

**Process:**
1. Generate initial video with Veo 3.1
2. Use Add/Remove Object feature
3. Specify what to add or remove with clear descriptions

## Combining Workflows

Advanced creators can chain workflows for maximum control:

**Example: Multi-Shot Character Dialogue**
1. Use Gemini 2.5 Flash Image to generate character reference images
2. Use Ingredients to Video with timestamp prompting for each shot
3. Create 3-4 shots of the dialogue scene
4. Use First and Last Frame between shots if transitions are needed

**Example: Image Animation with Enhanced Audio**
1. Start with user's provided image
2. Analyze image to understand scene
3. Generate Veo 3.1 prompt with rich audio details
4. Use image-to-video feature with the enhanced prompt

## Best Practices for Advanced Workflows

**Do:**
- Plan your sequence before generating
- Keep reference images consistent in style
- Use timestamp prompting for complex pacing
- Leverage Gemini 2.5 Flash Image for reference generation
- Test individual shots before creating full sequences

**Don't:**
- Mix incompatible visual styles in reference images
- Over-complicate timestamp segments (keep each clear and focused)
- Ignore audio opportunities (Veo 3.1 excels at audio)
- Expect perfect continuity across many separate generations
- Use Add/Remove for major scene reconstruction
