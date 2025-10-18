---
name: veo3-prompts
description: Creates effective prompts for Google's Veo 3.1 video generation model on Vertex AI. Use when generating video prompts, animating images, creating dialogue scenes, specifying cinematography, or crafting complex multi-shot sequences with audio. Supports text-to-video, image-to-video, and advanced workflows.
---

# Veo 3.1 Video Prompt Creator

Generate professional video prompts for Google's Veo 3.1 model using the official prompting framework. This skill covers the full range of Veo 3.1 capabilities including high-fidelity video with synchronized audio, image-to-video animation, consistent character generation, and advanced multi-shot workflows.

## Veo 3.1 Model Capabilities

**Core generation features:**
- **Resolution**: 720p or 1080p high-fidelity video
- **Aspect ratios**: 16:9 (widescreen) or 9:16 (portrait)
- **Clip length**: 4, 6, or 8 seconds
- **Audio**: Rich audio and dialogue generation with realistic sound effects and multi-person conversations
- **Scene understanding**: Deep narrative structure comprehension and cinematic style adherence

**Advanced creative controls:**
- **Image-to-video**: Animate source images with enhanced prompt adherence and audio-visual quality
- **Ingredients to video**: Use reference images for consistent characters, objects, or styles across shots (with audio)
- **First and last frame**: Generate seamless video transitions between two images with audio
- **Add/remove object**: Modify generated videos by introducing or removing objects
- **Timestamp prompting**: Direct multi-shot sequences with precise timing within a single generation

## The Five-Part Prompt Formula

Use this structured formula for consistent, high-quality results:

**[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]**

1. **Cinematography**: Define camera work and shot composition
2. **Subject**: Identify the main character or focal point
3. **Action**: Describe what the subject is doing
4. **Context**: Detail the environment and background elements
5. **Style & ambiance**: Specify overall aesthetic, mood, and lighting

**Example**: Medium shot, a tired corporate worker, rubbing his temples in exhaustion, in front of a bulky 1980s computer in a cluttered office late at night. The scene is lit by the harsh fluorescent overhead lights and the green glow of the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly grainy.

## Cinematography: The Language of the Camera

The cinematography element is your most powerful tool for conveying tone and emotion.

### Camera Movement

**Key movements:**
- **Dolly shot**: Camera moves toward or away from subject on tracks
- **Tracking shot**: Camera follows subject's movement laterally
- **Crane shot**: Vertical camera movement, ascending or descending
- **Aerial view**: Bird's eye view from above
- **POV shot**: Point-of-view from a character's perspective
- **Slow pan**: Horizontal rotation of camera
- **Orbit shot**: Camera circles around subject
- **Dolly in**: Camera moves closer to subject
- **Tracking drone view**: Aerial tracking movement

**Example - Crane shot**: Crane shot starting low on a lone hiker and ascending high above, revealing they are standing on the edge of a colossal, mist-filled canyon at sunrise, epic fantasy style, awe-inspiring, soft morning light.

### Composition

**Shot framing:**
- **Wide shot (WS)**: Shows full scene and context
- **Medium shot (MS)**: Subject from waist up
- **Close-up (CU)**: Face or important detail
- **Extreme close-up (ECU)**: Very tight on small detail
- **Two-shot**: Frames two subjects together
- **Low angle**: Camera looks up at subject
- **High angle**: Camera looks down at subject
- **Eye-level**: Camera at subject's eye height
- **Top-down shot**: Directly overhead view

### Lens & Focus

**Technical specifications:**
- **Shallow depth of field**: Subject sharp, background blurred (bokeh)
- **Deep focus**: Everything in frame is sharp
- **Wide-angle lens**: Captures more of scene, slight distortion
- **Macro lens**: Extreme close-up of small subjects
- **Soft focus**: Dreamy, slightly blurred aesthetic

**Example - Shallow depth of field**: Close-up with very shallow depth of field, a young woman's face, looking out a bus window at the passing city lights with her reflection faintly visible on the glass, inside a bus at night during a rainstorm, melancholic mood with cool blue tones, moody, cinematic.

## Subject Description

Detail your subjects with precision:

- **Appearance**: Physical characteristics, clothing, distinguishing features
- **Multiple subjects**: Clearly specify which character performs actions (e.g., "the man in the red hat")
- **Expression**: Emotions visible in face and body language
- **Count and placement**: Number of subjects and spatial relationships

**When using image-to-video**: Ensure actions and speech align with subjects in the input image. Use distinguishing descriptors like "the woman in the blue dress" when multiple subjects are present.

## Action

Describe what subjects are doing:

- **Specific verbs**: Walking, running, turning head, rubbing temples, dialing phone
- **Movement quality**: Urgently, calmly, frantically, gracefully
- **Interactions**: Between subjects or with environment
- **Progression**: How actions evolve over the clip

**Example**: A desperate man in a weathered green trench coat dials a rotary phone mounted on a gritty brick wall, his fingers fumbling with the dial as he desperately tries to connect.

## Context

Detail the environment and background:

- **Location specifics**: Urban street, mountain forest, office interior, outer space
- **Time and era**: 1980s, sunset, night, historical period
- **Weather and atmosphere**: Rain, fog, clear day, stormy
- **Background elements**: Props, scenery, other details that enrich the scene

**Example**: In a cluttered office late at night, a bulky 1980s computer on desk, harsh fluorescent overhead lights.

## Style & Ambiance

Define the overall aesthetic:

### Visual Style

- **Film style keywords**: Film noir, horror film, documentary style, cinematic
- **Animation styles**: 3D cartoon style render, anime style, realistic CGI
- **Era aesthetics**: 1970s, vintage, futuristic, retro
- **Quality markers**: Cinematic, movie still, professional, high-fidelity

### Lighting & Color

- **Lighting**: Natural light, golden hour, dramatic side lighting, neon glow, soft window light, harsh fluorescent
- **Color palettes**: Cool blue tones, warm orange tones, muted colors, pastel blue and pink tones
- **Ambiance descriptors**: Melancholic, awe-inspiring, energetic, peaceful, mysterious

**Example**: The scene is lit by the harsh fluorescent overhead lights and the green glow of the monochrome monitor. Retro aesthetic, shot as if on 1980s color film, slightly grainy.

## Audio Generation (Veo 3.1)

Veo 3.1 excels at generating realistic, synchronized sound. Use separate sentences to describe audio clearly.

### Dialogue

Use quotation marks for specific speech:
- **Format**: `The man in the red hat says, "Where is the rabbit?" Then the woman in the green dress replies, "There, in the woods."`
- **Vocal quality**: Include tone descriptors like "in a weary voice" or "replies cheerfully"

**Example**: The detective looks up and says in a weary voice, "Of all the offices in this town, you had to walk into mine."

### Sound Effects (SFX)

Describe sounds with clarity:
- **Format**: `SFX: thunder cracks in the distance`
- **Types**: Specific sounds (footsteps, door creaking), environmental sounds (wind, rain), action sounds (car engine, glass breaking)

**Example**: SFX: The rustle of dense leaves, distant exotic bird calls.

### Ambient Noise

Define the background soundscape:
- **Format**: `Ambient noise: the quiet hum of a starship bridge`
- **Atmosphere**: City traffic, ocean waves, forest sounds, cafe chatter

**Example**: The audio features water splashing in the background. Add soft orchestral music that swells gently.

## Image-to-Video Prompting

Animate existing images or images generated by Imagen/Gemini 2.5 Flash Image.

### Best Practices

1. **Describe visible elements**: Reference what's already in the image
2. **Specify action**: What should animate or move
3. **Maintain consistency**: Keep descriptions aligned with the source image
4. **Use descriptors for multiple subjects**: "The woman in the blue dress turns her head"

**Example**:
- Input image: Woman standing on beach at sunset
- Prompt: "A woman in a flowing white dress walks along the beach toward the horizon, her hair blowing gently in the wind. The waves crash softly on the shore. Peaceful and contemplative mood."

**Example - Bunny**:
- Input image: Bunny with chocolate candy bar
- Prompt: "Bunny runs away."

### When to Use Image-to-Video

- Animate existing assets or photos
- Maintain precise control over composition
- Ensure specific character appearance or scene setup
- Build on images generated by other AI models

### Comprehensive Image-to-Video Guidance

For detailed workflows including image analysis, prompt patterns for different image types, troubleshooting, and 10+ example transformations, see **references/image_to_video_guide.md**. Load this reference when:
- Working with uploaded images
- Animating portraits or product photos
- Need step-by-step image-to-video workflow
- Troubleshooting image-to-video results
- Creating dialogue from portrait images

## Advanced Creative Workflows

Combine Veo 3.1 with Gemini 2.5 Flash Image (Nano Banana) for multi-step workflows with unparalleled control.

### Workflow 1: Dynamic Transition with "First and Last Frame"

Create controlled camera movements or transformations between two distinct viewpoints.

**Step 1**: Generate starting frame with Gemini 2.5 Flash Image
- Example: "Medium shot of a female pop star singing passionately into a vintage microphone, dark stage with single dramatic spotlight, eyes closed, emotional moment."

**Step 2**: Generate ending frame with complementary angle
- Example: "POV shot from behind the singer on stage, looking out at large cheering crowd, stage lights creating lens flare, energetic atmosphere."

**Step 3**: Animate with Veo using both images and First and Last Frame feature
- Prompt: "The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage. The singer sings 'when you look me in the eyes, I can see a million stars.'"

### Workflow 2: Dialogue Scene with "Ingredients to Video"

Create multi-shot scenes with consistent characters using reference images.

**Step 1**: Generate character and setting reference images with Gemini 2.5 Flash Image
- Detective character reference
- Woman character reference  
- Office setting reference

**Step 2**: Compose Shot 1 using Ingredients to Video
- Prompt: "Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, 'Of all the offices in this town, you had to walk into mine.'"

**Step 3**: Compose Shot 2 maintaining consistency
- Prompt: "Using the provided images for the detective, the woman, and the office setting, create a shot focusing on the woman. A slight, mysterious smile plays on her lips as she replies, 'You were highly recommended.'"

### Workflow 3: Timestamp Prompting

Direct complete multi-shot sequences with precise cinematic pacing in a single generation.

**Format**: `[START_TIME-END_TIME] Shot description`

**Example**:
```
[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a hidden path.

[00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of dense leaves, distant exotic bird calls.

[00:04-00:06] Tracking shot following the explorer as she steps into the clearing and runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and reverence.

[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in the center of the vast, forgotten temple complex, half-swallowed by the jungle. SFX: A swelling, gentle orchestral score begins to play.
```

**Benefits**: 
- Create multiple distinct shots in one generation
- Ensure visual consistency across sequence
- Control precise timing and pacing
- Efficient scene construction

## Negative Prompts

Use negative prompts to specify what to exclude from the video.

### Best Practices

❌ **Don't use instructive language**: Avoid "no walls" or "don't show buildings"

✅ **Do describe what you want to avoid**: Use "wall, frame" or "urban background, man-made structures"

**Example**:
- **Positive elements**: "Large solitary oak tree with leaves blowing in wind, autumn colors, warm inviting palette"
- **Negative prompt**: "urban background, man-made structures, dark, stormy, or threatening atmosphere"

## Aspect Ratios

Choose the appropriate format for your content:

### 16:9 Widescreen
- **Use for**: Landscapes, wide scenes, horizontal action, TV/monitor display
- **Example**: Tracking drone view of a man driving a red convertible car in Palm Springs, 1970s, warm sunlight, long shadows.

### 9:16 Portrait
- **Use for**: Portraits, vertical subjects (buildings, waterfalls, trees), mobile/social media content
- **Example**: Smooth motion of a majestic Hawaiian waterfall within a lush rainforest, realistic water flow, natural lighting, dappled sunlight through canopy.

## Prompt Enhancement with Gemini

For simple prompts that need enrichment:

1. Provide your basic idea to Gemini
2. Ask Gemini to enhance with cinematic and descriptive language
3. Use the enhanced prompt with Veo 3.1

**Example transformation**:
- **Basic**: "Person walking in park"
- **Enhanced by Gemini**: "Medium tracking shot of a woman in autumn coat walking through tree-lined park path, fallen leaves crunching underfoot, warm golden hour sunlight filtering through orange and red foliage, peaceful and contemplative mood, natural documentary style."

## Best Practices Summary

### Do:
- **Use the five-part formula** for structured, consistent results
- **Be descriptive and specific** with cinematographic terminology
- **Separate audio descriptions** into their own sentences
- **Use quotation marks** for exact dialogue
- **Specify distinguishing details** for multiple subjects ("the man in red hat")
- **Layer details progressively** from broad to specific
- **Reference specific styles** (film noir, documentary, cinematic)

### Avoid:
- **Overly complex scenes** with too many simultaneous actions
- **Instructive negative prompts** (use descriptive instead)
- **Contradictory directions** (bright and dark simultaneously)
- **Vague descriptions** without visual anchors
- **Too many camera movements** at once (stick to 1-2)

## Prompting for Different Scenarios

### Text-to-Video (No Reference Image)
Use the full five-part formula with emphasis on context and subject description.

### Image-to-Video (With Reference Image)
- Describe visible elements in the image
- Focus on what should animate or change
- Ensure action descriptions align with subjects present

### Multi-Shot Sequences
- Use timestamp prompting for efficiency
- Maintain style consistency across shots
- Use Ingredients to Video for character consistency

### Dialogue Scenes
- Generate character references first
- Use Ingredients to Video feature
- Include vocal quality descriptors with dialogue
- Separate audio into distinct sentences

## Example Prompts from Official Documentation

### Detailed Cinematic Shot
"A close-up cinematic shot follows a desperate man in a weathered green trench coat as he dials a rotary phone mounted on a gritty brick wall, bathed in the eerie glow of a green neon sign. The camera dollies in, revealing the tension in his jaw and the desperation etched on his face as he struggles to make the call. The shallow depth of field focuses on his furrowed brow and the black rotary phone, blurring the background into a sea of neon colors and indistinct shadows, creating a sense of urgency and isolation."

### Smooth Motion Emphasis
"A video with smooth motion that dollies in on a desperate man in a green trench coat, using a vintage rotary phone against a wall bathed in an eerie green neon glow. The camera starts from a medium distance, slowly moving closer to the man's face, revealing his frantic expression and the sweat on his brow as he urgently dials the phone."

### 3D Animated Scene
"Create a short 3D animated scene in a joyful cartoon style. A cute creature with snow leopard-like fur, large expressive eyes, and a friendly, rounded form happily prances through a whimsical winter forest. The scene should feature rounded, snow-covered trees, gentle falling snowflakes, and warm sunlight filtering through the branches. The creature's bouncy movements and wide smile should convey pure delight."

### Architectural Scene
"An architectural rendering of a white concrete apartment building with flowing organic shapes, seamlessly blending with lush greenery and futuristic elements."

### POV with Weather
"A POV shot from a vintage car driving in the rain, Canada at night, cinematic."

## Prompt Examples Library

For 40+ genre-specific examples across Product, Nature, Urban, Portrait, Action, Food, Travel, Technology, and more, see **references/prompt_examples.md**.

## Troubleshooting

**Issue**: Generated video doesn't match desired mood
**Solution**: Add more lighting and ambiance descriptors, specify color palette

**Issue**: Camera movement unclear or not smooth
**Solution**: Use standard terms (dolly, tracking, crane) and add "smooth motion" to prompt

**Issue**: Subject appears generic
**Solution**: Add specific physical details, clothing, and distinguishing characteristics

**Issue**: Audio doesn't sync or sounds wrong
**Solution**: Use separate sentences for audio, include specific SFX: and dialogue formatting

**Issue**: Multiple subjects confused in image-to-video
**Solution**: Use distinguishing descriptors like "the woman in the blue dress"

**Issue**: Scene too complex or chaotic
**Solution**: Simplify to 1-2 main actions, use fewer simultaneous elements

**Issue**: Need consistent characters across shots
**Solution**: Use Ingredients to Video workflow with reference images

**Issue**: Need inspiration or examples
**Solution**: Load references/prompt_examples.md for comprehensive examples by genre
