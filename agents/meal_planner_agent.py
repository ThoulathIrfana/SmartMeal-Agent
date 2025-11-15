class MealPlannerAgent:
    def __init__(self, memory):
        self.memory = memory

    def create_weekly_plan(self, prefs):
        print("\n--- Creating Weekly Meal Plan ---")

        weekly_plan = {
            "Monday": "Oats + Vegetables",
            "Tuesday": "Rice + Dal",
            "Wednesday": "Idly + Sambar",
            "Thursday": "Chappathi + Veg Curry",
            "Friday": "Fruit Salad",
            "Saturday": "Curd Rice",
            "Sunday": "Lemon Rice"
        }

        self.memory["weekly_plan"] = weekly_plan
        return weekly_plan

    def print_plan(self, plan):
        for day, meal in plan.items():
            print(f"{day}: {meal}")

