***********Python Chatbot Application***************

A simple and interactive chatbot application built with Python. This project combines speech recognition, text-to-speech synthesis, and a graphical user interface (GUI) for an engaging user experience.

Key Features
Voice and Text Interaction: Interact via voice commands or text input.
Text-to-Speech Output: Chatbot responds aloud using pyttsx3.
Predefined Responses: Answers common queries effectively.
Continuous Listening: Multithreading ensures seamless voice input.
User-Friendly GUI: Features a chatbot avatar, chat history, and input field.
Libraries Used
pyttsx3: For text-to-speech.
SpeechRecognition: Converts voice to text.
Tkinter: GUI development.
Pillow: Displays the chatbot avatar.
Threading: Handles continuous listening.
How It Works
Launch: Opens a Tkinter GUI with the chatbot avatar.
Input: Accepts voice or text queries.
Response: Matches queries with predefined responses.
Output: Displays response in chat and speaks it aloud.
Extensibility
Enhance this project by:

Adding real-time APIs (e.g., weather, news).
Implementing NLP for smarter conversations.
Personalizing user interactions.
Prerequisites
Python 3.6+
Install dependencies:
bash

pip install pyttsx3 speechrecognition pillow
Usage
Clone the repository:
bash

git clone https://github.com/your-username/python-chatbot.git
cd python-chatbot
Add the chatbot avatar image (bot3.png) to the directory.
Run the chatbot:
bash

python chatbot.py
Example Queries
"Hello"
"What is your name?"
"Tell me a joke"
"How are you?"

Acknowledgements
Developed by Sahazad Alam Ansiri
