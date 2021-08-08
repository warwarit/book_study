list_place = ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

print(f'Original>> {list_place}\n')
print(sorted(list_place))
print(f'Original>> {list_place}\n')
print(sorted(list_place, reverse=True))
print(f'Original>> {list_place}\n')

print('=' * 80)
list_place.reverse()
print(f'Original>> {list_place}\n')
list_place.reverse()
print(f'Original>> {list_place}\n')

print('=' * 80)
print(f'Original>> {list_place}\n')
list_place.sort()
print(f'Original>> {list_place}\n')
list_place.sort(reverse=True)
print(f'Original>> {list_place}\n')