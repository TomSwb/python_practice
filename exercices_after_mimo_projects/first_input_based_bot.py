def learn_more():
    choice = input("Do you want to learn more? (yes/no) ").lower()
    if choice == "yes":
        return True
    else:
        print("Thank you for chatting with me, I hope you learned something new today!")
        print("Goodbye!")
        return False


def beginner_level():
    while True:
        print("I can help you with the following topics:")
        print("1. Variables")
        print("2. Data Types")
        choice = input(
            "Please choose a topic by entering the corresponding number: ")

        if choice == "1":
            print("Great choice! Let's talk about variables.")
            print("In Python, a variable is a name that refers to a value.")
            print(
                "You can create a variable by assigning a value to it using the '=' operator.")
            print("For example:")
            print("name = 'John'")
            print(
                "This creates a variable called 'name' that refers to the string 'John'.")
            print(
                "Now it's your turn! Create a variable called 'age' and assign it your age.")
            age = input("Enter your age: ")
            print(
                f"Great job! You've created a variable called 'age' with the value {age}.")
        elif choice == "2":
            print("Awesome! Let's talk about data types.")
            print("In Python, there are several built-in data types.")
            print("The most common ones are:")
            print("1. int (integer)")
            print("2. float (floating-point number)")
            print("3. str (string)")
            print("4. bool (boolean)")
            print("You can check the type of a variable using the 'type()' function.")
            print("For example:")
            print("age = 25")
            print("print(type(age))")
            print("This will print '<class 'int'>' to the console.")
        else:
            print("I don't recognize that choice, but I'm here to help you regardless!")

        if not learn_more():
            break


def intermediate_level():
    while True:
        print("I can help you with the following topics:")
        print("1. Functions")
        print("2. Loops")
        choice = input(
            "Please choose a topic by entering the corresponding number: ")

        if choice == "1":
            print("Great choice! Let's talk about functions.")
            print("A function is a block of reusable code that performs a specific task.")
            print("You can define a function using the 'def' keyword.")
            print("For example:")
            print("def greet():")
            print("    print('Hello!')")
            print("Now it's your turn! Create a function that prints your name.")
            print("Try it out in your Python environment!")
        elif choice == "2":
            print("Awesome! Let's talk about loops.")
            print("Loops allow you to repeat a block of code multiple times.")
            print("For example, a 'for' loop can iterate over a range of numbers:")
            print("for i in range(5):")
            print("    print(i)")
            print("This will print the numbers 0 to 4.")
            print("Now it's your turn! Write a loop that prints the numbers 1 to 10.")
            print("Try it out in your Python environment!")
        else:
            print("I don't recognize that choice, but I'm here to help you regardless!")

        if not learn_more():
            break


def advanced_level():
    while True:
        print("I can help you with the following topics:")
        print("1. Decorators")
        print("2. Generators")
        choice = input(
            "Please choose a topic by entering the corresponding number: ")

        if choice == "1":
            print("Great choice! Let's talk about decorators.")
            print(
                "A decorator is a function that modifies the behavior of another function.")
            print("For example:")
            print("@decorator")
            print("def my_function():")
            print("    pass")
            print(
                "Now it's your turn! Create a simple decorator that prints 'Hello' before calling a function.")
            print("Try it out in your Python environment!")
        elif choice == "2":
            print("Awesome! Let's talk about generators.")
            print(
                "A generator is a function that yields values one at a time using the 'yield' keyword.")
            print("For example:")
            print("def my_generator():")
            print("    yield 1")
            print("    yield 2")
            print("    yield 3")
            print(
                "Now it's your turn! Create a generator that yields the first 5 square numbers.")
            print("Try it out in your Python environment!")
        else:
            print("I don't recognize that choice, but I'm here to help you regardless!")

        if not learn_more():
            break


# Main program
name = input("Hi! What is your name, dear human? ")
print(
    f"Hello {name}, I am a bot, and I am here to help you with your Python journey.")

while True:
    level = input(
        "What is your level in Python? (beginner, intermediate, advanced) ").lower()

    if level == "beginner":
        print("That's great! Everyone starts somewhere. Let's learn together!")
        beginner_level()
    elif level == "intermediate":
        print("Awesome! You have a good grasp of Python. Let's take it to the next level!")
        intermediate_level()
    elif level == "advanced":
        print("Impressive! You're a Python pro. Let's dive into some advanced topics!")
        advanced_level()
    else:
        print("I don't recognize that level, but I'm here to help you regardless!")
        print("Let's start with the beginner level!")
        beginner_level()

    if not learn_more():
        break

print("Congratulations on completing your Python journey! Thank you for chatting with me. Goodbye!")
