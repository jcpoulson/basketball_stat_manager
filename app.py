import constants


new_player_data = []
panthers = []
bandits = []
warriors = []


def clean_data():
    players = constants.PLAYERS

    for player in players:
        # clean the height data
        for key, value in player.items():
            if key == 'height':
                height = int(value.split()[0])
                player['height'] = height
        # clean the experience data
        for key, value in player.items():
            if key == 'experience':
                if value == 'YES':
                    exp = bool(value)
                elif value == 'NO':
                    exp = False
                player['experience'] = exp
        # clean the guardian data
        for key, value in player.items():
            if key == 'guardians':
                guardian_val = value
                guardians = guardian_val.split('and')
                if len(guardians) == 2:
                    guardians[0] = guardians[0][:-1]
                    guardians[1] = guardians[1][1:]
                player['guardians'] = guardians
        new_player_data.append(player)


def balance_teams():
    players = new_player_data
    exp_players = []
    no_exp_players = []

    # sort the players with experience and no experience
    for player in players:
        if player['experience'] == True:
            exp_players.append(player)
        elif player['experience'] == False:
            no_exp_players.append(player)

    # for loop that assigns each experienced player to a team
    index = 0
    for player in exp_players:
        if index == 0:
            panthers.append(player)
            index = 1
        elif index == 1:
            bandits.append(player)
            index = 2
        elif index == 2:
            warriors.append(player)
            index = 0

    # for loop that assigns each inexperienced player to a team
    index2 = 0
    for player in no_exp_players:
        if index2 == 0:
            panthers.append(player)
            index2 = 1
        elif index2 == 1:
            bandits.append(player)
            index2 = 2
        elif index2 == 2:
            warriors.append(player)
            index2 = 0


def display_player_names(team, team_mascot):
    print()
    print("Team: {} Stats".format(team_mascot))
    print("-------------------")
    print("Total Players: {}".format(len(team)))
    print()
    
    # experienced players count
    exp_players_count = 0
    for player in team:
        for attr, value in player.items():
            if attr == 'experience':
                if value == True:
                    exp_players_count += 1
    print("Total Experienced: {}".format(exp_players_count))

    # inexperienced players count
    no_exp_players_count = 0
    for player in team:
        for attr, value in player.items():
            if attr == 'experience':
                if value == False:
                    no_exp_players_count += 1
    print("Total Experienced: {}".format(no_exp_players_count))

    # print out the average height of the team
    sum_height = 0
    for player in team:
        for attr, value in player.items():
            if attr == 'height':
                sum_height += value
    print("Average height: {}\n".format(round(sum_height / len(team), 2)))

    # print the names of the players
    player_str = ''
    print("Players on Team:")
    for player in team:
        for attr, value in player.items():
            if attr == 'name':
                player_str += value + ", "
    print(player_str)
    print()

    # print the names of the guardians
    guardian_str = ''
    print("Guardians:")
    for player in team:
        for attr, value in player.items():
            if attr == 'guardians':
                guardians = value
                for guardian in guardians:
                    guardian_str += guardian + ", "
    print(guardian_str)
    print()


def menu():
    while True:
        print("BASKETBALL TEAM STATS TOOL\n")
        print("---- MENU ----\n")
        print("Here are your choices:\n")
        try:
            choice = int(input("1) Display Team Stats\n2) Quit\n\nEnter an Option > "))
            if choice == 1:
                print("1) Panthers")
                print("2) Bandits")
                print("3) Warriors\n")
                team_chosen = int(input("Enter an option > "))
                if team_chosen == 1:
                    mascot = "Panther"
                    display_player_names(panthers, mascot)
                elif team_chosen == 2:
                    mascot = "Bandit"
                    display_player_names(bandits, mascot)
                elif team_chosen == 3:
                    mascot = "Warrior"
                    display_player_names(warriors, mascot)
                input("Press ENTER to continue....\n")
            elif choice == 2:
                break
        except ValueError:
            print("Please enter a valid value\n")


if __name__ == '__main__' :
    clean_data()
    balance_teams()
    menu()