# Реализовать класс пушки Gun. Он будет иметь два поля: калибр и длину ствола.
#   От калибра зависит урон, и, частично, способность к пробитию брони. 
#   От длины ствола – точность стрельбы.

# Помните, что для поражения цели должно произойти две вещи: 
#   попадание в цель и пробитие брони
# Так вот, пушка будет отвечать за первую из них: попадание. 
# Поэтому делаем булевый метод is_on_target, 
#   который принимает случайную величину 
#   (dice (бросок кубика)) и возвращает результат: попали или нет: 
#   ({длина пушки) *{dice}) > 100;

import random


class Gun():
    """Exist information about caliber and length of gun."""

    def __init__(self, caliber, gun_length):
        self.caliber = caliber
        self.gun_length = gun_length


    def is_on_target(self, dice=random.randint(1,7), x = 2) -> bool:
        """Checks """
        return self.gun_length * dice > 100


if __name__ == '__main__':
    caliber_123 = Gun(76, 30)
    print(caliber_123.is_on_target())