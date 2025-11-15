class IntakeAgent:
    def __init__(self, memory):
        self.memory = memory

    def collect_preferences(self):
        print("\n--- Collecting User Preferences ---")
        
        dietary = input("Dietary preference (veg/non-veg/vegan): ")
        allergies = input("Any allergies (comma separated): ")
        calories = input("Daily calorie target (e.g., 1800): ")

        prefs = {
            "dietary": dietary,
            "allergies": allergies.split(","),
            "calories": calories
        }

        self.memory["preferences"] = prefs
        return prefs

