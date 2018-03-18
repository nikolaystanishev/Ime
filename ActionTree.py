from math import inf
from copy import deepcopy

from FightingMechanics import Fight, BattleAction


class ActionTree:
    def __init__(self, pl_inv, en_inv):
        self.actions = [BattleAction.ATTACK, BattleAction.DEFEND, 'use']
        self.pl_inv = pl_inv
        self.en_inv = en_inv
        self.wins = 0

    def generate_tree(self, level=3):
        tree = Node(deepcopy(self.pl_inv), deepcopy(self.en_inv), None, None)
        self.add_children(tree, True, 0)
        self.path = []
        return tree

    def add_children(self, node, player_turn: bool, level):
        for action in self.actions:
            if player_turn:
                pl_inv, en_inv = deepcopy(node.pl_inv), deepcopy(node.en_inv)
            else:
                en_inv, pl_inv = deepcopy(node.pl_inv), deepcopy(node.en_inv)
            fight = Fight(pl_inv, en_inv)
            if type(action) is str:
                for item in pl_inv.items:
                    fight.execute_use(pl_inv, inv.items.index(item))
            else:
                fight.execute_action(action, pl_inv, en_inv)
            
            if not player_turn:
                pl_inv, en_inv = en_inv, pl_inv

            node.add_node(Node(pl_inv, en_inv, action, node))

        for curr_node in node.nodes:
            if pl_inv.health <= 0 or en_inv.health <= 0:
                self.wins +=1

            if level == 3:
                return

            self.add_children(curr_node, not player_turn, level+1)
            

    def minimax(self, node, maximizing_player, depth=3):
        # print(depth, len(node.nodes))
        if depth == 0 or len(node.nodes) == 0:
            return (node.en_inv.health - node.pl_inv.health, node)

        if maximizing_player:
            best_value =  inf * (-1)
            for child in node.nodes:
                val, action = self.minimax(child, False, depth - 1)
                best_value = max(best_value, val)
            return (best_value, action)
        else:
            best_value = inf
            for child in node.nodes:
                val, action = self.minimax(child, True, depth - 1)
                best_value = min(best_value, val)
            return (best_value, action)


class Node:

    def __init__(self, pl_inv, en_inv, action, parent):
        self.pl_inv = pl_inv
        self.en_inv = en_inv
        self.action = action
        self.parent = parent
        self.nodes  = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return str(self.pl_inv.health) + ' ' + str(type(self.action)) + ' ' + str(self.en_inv.health)

    def __repr__(self):
        return self.__str__()


def dfs(node):
    for child in node.nodes:
        print(child)
        dfs(child)


if __name__ == '__main__':
    from Inventory import Inventory

    pl_inv = Inventory(20, 50)
    en_inv = Inventory(10, 90)

    at = ActionTree(pl_inv, en_inv)
    tree = at.generate_tree()
    # dfs(tree)
    num, node = at.minimax(tree, True)
    print(node.parent.parent)