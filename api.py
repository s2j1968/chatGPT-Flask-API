from flask import Flask, request
import json
from flask import jsonify


import json
import textwrap
from os.path import exists
# from sys import argv
from revChatGPT import Chatbot



app = Flask(__name__)







# def get_input(prompt):
#     # prompt for input
#     lines = []
#     print(prompt, end="")
#     while True:
#         line = input()
#         if line == "":
#             break
#         lines.append(line)

#     # Join the lines, separated by newlines, and print the result
#     user_input = "\n".join(lines)
#     # print(user_input)
#     return user_input











@app.route('/prompt', methods=['post'])
def get_data():

    incomingData = request.get_json()
    inc_prompt = incomingData['prompt']

    prompt = inc_prompt

################### MAIN SUCCESS REESPONSE #####################
    # lines_printed = 0
    try:
        print("Chatbot: ")
        formatted_parts = []
        for message in chatbot.get_chat_response(prompt, output="stream"):
            # Split the message by newlines
            answer = message['message'].replace("\n","")
        
        print("Answer: ".format(answer))

        response = {
            "incoming prompt":inc_prompt,
            "chatGPT": answer
                }
        chatbot.reset_chat()
        return jsonify(response)

###############################################################


    except Exception as exc:
        print("Response not in correct format!")
        print(exc)
        response = {
            "incoming prompt":inc_prompt,
            "chatGPT": "Response not in correct format!"
                }

        return jsonify(response)







if __name__ == '__main__':
    ################ LOG in before the session starts ##############
    if exists("config.json"):
        with open("config.json", encoding="utf-8") as f:
            config = json.load(f)
            print("config")
       
        debug = True
        print("Logging in...")
        chatbot = Chatbot(config, debug=debug)
    else:
        print("Please create and populate config.json to ")
        exit()
    ################# STARTS SERVER ###########################
    from waitress import serve
    serve(app,port=8080)
    # app.run()