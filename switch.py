#!/usr/bin/env python3

from gpiozero import Button
from room import rooms


def switch(on):
    room = rooms()
    room.login()
    if on:
        room.poweroff()
        return False
    else:
        room.poweron()
        return True


def main():
    on = False
    while True:
        button = Button(2)
        button.wait_for_press()
        on = switch(on)

if __name__ == '__main__':
    main()
