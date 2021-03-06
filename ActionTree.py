from math import inf
from copy import deepcopy
# from functools import lru_cache
from FightingMechanics import Fight, BattleAction
from battle_action import BattleAction


class ActionTree:
    
    def __init__(self, pl_inv, en_inv,max_depth=10):
        self.actions = [BattleAction.ATTACK, BattleAction.DEFEND, 'use']
        self.pl_inv = pl_inv
        self.en_inv = en_inv
        self.wins = 0
        self.max_depth = max_depth

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
    def minimax(self, node, maximizing_player, depth=3):
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

    def get_move(self):
        tree = self.generate_tree()
        num, parent = self.minimax(tree, True, depth=3)
        actions = []
        while parent is not None:
            actions.append(parent.action)
            parent = parent.parent
        actions = actions[::-1]
        # The 0 is the None for the Head/Start of the Tree
        # If he dies instantly it feels bad man
        if len(actions) == 1:
            return BattleAction.DEFEND
        return actions[1]

    def alphabeta(self, node, maximizing_player,alpha,beta, depth=30):
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
                alpha=max(alpha,best_value)
                if beta<=alpha:
                    break

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
                beta=min(beta,best_value)
                if beta<=alpha:
                    break
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
        if other == None:
            return False
        return self.pl_inv == other.pl_inv and \
               self.en_inv == other.en_inv

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
    from Item import HealingItem, DamageItem
    pl = Inventory(2, 5)
    pl.items =  [HealingItem(1000), DamageItem(50)]
    ai = Inventory(40, 3)
    ai.items = [DamageItem(200), HealingItem(-150)]
    fm = Fight(pl, ai)
    fm.execute_player_action(BattleAction.ATTACK)
    fm.execute_enemy_action(ActionTree)
    fm.execute_player_action(BattleAction.DEFEND)
    fm.execute_enemy_action(ActionTree)
    fm.execute_enemy_action(ActionTree)
    print(pl.health)
    fm.execute_player_use(1)
    print(pl.get_combat_stats())
    fm.execute_player_use(0)
    print(pl.get_combat_stats())
    fm.execute_enemy_action(ActionTree)
    fm.execute_enemy_action(ActionTree)
    print(pl.get_combat_stats())
