unprinted_designs = ['One Piece', 'Naruto', 'Bleach', 'Fairy Tale']
completed_designs = []

def print_models(unprinted_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing Model: {current_design}')

        #append to completed design each
        completed_designs.append(current_design)

def show_completed_models(completed_designs):    
    for design in sorted(completed_designs):
        print(f"Printing Complete for {design}")



print_models(unprinted_designs[:])
print('-------------------------')
show_completed_models(completed_designs)
print('-------------------------')
print(unprinted_designs)