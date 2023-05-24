# Import the necessary libraries
import re
from datetime import datetime

# Define a dictionary containing some basic responses
responses = {
    r"hello\b|hi\b|hey\b": "Good {time_of_day}..! How can I help you today?",
    r"help\b.*food\b.*supply\b": "We provide free food supplies for those in need.for more information Please visit our website .",
    r"create\b.*account\b": "To create an account, please visit our website and follow the registration process.",
    r"business hours\b": "Our business hours are 24 hours of day.",
    r"payment methods\b": "We accept payments through UPI and all cards .",
    r"cancel\b.*order\b": "For the cancelling order,you will get cancell option in in my orders .",
    r"customer service\b": "To get in touch with customer service, please visit our website and navigate to the contact page.",
    r"job openings\b": "To view current job openings, please visit our website and navigate to the careers page.",
    r"find\b.*product\b": "To find a specific product, please use the search function on our website or browse our product categories.",
    r"reset\b.*password\b": "To reset your password, please visit our website and follow the password reset process.",
    r"bye\b|goodbye\b": "Goodbye! Thank you for contacting us.",
}

# Define a function that returns the appropriate response
def get_response(message):
    message = message.lower()
    for pattern, response in responses.items():
        if re.search(pattern, message):
            if "{time_of_day}" in response:
                time_of_day = get_time_of_day()
                response = response.format(time_of_day=time_of_day)
            return response
    return "I'm sorry, I don't understand your request. Please try again."

# Define a function that returns the time of day
def get_time_of_day():
    now = datetime.now()
    if now.hour < 12:
        return "morning"
    elif now.hour < 18:
        return "afternoon"
    else:
        return "evening"

# Start the chat loop
while True:
    message = input("You: ")
    response = get_response(message)
    print("Bot: " + response)
    if re.search(r"bye\b|goodbye\b", message):
        break

