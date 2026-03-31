class Texas_holdem:
    def __init__(self, v1, s1, v2, s2):
        self.v1 = v1
        self.s1 = s1
        self.v2 = v2
        self.s2 = s2

    def pocket_info(self):
        print("карты:")
        print(self.v1, self.s1)
        print(self.v2, self.s2)

    def win_chance(self):
        if self.v1 == self.v2:
            print("шанс победы высокий")
        else:
            print("шанс победы средний")


class Omaha_holdem(Texas_holdem):
    def __init__(self, v1, s1, v2, s2, v3, s3, v4, s4):
        super().__init__(v1, s1, v2, s2)
        self.v3 = v3
        self.s3 = s3
        self.v4 = v4
        self.s4 = s4

    def pocket_info(self):
        print("карты (Омаха):")
        print(self.v1, self.s1)
        print(self.v2, self.s2)
        print(self.v3, self.s3)
        print(self.v4, self.s4)

    def win_chance(self):
        if self.v1 == self.v2 or self.v1 == self.v3 or self.v1 == self.v4 \
           or self.v2 == self.v3 or self.v2 == self.v4 or self.v3 == self.v4:
            print("шанс победы высокий")
        else:
            print("шанс победы средний")
