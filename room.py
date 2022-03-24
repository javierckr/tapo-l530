#!/usr/bin/env python3


import os
from PyP100 import PyL530

from dotenv import load_dotenv

from time import sleep


class rooms:
    ## Methods and function for a group of bulbs

    def __init__(self):
        load_dotenv()  # take environment variables from .env.

        # Create list of bulbs
        self.bulbs = []
        self.bulbs.append(
            PyL530.L530("10.0.0.254", os.getenv("MAIL"), os.getenv("PASS"))
        )
        self.bulbs.append(
            PyL530.L530("10.0.0.253", os.getenv("MAIL"), os.getenv("PASS"))
        )
        self.bulbs.append(
            PyL530.L530("10.0.0.252", os.getenv("MAIL"), os.getenv("PASS"))
        )

    def login(self):
        """Login all bulbs"""

        # Login bulbs
        for bulb in self.bulbs:
            bulb.handshake()  # Creates the cookies required for further methods
            bulb.login()  # Sends credentials to the plug and creates AES Key
            # and IV for further methods

    def poweron(self):
        """Power on all bulbs"""
        for bulb in self.bulbs:
            bulb.turnOn()

    def poweroff(self):
        """Power off all bulbs"""
        for bulb in self.bulbs:
            bulb.turnOff()

    def disco(self):
        """Bulbs in disco mode"""
        self.poweron()
        for i in range(0, 100, 10):
            for j in range(0, 100, 10):
                for bulb in self.bulbs:
                    bulb.setColor(i, j)
                    sleep(1)
