Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

Project Overview
This project implements a rule-based interactive customer support chatbot using Python. The chatbot recognizes user intents through keywords and regular expressions and provides relevant responses to frequently asked questions about business hours, internship project submissions, and certificates.

It runs in the terminal and supports multiple intents in a single message, input normalization, error handling, and graceful exit commands.

Objectives
- Build an interactive terminal-based chatbot.
- Recognize greetings and frequently asked questions.
- Use regular expressions for keyword and intent matching.
- Normalize user input by converting it to lowercase and removing extra whitespace.
- Handle multiple intents in one message.
- Provide fallback responses for unrecognized queries.
- Handle errors and exit commands gracefully.

Technologies Used
- Python 3
- `re` — Regular expressions and pattern matching
- `json` — Loading FAQ data
- `pathlib` — Handling file paths

Project Structure
text
Task4_Customer_Support_Chatbot/
─ chatbot.py
─ faqs.json
─ README.md


Features
1. **Greeting Recognition:** Responds to greetings such as hello, hi, hey, good morning, and good afternoon.
2. **Business Hours:** Provides operating hours: Monday to Friday, 9:00 AM to 6:00 PM IST.
3. **Project Submission Support:** Explains how to submit the public GitHub repository link through the Student Workspace.
4. **Certificate Information:** Informs users that certificates are reviewed and issued within 3–5 business days after code review.
5. **Multi-Intent Recognition:** Identifies multiple supported intents in a single message and returns relevant responses.
6. **Fallback Handling:** Guides users when their queries are not recognized.
7. **Input Normalization:** Converts input to lowercase and removes unnecessary whitespace.
8. **Graceful Exit:** Supports `bye`, `exit`, and `quit` commands.
9. **Error Handling:** Handles missing or invalid JSON data and unexpected terminal interruptions.

Installation and Execution

Prerequisites
- Python 3 installed on your system.
- A code editor such as Visual Studio Code.

Steps
1. Download or clone the project repository.
2. Open the project folder in your terminal.
3. Ensure that `chatbot.py` and `faqs.json` are in the same directory.
4. Run the following command:

bash
python chatbot.py


On some systems, you may need to use:

bash
python3 chatbot.py


Sample Interaction

```text
=============================================
       DEATHON CUSTOMER SUPPORT BOT
=============================================
Type 'bye', 'exit', or 'quit' to end the chat.
You can ask more than one question in a message.

You: hello
Bot: Hello! Welcome to Deathon Support. How can I help you?

You: What are your hours?
Bot: We operate Monday through Friday from 9:00 AM to 6:00 PM IST.

You: How do I submit my project?
Bot: You can submit your public GitHub repository link through your Student Workspace.

You: When will I receive my certificate?
Bot: Certificates are reviewed and issued within 3-5 business days after your code review.

You: bye
Bot: Thank you for chatting with Deathon Support. Goodbye!
```

Error Handling
- Displays an error message if `faqs.json` is missing or contains invalid JSON.
- Requests input again when the user submits an empty message.
- Handles `Ctrl+C` and terminal input interruptions gracefully.
- Returns a fallback response when no supported intent is detected.

Future Improvements
- Add more FAQs and supported intents.
- Improve intent matching using a confidence-scoring mechanism.
- Load all FAQ responses dynamically from the JSON dataset.
- Add conversation history and contextual follow-up questions.
- Develop a graphical user interface or web-based chatbot.

Conclusion
This project demonstrates fundamental Python programming concepts, including functions, loops, conditional statements, regular expressions, JSON file handling, and exception handling. It provides a simple and extensible foundation for building rule-based customer support assistants.


**Internship:** Deathon Python Programming Internship  
**Task:** Task 4 — Rule-Based Interactive Terminal Assistant / Chatbot  
**Language:** Python 3
