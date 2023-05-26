from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain


# Twilio, Flask, ngrok, langchain
#personal key
os.environ["OPENAI_API_KEY"] = "<API KEY>"
openai.api_key = os.getenv("OPENAI_API_KEY")


#adding memory
llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

#using Flask app
app = Flask(__name__)

@app.route("/gpt", methods=['POST'])

def getinpt():
  
    input = request.form['Body'].lower()
    print(input)   

    reply = MessagingResponse()
    response = conversation.predict(input=input)

    
    reply.message(response)
    print(response)

    return str(reply)

if __name__ == "__main__":
    app.run(debug=True)
