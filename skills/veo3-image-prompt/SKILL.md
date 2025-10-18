---
name: veo3-image-prompt
description: Analyzes images and generates optimized prompts for Google's Veo 3.1 video generation model. Use when users provide an image and want to animate it or create a video prompt from it. Applies Veo 3.1's five-part formula (Cinematography + Subject + Action + Context + Style & Ambiance) and best practices from the official prompting guide.
---

# Veo 3.1 Image-to-Prompt Generator

Generate perfect Veo 3.1 prompts from images by analyzing visual elements and applying the official five-part prompting formula.

## Core Process

When a user provides an image for Veo 3.1 prompt generation:

1. **Analyze the image** thoroughly, identifying:
   - Main subjects and characters
   - Environment and setting
   - Visual style and aesthetic
   - Lighting and mood
   - Compositional elements
   - Potential actions or movements

2. **Apply the five-part formula** to structure the prompt:
   - **[Cinematography]**: Camera work and shot composition
   - **[Subject]**: Main character or focal point
   - **[Action]**: What the subject should do
   - **[Context]**: Environment and background
   - **[Style & Ambiance]**: Aesthetic, mood, lighting

3. **Enhance with cinematic techniques**:
   - Specify appropriate camera movements
   - Define shot composition (wide, close-up, etc.)
   - Include lens and focus details when relevant
   - Add audio direction (dialogue, SFX, ambient noise)

4. **Return as plain text in a code block** for easy copying

## Cinematography Language

Use precise cinematography terms to control tone and emotion:

**Camera Movement:**
- Dolly shot, tracking shot, crane shot, aerial view
- Slow pan, POV shot, handheld, Steadicam
- Push in, pull out, orbit, arc shot

**Composition:**
- Wide shot, medium shot, close-up, extreme close-up
- Low angle, high angle, eye level, Dutch angle
- Two-shot, over-the-shoulder, establishing shot

**Lens & Focus:**
- Shallow depth of field, deep focus
- Wide-angle lens, telephoto lens, macro lens
- Soft focus, rack focus, tilt-shift

## Audio Direction

Veo 3.1 generates audio based on text instructions:

**Dialogue:**
- Use quotation marks: `The woman says, "I've been waiting for this moment."`
- Specify tone: `in a whisper`, `shouting excitedly`, `in a weary voice`

**Sound Effects (SFX):**
- Be specific: `SFX: thunder cracks in the distance`
- Timing matters: `SFX: footsteps echo on wet pavement`

**Ambient Noise:**
- Set the soundscape: `Ambient noise: bustling city traffic and distant sirens`
- Match the environment: `Ambient noise: gentle waves and seagulls`

## Style & Mood Guidance

**Visual Styles:**
- Film-specific: `shot on 35mm film`, `8mm home video aesthetic`, `Super 8 grain`
- Era-specific: `1980s aesthetic`, `noir style`, `vintage Polaroid look`
- Genre-specific: `cyberpunk`, `epic fantasy style`, `documentary style`

**Mood & Lighting:**
- Emotional tone: `melancholic`, `joyful`, `tense`, `serene`
- Lighting quality: `golden hour light`, `harsh fluorescent`, `soft morning light`
- Color grading: `cool blue tones`, `warm sepia`, `high contrast`

## Output Format

Always return the prompt as plain text inside a code block for easy copying:

```
[Your generated Veo 3.1 prompt here]
```

## Best Practices

**DO:**
- Keep prompts concise but descriptive (2-4 sentences typical)
- Lead with cinematography for strongest control
- Specify what subjects ARE doing, not what they're NOT doing
- Use quotation marks for specific dialogue
- Include audio elements (dialogue, SFX, ambient) when appropriate
- Match camera movement to the intended emotion

**DON'T:**
- Use negative prompts (instead describe what IS present)
- Over-specify every detail (trust the model's understanding)
- Ignore the image's existing composition and lighting
- Forget to specify aspect ratio if it matters (16:9 or 9:16)

## Example Transformations

**Image Analysis:** Photo of a woman looking out a rainy window
**Generated Prompt:**
```
Close-up with shallow depth of field, a young woman's face, gazing pensively out a rain-streaked window with city lights blurred in the background, inside a dimly lit apartment at night. Her reflection is faintly visible on the glass. SFX: soft rain pattering on the window. Melancholic mood with cool blue tones, cinematic.
```

**Image Analysis:** Mountain landscape at sunrise
**Generated Prompt:**
```
Crane shot starting low on a lone hiker standing at the mountain summit and ascending high above, revealing a vast range of misty peaks bathed in golden sunrise light. The hiker raises their arms in triumph. SFX: wind whistling across the peaks. Epic, inspirational mood with warm morning light.
```

## Advanced Features

When users need more complex control, reference these Veo 3.1 capabilities:

- **First and Last Frame**: Create transitions between two images
- **Ingredients to Video**: Maintain consistency with reference images
- **Timestamp Prompting**: Multi-shot sequences (e.g., `[00:00-00:02] ...`)
- **Add/Remove Object**: Modify generated videos (note: uses Veo 2, no audio)

For detailed guidance on these workflows, see references/advanced-workflows.md.
