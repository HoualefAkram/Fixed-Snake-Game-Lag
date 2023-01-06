import sys
from getopt import getopt
from random import randint
from time import sleep
from tkinter import *

window = Tk()

window.resizable(False, False)
window.title("Call of Duty CyberPunk 3000")
size = 30
player_grid = [(size / 2, size / 2 - 1)]
game = Frame(master=window, bg='black')
last_movement = ""
speed = 20
score = -1
score_var = StringVar()

opts, args = getopt(sys.argv[1::], "s:v:")
for i, j in opts:
    if i == "-s":
        size = int(j)
    elif i == "-v":
        speed = int(j)

print(f"opts = {opts} , args = {args}")
for up in range(size):  # making the border
    Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=up)
for down in range(size):  # making the borders
    Label(master=game, bg="grey", width=2, height=1).grid(row=size - 1, column=down)
for left in range(size):  # making the borders
    Label(master=game, bg="grey", width=2, height=1).grid(row=left, column=0)
for right in range(size):  # making the borders
    Label(master=game, bg="grey", width=2, height=1).grid(row=right, column=size - 1)

panel = Label(master=window, textvariable=score_var, font=("Ariel", 30, "bold"))
panel.pack(side=TOP)

window.update()


def make_food():
    global score, food_cord  # NOQA
    score += 1
    score_var.set(f"score : {score}")
    food_cord = (randint(1, size - 2), randint(1, size - 2))
    Label(master=game, bg="#00FF00", width=2, height=1).grid(row=food_cord[0], column=food_cord[1])
    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                         column=int(player_grid[-1][1]))


make_food()


def end_game():
    global last_movement, player_grid, score, speed
    for nums in player_grid:
        Label(master=game, bg="black", width=2, height=1).grid(row=int(nums[0]), column=int(nums[1]))
    end = Label(master=window, text="YOU LOST!", fg="red", bg="black", font=("Ariel", 40, "bold"))
    end.place(x=size * 5, y=size * 10)
    window.update()
    sleep(3)
    end.destroy()
    Label(master=game, bg="black", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                           column=int(player_grid[-1][1]))  # empty_map()
    Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=0)
    score_var.set(f"score : {0}")
    score = 0
    player_grid = [[size / 2, size / 2 - 1]]
    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[0][0]), column=int(player_grid[0][1]))
    # make border
    for up in range(size):  # making the border # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=0, column=up)
    for down in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=size - 1, column=down)
    for left in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=left, column=0)
    for right in range(size):  # making the borders # NOQA
        Label(master=game, bg="grey", width=2, height=1).grid(row=right, column=size - 1)

    window.update()


Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[0][0]), column=int(player_grid[0][1]))


def move(event):
    global last_movement
    pressed = event.keysym
    while True:
        if player_grid[-1][0] == 0 or player_grid[-1][1] == 0 or player_grid[-1][0] == size - 1 or player_grid[-1][
            # over()
            1] == size - 1:  # NOQA
            end_game()
        for ps in range(len(player_grid) - 1):
            try:
                if player_grid[-1] == player_grid[ps]:
                    end_game()
            except IndexError:
                pass

        if pressed.lower() == "up":
            if last_movement != 'd':
                player_grid.append((player_grid[-1][0] - 1, player_grid[-1][1]))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))
                last_movement = "u"
                if player_grid[-1] == food_cord:
                    make_food()

                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)
            elif last_movement == 'd':
                player_grid.append((player_grid[-1][0] + 1, player_grid[-1][1]))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "d"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)

        if pressed.lower() == "down":
            if last_movement != "u":
                player_grid.append((player_grid[-1][0] + 1, player_grid[-1][1]))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "d"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)
            elif last_movement == "u":
                player_grid.append((player_grid[-1][0] - 1, player_grid[-1][1]))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "u"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)

        if pressed.lower() == "right":
            if last_movement != 'l':
                player_grid.append((player_grid[-1][0], player_grid[-1][1] + 1))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "r"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)
            elif last_movement == "l":
                player_grid.append((player_grid[-1][0], player_grid[-1][1] - 1))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "l"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)

        if pressed.lower() == "left":
            if last_movement != 'r':
                player_grid.append((player_grid[-1][0], player_grid[-1][1] - 1))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "l"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)
            elif last_movement == "r":
                player_grid.append((player_grid[-1][0], player_grid[-1][1] + 1))
                Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                     column=int(player_grid[-1][1]))

                last_movement = "r"
                if player_grid[-1] == food_cord:
                    Label(master=game, bg="Red", width=2, height=1).grid(row=int(player_grid[-1][0]),
                                                                         column=int(player_grid[-1][1]))
                    make_food()
                elif player_grid[-1] != food_cord:
                    Label(master=game, bg="Black", width=2, height=1).grid(row=int(player_grid[0][0]),
                                                                           column=int(player_grid[0][1]))
                    player_grid.pop(0)
        window.update()
        sleep(1 / speed)


for i in range(size):  # making the map
    if i == 0 or i == size - 1:
        Label(master=game, bg="grey", width=2, height=1).grid(row=i, column=i)
    else:
        Label(master=game, bg="black", width=2, height=1).grid(row=i, column=i)

window.bind("<Up>", move)
window.bind("<Down>", move)
window.bind("<Right>", move)
window.bind("<Left>", move)

game.pack()
window.mainloop()
