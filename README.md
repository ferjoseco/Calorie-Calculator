# Calorie Calculator

A Python application that calculates suggested daily calorie intake based on personal information including height, weight, age, gender, activity level, and weight goals.

## Overview

This Calorie Calculator helps individuals determine their optimal daily calorie intake using scientifically-backed formulas. The application calculates Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) to provide personalized nutrition recommendations.

## Features

- **BMR Calculation**: Uses the Mifflin-St Jeor equation to calculate Basal Metabolic Rate
- **TDEE Calculation**: Calculates Total Daily Energy Expenditure based on activity level
- **Weight Goal Adjustment**: Adjusts calorie recommendations based on weight goals (lose/maintain/gain)
- **User-Friendly Interface**: Interactive prompts with comprehensive input validation
- **Comprehensive Results**: Shows BMR, TDEE, and suggested calorie intake
- **Metric System Support**: Input in kilograms and centimeters for international compatibility

## Technical Stack

- **Python 3.6+** - Core programming language
- **Standard Library** - No external dependencies required
- **Mifflin-St Jeor Equation** - Scientifically validated BMR calculation
- **Activity Multipliers** - Based on established metabolic research

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calorie-calculator.git
cd calorie-calculator
```

2. Run the application:
```bash
python3 calorie_calculator.py
```

## Usage

The application provides an interactive command-line interface with the following workflow:

1. **Personal Information Input**:
   - Gender (male/female)
   - Age (years)
   - Height (centimeters)
   - Weight (kilograms)

2. **Activity Assessment**:
   - Sedentary (little or no exercise)
   - Lightly active (light exercise 1-3 days/week)
   - Moderately active (moderate exercise 3-5 days/week)
   - Very active (hard exercise 6-7 days/week)
   - Extremely active (very hard exercise, physical job)

3. **Weight Goal Selection**:
   - Lose weight (20% calorie deficit)
   - Maintain weight (no adjustment)
   - Gain weight (10% calorie surplus)

4. **Results Display**:
   - Basal Metabolic Rate (BMR)
   - Total Daily Energy Expenditure (TDEE)
   - Suggested daily calorie intake
   - Personalized recommendations

## Activity Levels

1. **Sedentary**: Little or no exercise (Multiplier: 1.2)
2. **Lightly Active**: Light exercise 1-3 days/week (Multiplier: 1.375)
3. **Moderately Active**: Moderate exercise 3-5 days/week (Multiplier: 1.55)
4. **Very Active**: Hard exercise 6-7 days/week (Multiplier: 1.725)
5. **Extremely Active**: Very hard exercise, physical job (Multiplier: 1.9)

## Weight Goals

- **Lose Weight**: 20% calorie deficit for safe, sustainable weight loss
- **Maintain Weight**: No adjustment to maintain current weight
- **Gain Weight**: 10% calorie surplus for healthy weight gain

## Error Handling

- **Input Validation**: Ensures numerical values for age, height, and weight
- **Range Checking**: Validates realistic values for all inputs
- **Gender Verification**: Confirms valid gender selection
- **Activity Level Protection**: Handles invalid activity level selections
- **Goal Selection Validation**: Ensures valid weight goal choices

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This calculator provides estimates based on general formulas and should not replace professional medical advice. For personalized nutrition advice, consult with a healthcare professional or registered dietitian. Individual metabolic rates may vary significantly.
