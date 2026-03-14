import os
import sys

def create_skill(base_dir, skill_name, description):
    # Form the deep folder name
    skill_dir = os.path.join(base_dir, skill_name)
    
    # Check if the skill already exists
    if os.path.exists(skill_dir):
        print(f"Error: A skill named '{skill_name}' already exists at {skill_dir}")
        sys.exit(1)

    # Establish directories
    dirs_to_make = [
        skill_dir,
        os.path.join(skill_dir, "scripts"),
        os.path.join(skill_dir, "examples"),
        os.path.join(skill_dir, "resources")
    ]
    
    for d in dirs_to_make:
        os.makedirs(d, exist_ok=True)
    
    # Try finding the Template File relative to this script's known location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "..", "resources", "template.md")
    
    # Use template if found, otherwise build raw text
    if os.path.exists(template_path):
        with open(template_path, 'r') as f:
            content = f.read()
            content = content.replace("{SKILL_NAME}", skill_name)
            content = content.replace("{SKILL_DESCRIPTION}", description)
    else:
        # Fallback just in case
        content = f"---\nname: {skill_name}\ndescription: {description}\n---\n\n# {skill_name} Skill\n\nAdd specific markdown instructions here.\n"

    # Write the SKILL.md file
    skill_file_path = os.path.join(skill_dir, "SKILL.md")
    with open(skill_file_path, "w") as f:
        f.write(content)
        
    print(f"Success! Scaffolded new skill '{skill_name}' at: {skill_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python generate_skill.py <target_agents_skills_dir> <new_skill_name> \"<description>\"")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    skill_name = sys.argv[2]
    description = sys.argv[3]
    
    create_skill(base_dir, skill_name, description)
