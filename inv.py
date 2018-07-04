inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)
print()
inventory['pocket'] = ('seashell','strange berry','lint')
print(inventory)
print()
inventory['backpack'].remove('dagger') 
print(inventory)
print()
g=inventory['gold']
inventory['gold'] = g+50
print(inventory)
