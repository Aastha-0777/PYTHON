import sqlite3

conn = sqlite3.connect("game.db")
cur = conn.cursor()

cur.execute("select score from gussthenum")
score = cur.fetchall()
print(score)

winner = max(score)
# print(winner[0])
print(winner)

cur.execute("select * from gussthenum where score = ?", (winner[0], ))
winnerDetail = cur.fetchall()
print(f"Winner's Details : {winnerDetail}")

conn.commit()
conn.close()