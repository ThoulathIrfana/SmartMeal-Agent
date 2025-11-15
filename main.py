import json
from agents.intake_agent import IntakeAgent
from agents.meal_planner_agent import MealPlannerAgent
from agents.grocery_agent import GroceryAgent

MEMORY_FILE = "memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def main():
    print("\n=== SmartMeal — AI Meal Planner & Grocery Assistant ===\n")

    memory = load_memory()

    intake = IntakeAgent(memory=memory)
    prefs = intake.collect_preferences()

    planner = MealPlannerAgent(memory=memory)
    plan = planner.create_weekly_plan(prefs)

    grocery = GroceryAgent()
    glist = grocery.generate_grocery_list(plan)

    print("\n--- Weekly Meal Plan (summary) ---")
    planner.print_plan(plan)

    print("\n--- Grocery List ---")
    grocery.print_grocery_list(glist)

    # Save preferences to memory for future sessions
    memory.setdefault("profiles", {})
    profile_name = prefs.get("name", "default")
    memory["profiles"][profile_name] = prefs
    save_memory(memory)

    # Simple follow-up loop (loop agent)
    while True:
        resp = input("\nWould you like to adjust the plan? (yes/no): ").strip().lower()
        if resp in ("no", "n"):
            print("\nPerfect — your plan is saved to memory.json. Good luck! 👩‍🍳")
            break
        # if yes, change budget or preferences and regenerate
        elif resp in ("yes", "y"):
            change = input("What would you like to change? (budget/time/diet/allergy/quit): ").strip().lower()
            if change == "quit":
                break
            if change == "budget":
                new = input("Enter new budget category (low/medium/high): ").strip().lower()
                prefs["budget"] = new
            elif change == "time":
                new = input("Enter max cooking time per meal in minutes (e.g., 30): ").strip()
                try:
                    prefs["max_time"] = int(new)
                except Exception:
                    print("Invalid number, skipping")
            elif change == "diet":
                new = input("Enter diet (omnivore/vegetarian/vegan/keto): ").strip().lower()
                prefs["diet"] = new
            elif change == "allergy":
                new = input("List allergies comma-separated (or 'none'): ").strip()
                prefs["allergies"] = [a.strip().lower() for a in new.split(",") if a.strip()] if new.lower() != "none" else []
            else:
                print("Unknown option, try again")
                continue

            # regenerate
            plan = planner.create_weekly_plan(prefs)
            glist = grocery.generate_grocery_list(plan)
            print("\n--- Updated Weekly Meal Plan ---")
            planner.print_plan(plan)
            print("\n--- Updated Grocery List ---")
            grocery.print_grocery_list(glist)

        else:
            print("Please answer 'yes' or 'no'")


if __name__ == "__main__":
    main()
