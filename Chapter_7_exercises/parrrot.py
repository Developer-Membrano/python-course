prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

flag = True

while flag:
    message = input(prompt).lower()
    if message == 'quit':
        flag = False
    else:
        print(message)