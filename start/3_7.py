list_guest = ['Djeki Chan', 'Tom Krus', 'Mila Yovovich']
print(list_guest)
list_guest[1] = 'Madonna'
print(list_guest)

print('=' * 80)

# add new gueste

list_guest.insert(0, 'Kim Kardashian') 
list_guest.insert(2, 'Sandra Balok') 
list_guest.append('Scarlet Yohonsan')

print(f'all guest a whant >> {list_guest}\n')

print('Sory but a not have big table')

sorry_messege = list_guest.pop(1)

print(f'Sorry {sorry_messege}')

print('=' * 80)

for guest in list_guest:
    print(f'Success {guest}\n')