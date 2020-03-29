# Programmer: Matthew Landes
# Date:		  March 21, 2020


def addToInventory(inventory, addItems):
	for i in addItems:
		if i in inventory:
			inventory[i] = inventory.get(i) + 1
		else:
			inventory[i] = 1
	return inventory
	
def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total = item_total + v
	print('Total number of items: ' + str(item_total))


stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)