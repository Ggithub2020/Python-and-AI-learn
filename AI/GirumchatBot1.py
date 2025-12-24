from flask import Flask, request, jsonify, render_template
import pandas as pd
import gradio  as gr

df = pd.read_csv("C:\Python_and_AI _Yayobe\AI\dataset\dev_dataset.csv", encoding='ISO-8859-1')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictchat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()
    #Try matching from dataset
    matched =df[df['question'].str.lower().str.contains(user_input, na=False)]
    if not matched.empty:
        response = matched.iloc[0]['answer']
    elif 'hi' in user_input or 'hello' in user_input:
      response = "Hello! This is Girum Power BI Support Assistant. How can I help you today?"
    elif 'your name' in user_input:
        response = "I am a chatbot created to assist you."
    elif 'goodbye' in user_input or 'bye' in user_input:
        response = "Goodbye! Have a great day!"
    elif 'help' in user_input:
        response = "Sure! What do you need help with?"
    elif 'thank you' in user_input or 'thanks' in user_input:
        response = "You're welcome! If you have any more questions, feel free to ask."
    else:
        response = "Sorry, I didn't understand that. Can you please rephrase?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)



import gradio as gr

# Define a simple chat function (replace this with your actual function)
def chat(message, history=[]):
    history = history or []
    history.append(("User", message))
    response = f"Echo: {message}"  # Example response
    history.append(("Bot", response))
    return history

# Launch the chat interface
gr.ChatInterface(chat, type="messages").launch()
