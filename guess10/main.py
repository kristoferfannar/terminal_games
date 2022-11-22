from time import time, sleep
from os import system, get_terminal_size, name

SECONDS = 10


def init():
    global TERM_X, TERM_Y, CLEAR
    TERM_X, TERM_Y = get_terminal_size()
    if name == 'nt':
        CLEAR = 'cls'
    else:
        CLEAR = 'clear'


def main():
    init()

    display_main()
    while (ui := input().lower()) != 'q':
        if ui == 'h':
            display_highscores("highscores.txt")
        elif ui == 'r':
            rules()
        elif ui == 'p':
            play()
        elif ui == 'fizzbuzz':
            fizzbuzz()
        else:
            print(f"{ui} is not a legal command")
            sleep(2)
        display_main()
    system(CLEAR)


def display_main():
    lines = 6
    display_init(lines)
    border = '#'*20
    print(f'{border:^{TERM_X}}')  # 1
    print(f'{"P - Play Game":^{TERM_X}}')  # 2
    print(f'{"R - Rules":^{TERM_X}}')  # 3
    print(f'{"H - Highscores":^{TERM_X}}')  # 4
    print(f'{"Q - Quit":^{TERM_X}}')  # 5
    print(f'{border:^{TERM_X}}')  # 6
    display_footer(lines)


def display_init(lines=0):
    system(CLEAR)
    print('\n'*round((TERM_Y - lines) / 2))


def display_footer(lines=0):
    print('\n'*round((TERM_Y - lines - 3) / 2))


def rules():
    quit = False
    while not quit:
        lines = 4
        display_init(lines)
        print(
            "Here you need to press ENTER exactly 10 seconds after the timer starts...")  # 1
        sleep(3)
        print("The closer you are to 10 seconds, the better your score is...")  # 2
        sleep(3)
        print("Will you make it into the top 10?")  # 3
        display_footer(lines)
        user = input("q - quit: ").lower()  # 4
        if user == 'q':
            quit = True


def display_highscores(file):
    highscores = get_highscores(file)
    print_highscores(highscores)
    user = input("Q - quit: ")  # 3


def print_highscores(highscores):
    lines = len(highscores) + 3
    display_init(lines)
    border = "#"*50
    print(f"{border:^{TERM_X}}")  # 1
    for index in range(len(highscores)):
        print(
            f"{index+1:>{round((TERM_X - 40) / 2)}}  |  NAME: {highscores[index][0][:11]:<10}   -  SCORE: {highscores[index][1]:>4}")  # highscores
    print(f"{border:^{TERM_X}}")  # 2
    display_footer(lines)


def get_highscores(file, num=5):
    scores = get_scores(file)
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[:num]


def get_scores(file):
    with open(file, 'r') as scores:
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

    save_score(score, "highscores.txt")


def countdown():
    for i in range(3, 0, -1):
        display_init()
        print(f"{i:^{TERM_X}}")
        sleep(1)
    system(CLEAR)


def calculate_score(difference):
    return int((100 / difference))


def save_score(score, file):
    name = input("Your name: ")
    with open(file, "a") as scores:
        scores.write(f"{name}, {score}\n")


################################

def fb_header(lines=0):
    system(CLEAR)
    rows = round((TERM_Y - lines) / 2)
    print('\n')
    print(f"{'------------':^{TERM_X}}")
    print(f"{'| FIZZBUZZ |':^{TERM_X}}")
    print(f"{'------------':^{TERM_X}}")
    print('\n'*(rows - 5))


def display_fb():
    lines = 5
    fb_header(lines)
    border = '*'*20
    print(f"{border:^{TERM_X}}")
    print(f"{'P - Play':^{TERM_X}}")
    print(f"{'H - Highscores':^{TERM_X}}")
    print(f"{'Q - Quit':^{TERM_X}}")
    print(f"{border:^{TERM_X}}")
    display_footer(lines)


def computer_play(num) -> str:
    if num % 15 == 0:
        return "fizzbuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return str(num)


def user_play(num):
    user_input = input()
    return computer_play(num) == user_input


def fb_calculate_score(total):
    return int(1000 / total)


def fb_play():
    countdown()
    start = time()

    for i in range(1, 21):
        if i % 2 == 1:
            print(computer_play(i))
        else:
            user_success = user_play(i)
            if not user_success:
                print("WRONG! - GAME OVER")
                sleep(3)
                return

    total = time() - start

    score = fb_calculate_score(total)

    save_score(score, "fizzbuzz.txt")


def fizzbuzz():
    display_fb()
    while (ui := input().lower()) != 'q':
        if ui == 'h':
            display_highscores("fizzbuzz.txt")
        elif ui == 'p':
            fb_play()
        else:
            print(f"{ui} is not a legal command")
            sleep(2)
        display_fb()


if __name__ == "__main__":
    main()
