class HULUWA:
    def __init__(self, name, age, atk):
        self.name = name
        self.age = age
        self.atk = atk

    def huluwa(self):
        print("————葫芦娃————")
        print(f"名字：{self.name}")
        print(f"年龄：{self.age}")
        print(f"技能：{self.atk}")


a = HULUWA('大娃', '13', '变大')
a.huluwa()
