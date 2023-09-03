
toppings = []
flag = ['quit', 'done', 'exit']
prompt = "Type the toppings you would like to add \nTo your pizza: "

while True:
    list_of_toppings = str(input(prompt))
    if list_of_toppings in flag:
        break

    toppings.append(list_of_toppings)

# for topping in toppings:
#     print(f'Rest assured I will add these {topping} to your pizza')

final_toppings = '\n'.join(toppings)
print(f'Rest assured I will add these \n{final_toppings}\nto your pizza')
    