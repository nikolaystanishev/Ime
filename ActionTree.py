from math import inf
from copy import deepcopy
# from functools import lru_cache

from FightingMechanics import Fight, BattleAction


class ActionTree:
    
    def __init__(self, pl_inv, en_inv):
        self.actions = [BattleAction.ATTACK, BattleAction.DEFEND, 'use']
        self.pl_inv = pl_inv
        self.en_inv = en_inv
        self.wins = 0
        self.max_depth = 10

    def generate_tree(self):
        tree = Node(deepcopy(self.pl_inv), deepcopy(self.en_inv), None, None)
        self.add_children(tree, True, 0)
        self.path = []
        return tree

    def add_children(self, node, player_turn: bool, level):
        if node.is_terminal():
            return

        for action in self.actions:
            if player_turn:
                pl_inv, en_inv = deepcopy(node.pl_inv), deepcopy(node.en_inv)
            else:
                en_inv, pl_inv = deepcopy(node.pl_inv), deepcopy(node.en_inv)

            fight = Fight(pl_inv, en_inv)
            if type(action) is str:
                for item in pl_inv.items:
                    fight.execute_use(pl_inv, pl_inv.items.index(item))
            else:
                fight.execute_action(action, pl_inv, en_inv)

            if not player_turn:
                pl_inv, en_inv = en_inv, pl_inv

            candidate_node = Node(pl_inv, en_inv, action, node)
            node.check_add_node(candidate_node)

        for curr_node in node.nodes:
            if pl_inv.health <= 0 or en_inv.health <= 0:
                return

            if level == self.max_depth:
                return

            self.add_children(curr_node, not player_turn, level+1)
            

    # @lru_cache(maxsize=None)
    def minimax(self, node, maximizing_player, depth=30):
        if node.en_inv.health <= 0:
            return (1, node)

        if node.pl_inv.health <= 0:
            return (0, node)

        if depth == 0 or len(node.nodes) == 0:
            return ((node.pl_inv.health)/(node.en_inv.health+node.pl_inv.health+0.001), node)

        values=[]
        nodes=[]
        if maximizing_player:
            best_value = inf * (-1)
            cool_node = node
            for child in node.nodes:
                val, parent_node = self.minimax(child, False, depth - 1)
                values+=[val]
                nodes+=[parent_node]
                if val > best_value:
                    cool_node = parent_node
                best_value = max(best_value, val)

            return (best_value, cool_node)
        else:
            best_value = inf
            cool_node = node
            for child in node.nodes:
                val, parent_node = self.minimax(child, True, depth - 1)
                values+=[val]
                nodes+=[parent_node]
                if val < best_value:
                    cool_node = parent_node
                best_value = min(best_value, val)
            return (best_value, cool_node)


class Node:

    def __init__(self, pl_inv, en_inv, action, parent):
        self.pl_inv = pl_inv
        self.en_inv = en_inv
        self.action = action
        self.parent = parent
        self.nodes  = []

    def is_terminal(self):
        return self.pl_inv.health<=0 or self.en_inv.health<=0

    def add_node(self, node):
        self.nodes.append(node)

    def check_add_node(self, node):
        parent = node.parent
        while parent is not None:
            parent = parent.parent
            if parent == node:
                return False
        self.nodes.append(node)        

    def __eq__(self, other):
        return self.pl_inv == pl_inv and \
               self.en_inv == en_inv

    def __str__(self):
        return str(self.pl_inv.health) + ' ' + str(self.action) + ' ' + str(self.en_inv.health)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return 1027 * (self.pl_inv.health + self.pl_inv.damage) + 2097 * (self.en_inv.health + self.en_inv.damage)


def dfs(node):
    for child in node.nodes:
        print(child)
        dfs(child)


if __name__ == '__main__':
    from Inventory import Inventory
    from Item import HealingItem
    from game_map.entities import Treasure
    t = Treasure(0, 0, [HealingItem(20)])
    pl_inv = Inventory(2,3)
    pl_inv.take_item(t)
    en_inv = Inventory(4,4)

    at = ActionTree(pl_inv, en_inv)
    tree = at.generate_tree()
    # dfs(tree)
    num, node = at.minimax(tree, True, depth=10)
    print(num)
    parent = node
    while parent is not None:
        print(parent.action)
        parent = parent.parent