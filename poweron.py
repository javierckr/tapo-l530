#!/usr/bin/env python3

import os
from PyP100 import PyL530

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Create list of bulbs
bulbs = []
bulbs.append(PyL530.L530("10.0.0.254", os.getenv("MAIL"), os.getenv("PASS")))
bulbs.append(PyL530.L530("10.0.0.253", os.getenv("MAIL"), os.getenv("PASS")))
bulbs.append(PyL530.L530("10.0.0.252", os.getenv("MAIL"), os.getenv("PASS")))

# Login bulbs
for bulb in bulbs:
    bulb.handshake()  # Creates the cookies required for further methods
    bulb.login()  # Sends credentials to the plug and creates AES Key
    # and IV for further methods

for bulb in bulbs:
    bulb.turnOn()


# All the bulbs have the PyP100 functions and additionally
# allows for setting brightness, colour and white temperature
# l530.setBrightness(100)  # Sends the set brightness request
# l530.setColorTemp(
#    2700
# )  # Sets the colour temperature to 2700 Kelvin (Warm White)
# l530.setColor(100, 100)  # Sends the set colour request
