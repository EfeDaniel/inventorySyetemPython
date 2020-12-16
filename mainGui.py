
from  tkinter import *
from dataBase import  *
import  tkinter.messagebox




class Product:



    def  __init__(self,root):
        #create object reference instance of Database class p
        p= DataBase()
        p.conn()




        self.root = root
        self.root.title("Warehouse Inventory System")
        self.root.geometry("1325x690")
        self.root.config(bg="red")


        pid = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()

        def close():
            print("Product : close method called ")
            close = tkinter.messagebox.askyesno("Warehouse Inventory System","Really... Do you want to close the system")
            if close > 0 :
                root.destroy()
                print("Application close")
                return
        def update():
            print("Save method called")
            if(len(pid.get())!=0):
                p.delete(pd[0])
            if(len(pid.get())!=0):
                p.insert(pid.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
            productList.insert(END,(pid.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get()))




        def clear():
            print("Clear method called")
            self.txtpID.delete(0,END)
            self.txtContact.delete(0, END)
            self.txtCompany.delete(0, END)
            self.txtName.delete(0, END)
            self.txtPrice.delete(0, END)
            self.txtQty .delete(0, END)


        def save():
            print("Save method called")
            try:
                if (len(pid.get())!=0):
                    p.insert(pid.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                    productList.delete(0,END)
                    productList.insert(pid.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                    clear()
                    #show()#Data to be called after saving info to the database table

                else:


                    tkinter.messagebox.showerror("Inventory Management System","Please input product id")
            except:
                  sqlite3.IntegrityError




        def show():#show all data from the db in the scroll bar product list
            print("Show method called")
            productList.delete(0,END)
            for row in p.show():#calling the show in class database
                productList.insert(END,row,str(""))
            print("Show method done")

        def productRec(event):
            print("Product : productRect method called")
            global pd

            try:
                searchPd = productList.curselection()[0]
                pd= productList.get(searchPd)


                self.txtpID.delete(0,END)
                self.txtpID.insert(END,pd[0])



                self.txtName.delete(0,END)
                self.txtName.insert(END, pd[1])

                self.txtPrice.delete(0,END)
                self.txtPrice.insert(END,pd[2])

                self.txtQty.delete(0,END)
                self.txtQty.insert(END,pd[3])

                self.txtCompany.delete(0, END)
                self.txtCompany.insert(END, pd[4])

                self.txtContact.delete(0, END)
                self.txtContact.insert(END, pd[5])


                print("product Record done")
            except:
                IndexError






        def deletez():
            print("Delete Method Called")
            if(len(pid.get())!=0):
                p.delete(pd[0])
                clear()
                show()



        def search():
            print("Sesrch method called")
            productList.delete(0,END)
            for row in p.search(pid.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get()):
                productList.insert(END,row,str(""))




        """Create the Frame"""
        MainFrame = Frame(self.root,bg = "Blue" )
        MainFrame.grid()



        HeadFrame = Frame(MainFrame, bd =2 ,bg= 'white', relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle = Label(HeadFrame, font = ('arial',50,'bold'), fg='red',width=33,text = 'Warehouse Inventory Sales Purchase', bg='white')
        self.ITitle.grid()

        operationFrame = Frame(MainFrame,bd =1, width=1300, height=60,padx=50,pady=20,bg='white', relief=RIDGE)
        operationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame,bd=2, width=1290,height=400,padx=30,pady=20,bg='white',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        leftBodyFrame = LabelFrame(BodyFrame, bd=2, width=600, height=380, padx=20, pady=10, bg='blue', relief=RIDGE,
                                   font=('arial', 15, 'bold')
                                   , text='Product Item Details:')
        leftBodyFrame.pack(side=LEFT)

        RIGHTBodyFrame = LabelFrame(BodyFrame,bd=2,width=500,height=380,padx=20,pady=10,bg='blue',relief=RIDGE,font=('arial',15,'bold')
                                    ,text='Product Item Information:')
        RIGHTBodyFrame.pack(side=RIGHT)


        """Add the Widgets to LeftBodyFrame"""

        self.labelpID = Label(leftBodyFrame,font=('arial',15,'bold'), text="Product id",padx=2,pady=2 ,bg="white",fg='blue')
        self.labelpID.grid(row=0,column=0, sticky=W)

        self.txtpID = Entry(leftBodyFrame, font=('arial',20,'bold'),textvariable=pid, width=35)
        self.txtpID.grid(row=0,column=1, sticky=W)


        self.labelName = Label(leftBodyFrame, font=('arial', 15, 'bold'), text="Product Name",padx=2,pady=2,bg="white", fg='blue')
        self.labelName.grid(row=1, column=0, sticky=W)

        self.txtName = Entry(leftBodyFrame, font=('arial', 20, 'bold'),textvariable=pName, width=35)
        self.txtName.grid(row=1, column=1, sticky=W)


        self.labelPrice = Label(leftBodyFrame, font=('arial', 15, 'bold'), text="Product Price", padx=2, pady=2,bg="white", fg='blue')
        self.labelPrice.grid(row=2, column=0, sticky=W)

        self.txtPrice = Entry(leftBodyFrame, font=('arial', 20, 'bold'),textvariable=pPrice, width=35)
        self.txtPrice.grid(row=2, column=1, sticky=W)

        self.labelQty = Label(leftBodyFrame, font=('arial', 15, 'bold'), text="Product Quantity",padx=2,pady=2 ,bg="white", fg='blue')
        self.labelQty.grid(row=3, column=0, sticky=W)

        self.txtQty = Entry(leftBodyFrame, font=('arial', 20, 'bold'),textvariable=pQty, width=35)
        self.txtQty.grid(row=3, column=1, sticky=W)


        self.labelCompany = Label(leftBodyFrame, font=('arial', 15, 'bold'), text="Mgf. Company",padx=2,pady=2 ,bg="white", fg='blue')
        self.labelCompany.grid(row=4, column=0, sticky=W)

        self.txtCompany = Entry(leftBodyFrame, font=('arial', 20, 'bold'),textvariable=pCompany, width=35)
        self.txtCompany.grid(row=4, column=1, sticky=W)

        self.labelContact = Label(leftBodyFrame, font=('arial', 15, 'bold'), text="Company Contact",padx=2,pady=2, bg="white", fg='blue')
        self.labelContact.grid(row=5, column=0, sticky=W)

        self.txtContact = Entry(leftBodyFrame, font=('arial', 20, 'bold'),textvariable=pContact, width=35)
        self.txtContact.grid(row=5, column=1, sticky=W)


        """Add Scroll Bar"""

        scroll = Scrollbar(RIGHTBodyFrame)
        scroll.grid(row=0, column=1, sticky='ns')

        productList= Listbox(RIGHTBodyFrame, width=40, height=16, font=('arial', 12, 'bold'),
                yscrollcommand=scroll.set)
        productList.bind( '<<ListboxSelect>>', productRec)
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)


        """Add the buttons to operation frame"""

        self.btnSave = Button(operationFrame,text="Save",font=('arial', 20, 'bold'),height=1, width=6,bd=4, command = save)
        self.btnSave.grid(row=0,column=0)

        self.btnShow = Button(operationFrame, text="Show", font=('arial', 20, 'bold'), height=1, width=6, bd=4, command=show)
        self.btnShow.grid(row=0, column=1)

        self.btnClear = Button(operationFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=6, bd=4 , command=clear)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(operationFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=6, bd=4, command= deletez)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(operationFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=6, bd=4, command=search)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(operationFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=6, bd=4,command=update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnPrint = Button(operationFrame, text="Print", font=('arial', 20, 'bold'), height=1, width=6, bd=4,
                                command=update)
        self.btnPrint.grid(row=0, column=6)

        self.btnClose = Button(operationFrame, text="Close", font=('arial', 20, 'bold'), height=1, width=6, bd=4,command= close )
        self.btnClose.grid(row=0, column=7)

        def close():
            print("Product : close method called ")
        # close = tkinter.messagebox.askyesno("Warehouse Inventory System","Really... Do you want to close the system")
        # if close > 0 :
        #     root.destory()
        #     print("Application close")
        #     return




    def update(self):
        print("Update method called")




if __name__ == "__main__":


    root = Tk()
    application = Product(root)

    root.mainloop()



