# Practicing creation of functions
# These are simple functions I am creating according to AI instruction
# There are not a copy of what AI told me to do but original creation
# I have some understanding on how a GUI work and try to adapt my code to it, e.g. english in all lower case to facilitate input understanding for the code


# Calculation of two variables from two parameters
def describe_rectangle(width, height):
    calculate_area = width * height
    calculate_perimeter = (width + height) * 2
    print(f"\nRectangle area: {calculate_area}")
    print(f"Rectangle perimeter: {calculate_perimeter}")

# describe_rectangle(40, 50)


# Calculate one variable from one parameter and a formulas


def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

# convert_temperature(1)


# Advance model from previous exercise, using variable parameter
# Calculates two variables, using parameters and formulas


def convert_temperature_two_ways(value, scale="C"):
    if scale == "C":
        result = (value * 9/5) + 32
        print(f"{value}°C is {result}°F")
    elif scale == "F":
        result = result = (value - 32) * 5/9
        print(f"{value}°F is {result}°C")
    else:
        print("Invalid scale! Please use 'C' for Celsius or 'F' for Fahrenheit.")

# convert_temperature_two_ways(20, C)


# Use a variable as parameter to define output based on conditions
def greet_user(name, language="english"):
    if language == "english":
        print(f"Hello, {name}")
    elif language == "francais":
        print(f"Bonjour, {name}")
    elif language == "espanol":
        print(f"Hola! {name}")
    else:
        print("Language not recognised - defaulting to English")
        print(f"Hi, {name}")

# greet_user("Thomas", "english")
