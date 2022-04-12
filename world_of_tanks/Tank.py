# 1. Реализовать класс Tank, который имеет следующее полня: 
#   model (str), 
#   gun (Gun), 
#   armors (List[Armors]), 
#   ammos (List[Ammo]), 
#   health (int), 
#   _is_gun_loaded.

# Для того, чтобы конструктор танка остался более-менее компактным, сделаем два 
#   вспомогательных приватных метода, которые добавляют три типа брони 
#   соответствующей толщины, и наполняют боеукладку 10 снарядами каждого из трех
#   типов: 
#   _add_armours(width: int) и 
#   _load_ammos

# 2. Реализовать два публичных метода 

#   select_armour(armour_type: string), 
#       который меняет броню у танка перед каждым ходом и 
#   load_gun(ammo_type: string), 
#   который заряжает пушку(ставим _is_gun_loaded в True) 
#   снарядом выбранного типа и уменьшает общее количество снарядов 
#   этого типа в боеукладке

from Gun import Gun
from Ammo import *
from Armor import *

class Tank():
    
    def __init__(self, model: str, gun: Gun, 
                #  armors: list[Armor], 
                #  ammos: dict[Ammo: int], 
                 armor,
                 ammo,
                 health: int, _is_gun_loaded: bool = False):
        self.model = model
        # self.gun = Gun()
        self.gun = gun
        self._is_gun_loaded = False
        # self.armors = self.__add_armors(10)
        # self.ammos = self.__load_ammos()
        armor = armor
        ammo = ammo
        
    def load_gun(self, ammo_type: str):
        self._is_gun_loaded = True
    
    def __add_armors(width: int):
        return [HArmor(width), CArmor(width), SArmor(width)]
    
    def __load_ammos():
        return {APCartridge(): 10, HEСartridge(): 10, HEATCartridge(): 10}

if __name__ == "__main__":
    leopard1 = Tank('Leopard 1', Gun(105, 56), HArmor(20), APCartridge('213','123'), 1500)
    