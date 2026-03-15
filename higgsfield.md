# End-to-End Higgsfield AI Video Workflow

This document outlines the complete workflow for taking an idea from scratch to a finished 1920s Lovecraftian cartoon video using the Higgsfield AI ecosystem, focusing specifically on their **Popcorn** storyboard tool.

## The Strategy

Higgsfield provides two major tools we will use:
1.  **Higgsfield Soul / Direct Image Generation**: Used for creating consistent characters (like Barker Blot) and base location moodboards.
2.  **Higgsfield Popcorn**: An AI storyboard tool that chains together scenes while maintaining character and stylistic consistency, which we then animate.

---

## Phase 1: Asset Preparation (The "Nothing" to "Something" Stage)

Before jumping into video, we need our core visual anchors. Our AI agents handle this part:

1.  **Concept Generation**: Have the `storywriter` and `lead_producer` decide on the scene's premise (e.g., "Barker Blot walks down the spooky path into Innsmouth").
2.  **Location Moodboard (The Background Anchor)**: Use the `designer` agent to generate a 16:9 base location image.
    *   *Purpose*: This moodboard serves as the static background reference image. You will upload this directly into Higgsfield Popcorn to establish the environment for your scenes, ensuring the AI keeps the background consistent even as the camera moves or characters act.
    *   *Prompt Requirements*: "Monotone charcoal sketch, 1920s animation style, heavy fog, film grain."
3.  **Character Setup (Higgsfield Soul)**: 
    *   Upload images of your main character (e.g., Barker Blot T-poses and face shots) into Higgsfield to create a **Soul**. This trains a mini-model on the character's likeness.
    *   This guarantees Barker looks like Barker in every shot, instead of morphing.

---

## Phase 2: Storyboarding with Higgsfield Popcorn

Popcorn is the bridge between static images and video. It generates a sequential storyboard based on your assets and prompts.

1.  **Access Popcorn**: Open the Higgsfield Popcorn tool.
2.  **Select Manual Mode (Recommended)**: While "Auto Mode" exists, "Manual Mode" offers the director-level precision needed to enforce our strict project aesthetic.
3.  **Frame by Frame Setup**:
    *   **Scene 1 Inputs**: Upload the location moodboard (as Background) and select the Barker Blot 'Soul' (as Character).
    *   **Directing the Scene**: Write a highly specific, action-oriented prompt.
        *   *Example Prompt*: "Barker Blot walking slowly towards the camera, looking terrified. Monotone charcoal sketch, 1920s rubber-hose animation, heavy fog, high contrast, pie-cut eyes wide in fear."
    *   **Scene 2, 3, etc.**: Add subsequent scenes. Popcorn ensures visual consistency between these shots (color tone, character appearance).
4.  **Generate Storyboard**: Let Popcorn generate the 2 to 8 keyframes that make up your short scene.
5.  **Iterate**: Review the generated storyboard. If Barker's outfit or the lighting isn't right, use Popcorn's visual editing tools to seamlessly swap elements before animating.

---

## Phase 3: Animation & Video Generation

Once the storyboard is perfect, we bring it to life.

1.  **Animate the Storyboard**: Within the Popcorn interface, select the finalized storyboard images to turn into video.
2.  **Select the Video Model**: Choose an advanced model (like Kling 2.6 or Veo, depending on what's available in your Ultimate Plan).
3.  **Apply Motion Prompts**: Keep camera motions simple and cinematic.
    *   *Motion*: Dolly-in, Pan, or slight Zoom.
    *   *Prompt Addition*: Re-iterate the action and style visually: "Camera dollies in slowly. Bouncy rubber-hose walking animation. Heavy film grain overlay."
4.  **Generate**: Higgsfield will process the 3-5 second clip.
5.  **Review against The Bible**: Does it have the pie-cut eyes? Is the fog present? Is it completely monotone? Do the limbs feel "spaghetti-like"? If it fails the test, tweak the text prompt and regenerate.

---

## Output

You will be left with a series of 3-5 second MP4 clips that are perfectly styled and character-consistent. These clips are then stitched together in your preferred video editor (e.g., Premiere, CapCut) along with audio and sound effects.

**CRITICAL AUDIO RULE:** Do *not* use Higgsfield's AI lip-sync or voice generation tools. All "Inkwell Innsmouth" videos are "Silent Era" cartoons. They should rely entirely on exaggerated motion, environmental sound effects, and a bouncy 1920s musical soundtrack added in post-production. AI voices will break the aesthetic.
