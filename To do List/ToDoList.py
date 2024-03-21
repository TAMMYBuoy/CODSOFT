import tkinter
from tkinter import *
from PIL import Image, ImageTk


list=Tk()
list.title("NOTES")
list.geometry("450x600+20+50")
list.resizable(True,True)

task_list= []
def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task !='\n':
                    task_list.append(task)
                    listbox.insert(END,task)
    except:
        file=open('tasklist.txt')
        file.close()

icon_image_path = "Images/pngwing.png"  # Ensure this path is correct
icon_image = Image.open(icon_image_path)
photo_icon = ImageTk.PhotoImage(icon_image)
list.iconphoto(False, photo_icon)
#icon on the window bar
#Image_icon=PhotoImage("Images\pngwing.png")
#list.iconphoto(False,Image_icon)
#heading.place(relx=0, rely=0.0, anchor=NW)

#TOP BAR
#TopImage=PhotoImage(file="Images/pngwing.com")
#Label(list,image=TopImage).pack()


# NOTEIMAGE
#noteImage=PhotoImage(file=)
#Label(list,image=noteImage, bg="").place(x=  , y=  )

frame2= Frame(list, bg="#f7eb3b")
frame2.pack(fill=BOTH, expand=TRUE)


heading=Label(frame2, text="TO DO LIST",font="tnr 30 bold", fg="white",border=30,bg="#f7eb3b")
heading.place(relx=0.5, rely=0.07, anchor=CENTER)


#main


frame= Frame(frame2,width=400, height=50, bg="white")
frame.place(relx=0.5, y= 110, anchor=CENTER)



task=StringVar()
task_entry=Entry(frame,width=18,font="timesnewroman 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD", font="arial 20 bold", width=6, bd=0, bg="blue", fg="white", command=addTask)
button.place(x=300, y=0)


#listbox
frame1= Frame(frame2, bd=3, width=700, height=280, bg="white")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12, 'bold',),width=40,height=16,bg="#f5c825",fg="white",cursor="hand2",selectbackground="#6ef525")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#deletion
#delete_image_path = "Images/trash.png"  # Update this path
#delete = Image.open(delete_image_path)
#photo = ImageTk.PhotoImage(delete)
#deletebutton = Button(frame2, image=photo)
#deletebutton.pack()
delete=Button(frame2,text="DELETE", font="arial 20 bold", width=10,height=2, bd=0, bg="Red", fg="white", command=deleteTask)
delete.place(x=300, y=0)
#Delete_icon=PhotoImage(file="Images/trash.png")
#Button(frame2,image=Delete_icon,bd=0,width=100, height=100).pack(pady=20)
delete.pack(pady=20)



list.mainloop()