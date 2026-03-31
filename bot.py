import time
import sys

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# --- NEW: Global Input Handler (Example 2: Escape Hatch) ---
def get_user_input(prompt_text):
    user_val = input(f"{prompt_text} ").strip().lower()
    if user_val in ["menu", "home", "restart"]:
        slow_print("Bot: Returning to the Main Menu...")
        return "GOTO_MENU"
    if user_val in ["agent", "human", "help"]:
        slow_print("Bot: Transferring you to a live representative. Please hold...")
        time.sleep(2)
        return "GOTO_AGENT"
    return user_val

def track_package_flow():
    print("\n[PACKAGE TRACKING]")
    attempts = 0
    
    while attempts < 3:
        user_id = get_user_input("Bot: Please enter your 8-digit Tracking ID:")
        
        # Handling Escape Hatches
        if user_id == "GOTO_MENU": return
        if user_id == "GOTO_AGENT": return

        # Example 1: Strict Validation with Retry Limit
        if len(user_id) == 8 and user_id.isdigit():
            slow_print(f"Bot: Searching for ID #{user_id}...")
            # ... (Rest of your logic) ...
            break
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"(!) That doesn't look like an 8-digit number. You have {remaining} attempts left.")
            else:
                slow_print("Bot: I'm having trouble understanding that ID. Let me connect you to an agent.")
                time.sleep(1)
                break

def product_recommendation_flow():
    print("\n[PRODUCT ADVISOR]")
    slow_print("Bot: (Tip: Type 'menu' at any time to go back)")
    
    choice = get_user_input("Bot: Are you looking for a (1) Laptop or (2) Tablet?")
    
    if choice == "GOTO_MENU": return
    if choice == "GOTO_AGENT": return

    # Handling unexpected text (Example of 'Catch-All' fallback)
    if choice == '1':
        slow_print("Bot: Laptops are great for productivity!")
    elif choice == '2':
        slow_print("Bot: Tablets are perfect for media!")
    else:
        # Generic Fallback for unexpected strings
        slow_print(f"Bot: I'm sorry, '{choice}' isn't a category I recognize yet. Let's try again.")
        product_recommendation_flow() # Recurse to try again

def main_menu():
    while True:
        print("\n" + "="*45)
        print("🤖 HELPBOT: MAIN MENU")
        print("="*45)
        print("1. Track Package | 2. Product Advice | 3. Tech Support | 4. Exit")
        
        choice = input("Select (1-4): ")
        if choice == '1': track_package_flow()
        elif choice == '2': product_recommendation_flow()
        elif choice == '3': slow_print("Bot: (Tech Support Flow placeholder)")
        elif choice == '4': break
        else: print("(!) Invalid choice. Please pick 1-4.")

if __name__ == "__main__":
    main_menu()