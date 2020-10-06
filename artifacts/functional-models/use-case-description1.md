# Use Case Name
Perform common calculator functions

## ID
01

## Importance Level
High

## Primary Actor
Calculator User

## Use Case Type
Detail, Essential

## Stakeholders and Interests
Calculator User - wants to execute quick mathmatical computations

## Brief Description
This use case describes how a Calculator User can perform arithmetic operations, trigonometric functions or unit conversions of length.

## Trigger
User wishes to perform math functions.

### Type
External

## Relationships
### Association
Calculator User
### Include
Validation
### Extend
### Generalization

## Normal Flow of Events
1. Calculator User chooses calculator functionality from three choices: arithmetic, trigonometry or unit conversion.
If the Calculator User wants to perform arithmetic, the **S-1 arithmetic subflow** is performed.
If the Calculator User wants to perform trigonometry, the **S-2 trigonometry subflow** is performed.
If the Calculator User wants to convert units of length, the **S-3 unit conversion subflow** is performed. 
2. After the calculation, Calculator gives Calculator User the option to:
  + Continue working with the current figure.
  + Choose from menu of calculator functionality.
  + End progam.

## Sub-Flows
### S-1: Arithmetic
1. Calculator User enters first number. 
2. Calculator User chooses artithmetic operation: addition, subtraction, multiplication or division.
3. Calculator User provides second number.
4. Calculator computes statement and displays resulting output.
  
### S-2: Trigonometry
1. Calculator User chooses trig function: sine. (More functions to come.)
2. Calculator User enters number. 
3. Calculator computes statement and displays resulting output.

### S-3 Unit Conversion
1. Calculator User enters first measurement.
2. Calculator provides list of units of length from which Calculator User.
3. Calculator User chooses original units of measurement.
4. Calculator User chooses desired units of conversion.
5. Calculator computes conversion and displays original measurement and resulting conversion.

## Alternate/Exeptional Flows
### S-1: Reset
1. Calculator User wishes to cancel out.
2. Calculator brings Calculator User to main menu.
  
### S-2: Validation
1. Calculator user enters an input that is not a valid number.
2. Calculator displays error message prompting Calculator User to enter a valid number.
