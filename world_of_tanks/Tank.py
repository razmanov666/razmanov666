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
    
    def __init__(self, model: str, 
                 weapon: dict,
                 thickness: int, 
                 ):
        self.model = model
        self.gun = Gun(weapon['caliber'], weapon['gun_length'])
        self._is_gun_loaded = False
        self.health = 5000 - 4 * weapon['gun_length'] - 2 ** (thickness/2.7)
        self.ammos = self.__load_ammos()
        # self.armors = self.__add_armors(thickness)
        self.armors = self.__add_armors()
        
    def load_gun(self, type_ammo: str):
        self._is_gun_loaded = True
    
    def __add_armors(thickness):
        return [HArmor(thickness), CArmor(thickness), SArmor(thickness)]
    
    def __load_ammos(self):
        return {'AP': APCartridge('213','123'): 10, 
                HEСartridge('213','123'): 10, 
                HEATCartridge('213','123'): 10}

    def show_tank_info(self):
        print('\nTank has model: ' + self.model)
        # for armor in self.armors:
        #     print(armor.type_armor)
        #     print(armor.thickness)
        print('HP: ' + str(self.health))
        print('\nTank has gun: ')
        print(' Caliber: ' + str(self.gun.caliber) + '\n'+
              ' Length of gun: ' + str(self.gun.gun_length))
        
        print('Ammos:\n')
        print(dict(self.ammos[]))

if __name__ == "__main__":
    health = 5000 - 2 * 'gun_length' - 5 * 'thickness'
    leopard1 = Tank('Leopard 1', Gun(105, 56), HArmor(20), APCartridge('213','123'), 1500)
    print(leopard1.gun.caliber)
    