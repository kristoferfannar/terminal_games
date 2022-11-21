from time import time, sleep
from os import system, get_terminal_size
from sys import platform

SECONDS = 10

print(platform)


def main():
    global TERM_X, TERM_Y
    TERM_X, TERM_Y = get_terminal_size()

    display_main()
    while (ui := input().lower()) != 'q':
        if ui == 'h':
            display_highscores()
        elif ui == 'r':
            rules()
        else:
            play()
        display_main()
    system("clear")


def display_main():
    display_init(5)
    border = '#'*20
    print(f'{border:^{TERM_X}}')
    print(f'{"P - Play Game":^{TERM_X}}')
    print(f'{"R - Rules":^{TERM_X}}')
    print(f'{"H - Highscores":^{TERM_X}}')
    print(f'{"Q - Quit":^{TERM_X}}')
    print(f'{border:^{TERM_X}}')


def display_init(lines=0):
    system("clear")
    print('\n'*round((TERM_Y-lines) / 2))


def rules():
    quit = False
    while not quit:
        display_init(5)
        print("Here you need to press ENTER exactly 10 seconds after the timer starts...")
        sleep(3)
        print("The closer you are to 10 seconds, the better your score is...")
        sleep(3)
        print("Will you make it into the top 10?")
        user = input("q - quit: ").lower()
        if user == 'q':
            quit = True


def display_highscores():
    highscores = get_highscores()
    print_highscores(highscores)
    user = input("Q - quit: ")


def print_highscores(highscores):
    display_init(len(highscores) + 4)
    border = "#"*50
    print(f"{border:^{TERM_X}}")
    for index in range(len(highscores)):
        print(
            f"{index+1:>{round((TERM_X - 40) / 2)}}  |  NAME: {highscores[index][0][:11]:<10}   -  SCORE: {highscores[index][1]:>4}")
    print(f"{border:^{TERM_X}}")


def get_highscores(num=5):
    scores = get_scores()
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[:num]


def get_scores():
    with open("highscores.txt", 'r') as scores:
        all_scores = [score.strip().split(', ')
                      for score in scores.readlines()]

    return [[score[0], int(score[1])] for score in all_scores]


def play():
    countdown()

    start = time()
    stopper = input()
    stop = time()

    user_time = stop - start

    difference = abs(SECONDS - user_time)

    score = calculate_score(difference)

    print(
        f"Your time was {round(user_time, 3)} seconds - {round(difference, 3)} seconds away!")

    print(f"Your score is: {score} points!!!")

    save_score(score)


def countdown():
    for i in range(3, 0, -1):
        display_init()
        print(f"{i:^{TERM_X}}")
        sleep(1)
    system('clear')


def calculate_score(difference):
    return int((100 / difference))


def save_score(score):

    name = input("Your name: ")
    with open("highscores.txt", "a") as scores:
        scores.write(f"{name}, {score}\n")


if __name__ == "__main__":
    main()
