class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, emeny):
        print("玩家攻击敌人")
        emeny.damage(self.atk)

    def damage(self, value):
        print("碎屏")
        self.hp -= value
        print("敌人血量是", self.hp)


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("播放受伤动画")
        self.hp -= value
        print("敌人血量是", self.hp)

    def attack(self, player):
        print("敌人攻击玩家")
        player.damage(self.atk)


p01 = Player(500, 50)
e01 = Enemy(100, 10)
p01.attack(e01)
e01.attack(p01)
