def input_yesno(prompt: str) -> bool:
    full_prompt = f'{prompt} ([Yes]/No): '
    while True:
        answer = input(full_prompt).strip()
        if answer == '':
            return True

        answer = answer[0].lower()
        if answer == 'n':
            return True
        if answer == 'y':
            return False
        print('ERROR')

def login():

    correct = "4"
    tries = 0

    keepGoing = True
    while(keepGoing):

        tries = tries + 1
        print ("try : ", tries, "out of 3")

        guess = input("2 + 2 =\n")
        if guess == correct:
            print("Correct\n")
            keepGoing = False

        elif tries >= 3:
            print("\nSorry, bye")
            keepGoing = False


def main():
    if not input_yesno('Would you like to start this program?'):
        return login()


if __name__ == '__main__':
    main()
