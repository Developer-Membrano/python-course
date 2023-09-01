numerical_sequence = []


def askInput():
    first_input = int(input("Let first sequence be: "))
    second_input = int(input("Let second sequence be: "))
    return first_input, second_input

def displaySequence():
    for _ in numerical_sequence:
        previous_seq = numerical_sequence[-2]
        last_seq = numerical_sequence[-1]

        next_position =  previous_seq + last_seq
        numerical_sequence.append(next_position)

        if numerical_sequence[-1] == 89:
            break

try:
    first_sequence, second_sequence = askInput()
    numerical_sequence.extend([first_sequence, second_sequence])
    numerical_sequence.sort(key=None, reverse=False)
except ValueError:
    print("Natural Numbers Only please ")

displaySequence()
print(numerical_sequence)


