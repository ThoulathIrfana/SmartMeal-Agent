class GroceryAgent:
    def generate_grocery_list(self, weekly_plan):
        print("\n--- Generating Grocery List ---")
        
        base_items = [
            "Rice", "Dal", "Vegetables", "Fruits",
            "Milk", "Curd", "Wheat flour", "Oats"
        ]

        return base_items

    def print_grocery_list(self, glist):
        for item in glist:
            print(f"- {item}")

