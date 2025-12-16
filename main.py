print("🤖 Welcome to CodeSensei")

while True:
    question = input("Ask me a coding question (type exit to quit): ").lower()

    if question == "exit":
        print("CodeSensei: Bye! Happy coding 👋")
        break

    elif "python" in question:
        print("CodeSensei: Python is a beginner-friendly programming language 🐍")

    elif "c" in question:
        print("CodeSensei: C is a powerful low-level programming language ⚙")

    elif "embedded" in question:
        print("CodeSensei: Embedded systems control hardware using software 🔌")

    else:
        print("CodeSensei: I am still learning this topic 😊")