class Battle:
    def fight(self, hero, monster):
        print(f"전투 시작 {hero.name} vs {monster.name}")
        hero_turn = hero.speed >= monster.speed
        turn = 1

        while hero.is_alive() and monster.is_alive():
            print(f"==턴 {turn}==")
            if hero_turn:
                damage = monster.take_damage(hero.attack)
                print(f"{hero.name}가 {monster.name}에게 {damage}의 데미지를 입힘")
                if not monster.is_alive():
                    print(f"몬스터 죽음")
                    hero.gain_exp(monster.exp_reward())
                    loot = monster.drop_loot()
                    if loot:
                        hero.equip(loot)
                    return
            else:
                damage = hero.take_damage(monster.attack)
                print(f"{monster.name}가 {hero.name}에게 {damage}의 데미지를 입힘")
                if not hero.is_alive():
                    print(f"히어로 죽음")
                    return
            hero_turn = not hero_turn



        print("전투 종료")
