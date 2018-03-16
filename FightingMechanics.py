from Inventory import Inventory
from Item import HealingItem, DamageItem
from typing import Type, Tuple

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

    def execute_player_use(self, item: int):
        self.player_inventory.use(item)

    def evaluate_enemy_action(self):
        # For now just Attack
        self.attack(self.enemy_inventory, self.player_inventory)

    def attack(self, from_inv: Type[Inventory], to_inv: Type[Inventory]):
        dmg = from_inv.get_damage()
        if to_inv.get_defence(): 
            dmg *= 0.7
        to_inv.add_health(-dmg)

    def defend(self, inv):
        inv.set_defence(True)

    def reset_effects(self):
        self.player_inventory.set_defence(False)
        self.enemy_inventory.set_defence(False)


class BattleAction(enum.Enum):
    ATTACK = 0
    DEFEND = 1
    USE = 2


if __name__ == '__main__':
    fm = Fight()
    pl = Inventory(10, 50)
    pl.items =  [HealingItem(1000), DamageItem(50)]
    ai = Inventory(40, 20)
    ai.items = [DamageItem(200), HealingItem(-150)]
    fm.fight(pl, ai)
