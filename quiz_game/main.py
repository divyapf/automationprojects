# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

print("Welcome to the Quiz!")

playing = input("do you want to play?yes/No:   ")

if playing.lower() != "yes":
    quit()

print("okay! lets play")

answer = input("what does DNA stand for ?  ")

#str.casefold()--to ignore case sensitivity of input text

if answer.casefold() == "deoxyribonuclicacid":
    print("Correct")
else:
    print("Incorrect")

answer = input("what does CPU stand for ?  ")

if answer.casefold() == "computer processing unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("what does RAM stand for ?  ")

if answer.casefold() == "random acess memory":
    print("Correct")
else:
    print("Incorrect")
