import requests
import os

api_key = os.getenv("???") # sets up API key, need to add your own openai key
url = "???" # need to add the url needed
headers = {"api-key": api_key}

# sets the back and force with the AI from your key
def send_message(user_message, thread_id):
    body = {"message": user_message}
    if thread_id:
        body["threadId"] = thread_id
    response = requests.post(url, headers=headers, json=body)
    return response.json()

# sets the initial thread number to none
current_thread_id = None

# welcome message - explanations
print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new thread for you.\n")

# opens a thread list for savegards
threads = []

# begins the interaction loop
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit": # allow user to exit the loop
        break
    elif user_message.lower() == "new": # allow use to create new threads
        current_thread_id = None
        print("A new thread began")
        continue

    response_data = send_message(user_message, current_thread_id) # send message to AI

    # gets the response from AI
    latest_message = response_data.get("response")
    current_thread_id = response_data.get("threadId")

    # print AI response readibly
    print(f"GPT: {latest_message}")

    # adds threads id to the list for tracking purposes
    threads.append(current_thread_id)
