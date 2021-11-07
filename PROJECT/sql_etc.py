import sqlite3

db = sqlite3.connect('db.db', check_same_thread=False)
sql = db.cursor()
d = sql.fetchall()
a = (sql.execute("SELECT * FROM goods ORDER BY good_name"))
d = sql.fetchall()  # d = good Description
b = (sql.execute("SELECT * FROM wishlist"))
w = sql.fetchall()  # w = Wishlist
c = (sql.execute("SELECT * FROM orders"))
o = sql.fetchall()  # o = Orders
osi = (sql.execute("SELECT * FROM order_string_id"))
osi2 = sql.fetchall()  # osi = Order String ID
order_string_id = osi2[0][0]

e = (sql.execute("SELECT * FROM reviews"))
r = sql.fetchall()  # r = Reviews

h = (sql.execute("SELECT * FROM recommend"))
f = sql.fetchall()  # f = recommendations For
