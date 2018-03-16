from abc import abstractmethod

class Item:

	@abstractmethod
	def use(inventory):
		pass

	@abstractmethod
	def __str__():
		pass

class HealingItem(Item):
	def __init__(self, heal=50):
		self.heal = heal

	def use(inventory):
		inventory.add_health(heal)

	def __str__(self):
		return "Heal yourself for {0}".format(self.heal)


class DamageItem(Item):
	def __init__(self, dmg=50):
		self.dmg = dmg

	def use(inventory):
		inventory.add_damage(damage)
