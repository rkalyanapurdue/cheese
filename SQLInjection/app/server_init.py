import sqlite3

conn = sqlite3.connect('database')
c = conn.cursor()

# set up the database
c.execute("DROP TABLE IF EXISTS emailcloud")
c.execute('''CREATE TABLE emailcloud
			 (username text, password text, email text)''')

users = [('Alice', 'pwd', 'alice@mail.com'),
		 ('Alice', 'pwd', 'second@mail.com'),
		 ('Alice', 'pwd', 'third@mail.com'),
		 ('Barney', 'pwd', 'ledgen@mail.com'),
		 ('Barney', 'pwd', 'waitforit@mail.com'),
		 ('Barney', 'pwd', 'dary@mail.com'),
		 ('Barney', 'pwd', 'awesome@mail.com'),
		 ('Charles', 'pwd', 'kiss@mail.com'),
		 ('Charles', 'pwd', 'donkey@mail.com'),
		 ('Charles', 'pwd', 'blahblah@mail.com'),
		 ('Donald', 'pwd', 'dumb@mail.com'),
		 ('Donald', 'pwd', 'wall@mail.com'),
		 ('Eric', 'pwd', 'eric@mail.com'),
		 ('Eric', 'pwd', 'xing@mail.com'),
		 ('Ericson', 'pwd', 'marsh@mail.com'),
		 ('Ericson', 'pwd', 'mello@mail.com')
		]

c.executemany("INSERT INTO emailcloud VALUES (?, ?, ?)", users)

conn.commit()
conn.close()
