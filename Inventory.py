from copy import deepcopy
from abc import abstractmethod

class Inventory:
	def __init__(self, damage=0, health=0):
		self.items = []
		self.damage= damage
		self.health = health

	def take_item(self, entity):
		item = deepcopy(entity.get_items())
		if len(item) != 0:
			self.items += item
	
	def use_item(self, item_num):
		self.items[item_num].use()

	def add_damage(self, damage):
		self.damage += damage

	def add_health(self, health):
		self.health += health

	def get_combat_stats(self):
		return (self.health, self.damage)

	def lose_inventory(self):
		items = self.items
		self.items = []
		return items

	def __str__(self):
		return_str = "|Your inventory contains:\n"
		for item in self.items:
			return_str += str(item)
		return_str += '|'
		return return_str