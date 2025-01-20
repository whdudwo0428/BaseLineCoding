import random

from RPG_character import Hero, Goblin, Orc, Dragon
from RPG_battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수):")
    hero = Hero(name,100,20,5,speed=12,role=role)
    print(hero)

    monter_pool = [
        Goblin("고블린",30,10,2,speed=10, level=1),
        Orc("오크", 50, 15,3,speed=5, level=3),
        Dragon("드래곤", 100, 30,5,speed=20, level=5)
    ]

    battle = Battle()
    while hero.is_alive():
        monter = random.choice(monter_pool)
        # random.choice는 인자로 들어오는 리스트 중 하나를 뽑아줌
        print(f"\n 몬스터 {monter.name} 등장")
        print(monter.Description())

        if not battle.fight(hero, monter):
            break


if __name__ == '__main__':
    main()