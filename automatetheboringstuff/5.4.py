# Fantasy Game Inventory
#
#Imagine that a vanquished dragon’s loot is represented as a list of strings
# like this: dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin',
#                          'ruby']
# 
# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like
# dragonLoot. The addToInventory() function should return a dictionary that
# represents the updated inventory. Note that the addedItems list can contain
# multiples of the same item.

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inventory, addedItems):
    for i in addedItems:
        item = inventory.get(i, 0)
        item += 1
        inventory[i] = item
    return inventory

print(addToInventory(inventory, dragonLoot))


