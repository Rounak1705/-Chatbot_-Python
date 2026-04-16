# -Chatbot_-Python
🤖 Smart Chatbot in Python

A simple rule-based chatbot built using Python and basic NLP techniques.
This chatbot can respond to greetings, questions, small talk, and more.

---

🚀 Features

- Responds to greetings (hello, hi, etc.)
- Answers basic questions
- Handles small talk and jokes
- Responds to thanks
- Simple NLP using tokenization and stemming
- No internet required (offline working)

---

🛠️ Technologies Used

- Python 🐍
- NLTK (Natural Language Toolkit)
- Random module

---

📁 Project Structure

Chatbot/
│── chatbot.py     # Main chatbot logic
│── data.py        # Dataset (intents & responses)
│── README.md      # Project documentation

---

⚙️ How It Works

1. User enters a message
2. Input is converted to lowercase and tokenized
3. Words are stemmed using PorterStemmer
4. Input is matched with predefined patterns
5. A random response is returned

---

▶️ How to Run

1. Clone the repository:

git clone https://github.com/your-username/chatbot.git

2. Navigate to project folder:

cd chatbot

3. Run the chatbot:

python chatbot.py

---

💬 Example

Chatbot: I am your chatbot here. Type 'exit' to end the conversation.

You: hi  
Chatbot: Hello!

You: how are you  
Chatbot: I'm doing great! Thanks for asking.

You: thanks  
Chatbot: You're welcome!

---

⚠️ Notes

- This is a rule-based chatbot (not AI-based like ChatGPT)
- Uses simple ".split()" instead of NLTK tokenizer (no download issues)
- Can be extended with more data and smarter logic

---

🔮 Future Improvements

- Add GUI using Tkinter
- Add voice input/output
- Use machine learning for better responses
- Deploy as a web app

---

👨‍💻 Author

Rounak Pan

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
