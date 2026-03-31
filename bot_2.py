import time
import sys

def bot_type(text):
    """Simulates natural typing speed."""
    print("Bot: ", end="", flush=True)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def get_input(prompt_text):
    """
    GLOBAL LISTENER: Intercepts commands like 'menu', 'agent', or 'help' 
    at any point in the conversation.
    """
    user_val = input(f"{prompt_text} ").strip().lower()
    
    if user_val == "menu":
        bot_type("Returning to the Main Menu...")
        return "COMMAND_MENU"
    elif user_val == "help":
        show_capabilities()
        return "COMMAND_HELP"
    elif user_val == "agent":
        bot_type("Connecting to a live agent... Please hold.")
        time.sleep(1)
        print("\n[CONNECTED TO AGENT SARAH]")
        print("Sarah: 'Hi! I've seen your chat history. How can I help further?'")
        sys.exit()
    elif user_val in ["exit", "quit"]:
        bot_type("Thank you for using our Support Terminal. Goodbye!")
        sys.exit()
    
    return user_val

def show_capabilities():
    """Explicitly tells the user what they can do to avoid confusion."""
    print("\n" + "-"*40)
    print("💡 I CAN ASSIST YOU WITH:")
    print("1. TRACKING  - Check status of a lost package")
    print("2. PRODUCTS  - Get a recommendation for a device")
    print("3. SUPPORT   - Basic troubleshooting for errors")
    print("\nCOMMANDS: Type 'AGENT' for a human or 'EXIT' to leave.")
    print("-"*40)

# --- Scenario Flows (Robust Edge Case Handling) ---

def track_package():
    bot_type("I'll need your 8-digit Tracking ID to look that up.")
    attempts = 0
    while attempts < 3:
        uid = get_input("ID #:")
        if uid in ["COMMAND_MENU", "COMMAND_HELP"]: return
        
        if uid.isdigit() and len(uid) == 8:
            bot_type(f"Searching... Package {uid} is 'In Transit'. ETA: 24-48 hours.")
            return
        else:
            attempts += 1
            bot_type(f"Invalid ID. (Attempt {attempts}/3). Please enter 8 numbers.")
    
    bot_type("I'm having trouble validating that. Let's get an agent to help.")
    get_input("agent")

def product_advice():
    bot_type("Are you looking for a Laptop or a Tablet?")
    choice = get_input("Choice:")
    if choice in ["COMMAND_MENU", "COMMAND_HELP"]: return

    if "laptop" in choice:
        bot_type("Our top pick is the 'Zenith X'. Is this for gaming or work?")
    elif "tablet" in choice:
        bot_type("The 'Tab-Go 10' is currently on sale for $299.")
    else:
        bot_type("I didn't quite catch that. Try saying 'Laptop' or 'Tablet'.")

def tech_support():
    bot_type("I'm sorry you're having trouble. Is the device powering on? (Yes/No)")
    ans = get_input("Response:")
    if ans in ["COMMAND_MENU", "COMMAND_HELP"]: return

    if ans in ["yes", "y", "yeah"]:
        bot_type("Great. Try holding the 'Reset' button for 10 seconds.")
    elif ans in ["no", "n", "nope"]:
        bot_type("Please ensure the power cable is firmly plugged into the wall.")
    else:
        bot_type("I need a 'Yes' or 'No' to proceed. If it's complicated, type 'AGENT'.")

# --- Intent Engine ---

def identify_intent(user_input):
    intents = {
        "tracking": ["track", "order", "package", "where", "status", "delivery"],
        "product": ["buy", "recommend", "laptop", "tablet", "suggest", "new"],
        "support": ["fix", "broken", "help", "troubleshoot", "error", "reset"]
    }
    for intent, keywords in intents.items():
        if any(word in user_input for word in keywords):
            return intent
    return "unknown"

# --- Main Entry Point ---

def main():
    print("\n" + "="*50)
    print("          AI CUSTOMER SUPPORT TERMINAL          ")
    print("="*50)
    bot_type("Welcome! I am your automated assistant.")
    
    # PROACTIVE HELP: Immediate display of options so user isn't confused
    show_capabilities()

    while True:
        user_msg = get_input("\nHow can I help you today?")
        
        # Skip logic if a global command (menu/help) was triggered
        if user_msg in ["COMMAND_MENU", "COMMAND_HELP"]:
            continue
        
        intent = identify_intent(user_msg)

        if intent == "tracking":
            track_package()
        elif intent == "product":
            product_advice()
        elif intent == "support":
            tech_support()
        else:
            bot_type("I'm not sure how to handle that request yet.")
            bot_type("Try saying 'Track my package' or 'Fix my laptop'.")
            show_capabilities() # Reminder of what it CAN do

if __name__ == "__main__":
    main()