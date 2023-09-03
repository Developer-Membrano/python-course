
def make_shirt(text_design, size="Large" ):
    prompt = f'{text_design.title()} will be display in front of the T-shirt \nwith a size of {size}'
    return prompt

avatar = make_shirt('Aang the Avatar', 'Medium')
naruto = make_shirt( size= 'Large', text_design='Naruto fighting sasuke')
onepiece = make_shirt('Luffy and Zoro')

print(avatar)
print(naruto)
print(onepiece)