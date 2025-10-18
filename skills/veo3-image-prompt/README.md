# Veo 3.1 Image-to-Prompt Skill - Usage Guide

## What This Skill Does

This skill enables Claude to analyze images and generate perfectly optimized prompts for Google's Veo 3.1 video generation model. It applies the official five-part prompting formula and cinematography best practices to create professional-quality video prompts.

## How to Use

1. **Upload your image** to Claude
2. **Ask Claude to generate a Veo 3.1 prompt** from it
3. **Receive a ready-to-use prompt** in a code block for easy copying

## Example Usage

**User:** "Can you create a Veo 3.1 prompt from this image of my dog playing in the park?"

**Claude will:**
1. Analyze the image (subject, setting, lighting, mood, potential actions)
2. Apply the five-part formula (Cinematography + Subject + Action + Context + Style & Ambiance)
3. Add appropriate audio elements (SFX, ambient noise)
4. Return a polished prompt in a code block

## What Makes This Skill Powerful

✅ **Applies official Veo 3.1 best practices** from Google's prompting guide
✅ **Uses professional cinematography terminology** (camera movements, shot types, lens characteristics)
✅ **Includes audio direction** (dialogue, SFX, ambient noise)
✅ **Optimized prompt structure** for best results
✅ **Returns plain text in code blocks** for easy copying

## Skill Features

### Core Capabilities
- Image analysis and interpretation
- Five-part prompt formula application
- Cinematography language integration
- Audio element generation
- Style and mood enhancement

### Reference Materials
- **advanced-workflows.md** - Complex techniques (first/last frame, ingredients to video, timestamp prompting)
- **cinematography.md** - Comprehensive reference of camera shots, angles, movements, and lighting terms

## What's Included in the Skill

```
veo3-image-prompt/
├── SKILL.md (main instructions)
└── references/
    ├── advanced-workflows.md (complex Veo 3.1 techniques)
    └── cinematography.md (complete cinematography reference)
```

## Installation

1. Download the `veo3-image-prompt.zip` file
2. In Claude, go to Settings → Skills
3. Click "Add Skill" and upload the zip file
4. The skill is now available for use!

## Example Outputs

### Simple Animation
**Input:** Beach sunset photo
**Output:**
```
Wide shot, gentle waves rolling onto a sandy beach at sunset, with the tide slowly advancing up the shore. The sky is painted in warm oranges and pinks reflecting on the wet sand. SFX: soft waves lapping, distant seagulls. Peaceful, tranquil mood with golden hour lighting, cinematic.
```

### Character Focus
**Input:** Portrait of person
**Output:**
```
Medium close-up with shallow depth of field, a young man with thoughtful expression, turning his head slowly toward the camera with a subtle smile beginning to form. Natural outdoor setting with trees blurred in background. Soft afternoon light filtering through leaves. Warm, intimate mood, shot on 35mm film.
```

### Action Scene
**Input:** Skateboarder photo
**Output:**
```
Tracking shot following a skateboarder as they push off and glide down an empty street, performing a smooth kickflip. Urban environment with colorful graffiti walls and afternoon shadows. SFX: wheels rolling on pavement, the snap of the board. Energetic, youthful vibe with high contrast and saturated colors.
```

## Tips for Best Results

1. **Provide clear images** - Better image quality = better prompt analysis
2. **Specify your intent** - Tell Claude if you want specific movements or moods
3. **Request audio elements** - Ask for dialogue, SFX, or ambient noise if desired
4. **Use advanced features** - Reference first/last frame or timestamp prompting for complex scenes

## Support & Documentation

For more information about Veo 3.1 capabilities, see:
- Official prompting guide: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Vertex AI documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation

---

**Created with the official Google Veo 3.1 prompting guide**
