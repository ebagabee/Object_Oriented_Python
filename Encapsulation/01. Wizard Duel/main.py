class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self, fireball_damage):
        damage = fireball_damage - self.__stamina
        self.health -= damage

    def drink_mana_potion(self, potion_mana):
        potion_value = potion_mana + self.__intelligence
        self.mana += potion_value
