from copy import deepcopy
from abc import abstractmethod


class Inventory:
    def __init__(self, damage=0, health=0):
        self.items = []
        self.damage= damage
        self.health = health
        self.defence = False
        self.active_buffs = []
        self.buffs_activated = False

    def take_item(self, entity):
        entity.enabled = False
        item = deepcopy(entity.get_items())
        if len(item) != 0:
            self.items += item

    def add_item(self, item):
        self.items.append(item)
    
    def use_item(self, item_num):
        self.items[item_num].use(self)
        del self.items[item_num]

    def add_damage(self, damage):
        self.damage += damage

    def add_health(self, health):
        self.health += health

    # Use this method for fights as it updates the
    # buffs on the base stats
    def get_combat_stats(self):
        self.activate_active_buffs()
        return (self.health, self.damage)

    def activate_active_buffs(self):
        if self.buffs_activated:
            return
        self.buffs_activated = True
        for buff in self.active_buffs:
            buff.activate(self)

    def get_health(self):
        self.activate_active_buffs()
        return self.health

    def get_damage(self):
        self.activate_active_buffs()
        return self.damage

    def set_defence(self, defence):
        self.defence = defence

    def get_defence(self):
        self.activate_active_buffs()
        return self.defence

    def lose_inventory(self):
        items = self.items
        self.items = []
        return items

    def get_items(self):
        return self.items

    # Call on turn end
    def reset_buffs(self):
        buffs_to_remove = []
        for indx in range(len(self.active_buffs)):
            buff = self.active_buffs[indx]
            buff.revert_buff_use(self)
            if not buff.round_pass():
                buffs_to_remove.append(indx)

        self.defence = False
        self.buffs_activated = False

        for i in buffs_to_remove[::-1]:
            del self.active_buffs[buffs_to_remove[i]]

    def __str__(self):
        return_str = "Your inventory contains:\n"
        for item in self.items:
            return_str += str(item)
        return return_str

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    inv = Inventory(50, 50)

    from Buff import Buff
    from Item import BuffedItem
    from game_map.entities import Treasure

    buff = Buff(damage=10, health=10,active_rounds=2)
    item = BuffedItem(buff)

    tr = Treasure(1, 2, [buff])
    inv.take_item(tr)
    inv.use_item(0)
    print('USED')

    print(inv.health, inv.damage)
    print(inv.get_combat_stats())
    inv.reset_buffs()
    # End round

    print(inv.get_combat_stats())
    inv.reset_buffs()
    # End round

    print(inv.get_combat_stats())
    inv.reset_buffs()
    # End round

    print(inv.get_combat_stats())
    inv.reset_buffs()
