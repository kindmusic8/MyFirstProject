
"""
File: DoubleBeepers.py
Name: TODO:
---------------------------------
TODO:
"""


from karel.stanfordkarel import *


def main():
    move()
    double_beeper()
    move()
    put_back_beeper()
    go_home()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()
def put_back_beeper():
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()
def go_home():
    turn_around()
    move()
    move()
    turn_around()
def turn_around():
    for i in range(2):
        turn_left()









####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)