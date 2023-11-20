#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6955309259:AAFNPDLOBzYOmqgym9Slfj3pOD7LdZOD6UM")
    API_ID = int(os.environ.get("API_ID", "28414026"))
    API_HASH = os.environ.get("API_HASH", "595e101e4009da570ae71cae7060d20f")
    AUTH_USERS = "1476002847"

