from abc import abstractmethod

class Inventory:
	def __init__(self, damage=0, health=0):
		self.items = []
		self.damage= damage
		self.health = health

	def take_item(self, entity):
		item = entity.get_items()
		if len(item) != 0:
			self.items += item
	
	def use_item(self, item_num):
		self.items[item_num].use()

	def add_damage(self, damage):
		self.damage += damage

	def add_health(self, health):
		self.health += health

	def take_combat_stats(self):
		return (self.health, self.damage)
