name = input("Hello! My name is Alpha Ai. What is your name? ")
print("Hello there", name)
while True:
    print("How are you feeling (good, bad or neutral)?")
    mood = input().lower()
    if mood == "good":
        print("Glad to hear it!!")
    elif mood == "bad":
        print("I am sorry to hear that.")
    else:
        print("That is perfectly normal")
    hobby = input("So what are your hobbies? Or what do you do in your freetime? ")
    if "," in hobby or " and " in hobby:
        print(hobby, "are really good hobbies!")
    else:
        print(hobby, "is a really good hobby!")
    grade = int(input("What grade are you in? "))
    print("Ohh thats nice!")
    school = input("How are you doing in school right now? ")
    print("Thats good, but it can be better though.")
    again = input("Do you want to keep on chatting? (yes or no) ")
    if again == "no":
        print("Okay", name, ". Nice talking to you!")
        print("Bye Bye!")
    else:
        print("")

