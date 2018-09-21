import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
seat_num = 3 #that is gotten by raspberrypi
is_seat_empty = "seated"
c.execute("UPDATE blog_seats SET is_seat_empty = '{}'  WHERE seat_num is {}".format(is_seat_empty,seat_num))
conn.commit()
