import re  # to look for numbers in variable names (invalid variable)
from sys import exit  # to exit the infinite while loop!


# From StackOverFlow
# Function that returns True if variable has digit `\d` in the name
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


while 1:  # AKA while True
    nums = ""
    while nums == "":
        # while nums is empty, nothing will happen
        nums = input()

    if nums == "/exit":
        print("Bye!")
        exit(0)
    if nums == "/help":
        print("This Program calculates the SUM and the SUB of numbers or variables")
        continue

    # when the user wants to add a variable
    if "=" in nums:
        # if the variable name, before the `=` has numbers,
        # then it is not a valid variable name
        if hasNumbers(nums.split("=")[0]):
            print("Invalid identifier")
            continue
        try:
            nums = nums.strip()
            exec(nums)
            continue
        except:
            print("Invalid assignment")
            continue

    try:
        if "//" in nums:
            print("Invalid expression")
        else:
            print(int(eval(nums)))


    except NameError:
        print("Unknown variable")
    except SyntaxError:
        if nums.startswith('/'):
            print("Unknown command")
        else:
            print("Invalid expression")
