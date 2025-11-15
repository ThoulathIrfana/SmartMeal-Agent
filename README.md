# SmartMeal — AI Meal Planner & Grocery Assistant

**Track:** Concierge Agents  

## Project Overview
SmartMeal is an AI-powered multi-agent system designed to simplify meal planning and grocery management. Users can generate a full weekly meal plan based on their dietary preferences, calorie goals, and allergies, along with a detailed grocery list. The system uses sequential and loop agents to ensure personalized and adaptable planning.

## Features
- Multi-Agent System: Intake Agent, Meal Planner Agent, Grocery Generator Agent
- Loop Agent: Iteratively updates meal plans based on user feedback
- Memory Storage: Saves user preferences for future sessions
- Custom Tools: Ingredient parser for grocery list generation
- Gemini-Powered Reasoning: AI logic for optimal meal recommendations
- Interactive Command-Line Interface: Easy-to-use terminal input/output

## How It Works
1. Intake Agent: Collects user information including dietary preference, allergies, and calorie target.
2. Meal Planner Agent: Generates a 7-day meal plan tailored to the user.
3. Grocery Generator Agent: Produces a grocery list and calculates basic costs.
4. Loop Agent: Allows iterative modifications and plan updates.
5. Memory Module: Stores preferences in `memory.json` for future personalized recommendations.

## Sample Run
Dietary preference: veg
Allergies: none
Calorie target: 2000

--- Weekly Meal Plan ---
Monday: Oats + Vegetables
Tuesday: Rice + Dal
Wednesday: Vegetable Stir-fry + Quinoa
Thursday: Chapati + Paneer Curry
Friday: Salad + Lentil Soup
Saturday: Idli + Sambar
Sunday: Mixed Vegetable Curry + Rice

--- Grocery List ---

Rice

Dal

Vegetables

Fruits

Quinoa

Paneer

Lentils

Chapati Flour

Spices


## Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/ThoulathIrfana/SmartMeal-Agent.git
cd SmartMeal-Agent
pip install -r requirements.txt
python main.py

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request. Make sure to follow the code style and add clear comments.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

