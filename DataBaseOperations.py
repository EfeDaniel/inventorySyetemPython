
from mainGui import *
import  tkinter.messagebox


def closes ():


    print("Product : close method called ")
    close = tkinter.messagebox.askyesno("Warehouse Inventory System","Really... Do you want to close the system")
    if close > 0 :
         root.destroy()
         print("Application close")
         return




def clear():
    print("Clear method called")





def show():
    print("Show method called")

def deletez():
    print("Delete Method Called")

def search ():
    print("Sesrch method called")

def update():
    print("Update method called")




def main():
    closes()

    show()
    deletez()
    search()
    update()




if __name__== "__main__":
    main()



