
import json
import re
from pathlib import Path


# Load FAQ data
def load_data():
    file_path = Path(__file__).parent / "faqs.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error loading FAQ data: {error}")
        return {"greetings": [], "faqs": []}


data = load_data()


def normalize(text):
    """Convert input to lowercase and remove extra spaces."""
    return re.sub(r"\s+", " ", text.lower()).strip()


def find_intents(message):
    """Identify one or more intents in the user's message."""
    intents = []

    if re.search(r"\b(hello|hi|hey|good morning|good afternoon)\b", message):
        intents.append("greeting")

    if re.search(r"\b(hours?|timings?|open|close|operation)\b", message):
        intents.append("hours")

    if re.search(r"\b(submit|submission|upload|project|github|repository)\b", message):
        intents.append("submission")

    if re.search(r"\b(certificate|certification|when will i receive)\b", message):
        intents.append("certificate")

    return intents


def get_response(message):
    """Generate contextual responses for recognized intents."""
    intents = find_intents(message)
    responses = []

    for intent in intents:
        if intent == "greeting":
            responses.append("Hello! Welcome to Deathon Support. How can I help you?")

        elif intent == "hours":
            responses.append(
                "We operate Monday through Friday from 9:00 AM to 6:00 PM IST."
            )

        elif intent == "submission":
            responses.append(
                "You can submit your public GitHub repository link through your Student Workspace."
            )

        elif intent == "certificate":
            responses.append(
                "Certificates are reviewed and issued within 3-5 business days after your code review."
            )

    if responses:
        return "\n".join(responses)

    return (
        "I'm sorry, I didn't understand that. "
        "You can ask about business hours, project submission, or certificates."
    )


def chatbot():
    """Run the interactive terminal chatbot."""
    print("=" * 45)
    print("       DEATHON CUSTOMER SUPPORT BOT")
    print("=" * 45)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("You can ask more than one question in a message.")

    while True:
        try:
            user_input = input("\nYou: ")
            message = normalize(user_input)

            if not message:
                print("Bot: Please enter a question.")
                continue

            if re.fullmatch(r"(bye|exit|quit)", message):
                print("Bot: Thank you for chatting with Deathon Support. Goodbye!")
                break

            response = get_response(message)
            print(f"Bot: {response}")

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat ended. Goodbye!")
            break


if __name__ == "__main__":
    chatbot()
