import random
from game import GameCharacter, AiCharacter

player_units = []
ai_units = []


def all_dead(units):
    return all(not u.alive() for u in units)


def choose_index(prompt, lo, hi):
    while True:
        try:
            idx = int(input(prompt)) - 1
            if lo <= idx <= hi:
                return idx
        except ValueError:
            pass
        print(f"Invalid choice. Pick a number {lo+1}-{hi+1}.")


def main():
    input("Press Enter to start...")
    print("..........progressing.......")
    print("__--__--__--WELCOME TO PYTHON GAME!!--__--__--__\n\n{:Main Menu:}\n")

    while True:
        print("\n1. Play Game\n2. Game rules\n3. Credits\n4. Quit\n")
        answer = input("-- ").strip()

        if answer == "1":
            gamestart()
        elif answer == "2":
            print(
                "\n____Character Ranges____\n"
                "HP starts at 100, EXP at 0.\n"
                "1. Warrior    At[5-20],  Df[1-10]\n"
                "2. Tanker     At[1-10],  Df[5-15]\n"
                "3. MagicAlice At[10-30], Df[7-17]\n"
                "\n____Coins & EXP____\n"
                "- Earn 10 coins when your hit deals ≥5 damage\n"
                "- Extra +40 EXP the first time you reach 15 coins\n"
                "- Rank up every 100 EXP (+20 coins)\n"
                "- Unit is out when HP reaches 0\n"
            )
        elif answer == "3":
            print(
                "Developed by: Nang\n"
            )
        elif answer == "4":
            print("Thank you for playing! See you again! :))")
            break
        else:
            print("Pick 1-4, please.")


def gamestart():
    # clear previous game state
    player_units.clear()
    ai_units.clear()

    print("__--__--__--{GET READY! YOUR ENEMIES ARE HERE!!}--__--__--__")
    print("----- GAME START -----\n")

    option_map = {'w': 'warrior', 't': 'tanker', 'm': 'MagicAlice'}
    ai_nameoption = ['Alexa', 'Peter', 'Olive', 'Max', 'Bot']

    # create player units
    for i in range(3):
        while True:
            char_type = input("Choose your character: Warrior[w], Tanker[t], MagicAlice[m] = ").strip().lower()
            if char_type in option_map:
                break
            print("Invalid character type. Enter w / t / m.")
        char_name = input("Enter character name: ").strip() or f"Hero{i+1}"
        player_units.append(GameCharacter(char_type, char_name))

    # create AI units
    for x in range(3):
        ai_type = random.choice(list(option_map.values()))
        ai_name = random.choice(ai_nameoption)
        ai_units.append(AiCharacter(ai_type, ai_name))
        print(f"Enemy {x+1}: type={ai_type} | name={ai_name}")

    rounds = 1
    MAX_ROUNDS = 10

    while rounds <= MAX_ROUNDS and not all_dead(player_units) and not all_dead(ai_units):
        print(f"\n==== Round {rounds} ====")

        # Player turn
        print("Your turn:")
        alive_players = [i for i, u in enumerate(player_units) if u.alive()]
        alive_enemies = [i for i, u in enumerate(ai_units) if u.alive()]

        print("Your units:")
        for i in alive_players:
            u = player_units[i]
            print(f"  {i+1}. {u.char_name} ({u.char_type}) HP:{u.hp} At:{u.at} Df:{u.df}")

        print("Enemy units:")
        for i in alive_enemies:
            u = ai_units[i]
            print(f"  {i+1}. {u.ai_name} ({u.ai_type}) HP:{u.hp} At:{u.at} Df:{u.df}")

        p_idx = choose_index("Enter character to use [1-3]: ", 0, 2)
        while not player_units[p_idx].alive():
            print("That unit is down. Pick another.")
            p_idx = choose_index("Enter character to use [1-3]: ", 0, 2)

        e_idx = choose_index("Enter enemy to attack [1-3]: ", 0, 2)
        while not ai_units[e_idx].alive():
            print("That enemy is already down. Pick another.")
            e_idx = choose_index("Enter enemy to attack [1-3]: ", 0, 2)

        player_units[p_idx].attack(ai_units[e_idx])

        if all_dead(ai_units) or all_dead(player_units):
            break

        # AI turn
        print("\nEnemy turn:")
        ai_choices = [i for i, u in enumerate(ai_units) if u.alive()]
        player_choices = [i for i, u in enumerate(player_units) if u.alive()]
        a_idx = random.choice(ai_choices)
        t_idx = random.choice(player_choices)
        print(f"Enemy unit {a_idx+1} attacks your unit {t_idx+1}")
        ai_units[a_idx].attack(player_units[t_idx])

        rounds += 1

    # result
    if all_dead(ai_units) and not all_dead(player_units):
        print("\n>>> Congratulations! You win! <<<\n")
    elif all_dead(player_units) and not all_dead(ai_units):
        print("\n>>> Game over... Try again. <<<\n")
    else:
        print("\n>>> Draw. Try again. <<<\n")


if __name__ == "__main__":
    main()
