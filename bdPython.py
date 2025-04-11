import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  database="bdpython",
  port="3306",
  user="root",
  password="root"
)
#cursor e a forma que podemos acessar o banco de dados
mycursor = con.cursor()

sql = "INSERT INTO pessoa (nome, idade) VALUES (%s, %s)"
val = ("Lucas", "25")
mycursor.execute(sql, val)
con.commit()

mycursor.execute("SELECT * FROM pessoa")
for x in mycursor:
    for i in x:
        print(i)
    