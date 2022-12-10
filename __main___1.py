import json
import textwrap
from os.path import exists
from sys import argv

from revChatGPT import Chatbot


def get_input(prompt):
    # prompt for input
    lines = []
    print(prompt, end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and print the result
    user_input = "\n".join(lines)
    # print(user_input)
    return user_input


def main():
    if exists("config.json"):
        with open("config.json", encoding="utf-8") as f:
            config = json.load(f)
            print("config")
        if "--debug" in argv:
            print("Debugging enabled.")
            debug = True
        else:
            debug = False
        print("Logging in...")
        chatbot = Chatbot(config, debug=debug)
    else:
        print("Please create and populate config.json to continue")
        exit()

   
    # incomingData = request.get_json()
    # inc_prompt = incomingData['prompt']


    prompt = "what is water"

    if prompt.startswith("!"):

        if prompt == "!refresh":
            chatbot.refresh_session()
            print("Session refreshed.\n")
            
        elif prompt == "!rollback":
            chatbot.rollback_conversation()
            print("Chat session rolled back.")
            
        elif prompt == "!config":
            print(json.dumps(config, indent=4))
        


    lines_printed = 0
    answer = ""
    try:
        print("Chatbot: ")
        formatted_parts = []
        for message in (chatbot.get_chat_response(prompt, output="stream")):
            # # Split the message by newlines
            message_parts = message["message"].split("\n")
            # answer = answer+
            # answer = message['message']
            # Wrap each part separately
            formatted_parts = []
            for part in message_parts:
                formatted_parts.extend(
                    textwrap.wrap(part, width=80))
                for _ in formatted_parts:
                    if len(formatted_parts) > lines_printed + 1:
                        print(formatted_parts[lines_printed])
                        lines_printed += 1
        
        print(formatted_parts[lines_printed])
        # print(answer)
    except Exception as exc:
        print("Response not in correct format!")
        print(exc)
   


if __name__ == "__main__":
    main()
