class Player_a:  # 定义一个白衣的类
    def __init__(self, atk, hp, de):
        self.atk = atk
        self.hp = hp
        self.de = de
      # 定义一个函数 对应白衣玩家的属性

    def attack(self, emeny):
        print("红衣攻击白衣")
        emeny.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print("敌人血量是", self.hp)


class Player_b:
    def __init__(self, atk, hp, de):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("播放受伤动画")
        self.hp -= value
        print("敌人血量是", self.hp)

    def attack(self, player):
        print("敌人攻击玩家")
        player.damage(self.atk)


red_player = Player_a(166, 620, 36)
# 定义白衣 和红衣玩家定义血量 攻击力和防御力
white_player = Player_b(174, 592, 35)
red_player.attack(white_player)
white_player.attack(red_player)
