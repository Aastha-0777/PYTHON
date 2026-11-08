"""
This is Just for testing purpose only
"""
import sqlite3
c = sqlite3.connect("prices.db")
c.execute("""UPDATE prices SET price = price - 5
             WHERE id = (SELECT MAX(id) FROM prices WHERE product_id = 1)""")
c.commit()