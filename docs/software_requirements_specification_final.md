# Overview
This document provides the software specification requirements, change management plan, traceability tables and software artifacts for our project, a calculator app. The project was completed in December 2020 for the Systems Analysis and Design graduate course (CIS 641) at Grand Valley State University.

### Table of contents
* [Software Requirements](#software-requirements)
  * [Functional Requirements](#functional-requirements)
  * [Nonfunctional Requirements](#non-functional-requirements)
* [Change Management Plan](#change-management-plan)
  * [Introduction](#introduction)
  * [Integration](#integration)
  * [Training](#training)
  * [Issue Resolution](#issue-resolution)
* [Traceability Links](#traceability-links)
* [Software Artifacts](#software-artifacts)

# Software Requirements
This section documents the functional and nonfunctional requirements of the calculator app. They have been organized as overarching categories that each list requirements specific to that category.

## Functional Requirements

### User Interface
| ID  | Requirement |
| :-: | :---------- |
| FR1 | The user shall interact with the system via a Graphical User Interface designed to emulate a regular calculator. |
| FR2 | The interface shall provide the user a means for exiting the app regardless of any operation in progress. |
| FR3 | The buttons shall be grouped together based on functionality. |
| FR4 | The Clear button shall be colored differently than the other buttons so the user can locate it easily. |
| FR5 | The User Interface size shall not exceed 515 pixels in width and 460 pixels in height.|

### Display
| ID  | Requirement |
| :-: | :---------- |
| FR6 | The calculator shall display the user’s current input and then update with the calculated answer. |
| FR7 | The Clear button shall not just clear the screen but also the history (memory) of the calculation. |
| FR8 | Input, errors and output shall display in the same single text screen. |
| FR9 | The display shall include an abbreviation for the unit of measurement when executing unit conversions. |
| FR10| When the system returns decimal numbers, the numbers shall be rounded to four decial digits. |

### Calculations
| ID  | Requirement |
| :-: | :---------- |
| FR11 | The system shall perform the arithmetic operations of addition, subtraction, multiplication and division. |
| FR12 | _Complex calculations shall be done only using "math" library from Python, not other manual ways._|
| FR12 | When more than one valid arithmetic operator is entered, the system shall evaluate the statement the order of operations. |
| FR13 | The system shall compute decimal calculations. |
| FR14 | _The system shall receive input from only the GUI buttons, not the keyboard._ |
| FR15 | _The system shall require that one operand be entered first before an operation or function key may be pressed._ |

### Trigonometric and Unit conversion features
| ID  | Requirement |
| :-: | :---------- |
| FR16 | The system shall perform the trigonometric functions of sine, cosine and tangeant. |
| FR17 | Trigonometric results shall be converted and shown in degrees, not in radian. |
| FRXX | _The calculator shall assume a number entered for use in a trigonometric function is in degrees._ | 
| FR18 | The system shall convert units of measurement from feet to meters and meters to feet. |
| FR19 | _The system shall calculate the results for trigonometric calculations only using math library from python, not other ways._ |
| FR20 | The user shall be able to choose which their preferred unit conversion. |

### Validations
| ID  | Requirement |
| :-: | :---------- |
| FR21 | The system shall check the user’s input for non-number or -arithmetic characters. |
| FR22 | The system shall check the user’s input for requesting invalid mathematical treatments such as "++" or ".." |
| FR23 | The user shall be notified with an error message upon entering invalid input. |
| FR24 | The system shall prevent the app from crashing if the user enters invalid input. |
| FR25 | _The system shall prevent the app from crashing when it deals with infinity. For example, computing tan 90 shows some value rather than just infinity._ |

## Non-Functional Requirements

### Accessibility and Usability
| ID  | Requirement |
| :-: | :---------- |
| NFR1 | The layout shall incorporate white space for readability purposes. |
| NFR2 | _All the results and error messages shall be shown in same display._ |
| NFR3 | The size of the equals, clear, convert, sine, cosine and tangeant buttons shall be bigger than the calculator's other buttons. |
| NFR4 | The GUI shall not contain any hidden or hard-to-find features that require hunting or multiple clicks to find. |
| NFR5 | _Both the interface and functionality shall be matched with regular calculator to make user easy to use the application._ |

### Performance and Efficiency
| ID  | Requirement |
| :-: | :---------- |
| NFR6 | The system shall perform a given calculation within half a second. |
| NFR7 | The application shall execute in any machine that supports its underlying programming language. |
| NFR8 | The application shall not require more than 5 megabytes of run-time memory .|
| NFR9 | The application shall not require more than a few megabytes of storage capacity in the system.|
| NFR10 | _Users shall be able to use the keyboard shortcuts for copy and paste (Ctrl + C and Ctrl + V for Windows; Cmd + C and Cmd + V for Mac) the contents in the display to another application._ |

### Appearance
| ID  | Requirement |
| :-: | :---------- |
| NFR11 | _The functionalities of arithmetic, trigonometry and unit conversion shall be separately grouped in GUI. For example, buttons related to the arithmetic function are grouped in one place and buttons related to unit conversion are grouped in another place._ |
| NFR12 | The calculator shall use high-contrast colors for improved readability. |
| NFR13 | The calculator's font choice shall prioritize legibility and reader-friendly size. |
| NFR14 | Non-Functional Requirement 14 |
| NFR15 | Non-Functional Requirement 15 |

### Reliability, Availability and Maintainability
| ID  | Requirement |
| :-: | :---------- |
| NFR16 | The system shall never crash even upon providing more than 10 digits for calculation. |
| NFR17 | The system shall always produce a correct result. |
| NFR18 | When prompted, the system shall load in under 1 second. |
| NFR19 | The system shall operate independently on each machine it's installed on, meaning it is not affected by user load. |
| NFR20 | Non-Functional Requirement 20 |

### Portability and Compatibility
| ID  | Requirement |
| :-: | :---------- |
| NFR21 | The system shall work in a wide variety of modern-day computer operating systems. |
| NFR22 | _The system shall not require internet access; it shall operate as a completely offline application._ |
| NFR23 | Non-Functional Requirement 23 |
| NFR24 | Non-Functional Requirement 24 |
| NFR25 | Non-Functional Requirement 25 |

# Change Management Plan
In the coming months, we will be transitioning from the use of physical calculators to a calculator app installed on all work stations. This section details the organizational plan that the company will follow to roll out that change.

## Introduction
The company is pursuing this change for a number of reasons:

* **Improved accuracy and efficiency** - Staff will no longer have to first perform calculations on their physical calculator and then manually key in the calculated figures into the digital documents on their workstation.
* **Convenience** - Staff will no longer have to ensure they have their physical calculator or even the calculator app on their phone with them. This enables the staff to have to keep track of and account for one less piece of hardware.
* **Cost** - The company will no longer have to supply new employees with calculators and replace broken, worn-out or missing calculators. 

This change will affect all staff, particularly those who use calculators the most: front-line staff and those in the finance department.

In the large scale of company operations, this change is relatively minor but we want everyone to be aware of the shift. Training will be provided to ensure staff are comfortable with the new tool. The app works much like a physical calculator does, a familiarity that will help staff process how to use it and adjust more easily.

## Integration
### Scheduling

Before training begins, the I.T. department will reach out to department heads to discuss the implementation. By this time, we ask that department heads announce to their staff the planned roll-out of the calculator app and collect feedback on the points listed below.

The I.T. department seeks the following information:

* Dates and times convenient to the department for the install of the calculator software. The software install will be done remotely but the department wishes to be aware of any department operations going on that may need to be planned around to avoid undue interruption.
* A list of staff and/or workstations that need keyboards with a numerical keypad. The I.T. department will take care of these swaps gradually throughout the transition period. If there are busy times to avoid, please let the I.T. department know.
* Early questions, comments and concerns from staff that can be integrated into and addressed at training.
* A post-install date by which time the department is comfortable enough to relinquish their physical calculators, which will be collected by the  I.T. Department. Until that date, during the training and transition period, staff may retain and use their physical calculators.

### Timeline
| Dates | Action Taken |
| --: | :-- |
| Dec. 16, 2020 | Formal announcement about switch to calculator app to staff. |
| Dec. 17 - Dec. 31, 2020 | Department heads collect info from staff for transition. |
| Jan. 4-15, 2021 | I.T. discusses and schedules transition with department heads. |
| Jan. 18 - Feb. 5, 2021 | I.T. deploys calculator app to workstations and swaps out keyboards.
| Jan. 25 - Feb. 26, 2021 | Staff training. |
| March 15 - April 2, 2021 | Physical calculators collected. |

## Training

### Audience
Training in the calculator app is mandatory for all staff who have been issued physical calculators; they may complete training by choosing their preferred learning format.

### What the training will cover
The objective of the training is that staff can do with the calculator app everything they would normally do with a physical calculator, with the added benefit of being able to copy and paste figures without having to retype them.

* Launching the calculator app
* Performing basic arithmetic
* Performing the trigonometric functions of sine, cosine and tangent
* Converting between units of measurement
* Clearing the screen (starting over)
* Copying and pasting from the display
* Exiting the calculator app
* Where to find support, documentation and updates on the app

It is anticipated that the app will continue to be updated with additional features over time. Staff will be trained on the current features and directed to where they can stay informed of new features as they are released and how to use them.

### Method of delivery
The I.T. Department will be providing the calculator app training in several different formats. Staff may choose whichever format they prefer.

* In-person training sessions organized by department
* Video tutorials
* Written instructions

All staff who participate in the training must complete a brief quiz reviewing their understanding of how the calculator app works. The quiz may be retaken as many times as necessary to pass.

Once everyone in a department has completed training, the department will be thrown a pizza party to mark the occasion. There will also be a drawing among all quiz completers; the winner earns cupcakes for everyone in their department.

## Issue resolution
Although the calculator app has been tested, no software is foolproof. If any anomalies or issues arise during the transition phase or after implementation is complete, please open a ticket in the I.T. department’s ticket system logging as many details as possible. 

The I.T. department will prioritize the ticket based on urgency and operational impact. If the department is unable to solve the problem and deem it a substantial enough issue, they will elevate the ticket to the app vendor for resolution.

# Traceability Links
Description of this section

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| UseCase1 | Move Player | FR5 |
| … | … | … |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| classPlayer | NFR3, FR5 |
| … | … | … |

## Activity Diagram Traceability
In this case, it makes more sense (I think, feel free to disagree) to link to the file and to those requirements impacted

| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| <filename> | Handle Player Input | FR1-5, NFR2 |
| … | … | … |

# Software Artifacts
Describe the purpose of this section
* [I am a link](to_some_file.pdf)