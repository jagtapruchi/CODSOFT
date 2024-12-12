#function for dynamically getting current script's directory:
def load_image(file_name):
    image_path = os.path.join(script_dir,file_name)
    return Image.open(image_path)

#contacts image:
image2 = load_image("profile.jpg")
photo2 = ImageTk.PhotoImage(image2)
image2_label = tk.Label(f2,image=photo2,borderwidth=0,height=35,bg="white")
image2_label.place(x=10,y=210)
image2_label.image = photo2

contacts_label = tk.Label(f2,text="Contacts",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
contacts_label.place(x=43,y=210)
contacts_label.bind("<Button-1>",lambda event: show_contacts())

#frequent contacts image:
image3 = load_image("frequent.jpg")
photo3 = ImageTk.PhotoImage(image3)
image3_label = tk.Label(f2,image=photo3,borderwidth=0,height=35,bg="white")
image3_label.place(x=10,y=260)
image3_label.image = photo3

l5 = tk.Label(f2,text="Frequent",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
l5.place(x=43,y=260)
l5.bind("<Button-1>", lambda event: fre_contacts())

#favorites image:
image4 = load_image("heart.jpg")
photo4 = ImageTk.PhotoImage(image4)
image4_label = tk.Label(f2,image=photo4,borderwidth=0,height=35,bg="white")
image4_label.place(x=10,y=310)
image4_label.image = photo4

l5 = tk.Label(f2,text="Favorites",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
l5.place(x=43,y=310)
l5.bind("<Button-1>",lambda event: fav_contacts())

#recycle bin image:
image5 = load_image("bin.jpg")
photo5 = ImageTk.PhotoImage(image5)
image5_label = tk.Label(f2,image=photo5,borderwidth=0,height=35,bg="white")
image5_label.place(x=10,y=365)
image5_label.image = photo5

l6 = tk.Label(f2,text="Recycle Bin",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
l6.place(x=43,y=365)
l6.bind("<Button-1>",lambda event: recycle_bin())