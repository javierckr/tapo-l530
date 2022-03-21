#!/usr/bin/env python3

from gpiozero import Button
from room import rooms


def switch(on):
    room = rooms()
    room.login()
    if on:
        try:
            room.poweroff()
            return False
        except Exception:
            return True
    else:
        try:
            room.poweron()
            return True
        except Exception:
            return False


def main():
    on = False
    button = Button(2)
    while True:
        button.wait_for_press()
        on = switch(on)


if __name__ == "__main__":
    main()
