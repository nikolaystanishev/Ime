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

	def use(self, inventory):
		inventory.add_health(self.heal)

	def __str__(self):
		return "Heal potion! Heal yourself for {0}\n".format(self.heal)


class DamageItem(Item):
	def __init__(self, dmg=50):
		self.dmg = dmg

	def use(self, inventory):
		inventory.add_damage(self.dmg)

	def __str__(self):
		return "Damage potion! Add {0} damage to your combat stats\n".format(self.dmg)