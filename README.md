# Deathon Python Programming Internship

## Overview
This repository contains four Python projects developed as part of the Deathon Python Programming Internship. Each project focuses on practical programming skills, problem-solving, automation, data processing, and interactive application development.

## Projects Included

### Task 1: Hangman Word Guessing Game
**Description:** A console-based word guessing game in which the player attempts to identify a hidden word by guessing letters.

**Features:**
- Random word selection from a supplied word list.
- Maximum of six incorrect guesses.
- ASCII hangman artwork that updates after incorrect guesses.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Displays win or loss messages.

**Technologies:** Python 3, `random`

**Main file:** `hangman.py`

### Task 2: Stock Portfolio Performance Tracker
**Description:** A Python application that tracks stock portfolio investments and calculates portfolio performance.

**Features:**
- Accepts stock tickers, purchase prices, and quantities.
- Calculates invested capital and current portfolio value.
- Calculates gains or losses and their percentages.
- Generates a CSV portfolio summary.

**Technologies:** Python 3, CSV processing

**Main file:** `portfolio.py`

**Output file:** `portfolio_summary.csv`

### Task 3: Automated File Organizer and Cleanup Utility
**Description:** A Python utility that organizes files into appropriate folders based on file types and helps simplify file management.

**Features:**
- Identifies files by their extensions.
- Organizes files into categorized folders.
- Uses file-management operations to move files.
- Improves folder organization and reduces manual effort.

**Technologies:** Python 3, `os`, `shutil`, `pathlib`

**Main file:** `file_organizer.py`

### Task 4: Rule-Based Interactive Terminal Assistant / Chatbot
**Description:** An interactive customer support chatbot that recognizes user intents and responds to frequently asked questions using predefined rules.

**Features:**
- Recognizes greetings and common customer queries.
- Answers questions about business hours.
- Provides internship project submission instructions.
- Provides certificate processing information.
- Uses regular expressions for intent matching.
- Supports multiple intents in a single message.
- Normalizes user input and handles empty messages.
- Provides fallback responses for unknown queries.
- Supports `bye`, `exit`, and `quit` commands.
- Handles missing or invalid FAQ data gracefully.

**Technologies:** Python 3, `re`, `json`, `pathlib`

**Main file:** `chatbot.py`

**Data file:** `faqs.json`

## Repository Structure

```text
Deathon_Python_Programming_Internship/
│
├── Task1_Hangman_Game/
│   ├── hangman.py
│   ├── words.txt
│   └── README.md
│
├── Task2_Stock_Portfolio_Tracker/
│   ├── portfolio.py
│   ├── README.md
│   └── portfolio_summary.csv
│
├── Task3_File_Organizer/
│   ├── file_organizer.py
│   └── README.md
│
├── Task4_Customer_Support_Chatbot/
│   ├── chatbot.py
│   ├── faqs.json
│   └── README.md

```


## Requirements
- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.
- A terminal or command prompt.

## How to Run the Projects

Open a terminal in the relevant project folder and run the corresponding command.

**Task 1 — Hangman Game**
```bash
python hangman.py
```

**Task 2 — Stock Portfolio Tracker**
```bash
python portfolio.py
```

**Task 3 — File Organizer**
```bash
python file_organizer.py
```

**Task 4 — Customer Support Chatbot**
```bash
python chatbot.py
```

On some systems, use `python3` instead of `python`.

## Learning Outcomes
Through these projects, I practised:
- Python functions, loops, conditionals, and modular programming.
- Lists, dictionaries, strings, and random selection.
- File handling and directory management.
- CSV data processing.
- Regular expressions and JSON data handling.
- Exception handling and input validation.
- Building interactive terminal applications.
- Organizing code into separate project folders.
- Using GitHub to manage and present project work.

## Conclusion
These four projects demonstrate the practical application of Python programming concepts to games, portfolio analysis, file automation, and rule-based conversational systems.

This repository represents my practical work and learning progress during the Deathon Python Programming Internship.

**Internship:** Deathon Python Programming Internship  
**Language:** Python 3  
**Repository:** Deathon_Python_Programming_Internship


