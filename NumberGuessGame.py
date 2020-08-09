import random


def guess_right_control(guess_right):
    if guess_right == 0:
        print("GAME OVER!!!\n"
              "NUMBER ---> ", pc_num,
              "PLEASE TRY AGAIN!!!")
        return 0


pc_num = random.randint(1, 100)  # generating random int
guess_right = 10  # you can change to

print("WELCOME GAME\n"
      "*******************************\n"
      "GUESS TO NUMBER BETWEEN 1-100\n"
      "YOU HAVE 10 RIGHT OF CHOICE\n"
      "*******************************")

while guess_right != 0:

    guess = int(input("YOUR GUESS : "))

    if pc_num == guess:
        print("CONGRULATIONS!!!\n")
        break

    elif pc_num > guess:
        print("PLEASE INCREASE YOUR GUESS!!!")
        guess_right -= 1
        print("REMAINING : ", guess_right)
        guess_right_control(guess_right)

    elif pc_num < guess:
        print("PLEASE DECREASE YOUR GUESS!!!")
        guess_right -= 1
        print("REMAINING : ", guess_right)
        guess_right_control(guess_right)
