from pathlib import Path

def load_prompt_from_file(persona_name):
    """
    Load persona prompt from text file in prompts folder
    """
    prompt_file = Path(f"prompts/{persona_name.lower()}.txt")
    
    if prompt_file.exists():
        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Fallback to default personas
        from utils.personas import PERSONAS
        return PERSONAS.get(persona_name, PERSONAS["Rama"])