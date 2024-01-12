text = input('Type Sum!! ')

result = text.find("the")

if result == -1:
    print("The word the is not in the string. ")
else:
    print("The word the is in the string. ")
    print(text.index("the"))


