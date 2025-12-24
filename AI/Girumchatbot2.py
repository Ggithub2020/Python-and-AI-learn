from flask import Flask, request, jsonify, render_template
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Python_and_AI _Yayobe\AI\dataset\dev_dataset.csv", encoding='ISO-8859-1')

app = Flask(__name__)

# Dictionary of educational websites by topic
educational_websites = {
    "python": "You can learn Python at https://www.learnpython.org/ or https://www.coursera.org/courses?query=python",
    "data science": "Check out https://www.kaggle.com/learn and https://www.coursera.org/specializations/data-science",
    "ai": "Great AI courses are on https://www.deeplearning.ai/ and https://www.edx.org/learn/artificial-intelligence",
    "machine learning": "Try https://www.coursera.org/learn/machine-learning by Andrew Ng",
    "statistics": "See https://www.khanacademy.org/math/statistics-probability",
    "power bi": "Check Microsoft Power BI docs https://learn.microsoft.com/en-us/power-bi/ or https://www.edx.org/learn/power-bi"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictchat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()

    # Try matching from dataset
    matched = df[df['question'].str.lower().str.contains(user_input, na=False)]
    if not matched.empty:
        response = matched.iloc[0]['answer']

    # Educational websites check
    elif any(keyword in user_input for keyword in educational_websites.keys()):
        for keyword, site in educational_websites.items():
            if keyword in user_input:
                response = site
                break

    elif 'hi' in user_input or 'hello' in user_input:
        response = "Hello! This is Girum Power BI Support Assistant. How can I help you today?"
    elif 'your name' in user_input:
        response = "I am a chatbot created to assist you."
    elif 'goodbye' in user_input or 'bye' in user_input:
        response = "Goodbye! Have a great day!"
    elif 'help' in user_input:
        response = "Sure! What do you need help with?"
    elif 'who created you' in user_input or 'who is your creator' in user_input:
        response = "I was created by Girum."
    elif 'what can you do' in user_input:
        response = "I can help you with Power BI related questions and provide educational resources."
    elif 'joke' in user_input:
        response = "I have no time for joking?" # Humor can be subjective
    elif 'how are you' in user_input:
        response = "I'm just a program, but thanks for asking!"
    elif 'what is ai' in user_input or 'what is artificial intelligence' in user_input:
        response = "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn."
    elif 'what is machine learning' in user_input:
        response = "Machine Learning is a subset of AI that involves the use of algorithms and statistical models to enable computers to improve their performance on a task through experience."
    elif 'thank you' in user_input or 'thanks' in user_input:
        response = "You're welcome! If you have any more questions, feel free to ask."
    elif 'sorry ' in user_input:
        response = "No worries! How can I assist you further?"
    elif 'I love you' in user_input:
        response = "I'm just a program, but I'm here to help you!"
    elif 'I hate you' in user_input:
        response = "I'm sorry to hear that. How can I improve?"
    elif ' I dont know' in user_input:
        response = "That's okay! Feel free to ask me anything."
    elif 'great' in user_input or 'awesome' in user_input:
        response = "I'm glad to hear that! How can I assist you further?"
    else:
        response = "Sorry, I didn't understand that. Can you please rephrase?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
