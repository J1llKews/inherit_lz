class Texas_holdem:
    def __init__(self, first_card_value, first_card_suit, #я не знаю зачем такие длинные атрибуты(((
                 second_card_value, second_card_suit):
        self.first_card_value = first_card_value   # значение первой карты
        self.first_card_suit = first_card_suit     # масть первой карты
        self.second_card_value = second_card_value # значение второй карты
        self.second_card_suit = second_card_suit   # масть второй карты

    def pocket_info(self):
        print("карты:")
        print(self.first_card_value, self.first_card_suit)
        print(self.second_card_value, self.second_card_suit)

    def win_chance(self):
        if self.first_card_value == self.second_card_value:
            print("шанс победы высокий")
        else:
            print("шанс победы средний")


class Omaha_holdem(Texas_holdem):
    def __init__(self, first_card_value, first_card_suit,
                 second_card_value, second_card_suit,
                 third_card_value, third_card_suit,
                 fourth_card_value, fourth_card_suit):

        self.first_card_value = first_card_value
        self.first_card_suit = first_card_suit
        self.second_card_value = second_card_value
        self.second_card_suit = second_card_suit
        self.third_card_value = third_card_value
        self.third_card_suit = third_card_suit
        self.fourth_card_value = fourth_card_value
        self.fourth_card_suit = fourth_card_suit

    def pocket_info(self):
        print("карты (омаха):")
        print(self.first_card_value, self.first_card_suit)
        print(self.second_card_value, self.second_card_suit)
        print(self.third_card_value, self.third_card_suit)
        print(self.fourth_card_value, self.fourth_card_suit)

    def win_chance(self):
        if self.first_card_value == self.second_card_value or \
           self.first_card_value == self.third_card_value or \
           self.first_card_value == self.fourth_card_value or \
           self.second_card_value == self.third_card_value or \
           self.second_card_value == self.fourth_card_value or \
           self.third_card_value == self.fourth_card_value:
            print("шанс победы высокий")
        else:
            print("шанс победы средний")