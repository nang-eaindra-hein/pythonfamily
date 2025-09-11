import random


class GameCharacter:
    def __init__(self, char_type: str, char_name: str):
        # char_type is 'w' | 't' | 'm' from the player menu
        self.char_type = char_type
        self.char_name = char_name
        self.at = 0
        self.hp = 100
        self.df = 0
        self.exp = 0
        self.rk = 1
        self.coins = 0

        if char_type == 'w':
            self.setup_warrior()
        elif char_type == 't':
            self.setup_tanker()
        elif char_type == 'm':
            self.setup_MagicAlice()
        else:
            raise ValueError("Invalid character type. Use 'w', 't', or 'm'.")

    def setup_warrior(self):
        self.char_type = "warrior"
        self.at = random.randint(5, 20)
        self.df = random.randint(1, 10)

    def setup_tanker(self):
        self.char_type = "tanker"
        self.at = random.randint(1, 10)
        self.df = random.randint(5, 15)

    def setup_MagicAlice(self):
        self.char_type = "MagicAlice"
        self.at = random.randint(10, 30)
        self.df = random.randint(7, 17)

    def alive(self):
        return self.hp > 0

    def attack(self, target: "AiCharacter"):
        raw = self.at - target.df + random.randint(-5, 10)
        damage = max(0, raw)

        print(f"{self.char_name} hits {getattr(target, 'ai_name', 'Enemy')} for {damage} damage!")
        if damage > 0:
            target.hp = max(0, target.hp - damage)
            print(f"{getattr(target, 'ai_name', 'Enemy')} HP = {target.hp}")

        # award exp/coins safely
        self.exp += damage
        print(f"{self.char_name} EXP = {self.exp} | coins = {self.coins} | rank = {self.rk}")

        # small bonus/penalty to target exp based on outcome (optional)
        if damage > 10:
            target.exp = int(target.exp * 1.2)
        elif damage == 0:
            target.exp = int(target.exp * 1.1)

        # coins for good hits
        if damage >= 5:
            self.coins += 10
            print(f"-_-_-_-_-_-_-_-_-_-_-_-_-_ {self.char_name} earned 10 coins! (total {self.coins}) -_-_-_-_-_-_-_-_-_-_-_-_-_")

        # milestone coin bonus (first time reaching 15 coins before rank-up)
        if self.coins >= 15 and self.exp < 100:
            self.exp += 40
            print(f"_-_-_-_-_-_-_-_-_- {self.char_name} earned extra 40 EXP for reaching 15 coins! (EXP {self.exp}) _-_-_-_-_-_-_-_-_-")

        # level up(s)
        leveled = False
        while self.exp >= 100:
            self.exp -= 100
            self.rk += 1
            self.coins += 20
            leveled = True

        if leveled:
            # braces must be doubled in f-strings if you want to show them literally
            print(
                f"_-_-_-_-_-_-_-_-_-_-_-_-_-_ AMAZING! {self.char_name} RANK UP! _-_-_-_-_-_-_-_-_-_-_-_-_-_\n"
                f"{self.char_name} rank = {self.rk}, +20 coins (total {self.coins})\n"
                f"_-_-_-_-_-_-_-_-_-_-_-_-_-_ This is awesome! You’re awesome! Way to go! _-_-_-_-_-_-_-_-_-_-_-_-_-_\n"
                f"_-_-_-_-_-_-_-_-_-_-_-_-_-_ COOL! You’ve earned <<<20>>> coins from getting new rank! _-_-_-_-_-_-_-_-_-_-_-_-_-_"
            )


class AiCharacter:
    def __init__(self, ai_type: str, ai_name: str):
        # ai_type should be 'warrior' | 'tanker' | 'MagicAlice'
        self.ai_type = ai_type
        self.ai_name = ai_name
        self.at = 0
        self.hp = 100
        self.df = 0
        self.exp = 0
        self.rk = 1
        self.coins = 0

        if ai_type == 'warrior':
            self.setup_warrior()
        elif ai_type == 'tanker':
            self.setup_tanker()
        elif ai_type == 'MagicAlice':
            self.setup_MagicAlice()
        else:
            # fallback
            self.setup_warrior()

    def setup_warrior(self):
        self.ai_type = "warrior"
        self.at = random.randint(5, 20)
        self.df = random.randint(1, 10)

    def setup_tanker(self):
        self.ai_type = "tanker"
        self.at = random.randint(1, 10)
        self.df = random.randint(5, 15)

    def setup_MagicAlice(self):
        self.ai_type = "MagicAlice"
        self.at = random.randint(10, 30)
        self.df = random.randint(7, 17)

    def alive(self):
        return self.hp > 0

    def attack(self, target: GameCharacter):
        # don’t zero out target.df; compute damage properly
        raw = self.at - target.df + random.randint(-5, 10)
        damage = max(0, raw)

        print(f"{self.ai_name} hits {target.char_name} for {damage} damage!")
        if damage > 0:
            target.hp = max(0, target.hp - damage)
            print(f"{target.char_name} HP = {target.hp}")

        # AI exp/coins
        self.exp += damage
        if damage >= 5:
            self.coins += 10

        if self.coins >= 15 and self.exp < 100:
            self.exp += 40
            print(f"____________<<<<ALERT>>>> {self.ai_name} got +40 EXP for reaching 15 coins! ____________")

        # level up(s)
        while self.exp >= 100:
            self.exp -= 100
            self.rk += 1
            print(f"-_-_-_-_-_-_-_-_-_-_-_-_-_ THE ENEMY RANK HAS UPDATED!!! _-_-_-_-_-_-_-_-_-_-_-_-_-_")
            print(f"Enemy Rank = {self.rk}")
