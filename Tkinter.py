from tkinter import *
import Test
def lookup():
    master=Tk()
    master.geometry('400x400')
    master.config(background='blue')


    def Submit():
        if len(vi.get())!=0:
            print("Sentimental Analysis for ",vi.get() ,"is \n")
            Test.aditya(vi.get())
        else:
            print('Enter String Please')
    def Cancel():
        master.destroy()
    vi=StringVar()
    l=Label(master,text="Enter The String to Analyse",font='verdana 19 bold',bg='skyblue',fg='Red').place(x=0,y=50,height=40,width=400)
    e=Entry(master,textvariable=vi).place(x=75,y=150,height=40,width=225)
            
    SubmitButton=Button(master,text='submit',font='verdana 16',bg='white',relief='flat',border=5,command=Submit).place(x=50,y=330,height=40,width=100)

    HomeButton=Button(master,text='Cancel',command=Cancel,font='verdana 16',bg='white',relief='flat',border=5).place(x=250,y=330,height=40,width=100)

    master.mainloop()

lookup()
