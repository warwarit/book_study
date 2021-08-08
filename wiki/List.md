# List

## Change to index

```py
list_guest[1] = 'Madonna'
```

## Add

### To index

```py
list_guest.insert(0, 'Kim Kardashian') 
list_guest.insert(2, 'Sandra Balok') 
```

### To and

```py
list_guest.append('Scarlet Yohonsan')
```

## Delete

```py
sorry_messege = list_guest.pop(1)
```

## Sort

```py
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
```

* вывод

```
Original>> ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

['Amsterdam', 'Berlin', 'Praga', 'Singapur', 'Tokyo']
Original>> ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

['Tokyo', 'Singapur', 'Praga', 'Berlin', 'Amsterdam']
Original>> ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

================================================================================
Original>> ['Singapur', 'Tokyo', 'Amsterdam', 'Praga', 'Berlin']

Original>> ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

================================================================================
Original>> ['Berlin', 'Praga', 'Amsterdam', 'Tokyo', 'Singapur']

Original>> ['Amsterdam', 'Berlin', 'Praga', 'Singapur', 'Tokyo']

Original>> ['Tokyo', 'Singapur', 'Praga', 'Berlin', 'Amsterdam']
```
