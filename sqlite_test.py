import sqlite3
conn = sqlite3.connect("mytest2.db")
cursor = conn.cursor()
#creat a table

order_create = """create table books3 (
ID INT PRIMARY KEY     NOT NULL,
NAME   TEXT    NOT NULL,
PRICE REAL NOT NULL);
"""
order='insert into books3(ID, NAME ,PRICE) values(1,"A",10);'

order2='insert into books3(ID, NAME ,PRICE) values(2,"B",20);'

order3='insert into books3(ID, NAME ,PRICE) values(3,"C",30);'

cursor.execute(order)
cursor.execute(order2)
cursor.execute(order3)
cursor.execute('update books3 set NAME = ?   where id = ? ',("b2",2))
cursor.execute("select * from books3")
#该例程对 seq_of_parameters 中的所有参数或映射执行一个 SQL 命令。
order='insert into books3(ID, NAME ,PRICE) values(?,?,?);'
cursor.executemany(order,[(4,"D",40),(5,"E",50)])

#result1= cursor.fetchone()
#result2= cursor.fetchmany(2)
result3= cursor.fetchall()
#print(result1)
#print(result2)
print(result3)
#delete
cursor.execute("delete from books3 where id=?",(1,))
cursor.execute("select * from books3")
result_new= cursor.fetchall()
print(result_new)

print("changed numbers, ",conn.total_changes())
conn.commit()
cursor.close()
conn.close()
