from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from rich.console import Console
from rich.table import Table
from rich import box

from llm_provider import LLM

console = Console()

ASCII_BANNER = r"""
  _____             _____                 _             
 |  __ \           / ____|               | |            
 | |__) |___  __ _| (___  _ __   ___  ___| |_ ___  _ __ 
 |  _  // _ \/ _` |\___ \| '_ \ / _ \/ __| __/ _ \| '__|
 | | \ \  __/ (_| |____) | |_) |  __/ (__| || (_) | |   
 |_|  \_\___|\__, |_____/| .__/ \___|\___|\__\___/|_|   
                | |      | |                            
                |_|      |_|                            

A simple CLI to analyze your system requirements with Large Language Models (LLMs).
Quit: ":q", Help: ":help"
"""

OPTIONS = {
    "1": "Groq",
    "2": "OpenAI",
    "3": "Anthropic",
    "4": "Ollama",
    ":q": "Quit",
    ":help": "Help"
}

HELP_TEXT = """
":q" - Quit the program
":help" - Display help information
"CRTL + S" - Submit multi-line input to LLM
"""

def main():
    print(ASCII_BANNER)
    provider = None

    while True:
        choice = input("Please select a LLM provider [1-4] (default ENTER is Groq Cloud): ").strip() or "1"
        if choice in OPTIONS:
            if choice == ":q":
                print("Exiting the program. Goodbye!")
                return
            elif choice == ":help":
                print(HELP_TEXT)
                quit_help = input("Press ENTER to continue or type ':q' to quit: ").strip()
                if quit_help == ":q":
                    print("Exiting the program. Goodbye!")
                    return
                else:
                    continue
            else:
                provider = OPTIONS[choice]
                print(f"You selected: {provider}")
                break
        else:
            print("Invalid choice. Please try again.")


    model_name = input("Enter the model name (default 'llama-3.1-8b-instant'): ").strip() or "llama-3.1-8b-instant"
    print(f"Initializing {provider} provider...")
    llm = LLM(provider, model_name)

    # Test the provider connection
    if not llm.test_connection():
        print(f"Failed to connect to {provider}. Please check your configuration. (model name and API keys)")
        return
    print(f"Successfully connected to {provider} with model {model_name}.")
    print("You can now enter your system requirements to analyze.")

    while True:
        try:
            user_input = get_multiline_input()
            if user_input.strip() == "":
                print("No input provided. Please enter your system requirements.")
                continue
            if user_input.strip() == ":q":
                print("Exiting the program. Goodbye!")
                break
            elif user_input.strip() == ":help":
                print(HELP_TEXT)
                quit_help = input("Press ENTER to continue or type ':q' to quit: ").strip()
                if quit_help == ":q":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    continue

            print("Sending your input to the LLM for analysis...")
            response = llm.generate_response(user_input)
            print("\nLLM Response:\n")
            display_results(response)
            print("\nYou can enter more requirements or type ':q' to quit.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def get_multiline_input():
    kb = KeyBindings()

    @kb.add('c-s')
    def _(event):
        event.app.exit(result=event.app.current_buffer.text)

    session = PromptSession(key_bindings=kb)
    message = session.prompt('Enter your message (Ctrl + s to submit):\n', multiline=True)
    return message

def display_results(result: dict):
    """Pretty-print analysis in a color table."""
    table = Table(title="Requirement Analysis", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Criterion", style="bold")
    table.add_column("Value", style="bold cyan")
    table.add_column("Reason", style="dim")

    color_map = {"High": "green", "Medium": "yellow", "Low": "red", True: "green", False: "red"}

    for key, data in result.items():
        val = data.get("rating") or data.get("value")
        reason = data.get("reason", "")
        val_str = str(val)
        color = color_map.get(val, "white")
        table.add_row(key, f"[{color}]{val_str}[/{color}]", reason)

    console.print(table)

if __name__ == "__main__":
    main()

