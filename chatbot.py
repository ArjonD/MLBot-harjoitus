from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_sentences = [
    "hello", "hi", "hey",
    "how are you", "what's up", "how is it going",
    "what is your name", "who are you",
    "bye", "goodbye", "see you later",
    "tell me a joke", "make me laugh"
]

training_labels = [
    "greeting", "greeting", "greeting",
    "status", "status", "status",
    "name", "name",
    "farewell", "farewell", "farewell",
    "joke", "joke"
]

responses = {
    "greeting": "Hello! Nice to meet you.",
    "status": "Im doing great, thanks for asking.",
    "name": "im MLBot, your local chatbot.",
    "farewell": "Goodbye! Have a nice day.",
    "joke": "Why cant scientists trust atoms? Because they make up everything!"
}

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_sentences)

clf = MultinomialNB()
clf.fit(X, training_labels)

print("Chatbot is ready! Type quit to exit")
while True:
    userinput = input("You: ")
    if userinput.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    X_test = vectorizer.transform([userinput])
    predicted_intent = clf.predict(X_test)[0]

    print("Chatbot:", responses.get(predicted_intent, "Sorry, i didn't understand that."))