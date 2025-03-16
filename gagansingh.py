import random

# Track used excuses to prevent repetition
used_excuses = {}

def intro_screen():
    print("My name is Gagan Singh and we're in Durham, North Carolina.")
    print("Unfortunately, I don’t come with this excuse app.\n")
    input("[Press Enter to continue]")
    main_menu()

def main_menu():
    print("\nWell well well...\n")
    print("What's your excuse for?")
    print("1. School")
    print("2. Work")
    print("3. Relationships")
    print("4. Legal Trouble")
    print("5. Friends")
    print("6. Other")
    choice = input("Enter the number of your choice: ")
    
    categories = ["school", "work", "relationships", "legal trouble", "friends", "other"]
    if choice in map(str, range(1, 7)):
        category = categories[int(choice) - 1]
        if category == "other":
            custom_excuse()
        else:
            subcategory_menu(category)
    else:
        print("Invalid choice. Try again.")
        main_menu()

def subcategory_menu(category):
    print(f"\nOf course, you need an excuse for {category}...")
    subcategories = excuses.get(category, {})
    if not subcategories:
        print("No excuses available.")
        return
    
    keys = list(subcategories.keys())
    for idx, key in enumerate(keys, 1):
        print(f"{idx}. {key}")
    
    choice = input("Enter the number of your choice: ")
    if choice in map(str, range(1, len(keys) + 1)):
        subcategory = keys[int(choice) - 1]
        action_menu(category, subcategory)
    else:
        print("Invalid choice. Try again.")
        subcategory_menu(category)

def action_menu(category, subcategory):
    print(f"\n{subcategory.title()}: Choose an option")
    print("1. Something specific (Go to Gagan.AI)")
    print("2. Generate random excuses")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("\nRedirecting to Gagan.AI for custom excuses...")
    elif choice == "2":
        generate_excuse(category, subcategory)
    else:
        print("Invalid choice. Try again.")
        action_menu(category, subcategory)

def generate_excuse(category, subcategory):
    global used_excuses
    print(f"\n{subcategory.title()}: Here are your excuses:")
    print("-" * 40)
    
    available_excuses = excuses[category][subcategory]
    selected_excuses = random.sample(available_excuses, 5)
    
    for excuse in selected_excuses:
        print(f"- {excuse}")
    print("-" * 40)
    
    choice = input("\nDon't like them? Type 'r' to regenerate or 'm' to go back to the main menu: ")
    if choice.lower() == 'r':
        generate_excuse(category, subcategory)
    elif choice.lower() == 'm':
        main_menu()
    else:
        print("Invalid choice. Returning to menu.")
        main_menu()

def custom_excuse():
    print("\nTell us the tea!!")
    input_text = input("Enter what happened: ")
    print("\nOh nah.....")
    print("Let's figure this out together!")
    print("(AI chat would start here in the real version)")
    main_menu()

excuses = {
    "school": {
        "homework": [f"Enter random excuse {i}" for i in range(1, 26)],
        "class attendance": [f"Enter random excuse {i}" for i in range(1, 26)],
        "cheating": [f"Enter random excuse {i}" for i in range(1, 26)]
    },
    "work": {
        "attendance issues": [f"Enter random excuse {i}" for i in range(1, 26)],
        "missed deadlines": [f"Enter random excuse {i}" for i in range(1, 26)],
        "quitting job": [f"Enter random excuse {i}" for i in range(1, 26)]
    },
    "relationships": {
        "avoidance": [f"Enter random excuse {i}" for i in range(1, 26)],
        "breakup": [f"Enter random excuse {i}" for i in range(1, 26)],
        "reasons to break no contact": [f"Enter random excuse {i}" for i in range(1, 26)]
    },
    "legal trouble": {  
        "minor crimes": [f"Enter random excuse {i}" for i in range(1, 26)],
        "serious crimes": [f"Enter random excuse {i}" for i in range(1, 26)],
        "general excuses": [f"Enter random excuse {i}" for i in range(1, 26)]
    },
    "friends": {
        "trust issues": [f"Enter random excuse {i}" for i in range(1, 26)],
        "ex drama": [f"Enter random excuse {i}" for i in range(1, 26)],
        "unreliable friend behavior": [f"Enter random excuse {i}" for i in range(1, 26)]
    }
}

if __name__ == '__main__':
    intro_screen()
