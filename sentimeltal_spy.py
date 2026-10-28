from textblob import TextBlob

print(f"Welcome to Sentiment Spy!")
name = input(f"Please enter your name: "). strip()
if not name:
    name = "Mystery Agent"

conversation.history[]

print(f"Hello Agent", name)
print(f"Type a sentence and I will annalyze your sentence with TextBlob and show you sentiment.")
print(f"Type reset, history, " f"or exit to quit. \n")

while True:
    user_input = input(f"--").strip()
    if not user_input:
        print(f"Please enter some text or valid comment.")
        continue
    if user_input.lower() == "exit":
        print(f"\n Exiting Sentimental Spy. Goodbye Agent", name)
        break
    elif user_input.lower == "reset":
        conversation.history.clear()
        print(f"All conversation history cleared.")
        continue
