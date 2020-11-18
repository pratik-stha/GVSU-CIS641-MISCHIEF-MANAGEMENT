# Overview
This document serves as the software requirement specifications for our project, a calculator app. It defines the functional and nonfunctional characteristic expected of the app.

# Functional Requirements
1. User Interface
	1. The user shall interact with the system via a Graphical User Interface designed to emulate a regular calculator.
	1. The interface shall provide the user a means for exiting the app disregard of any operation on progress.

1. Display
	1. The calculator shall display the user’s current input and then update with the calculated answer.
	1. The user shall be notified with error message upon entering invalid input.
	1. The clear button shall not just clear the screen but also the history (memory) of the calculation.
1. Calculations
	1. The system shall perform the arithmetic operations of addition, subtraction, multiplication and division.
	1. The system shall perform the trigonometric function of sine.
		1. The system may perform the trigonometric functions of cosine and tangent.
	1. The system shall convert units of measurement from feet to meters and meters to feet.
		1. 	The system may perform additional unit conversions.
1. Validations
	1. The system shall check the user’s input and operation choice(s) for invalid data such as double decimals, dividing by zero or non-number or -arithmetic characters.
	1. The system shall prevent the app from crashing upon entering the invalid inputs. For e.g., pressing ‘=’ after ‘1’,’+’,’2’,’+’,’3’ is valid but after ‘1’,’+’,’2’,’+’,’-’ is not valid.
# Nonfunctional Requirements

1. Accessibility
	1. The layout shall incorporate white space for readability purposes.
	1. The font choice shall prioritize legibility and reader-friendly size.
1. Performance
	1. The system shall perform given calculation within about half a second.
1. Appearance
	1. The functionalities like Arithmetic, Trigonometric and Unit Conversion shall be separately grouped in GUI. For E.g., buttons related to Arithmetic function are grouped at one place, buttons related to Unit conversion are grouped into another place etc.
1. Size
	1. The application size shall be very small in size, around few Megabytes.