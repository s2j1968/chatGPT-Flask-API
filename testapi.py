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


        return "I am response"







if __name__ == '__main__':

    ################# STARTS SERVER ###########################
    from waitress import serve
    print("starting waitress wsgi ")
    serve(app,host="0.0.0.0",port=8080)
    print("starting waitress wsgi...")
    # app.run()