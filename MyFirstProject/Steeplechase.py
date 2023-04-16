"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()

def jump():
    turn_left()
    go_up()
    cross()
    down()


def go_up():
    """
    pre-condition: Karel is on the left,facing East
    post-condition:Karel is at the upper left,facing North
    """
    while not right_is_clear():
        move()
def cross():
    """
    pre-condition:Karel is at the upper left,facing North
    post_condition:karel is at upper right,facing south
    """

    while right_is_clear():
        turn_right()
        move()
        turn_right()
        move()

def down():
    """
    pre-condition:karel is at upper right,facing south
    post-condition:Karel is on the left,facing East
    """
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
