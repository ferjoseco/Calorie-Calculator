#!/usr/bin/env python3
"""
Calorie Calculator - Calculate suggested daily calorie intake
Based on height, weight, age, gender, and activity level
"""

def calculate_bmr(weight_kg, height_cm, age, gender):
    """
    Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation
    BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age + gender_factor
    """
    if gender.lower() == 'male':
        gender_factor = 5
    else:  # female
        gender_factor = -161
    
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + gender_factor
    return bmr

def get_activity_multiplier(activity_level):
    """
    Return activity multiplier based on activity level
    """
    activity_multipliers = {
        '1': 1.2,  # Sedentary (little or no exercise)
        '2': 1.375,  # Lightly active (light exercise 1-3 days/week)
        '3': 1.55,   # Moderately active (moderate exercise 3-5 days/week)
        '4': 1.725,  # Very active (hard exercise 6-7 days/week)
        '5': 1.9     # Extremely active (very hard exercise, physical job)
    }
    return activity_multipliers.get(activity_level, 1.2)

def calculate_tdee(bmr, activity_multiplier):
    """
    Calculate Total Daily Energy Expenditure
    TDEE = BMR * Activity Multiplier
    """
    return bmr * activity_multiplier

def get_weight_goal_multiplier(goal):
    """
    Return calorie adjustment based on weight goal
    """
    goal_multipliers = {
        '1': 0.8,   # Lose weight (20% deficit)
        '2': 1.0,   # Maintain weight
        '3': 1.1    # Gain weight (10% surplus)
    }
    return goal_multipliers.get(goal, 1.0)

def get_height_cm():
    """Get height input in centimeters"""
    while True:
        try:
            height_cm = float(input("Height (cm): "))
            if height_cm > 0:
                return height_cm
            print("Please enter a valid height")
        except ValueError:
            print("Please enter a valid number")

def get_weight_kg():
    """Get weight input in kilograms"""
    while True:
        try:
            weight_kg = float(input("Weight (kg): "))
            if weight_kg > 0:
                return weight_kg
            print("Please enter a valid weight")
        except ValueError:
            print("Please enter a valid number")

def main():
    print("=" * 60)
    print("           CALORIE CALCULATOR")
    print("=" * 60)
    print("This calculator will help you determine your suggested")
    print("daily calorie intake based on your personal information.")
    print()
    
    # Get user inputs
    print("Please enter your information:")
    print()
    
    # Gender
    while True:
        gender = input("Gender (male/female): ").strip()
        if gender.lower() in ['male', 'female']:
            break
        print("Please enter 'male' or 'female'")
    
    # Age
    while True:
        try:
            age = int(input("Age (years): "))
            if age > 0:
                break
            print("Please enter a valid age")
        except ValueError:
            print("Please enter a valid number")
    
    # Height
    print("\nHeight:")
    height_cm = get_height_cm()
    
    # Weight
    weight_kg = get_weight_kg()
    
    # Activity Level
    print("\nActivity Level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise 1-3 days/week)")
    print("3. Moderately active (moderate exercise 3-5 days/week)")
    print("4. Very active (hard exercise 6-7 days/week)")
    print("5. Extremely active (very hard exercise, physical job)")
    
    while True:
        activity_choice = input("Choose activity level (1-5): ").strip()
        if activity_choice in ['1', '2', '3', '4', '5']:
            break
        print("Please enter a number between 1 and 5")
    
    # Weight Goal
    print("\nWeight Goal:")
    print("1. Lose weight")
    print("2. Maintain weight")
    print("3. Gain weight")
    
    while True:
        goal_choice = input("Choose your goal (1-3): ").strip()
        if goal_choice in ['1', '2', '3']:
            break
        print("Please enter 1, 2, or 3")
    
    # Calculate results
    print("\n" + "=" * 60)
    print("           CALCULATION RESULTS")
    print("=" * 60)
    
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)
    activity_multiplier = get_activity_multiplier(activity_choice)
    tdee = calculate_tdee(bmr, activity_multiplier)
    goal_multiplier = get_weight_goal_multiplier(goal_choice)
    suggested_calories = tdee * goal_multiplier
    
    print(f"Your Basal Metabolic Rate (BMR): {bmr:.0f} calories/day")
    print(f"Your Total Daily Energy Expenditure (TDEE): {tdee:.0f} calories/day")
    print()
    print(f"Suggested daily calorie intake: {suggested_calories:.0f} calories")
    print()
    
    # Additional recommendations
    if goal_choice == '1':
        print("💡 Weight Loss Tips:")
        print("   • Aim for a 500-750 calorie deficit per day")
        print("   • Focus on whole foods and lean proteins")
        print("   • Stay hydrated and get adequate sleep")
    elif goal_choice == '2':
        print("💡 Weight Maintenance Tips:")
        print("   • Monitor your weight weekly")
        print("   • Maintain consistent eating patterns")
        print("   • Continue regular exercise")
    else:
        print("💡 Weight Gain Tips:")
        print("   • Focus on calorie-dense, nutritious foods")
        print("   • Include strength training in your routine")
        print("   • Eat frequent, balanced meals")
    
    print("\n" + "=" * 60)
    print("Note: This is an estimate. Consult a healthcare professional")
    print("for personalized nutrition advice.")
    print("=" * 60)

if __name__ == "__main__":
    main()
