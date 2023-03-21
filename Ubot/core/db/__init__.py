
from ubotlibs.ubot.database import cli
from .usersdb import *
from .accesdb import *
from .notesdb import *
from Ubot import *

import sqlite3

def create_database(client_name):
    conn = sqlite3.connect(f"{client_name}.db")
    conn.close()


create_database(bot1.name)
create_database(bot2.name)
create_database(bot3.name)
create_database(bot4.name)
create_database(bot5.name)
create_database(bot6.name)
create_database(bot7.name)

