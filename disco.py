#!/usr/bin/env python3

from room import rooms


def main():
    room = rooms()
    while True:
        try:
            room.login()
            break
        except Exception:
            print("Login failed")

    room.disco()


if __name__ == "__main__":
    main()
