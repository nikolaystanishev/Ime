from Inventory import Inventory
from Item import HealingItem, DamageItem
from typing import Type, Tuple
from battle_action import BattleAction


class Fight:
    def __init__(self, player_inventory, enemy_inventory):
        self.player_inventory = player_inventory
        self.enemy_inventory = enemy_inventory
        self.actions = {
            BattleAction.ATTACK: self.attack,
            BattleAction.DEFEND: self.defend
        }

    def execute_player_action(self, action: Type[BattleAction]):
        self.actions[action](self.player_inventory, self.enemy_inventory)
        self.player_turn = False

    def execute_player_use(self, item: int):
        self.player_inventory.use_item(item)
        self.player_turn = False

    # CLS should be from type ActionTree 
    def execute_enemy_action(self, cls):
        # For now just Attack
        at = cls(self.enemy_inventory, self.player_inventory)
        action = at.get_move()
        if type(action) is str:
            # print("ADD USE SUPPORT")
            return
        self.actions[action](self.enemy_inventory, self.player_inventory)

    def attack(self, from_inv: Type[Inventory], to_inv: Type[Inventory]):
        dmg = from_inv.get_damage()
        if to_inv.get_defence(): 
            dmg = int(dmg * 0.7)
        to_inv.add_health(-dmg)

    def defend(self, inv, *args):
        inv.set_defence(True)
    
    def get_player_inventory(self):
        return self.player_inventory

    def get_enemy_inventory(self):
        return self.enemy_inventory

    def is_battle_over(self):
        if(self.player_inventory.get_health() <= 0 or self.enemy_inventory.get_health() <= 0):
            return True
        return False



    # Methods for the tree generation: 
    def execute_action(self, action: Type[BattleAction], from_inv, to_inv):
        self.actions[action](from_inv, to_inv)

    def execute_use(self, inv, item_indx: int):
        inv.use_item(item_indx)

if __name__ == '__main__':
    pl = Inventory(10, 1000)
    pl.items =  [HealingItem(1000), DamageItem(50)]
    ai = Inventory(40, 1000)
    ai.items = [DamageItem(200), HealingItem(-150)]
    fm = Fight(pl, ai)
    fm.execute_player_action(BattleAction.ATTACK)
    fm.execute_enemy_action()
    print(pl.health)
    fm.execute_player_action(BattleAction.DEFEND)
    fm.execute_enemy_action()
    fm.reset_effects()
    fm.execute_enemy_action()
    print(pl.health)
    fm.execute_player_use(1)
    print(pl.get_combat_stats())
    fm.execute_player_use(0)
    print(pl.get_combat_stats())
    fm.execute_enemy_action()
    fm.execute_enemy_action()
    print(pl.get_combat_stats())
