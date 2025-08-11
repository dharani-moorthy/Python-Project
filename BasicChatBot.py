while True:
    Input = input("You: ").lower().strip()
    if Input == "hi":
        print("Hello")
    elif Input == "how are you":
        print("I'm fine,thanks!")
    elif Input == "bye":
        print("Goodbye!")
        break
    else:
        print("invalid")

