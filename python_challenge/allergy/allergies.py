
class Allergies():
    def __init__(self, num):
        self.lst = []
        self.num = num
        self.allergie_table = [
            ("eggs", 1),
            ("peanuts", 2),
            ("shellfish", 4),
            ("strawberries", 8),
            ("tomatoes", 16),
            ("chocolate", 32),
            ("pollen", 64),
            ("cats", 128)
        ]

        # self.allergies

        self.make_list()

    def make_list(self):
        nums = self.num
        while nums != 0:
            for name, key in reversed(self.allergie_table):
                if nums - key >= 0:
                    self.lst.append(name)
                    nums -= key


        # eggs(1)
        # peanuts(2)
        # shellfish(4)
        # strawberries(8)
        # tomatoes(16)
        # chocolate(32)
        # pollen(64)
        # cats(128)

    def is_allergic_to(self, food):
        if food in self.lst:
            return True



