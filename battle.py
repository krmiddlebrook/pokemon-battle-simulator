from fight import fight

def battle(my_pokemon, their_pokemon):

    print("Current HP is %s" % my_pokemon.stats['HP'][0])

    while my_pokemon.stats['HP'][0] > 0 and their_pokemon.stats['HP'][0] > 0:

        # First need to choose an action (fight, bag, pokemon, run)

        chosen_action = choose_action(my_pokemon.name)

        if chosen_action == 'Fight' or \
            chosen_action == 'Bag' or \
            chosen_action == 'Pokemon' or \
                chosen_action == 'Run':

            # Have all of them call the fight function for now

            fight(my_pokemon, their_pokemon)

    if my_pokemon.stats['HP'][0] == 0:
        print('Your %s has fainted!' % my_pokemon.name)
        my_pokemon.update_state_file()
    if their_pokemon.stats['HP'][0] == 0:
        print('Their %s has fainted!' % their_pokemon.name)

        # should then gain some xp for beating the opponent

        my_pokemon.update_xp(50)

    print('Your %s\'s HP is %s' % (my_pokemon.name, my_pokemon.stats['HP'][0]))
    print('Their %s\'s HP is %s' % (their_pokemon.name, their_pokemon.stats['HP'][0]))

def choose_action(pokemon_name):

    available_actions = [
        'Fight',
        'Bag',
        'Pokemon',
        'Run'
    ]

    while True:
        print('\nWhat will %s do?' % pokemon_name)

        for action in available_actions:
            print(action)
        print('\n')
        choice = input()

        if choice in available_actions:
            break
        else:
            print('That action doesn\'t exist, please choose a valid action')

    return choice
