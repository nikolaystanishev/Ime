from Inventory import Inventory
from Item import HealingItem, DamageItem
from typing import Type, Tuple
import enum

class BattleAction(enum.Enum):
    ATTACK = 0
    DEFEND = 1
    USE = 2


class Fight:
    def __init__(self, player_inventory, enemy_inventory):
        self.player_inventory = player_inventory
        self.enemy_inventory = enemy_inventory
        self.actions = {
            BattleAction.ATTACK: self.attack,
            BattleAction.DEFEND: self.defend
        }

    def execute_player_action(self, action: Type[BattleAction]):
        if self.player_turn == False:
            return
        self.actions[action](self.player_inventory, self.enemy_inventory)
        self.player_turn = False

    def execute_player_use(self, item: int):
        if self.player_turn == False:
            return
        self.player_inventory.use_item(item)
        self.player_turn = False

    def execute_enemy_action(self):
        if self.player_turn == False:
            return
        # For now just Attack
        self.attack(self.enemy_inventory, self.player_inventory)
        self.player_turn = True

    def attack(self, from_inv: Type[Inventory], to_inv: Type[Inventory]):
        dmg = from_inv.get_damage()
        if to_inv.get_defence(): 
            dmg = int(dmg * 0.7)
        to_inv.add_health(-dmg)

    def defend(self, inv, *args):
        inv.set_defence(True)

    def is_battle_over(self):
        if(self.player_inventory.get_health() <= 0 or self.enemy_inventory.get_health() <= 0):
            return True
        return False



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
