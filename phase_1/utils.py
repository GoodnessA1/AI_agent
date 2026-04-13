import anthropic, os
#from dotenv import load_dotenv
from settings import Settings

#load_dotenv()
config = Settings()
client = ...  # YOUR TASK: Initialise the Anthropic client.

def call_claude(system_prompt: str, user_message: str, temperature: float = 0.3) -> str:
    """
    Send a single message to Claude and return the response text.
    Args:
        system_prompt : Sets model role and constraints.
        user_message  : The question or task.
        temperature   : 0.0 - 0.3 for clinical content.
        Returns: plain string response.
    """
    
    # YOUR TASK: Call client.messages.create().
    # Model: claude-sonnet-4-20250514. Return only the text.
    


def print_result(technique: str, question: str, response: str) -> None:
    """Print technique name, question, and response with clear formatting."""
    # YOUR TASK: Use separators and labels. Make it easy to read
