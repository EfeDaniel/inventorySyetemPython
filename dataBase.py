import  sqlite3

class DataBase:
    def conn(self):
        print("Database : connection me")

        con =  sqlite3.connect("inventory.db")
        cur= con.cursor()
        query= "create table if not exists product(pid integer primary key, pname text," \
               "price text, quantity text, company text, contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connected")


    def insert(self,pid,name,price,quantity,company,contact):
        print("Database : insert method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()

        cur.execute("insert into product values(?,?,?,?,?,?)",(pid,name,price,quantity,company,contact))
        con.commit()
        con.close()
        print("Database : insert done" )

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query ="select  * from  product"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method done")
        return  rows

    def delete(self,pid):
        print("Database : Delete method called",pid)
        con  = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute( "delete from  product where pid =? ",(pid,))
        con.commit()
        con.close()
        print(pid,"Database : Delete method called")


    def search(self,pid="",name = "" , price="", quantity="",company="", contact=""):
        print("Database : search method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("select * from product where pid =? or pname =? or price =? or quantity =? or company =? or contact =?",(pid,name,price,quantity,company,contact))
        row = cur.fetchall()
        print("row",row)
        con.close()
        print("Database : search method done")
        return  row


    def update(self,pid="",name = "" , price="", quantity="",company="", contact=""):
        print("Database : update method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("update set pid=? or pname=? or price=? or quantity=? company=? or contact=? where pid=? ",(pid,name,price,quantity,company,contact ))
        con.commit()
        con.close()
        print("Database : update method done")






















