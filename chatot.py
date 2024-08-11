import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello,Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.Can i know your name",]
    ],
    [
        r"Why not",
        ["then what is your name",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine|I'm doing good|It's good|All fine",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"quit|Bye",
        ["Bye! Take care. See you soon.",]
    ],
    [
        r"What are you doing",
        ["Nothing much spending Time with you.",]
    ],
    [
        r"Okay",
        ["okay..!",]
    ]
]

# Default message at the start
print("Hi, I'm the chatbot you created. How can I help you today?")

# Create Chatbot
chat = Chat(pairs, reflections)

# Start conversation
chat.converse()
