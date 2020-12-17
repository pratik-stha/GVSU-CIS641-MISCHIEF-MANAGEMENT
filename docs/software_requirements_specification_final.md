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
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| FR1 | The user shall interact with the system via a Graphical User Interface designed to emulate a regular calculator, reducing training time. | TBD |
| FR2 | The interface shall provide the user a means for exiting the app regardless of any operation in progress. | TBD |
| FR3 | The Clear button shall not just clear the screen but also the history (memory) of the calculation | TBD |
| FR4 | The Clear button shall be colored differently than the other buttons so the user can locate it easily. | TBD |
| FR5 | The User Interface size shall not exceed 515 pixels in width and 460 pixels in height.| TBD |

### Display
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| FR6 | The calculator shall display the user’s current input and then update with the calculated answer. | TBD |
| FR7 | The display shall show up to 25 digits at a time maximum. | TBD |
| FR8 | Input, errors and output shall display in the same single text screen. | TBD |
| FR9 | The display shall include an abbreviation for the unit of measurement when executing unit conversions. | TBD |
| FR10| When the system returns decimal numbers, the numbers shall be rounded to four decimal digits. | 5 |

### Calculations
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| FR11 | The system shall perform the arithmetic operations of addition, subtraction, multiplication and division. | TBD |
| FR12 | When more than one valid arithmetic operator is entered, the system shall evaluate the statement the order of operations. | TBD |
| FR13 | The system shall compute decimal calculations. | TBD |
| FR14 | The system shall receive input from only the GUI buttons, not the keyboard. | TBD |
| FR15 | The system shall require that operands be entered first before an operation or function key may be pressed. | TBD |
 
### Trigonometric and Unit conversion features
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| FR16 | The system shall perform the trigonometric functions of sine, cosine and tangent. | 6-9 |
| FR17 | The system shall assume a number entered for use in a trigonometric function is in radians. | TBD |
| FR18 | Trigonometric results shall be converted from radian to degrees and shown in degrees. | TBD |
| FR19 | The system shall convert units of measurement from feet to meters and meters to feet. | TBD |
| FR20 | The user shall be able to choose their preferred unit conversion. | 11, 13 |

### Validations
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| FR21 | The system shall check the user’s input for non-number or -arithmetic characters. |1, 3, 14, 15 |
| FR22 | The system shall check the user’s input for requesting invalid mathematical treatments such as "++" or ".." | 2 |
| FR23 | The user shall be notified with an error message upon entering invalid input. | TBD |
| FR24 | The system shall prevent the app from crashing if the user enters invalid input. | 4, 12, 16-22 |
| FR25 | The system shall prevent the app from crashing when it deals with infinity. For example, computing tan(90) gives an error message rather than infinity. | 10 |

## Non-Functional Requirements

### Accessibility and Usability
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| NFR1 | The layout shall incorporate white space for readability purposes. | TBD |
| NFR2 | Users shall be able to use the keyboard shortcuts for copy and paste (Ctrl + C and Ctrl + V for Windows; Cmd + C and Cmd + V for Mac) the contents in the display to another application. | TBD |
| NFR3 | The calculator's font choice shall prioritize legibility and reader-friendly size. | TBD |
| NFR4 | The GUI shall not contain any hidden or hard-to-find features that require hunting or multiple clicks to find. | TBD |
| NFR5 | Both the interface and functionality shall match with a regular calculator to make it easy for the user to use the application. | TBD |

### Appearance
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| NFR6 | The functionalities of arithmetic, trigonometry and unit conversion shall be separately grouped in GUI. For example, buttons related to the arithmetic function are grouped in one place and buttons related to unit conversion are grouped in another place. | TBD | 
| NFR7 | Labels shall distinguish the system's sections for trigonometry and unit conversion. | TBD |
| NFR8 | The calculator shall use high-contrast colors for readability. | TBD |
| NFR9 | The size of the equals, clear, convert, sine, cosine and tangeant buttons shall be bigger than the calculator's other buttons. | TBD |
| NFR10 | The size of all buttons on the calculator shall be large enough to make them easy targets for a mouse cursor. | TBD |

### Performance and Efficiency
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| NFR11 | The system shall perform a given calculation within half a second. | TBD |
| NFR12 | At launch, the entire GUI will load simultaneously; no sections will load at varying times. | TBD |
| NFR13 | The application shall require no more than 5 megabytes of run-time memory. | TBD |
| NFR14 | The application shall require no more than a few megabytes of storage capacity in the system.| TBD |
| NFR15 | The system shall operate independently on each machine it is installed on, unaffected by concurrent user load. | TBD |

### Reliability, Availability and Maintainability
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| NFR16 | The system shall not crash even if provided more than 10 digits for calculation. | TBD |
| NFR17 | The system shall always produce a correct result. | TBD |
| NFR18 | The system shall load in under 1 second. | TBD |
| NFR19 | The system shall have a 99 percent availability rate. | TBD |
| NFR20 | Scheduled maintenance shall require less than an hour of downtime per year the first three years.  | TBD |

### Portability and Compatibility
| ID  | Requirement | Test Case ID |
| :-: | :---------- | :-: |
| NFR21 | The system shall work on modern-day Mac, Windows and Linux computer operating systems. | TBD |
| NFR22 | The system shall not require internet access; it shall operate as a completely offline application. | TBD |
| NFR23 | The system shall be easily removed from a computer by deleting the application files from its home directory. | TBD |
| NFR24 | The application shall execute in any machine that can run its underlying programming language. | TBD |
| NFR25 | Running the application shall not interfere with the running of any other application in the same operating system. | TBD |

# Change Management Plan
In the coming months, we will be transitioning from the use of physical calculators to a calculator app installed on all work stations. This section details the organizational plan that the company will follow to roll out that change.

## Introduction
The company is pursuing this change for a number of reasons:

* **Improved accuracy and efficiency** - Staff will no longer have to first perform calculations on their physical calculator and then manually key in the calculated figures into the digital documents on their workstation.
* **Convenience** - Staff will no longer have to ensure they have their physical calculator or the calculator app on their phone with them. This enables the staff to have to keep track of and account for one less piece of hardware.
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
* A post-install date by which time the department is comfortable enough to relinquish their physical calculators, which will be collected by the I.T. Department. Until that date, during the training and transition period, staff may retain and use their physical calculators.

### Timeline
| Dates | Action Taken |
| --: | :-- |
| Dec. 16, 2020 | Formal announcement about switch to calculator app to staff. |
| Dec. 17 - Dec. 31, 2020 | Department heads collect info from staff for transition. |
| Jan. 4-15, 2021 | I.T. discusses and schedules transition with department heads. |
| Jan. 18 - Feb. 5, 2021 | I.T. deploys calculator app to workstations and swaps out keyboards.
| Jan. 25 - Feb. 26, 2021 | Staff training. |
| March 15 - April 2, 2021 | Physical calculators collected. |

Please note that  during training, you will be directed to use your mouse or, if using a touchpad screen, the actual calculator app buttons. At this time the calculator app does not work with keyboard input. We anticipate this feature will be added soon, which is why we are still ensuring everyone has a keypad on their keyboards.

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
Although the calculator app has been tested, no software is foolproof. If any anomalies or issues arise during the transition phase or after implementation is complete, please contact the I.T. department by phone or email. 

If the issue can be addressed easily and immediately, I.T. staff will do so. If not, you may be asked to open a ticket in the I.T. department’s ticket system logging as many details as possible. This allows the I.T. department to monitor possible troubleshooting trends.  

The I.T. department will prioritize the ticket based on urgency and operational impact. If I.T. staff are unable to solve the problem, they may elevate the ticket to the app vendor for resolution.

# Traceability Links
This section serves to connect artifacts and artifact elements with their relevant software requirement specifications.

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :---------- | :---------- |
| [UseCase1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram1-calculator-system.png) | Perform arithmetic | FR11-13, FR15, NFR6 |
| [UseCase1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram1-calculator-system.png) | Perform trigonometry | FR16-18, NFR6-7, NFR9 |
| [UseCase1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram1-calculator-system.png) | Convert units | FR9, FR19-20, NFR6-7 |
| [UseCase1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram1-calculator-system.png) | Validate | FR21-25 |
| [UseCase2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png) | Enter number | FR15 |
| [UseCase2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png) | Choose math function | FR11, FR16, FR19 |
| [UseCase2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png) | Computer (equals) | FR6, FR13, NFR9 |
| [UseCase2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png), [UseCase3](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram3-unit-conversion.png) | Reset | FR3-4, NFR9 |
| [UseCase2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png), [UseCase3](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram3-unit-conversion.png) | Display | FR6-10, FR23 |
| [UseCase3](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram3-unit-conversion.png) | Convert meters to feet | FR9, FR19-20, NFR6-7 |
| [UseCase3](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram3-unit-conversion.png) | Convert feet to meters | FR9, FR19-20, NFR6-7 |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| :-------------: |:---------- |
| [classUnitConversion](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/structural-models/Class%20diagram.pdf) | FR9, FR19-20, NFR6-7 |

## Activity Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :---------- | :---------- |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Get initial input number | FR15 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Addition | FR11-12, NFR5-6 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Subtraction | FR11-12, NFR5-6 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Multiplication | FR11-12, NFR5-6 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Division | FR11-12, NFR5-6 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Get next number | FR15 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Input validation | FR21-25 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Error message | FR23 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Choose sin(x) | FR16-18, NFR5-7, NFR9 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Convert feet to meters | FR9, FR19-20, NFR6-7 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Convert meters to feet | FR9, FR19-20, NFR6-7 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Close app | FR2 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Compute | FR6, FR13, NFR5 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Clear Screen | FR3-4, NFR5, NFR9 |
| [ActivityDiagram1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf) | Display | FR6-10, NFR5 |

## Test Case Traceability

Both unit testing as well as integrated testing were performed in this project. Unit testing was performed in each of the three modules -- i.e. arithmetic, trigonomety and unit conversion. Most of the possible combinations of inputs were taken into account when performing the testing. 

After testing was perfomed, the expected output and actual output were compared to determine if the requirment had been met or not. Similarly, after all the modules had been put together, integrated testing was performed. For this part, various sequences of operations were conducted and checked, such as if one operation followed by others performed well or not. 

Here again, most of the possible combinations were taken into considerations. The Google Doc mentioned below lists the test cases that were used, along with their corresponding requirements.

* [Google Doc of test cases, their IDs and relevant requirements](https://drive.google.com/file/d/1z54HzWOPk4t5-omgNWgOWMaNJVKQcgJ5/view?usp=sharing)

# Software Artifacts
This section is a list of the diagrams and documentation created during the course of this project.

* [Final presentation (Dec. 16, 2020)](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/docs/final-presentation.pdf)
* [Project README file](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/README.md)
* [Weekly meeting minutes](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/tree/master/meetings)
* [Gantt chart of project timeline](https://docs.google.com/spreadsheets/d/1fueWszEguuGhWwA7LTNIGlknG-qABH2ABIWLH1lTMMg/edit?usp=sharing)
* [User interface design diagram](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/uid-models/wnd.png)
* [Data persistence mapping](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/Mapping%20Diagram/Mapping%20Diagram(1).pdf)
  * Mapping of a class to a relational database
  * Mapping of a class to a NoSQL database object
  * Mapping of a class to a flat file
* [Midterm presentation (Oct. 28, 2020)](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/docs/midterm-presentation.pdf)
* [Class diagram, object diagram and CRC card](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/structural-models/Class%20diagram.pdf)
* [Activity diagram 1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%201.pdf)
* [Activity diagram 2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/Activity%20Diagram%202.pdf)
* [Use case description](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-description1.md)
* [Use case diagram 1](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram1-calculator-system.png)
* [Use case diagram 2](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram2-graphic-interface.png)
* [Use case diagram 3](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/artifacts/functional-models/use-case-diagram3-unit-conversion.png)
* [Initial program proposal](https://github.com/pratik-stha/GVSU-CIS641-MISCHIEF-MANAGEMENT/blob/master/docs/Project%20Proposal.md)
