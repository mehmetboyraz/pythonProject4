
import sqlite3 as sql

connection = sql.connect("berkbank_customers.db")
cursor= connection.execute("select * from customer")
datacustomer = cursor.fetchall()
connection.close()


def update(secılencolon, yenı_değer, secılenHucre  ):
    connection = sql.connect("berkbank_customers.db")
    connection.execute(" update customer set " + secılencolon+" = "+ str(yenı_değer) + " where  customerId = "+str(secılenHucre))
    connection.commit()
    connection.close()