from Inventory import Inventory
from Item import HealingItem, DamageItem
from typing import Type, Tuple

# added for testing purpose
BATTLE_ACTIONS = ['attack', 'defend', 'use']


class FightingMechanics:

    def fight(self, player_inventory: Type[Inventory], enemy_inventory: Type[Inventory]):
        turn_order = (player_inventory, enemy_inventory)
        while not self.is_dead_entity(player_inventory, enemy_inventory):
            user_inp = self.get_user_input()
            # This should be done using the input from the terminal
            if user_inp[0] == 'attack':
                self.attack(turn_order[0], turn_order[1])
            if user_inp[0] == 'use':
                turn_order[0].use_item(int(user_inp[1]))
            print(player_inventory.health)
            turn_order = FightingTurns.next_turn(turn_order[0], turn_order[1])

    # This method is added just for testing purposes
    def get_user_input(self):
        inp = input()
        inp = inp.split()
        if inp[0] in BATTLE_ACTIONS:
            return inp

    def attack(self, from_inv: Type[Inventory], to_inv: Type[Inventory]):
        dmg = from_inv.get_damage()
        to_inv.add_health(-dmg)

    def is_dead_entity(self, player_inventory: Type[Inventory], enemy_inventory: Type[Inventory]):
        return player_inventory.get_health() <= 0 or\
               enemy_inventory.get_health() <= 0


class FightingTurns:
    @classmethod
    def next_turn(turn, played_inv: Type[Inventory], to_be_played_inv: Type[Inventory]) -> Tuple[Type[Inventory], Type[Inventory]]:
        return (to_be_played_inv, played_inv)


if __name__ == '__main__':
    fm = FightingMechanics()
    pl = Inventory(10, 50)
    pl.items =  [HealingItem(1000), DamageItem(50)]
    ai = Inventory(40, 20)
    ai.items = [DamageItem(200), HealingItem(-150)]
    fm.fight(pl, ai)
