#!/usr/bin/env python3

from gpiozero import Button
from room import rooms


def switch(on):
    room = rooms()
    while True:
        try:
            room.login()
            break
        except Exception:
            print("Login error, retrying")
    if on:
        room.poweroff()
        return False
    else:
        room.poweron()
        return True


def main():
    on = False
    button = Button(2)
    while True:
        button.wait_for_press()
        on = switch(on)


if __name__ == "__main__":
    main()
