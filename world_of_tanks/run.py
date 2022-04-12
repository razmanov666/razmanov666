
from Tank import Tank
from weapon_base import *

# weapon1 = weapons[data_tank['weapon']]
tank1 = Tank(data_tank['model'], weapons[data_tank['weapon']], data_tank['thickness'])
tank1.show_tank_info()