# Higgsfield Video Generation Template

*Use this template when requesting a new video sequence.*

## 1. Initial Briefing
Provide the core details of the video you want to generate:
- **Characters to Include:** (e.g., Barker Blot, new character, etc.)
- **The Scene/Action:** (e.g., Barker walking down a spooky path, looking terrified)
- **Desired Length:** (e.g., 3-5 seconds, or a longer sequence requiring multiple shots)

---

## 2. Asset Checklist (The Pipeline)
*The Agent will guide you through this checklist step-by-step. Let the Agent know if you already have existing assets that can be reused.*

### Step 1: Character Definition 
**Tool:** `character` agent -> **Platform:** [Higgsfield Characters](https://higgsfield.ai/character)
- [ ] Do we have a base character design for this sequence? 
  *If yes, provide the asset name/URL. If no, the agent will prompt the `character` skill.*

### Step 2: Location Moodboard
**Tool:** `designer` agent -> **Platform:** [Higgsfield Moodboard](https://higgsfield.ai/moodboard/upload)
- [ ] Do we have a 16:9 environmental moodboard establishing the 1920s Lovecraftian setting?
  *If yes, provide the asset name/URL. This is the background anchor.*

### Step 3: Character Consistency (Soul)
**Tool:** `video_generator` agent -> **Platform:** [Higgsfield Soul v2](https://higgsfield.ai/image/soul-v2)
- [ ] Has a 'Soul' been trained on this character to ensure facial and anatomical consistency?
  *If yes, provide the Soul name. If no, follow instructions to create one using the character assets.*

### Step 4: Storyboard Generation
**Tool:** `video_generator` agent -> **Platform:** [Higgsfield Popcorn](https://higgsfield.ai/) (Manual Mode)
- [ ] **Prompt Formulation:** The agent will provide the exact text prompt, incorporating the character, action, and strict aesthetic tags (`1920s rubber-hose animation, monotone charcoal sketch, heavy fog, film grain`).
- [ ] **Scene Assembly:** Upload the Moodboard (Background) and select the Soul (Character). Input the generated prompt.

### Step 5: Final Video Generation
**Tool:** `video_generator` agent -> **Platform:** Higgsfield Video Interface
- [ ] **Animation:** Animate the approved Popcorn storyboard frames.
- [ ] **No Voices:** explicitly skip any lip-sync or AI voice generation steps to maintain the silent-era cartoon style.
- [ ] **Motion Controls:** The agent will recommend specific cinematic camera motions (e.g., Dolly-in, Pan).
- [ ] **Review:** Verify the final 3-5 second MP4 against the project bible (pie-cut eyes, monotone, spaghetti limbs).
