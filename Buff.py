class Buff:
    # Use KWargs for the initialization of the class
    def __init__(self, health=0, damage=0, defence=False, active_rounds=1):
        self.health_buff = health
        self.damage_buff = damage
        self.defence_buff = defence
        self.active_rounds = active_rounds

    def activate(self, inventory):
        inventory.add_health(self.health_buff)
        inventory.add_damage(self.damage_buff)
        inventory.set_defence(inventory.get_defence() or self.defence_buff)

    def use(self, inventory):
        inventory.active_buffs.append(self)

    def revert_buff_use(self, inventory):
        inventory.add_health(-self.health_buff)
        inventory.add_damage(-self.damage_buff)
        inventory.set_defence(False)


    def is_buff_active(self):
        return self.active_rounds > 0

    def round_pass(self):
        self.active_rounds -= 1
        print("Active rounds: ", self.active_rounds)
        return self.active_rounds > 0

    def __str__(self):
        return "Buff combat stats: {0} heal, {1} damage, {2} defence for the next {3} rounds"\
                .format(self.health_buff, self.damage_buff, self.defence_buff, self.active_rounds)
