import random
condition = ''
enmy_wins = 0
plyr_wins = 0
RPS = ['rock' , 'paper', 'scissors']
while True:
    validanschosenyet = False
    n = random.randint(0, 2)
    enmy_choice = RPS[n]
    player_choice = input('Rock,Paper,Scissors,: ').lower().strip()
    for i in RPS:
        if player_choice == i:
            validanschosenyet = True
            break
    if validanschosenyet:
        if player_choice == enmy_choice:
            condition = 'Tied'
        elif enmy_choice == RPS[0] and player_choice == RPS[1]:
            plyr_wins += 1
            condition = 'Win'
        elif enmy_choice == RPS[1] and player_choice == RPS[0]:
            enmy_wins += 1
            condition = 'Lose'
        elif enmy_choice == RPS[1] and player_choice == RPS[2]:
            plyr_wins += 1
            condition = 'Win'
        elif enmy_choice == RPS[2] and player_choice == RPS[1]:
            enmy_wins += 1
            condition = 'Lose'
        elif enmy_choice == RPS[2] and player_choice == RPS[0]:
            plyr_wins += 1
            condition = 'Win'
        elif enmy_choice == RPS[0] and player_choice == RPS[2]:
            enmy_wins += 1
            condition = 'Lose'
        print(f'''
                               You picked {player_choice}
                               Enemy picked {enmy_choice}
                               You {condition}

                               Your wins = {plyr_wins}
                               Enemy wins = {enmy_wins}''')
    if not validanschosenyet:
        print("please choose a valid answer")
