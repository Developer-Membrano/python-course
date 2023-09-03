
messages = ['Sit cillum non sit aliqua .', 
            'Proident veniam esse veniam adipisicing.',
            'Elit deserunt in cillum cupidatat cillum non elit dolore nostrud do.',
            'Officia ad eu ad magna nisi ex.']

sent_messages = []


def show_message(_messages):
    for message in _messages:
       print(f"Sending message: {message}.... ")
       sent_messages.append(message)
       

def send_messages(sent_messages):
    for received_messages in sent_messages:
        print(f"Message received: {received_messages}")

show_message(messages[:])
print("--------------------------")
send_messages(sent_messages)
print("--------------------------")
