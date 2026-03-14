---
name: skill_generator
description: Automates the scaffolding and generation of new AI skills, ensuring they follow the built-in system architecture best practices.
---

# Skill Generator Skill

This skill allows the AI Agent to automatically scaffold new skill directories and generate the necessary boilerplate files (`SKILL.md` with YAML frontmatter, `scripts/`, `examples/`, `resources/`).

## When to use this skill
Whenever the user explicitly requests to build a new technical "skill" for the agent.

## Core Directives
1. A valid skill must live in its own directory under `.agents/skills/<skill_name>`.
2. A valid skill must contain a `SKILL.md` file with a YAML frontmatter block defining its `name` and `description`.
3. If the skill involves complex functionality, it should have `scripts/`, `examples/`, and `resources/` directories.

## Execution Steps

1. **Ask the user for details**: Gather the proposed name of the skill and a brief description of what it will do.
2. **Determine the deployment directory**: Generally, skills should be built in the project folder (e.g., `[project-path]/.agents/skills/<skill-name>`). Verify the exact absolute path where the `.agents/skills` root resides.
3. **Execute the generator script:**
   Run the `generate_skill.py` script from the `scripts/` folder of this skill to scaffold the new skill structure automatically.

   ```bash
   python /path/to/skill_generator/scripts/generate_skill.py <target_agents_skills_dir> <new_skill_name> "<skill_description>"
   ```
4. **Flesh out the generated `SKILL.md`**: Once the script completes, use your code replacing tools to add the specific markdown instructions necessary for the new skill.
