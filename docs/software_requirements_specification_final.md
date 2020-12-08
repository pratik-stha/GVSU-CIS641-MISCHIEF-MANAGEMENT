# Overview
This document serves as the software requirement specifications for our project, a calculator app. It defines the functional and nonfunctional characteristic expected of the app.

# Software Requirements
This section documents the functional and nonfunctional requirements of the calculator app. They have been organized as overarching categories that each list requirements specific to that category.

## Functional Requirements

### User Interface
| ID  | Requirement |
| :-: | :---------- |
| FR1 | The user shall interact with the system via a Graphical User Interface designed to emulate a regular calculator. |
| FR2 | The interface shall provide the user a means for exiting the app regardless of any operation in progress. |
| FR3 | Requirement 3 |
| FR4 | Requirement 4 |
| FR5 | Requirement 5 |

### Display
| ID  | Requirement |
| :-: | :---------- |
| FR6 | The calculator shall display the user’s current input and then update with the calculated answer. |
| FR7 | The user shall be notified with an error message upon entering invalid input. |
| FR8 | The clear button shall not just clear the screen but also the history (memory) of the calculation. |
| FR9 | Requirement 9 |
| FR10 | Requirement 10 |

### Calculations
| ID  | Requirement |
| :-: | :---------- |
| FR11 | The system shall perform the arithmetic operations of addition, subtraction, multiplication and division. |
| FR12 | The system shall perform the trigonometric function of sine. |
| FR13 | The system may perform the trigonometric functions of cosine and tangent. |
| FR14 | The system shall convert units of measurement from feet to meters and meters to feet. |
| FR15 | The system may perform additional unit conversions. |

### Validations
| ID  | Requirement |
| :-: | :---------- |
| FR16 | The system shall check the user’s input and operation choice(s) for invalid data such as double decimals, dividing by zero or non-number or -arithmetic characters. |
| FR17 | The system shall prevent the app from crashing upon entering the invalid inputs. For example, pressing ‘=’ after ‘1’,’+’,’2’,’+’,’3’ is valid but after ‘1’,’+’,’2’,’+’,’-’ is not valid. |
| FR18 | Requirement 18 |
| FR19 | Requirement 19 |
| FR20 | Requirement 20 |

### Name of Feature 5
| ID  | Requirement |
| :-: | :---------- |
| FR21 | Requirement 21 |
| FR22 | Requirement 22 |
| FR23 | Requirement 23 |
| FR24 | Requirement 24 |
| FR25 | Requirement 25 |

## Non-Functional Requirements

### Accessibility
| ID  | Requirement |
| :-: | :---------- |
| NFR1 | The layout shall incorporate white space for readability purposes. |
| NFR2 | The font choice shall prioritize legibility and reader-friendly size. |
| NFR3 | Non-Functional Requirement 3 |
| NFR4 | Non-Functional Requirement 4 |
| NFR5 | Non-Functional Requirement 5 |

### Performance
| ID  | Requirement |
| :-: | :---------- |
| NFR6 | The system shall perform a given calculation within about half a second. |
| NFR7 | Non-Functional Requirement 7 |
| NFR8 | Non-Functional Requirement 8 |
| NFR9 | Non-Functional Requirement 9 |
| NFR10 | Non-Functional Requirement 10 |

### Appearance
| ID  | Requirement |
| :-: | :---------- |
| NFR11 | The functionalities of arithmetic, trigonometry and unit conversion shall be separately grouped in GUI. For example, buttons related to the arithmetic function are grouped in one place and buttons related to unit conversion are grouped in another place. |
| NFR12 | Non-Functional Requirement 12 |
| NFR13 | Non-Functional Requirement 13 |
| NFR14 | Non-Functional Requirement 14 |
| NFR15 | Non-Functional Requirement 15 |

### Size
| ID  | Requirement |
| :-: | :---------- |
| NFR16 | The application size shall be very small in size, no more than a few megabytes. |
| NFR17 | Non-Functional Requirement 17 |
| NFR18 | Non-Functional Requirement 18 |
| NFR19 | Non-Functional Requirement 19 |
| NFR20 | Non-Functional Requirement 20 |

### Name of Feature 5
| ID  | Requirement |
| :-: | :---------- |
| NFR21 | Non-Functional Requirement 21 |
| NFR22 | Non-Functional Requirement 22 |
| NFR23 | Non-Functional Requirement 23 |
| NFR24 | Non-Functional Requirement 24 |
| NFR25 | Non-Functional Requirement 25 |

# Change management plan
Description of what this section is

# Traceability links
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