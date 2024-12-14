import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health_gamer = 100

    def take_damage(self):
         amount = random.randint(10, 35)
         self.health_gamer -= amount
         if self.health_gamer < 0:
             self.health_gamer = 0
         return f'{self.name} получил {amount} урона. Текущее здоровье: {self.health_gamer}'

    def heal(self):
        healer = random.randint(5, 20)
        if healer + self.health_gamer > 100:
            self.health_gamer = 100
            return f'Ваш персонаж полностью излечился'
        else:
            self.health_gamer += healer
            return f'Персонаж излечился на {healer} хп'

    def run_away(self):
        lucky = random.randint(1,2)
        points = random.randint(10, 35)
        if lucky == 1:
            self.health_gamer -= points
            if self.health_gamer < 0:
                self.health_gamer = 0
            return f'{self.name} получил {points} урона, здоровье: {self.health_gamer}, но всё таки покинул комнату'
        else:
            return f'Вы успешно сбежали'

    def traps(self):
        trap =  random.randint(1,4)
        if trap == 1:
            points = random.randint(9, 15)
            self.health_ai -= points
            self.health_gamer -= points
            return f'В комнате обнаружены мины, вы и ваш противник получили {points} урона'
        elif trap == 2:
            points = random.randint(5, 8)
            self.health_ai -= points
            self.health_gamer -= points
            return f'В комнате обнаружены колючки, вы и ваш противник получили {points} урона'
        elif trap == 3:
            points = random.randint(4, 18)
            self.health_ai -= points
            self.health_gamer -= points
            return f'В комнате обнаружены копья, вы и ваш противник получили {points} урона'
        else:
            return f'В комнате нет ловушек, но всё ещё находится монстр'


class Room:
    def __init__(self, desc):

        self.desc = desc


class Enemy(Player):
    def __init__(self, name_ai):
        super().__init__(name_ai)
        self.health_ai = random.randint(50,100)

    def damage(self):
        points = random.randint(10, 35)
        self.health_ai -= points
        if self.health_ai < 0:
            self.health_ai = 0
        return f'{self.name} получил {points} урона, здоровье: {self.health_ai}'


rooms = [
    Room('Башня'),
    Room('Цитадель'),
    Room('Некрополь')
]

enemies = [
    Enemy('Грифон'),
    Enemy('Орк'),
    Enemy('Cкелет')
]

hero = Player('Vadim')

# Выбор комнаты

def rooom():
    global enemy1
    print('Вы видите три двери с цифрами "1", "2", "3", выберите любую: ')
    door = int(input())
    if door == 1:
        enemy1 = enemies[0].name
        print( f'Вы попали на локацию {rooms[0].desc} и встретили противника {enemies[0].name}')
    elif door == 2:
        enemy1 = enemies[1].name
        print(f'Вы попали на локацию {rooms[1].desc} и встретили противника {enemies[1].name}')
    elif door == 3:
        enemy1 = enemies[2].name
        print(f'Вы попали на локацию {rooms[2].desc} и встретили противника {enemies[2].name}')
    else:
        print('Не верный ввод, выберите цифру от 1 до 3')


rooom()

enemy = Enemy(enemy1)
print(enemy.traps()) # ловушки
print(f'У противника над головой полоска хп и она равна: {enemy.health_ai}')

def fight():
    enemy.traps()
    while True:
        print(f'Выберите действие: \n'
              f'1) Ударить врага\n'
              f'2) Полечиться\n'
              f'3) Сбежать')
        choice = int(input())
        if choice == 1:
            print(f'{hero.name} атакует')
            print(enemy.damage())
            print(f'{enemy.name} атакует')
            print(hero.take_damage())
        elif choice == 2:
            print(hero.heal())
            print(f'{enemy.name} атакует')
            print(hero.take_damage())
        elif choice == 3:
            print(hero.run_away())
            return
        if hero.health_gamer == 0:
            print('Вы проиграли')
            return
        elif enemy.health_ai == 0:
            print('Вы победили')
            return


fight()

