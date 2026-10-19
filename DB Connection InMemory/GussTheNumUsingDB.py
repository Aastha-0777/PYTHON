import random
import sqlite3

conn = sqlite3.connect("game.db")
cur = conn.cursor()

gussedNum = random.randint(1, 501)

playerName = input('Enter You Name : ')
player1Guss = []
gussCounter = 0

print('------ GUSS THE NUMBER ------')

while True:

    p1Num = int(input(f'{playerName} Enter Your Number : '))
    player1Guss.append(p1Num)

    if p1Num < gussedNum:
        print('Your Guss is too less...')
        gussCounter += 1
    elif p1Num > gussedNum:
        print('Your Guss is too high...')
        gussCounter += 1
    else:
        print(f'Eureka!! {playerName} You have Won the Game...')
        gussCounter += 1
        break


print(f'{playerName} Guss : {player1Guss}')

cur.execute("""

CREATE TABLE IF NOT EXISTS GUSSTHENUM(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
score INTEGER
)

""")

conn.commit()

cur.execute("insert into GUSSTHENUM(name, score) Values(?, ?)", (playerName, gussCounter))
conn.commit()

