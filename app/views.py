from flask import Blueprint, render_template
from flask_socketio import send
from openai import OpenAI
from . import socketio

client = OpenAI()

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f"Chatbot: {message}")
    response = chat_with_bot(message)
    send(response, broadcast=True)


def chat_with_bot(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a friendly AI assistant who loves helping the user with any issues they might have or to just have a simple conversation."},
        {"role": "user", "content": f"{prompt}"}
    ]
    )
    return response.choices[0].message.content.strip()
