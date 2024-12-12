import tkinter as tk
root=tk.Tk()
root.geometry("500x500")

main_frame=tk.Frame(root,bg="light yellow")
main_frame.pack(fill="both",expand=True)

title = tk.Label(root, anchor="center", font=("Times New Roman", 30),text="TO DO LIST", fg="black",bg="light yellow",relief="raised",width="10").place(x="650",y="15")

#name and date:
data1=tk.Label(root,text="Your Name: ",fg="Black",relief="flat",font=("Courier New",15,"bold"),bg="peachpuff2").place(x=10,y=115)
e1=tk.Entry(root, fg="gray26", font=("arial", 15))
e1.place(x="180", y="120",width=280)

data2=tk.Label(root,text="Month & Date: ",fg="Black",relief="flat",font=("Courier New",15,"bold"),bg="peachpuff2").place(x=500,y=115)
e2=tk.Entry(root, fg="gray26", font=("arial", 15))
e2.place(x="700", y="115",width=280)

data3=tk.Label(root,text="Affirmations: ",fg="Black",relief="flat",font=("Courier New",15,"bold"),bg="peachpuff2").place(x=1000,y=115)
e2=tk.Entry(root, fg="gray26", font=("arial", 15))
e2.place(x="1185", y="115",width=280)


#Top Priorities:
f1=tk.Frame(root,bg="Indianred3")
f1.place(x=1000,y=200,width=500,height=250)

l1=tk.Label(f1,text="My Top Priorities: ",font=("Courier New",15,"bold"),relief="raised",width=20,bg="white").place(x=5,y=10)

e3=tk.Entry(f1,fg="brown4",font=("Courier New",15,"bold"))
e3.place(x=5,y=50,width=480)

e4=tk.Entry(f1,fg="brown4",font=("Courier New",15,"bold"))
e4.place(x=5,y=95,width=480)

e5=tk.Entry(f1,fg="brown4",font=("Courier New",15,"bold"))
e5.place(x=5,y=140,width=480)

e6=tk.Entry(f1,fg="brown4",font=("Courier New",15,"bold"))
e6.place(x=5,y=190,width=480)


#Remind me:
f2=tk.Frame(root,bg="peachpuff")
f2.place(x=1000,y=500,width=500,height=260)

l2=tk.Label(f2,text="Remind me!", font=("Courier New",15,"bold"),relief="raised",width=15,bg="white")
l2.place(x=5,y=10)

text =tk.Text(f2,width=42,height=7,fg="maroon",wrap="word",font=("Courier New",15,"bold"),padx=10,pady=10)
text.place(x=7,y=45)

scrollbar1 = tk.Scrollbar(f2, orient="vertical", command=text.yview)
scrollbar1.place(x=480, y=45, height=195) 
text.config(yscrollcommand=scrollbar1.set)


#To do:
f3 = tk.Frame(root, bg="peachpuff")
f3.place(x=20, y=200, width=950, height=570)

l3= tk.Label(f3, text="Tasks to do:", width=25, font=("Courier New", 20, "bold"),relief="raised", bg="white")
l3.pack(pady=10)

canvas = tk.Canvas(f3, bg="peachpuff")
canvas.pack(side="left", fill="both", expand=True, padx=10, pady=50)

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

task_container = tk.Frame(canvas, bg="peachpuff")
task_container_id = canvas.create_window((0, 60), window=task_container, anchor="nw")

def update_scrollregion(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

task_container.bind("<Configure>", update_scrollregion)


def add_task():
    task_text = task_entry.get()
    if task_text:
        task_frame = tk.Frame(task_container,bg="bisque")
        task_frame.pack(fill="x",padx=5,pady=5)
        
        task_label = tk.Label(task_frame,text=task_text,font=("Courier New",15,"bold","underline"),bg="bisque",fg="maroon",height=2)
        task_label.pack(side="left",padx=10)
        
        task_button = tk.Button(task_frame,text="Completed!",bg="white",command=lambda: remove_task(task_frame),font=("Courier New",33,"bold"))
        task_button.pack(side="right",padx=5)
        
        task_entry.delete(0,tk.END)
        
        update_scrollregion()
    
def remove_task(task_frame):
    task_frame.destroy()
    update_scrollregion()

task_entry = tk.Entry(f3,font=("Courier New",15,"bold"),width=13,fg="Indianred3")
task_entry.place(x=270,y=60)

add_task_button = tk.Button(f3,text="add task",font=("Courier New",12,"bold"),command=add_task,bg="white")
add_task_button.place(x=700,y=60)

def add_task():
    task_text = task_entry.get()
    if task_text:
        task_frame = tk.Frame(task_container,bg="bisque")
        task_frame.pack(fill="x",padx=5,pady=5)
        
        task_label = tk.Label(task_frame,text=task_text,font=("Courier New",15,"bold","underline"),bg="bisque",fg="maroon",height=2)
        task_label.pack(padx=10,side="left")
        
        task_button = tk.Button(task_frame,text="Completed!",bg="white",command=lambda: remove_task(task_frame),font=("Courier New",12,"bold"))
        task_button.pack(side="right",padx=5)
        
        task_entry.delete(0,tk.END)
        
        update_scrollregion()

def remove_task(task_frame):
    task_frame.destroy()
    update_scrollregion()
    
task_entry = tk.Entry(f3,font=("Courier New",15,"bold"),width=33,fg="Indianred3")
task_entry.place(x=270,y=60)

add_task_button = tk.Button(f3,text="add task",font=("Courier New",12,"bold"),command=add_task,bg="white")
add_task_button.place(x=700,y=60)

root.mainloop()