print("Hello! I am an AI Chatbot. What is your name?")
name = input()
print("Hello there", name)
print("How are you feeling today? (good or bad)")
feeling = input().lower()
if feeling == "good":
    print("That is wonderful to hear!")
elif feeling == "bad":
    print("Oh. I am sorry to hear that. Is there something I can do to help?")
else:
    print("That is great!")