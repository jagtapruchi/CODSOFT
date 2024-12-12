import tkinter as tk
from tkinter import ttk
import os
from PIL import Image,ImageTk
from tkinter import messagebox
import re

root = tk.Tk()

#recycle bin:
recycle_bin_list =[]

def recycle_bin():
    for widget in f1.winfo_children():
        widget.destroy()
        
    title = tk.Label(f1,text="Recycle Bin",font=("arial",25,"bold"),fg="black",bg="white",borderwidth=0,cursor="hand2" )
    title.place(x=10,y=20,anchor="nw")
    
    if not recycle_bin_list:
        tk.Label(f1,text="Recycle Bin is empty",fg="black",bg="white",font=("bold",18),borderwidth=0,cursor="hand2").place(relx=0.5,rely=0.5,anchor="center")
        return
    else:
        y_offset = 100  # Start below the title
        vertical_spacing = 70  # Spacing between rows
        
        for contact in recycle_bin_list:
            # Display contact details
            contact_display = f"{contact['first_name']} {contact['surname']} ({contact['phone']})"
            contact_label = tk.Label(f1, text=contact_display, fg="black", bg="white", font=("arial", 20))
            contact_label.place(x=20, y=y_offset)
            
            # Restore button
            restore_btn = tk.Button(f1, text="Restore", bg="green", fg="white", command=lambda c=contact: restore_contact(c), font=("arial", 15))
            restore_btn.place(x=400, y=y_offset)
            
            # Increment y_offset for the next contact
            y_offset += vertical_spacing

def restore_contact(contact):
    recycle_bin_list.remove(contact)
    contacts.append(contact)
    messagebox.showinfo("Restored", f"Contact {contact['first_name']} {contact['surname']} has been restored")
    recycle_bin()
    


#function to delete contacts:
def delete_contacts(contact):
    confirm = messagebox.askyesno("Confirm Delete",f"Are you sure you want to delete {contact['first_name']} {contact['surname']}?")
    if confirm:
        contacts.remove(contact)
        recycle_bin_list.append(contact)
        update_contacts_list()
        messagebox.showinfo("Deleted","Contact has been deleted.")
    else: print("Delete operation cancelled.")



#function for update button:
def update_contact(contact):
    for widget in f1.winfo_children():
        widget.destroy()
    
    tk.Label(f1,text="Update Contact",font=("arial",25,"bold"),bg="white",fg="black").pack(pady=10)
    
    tk.Label(f1,text="First Name: ",font=("arial,18"),bg="white").place(x=35,y=15)
    first_name_entry = tk.Entry(f1,width=45,borderwidth=1,font=("arial",16))
    first_name_entry.place(x=185,y=20)
    first_name_entry.insert(0,contact['first_name'])
    
    tk.Label(f1, text="Surname: ", font=("arial", 18), bg="white").place(x=35, y=70)
    surname_entry = tk.Entry(f1, width=45, borderwidth=1, font=("arial", 16))
    surname_entry.place(x=185, y=75)
    surname_entry.insert(0, contact['surname'])
    
    tk.Label(f1, text="Home address: ", font=("arial", 18), bg="white").place(x=35, y=120)
    home_address_entry = tk.Entry(f1, width=45, borderwidth=1, font=("arial", 16))
    home_address_entry.place(x=197, y=125)
    home_address_entry.insert(0, contact['home_address'])
    
    tk.Label(f1, text="Work address: ", font=("arial", 18), bg="white").place(x=35, y=177)
    work_address_entry = tk.Entry(f1, width=45, borderwidth=1, font=("arial", 16))
    work_address_entry.place(x=196, y=179)
    work_address_entry.insert(0, contact['work_address'])
    
    tk.Label(f1, text="Phone: ", font=("arial", 18), bg="white").place(x=35, y=232)
    phone_entry = tk.Entry(f1, width=45, borderwidth=1, font=("arial", 16))
    phone_entry.place(x=185, y=233)
    phone_entry.insert(0, contact['phone'])
    
    tk.Label(f1, text="Email Id: ", font=("arial", 18), bg="white").place(x=35, y=288)
    email_entry = tk.Entry(f1, width=45, borderwidth=1, font=("arial", 16))
    email_entry.place(x=185, y=290)
    email_entry.insert(0, contact['email_id'])
    
    tk.Label(f1, text="Day: ", font=("arial", 18), bg="white").place(x=35, y=345)
    day_entry = tk.Entry(f1, width=5, borderwidth=1, font=("arial", 16))
    day_entry.place(x=95, y=345)
    day_entry.insert(0, contact['day'])
    
    month_entry = ttk.Combobox(f1, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], font=("arial", 12))
    month_entry.place(x=200, y=345, height=30, width=180)
    month_entry.set(contact['month'])
    
    tk.Label(f1, text="Year: ", font=("arial", 18), bg="white").place(x=399, y=345)
    year_entry = tk.Entry(f1, width=7, borderwidth=1, font=("arial", 16))
    year_entry.place(x=469, y=345)
    year_entry.insert(0, contact['year'])
    
    tk.Label(f1, text="Notes: ", font=("arial", 18), bg="white").place(x=35, y=400)
    notes_entry = tk.Text(f1, width=50, height=5, font=("arial", 14), wrap="word", borderwidth=2)
    notes_entry.place(x=35, y=450)
    notes_entry.insert("1.0", contact['notes'])
    
    def save_updated_contact():
        contact['first_name'] = first_name_entry.get()
        contact['surname'] = surname_entry.get()
        contact['home_address'] = home_address_entry.get()
        contact['work_address'] = work_address_entry.get()
        contact['phone'] = phone_entry.get()
        contact['email_id'] = email_entry.get()
        contact['day'] = day_entry.get()
        contact['month'] = month_entry.get()
        contact['year'] = year_entry.get()
        contact['notes'] = notes_entry.get("1.0", "end-1c").strip()
        
        messagebox.showinfo("Success",f"Contact for {contact['first_name']} {contact['surname']} updated!")
        show_contacts()
        
    save_updates_btn = tk.Button(f1,text="Save Changes",bg="red",fg="white",font=("arial",19),command=save_updated_contact)
    save_updates_btn.place(x=300,y=590)
    
    

#function for more info button:
def show_more_info(contact):
    for widget in f1.winfo_children():
        widget.destroy()
    
    tk.Label(f1, text="Contact Details", font=("arial", 25, "bold"), bg="white", fg="black").pack(pady=10)
    tk.Label(f1, text=f"First Name: {contact['first_name']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Surname: {contact['surname']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Phone: {contact['phone']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Home address: {contact['home_address']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Work address: {contact['work_address']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Email Id: {contact['email_id']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"D.O.B: {contact['day']}-{contact['month']}-{contact['year']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)
    tk.Label(f1, text=f"Notes: {contact['notes']}", font=("arial", 18), bg="white").pack(anchor="w", padx=20)

    update_btn = tk.Button(f1,text="Update",bg="lightsalmon2",fg="black",font=("arial",18),command= lambda: update_contact(contact))
    update_btn.pack(side=tk.LEFT, padx=60)
    
    delete_btn = tk.Button(f1,text="Delete Contact",bg="gainsboro",fg="black",font=("arial",18),command = lambda: delete_contacts(contact))
    delete_btn.pack(side=tk.LEFT, padx=15)
    
    
    


#function to add contacts to frequently contacted contacts:
frequent_contacts = []
def fre_contacts():
    add_to_frequent()

def add_to_frequent():
    for widget in f1.winfo_children():
        widget.destroy()
        
    frequent_contact_label = tk.Label(f1,text="Frequently Contacted",font=("arial",25,"bold"),fg="black",bg="white",borderwidth=0,cursor="hand2" )
    frequent_contact_label.place(x=10,y=10,anchor="nw")
    frequent_contact_label.bind("<Button-1>",lambda event: fre_contacts())
    
    create_contact_label = tk.Label(f1, text="+  Create Contact ", font=("arial", 15), fg="black", bg="white",borderwidth=0, cursor="hand2",activebackground="white", relief="raised")
    create_contact_label.pack(padx=10, pady=80, anchor="w")
    create_contact_label.bind("<Button-1>", lambda event: create_contact())
    
    if len(favorite_contacts) == 0:
        text3 = tk.Label(f1,text="No frequent contacts yet",font=("bold",18),bg="white",fg="black")
        text3.place(relx=0.5,rely=0.5,anchor="center")
    
    for contact in frequent_contacts:
        contact_display = f"{contact['first_name']} {contact['surname']} ({contact['phone']})"
        tk.Label(f1, text=contact_display, font=("arial", 22), fg="black", bg="white",borderwidth=0, anchor="w").pack(padx=15, pady=1,anchor="nw")


#function to add contacts to favorites:
favorite_contacts = []

def add_to_favorites(contact):
    if contact not in favorite_contacts:
        favorite_contacts.append(contact)
        messagebox.showinfo("Success", f"{contact['first_name']} {contact['surname']} added to favorites!")
    else:
        messagebox.showinfo("Already Added", f"{contact['first_name']} {contact['surname']} is already in your favorites!")

    fav_contacts()


def fav_contacts():
    add_to_fav()

def add_to_fav():
    for widget in f1.winfo_children():
        widget.destroy()
        
    fav = tk.Label(f1,text="My Favorites",font=("arial",25,"bold"),fg="black",bg="white",borderwidth=0,cursor="hand2" )
    fav.place(x=10,y=10,anchor="nw")
    fav.bind("<Button-1>",lambda event: fav_contacts())
    
    create_contact_label = tk.Label(f1, text="+  Create Contact ", font=("arial", 15), fg="black", bg="white",borderwidth=0, cursor="hand2",activebackground="white", relief="raised")
    create_contact_label.pack(padx=10, pady=80, anchor="w")
    create_contact_label.bind("<Button-1>", lambda event: create_contact())
    
    if len(favorite_contacts) == 0:
        text3 = tk.Label(f1,text="No favorite contacts yet",font=("bold",18),bg="white",fg="black")
        text3.place(relx=0.5,rely=0.5,anchor="center")
    
    for contact in favorite_contacts:
        contact_display = f"{contact['first_name']} {contact['surname']} ({contact['phone']})"
        tk.Label(f1, text=contact_display, font=("arial", 22), fg="black", bg="white",borderwidth=0, anchor="w").pack(padx=15, pady=1,anchor="nw")


#function to save created contacts:
contacts = []

def save_contact(first_name, surname, phone, home_address, work_address,email_id, day,month,year, notes):
    # Check if mandatory fields are filled
    if not first_name.strip():
        messagebox.showerror("Input Error", "First Name is required!")
        return
    if not phone.strip():
        messagebox.showerror("Input Error", "Phone is required!")
        return

    # Validate that the phone field contains only numeric characters
    if not phone.isdigit():
        messagebox.showerror("Input Error", "Phone number must contain only digits!")
        return
    
    # Checks valid phone number pattern
    phone_pattern = r'^\+?[0-9]*$'  # Allow optional '+' at the beginning
    if not re.match(phone_pattern, phone):
        messagebox.showerror("Input Error", "Phone number is invalid!")
        return
    
    for contact in contacts:
        if contact["phone"] == phone:
            messagebox.showerror("Duplicate Contact", "A contact with this phone number already exists!")
            return
    
    new_contact = {
        "first_name": first_name,
        "surname": surname,
        "phone": phone,
        "home_address": home_address,
        "work_address": work_address,
        "email_id": email_id,
        "day":day,
        "month":month,
        "year":year,
        "notes":notes        
    }

    contacts.append(new_contact)
    messagebox.showinfo("Success", f"Contact for {first_name} {surname} saved!")
    show_contacts()
    
    

def show_contacts():
    update_contacts_list()
    
def update_contacts_list():
    for widget in f1.winfo_children():
        widget.destroy()
        
    contacts_label = tk.Label(f1,text="My Contacts",font=("arial",25,"bold"),fg="black",bg="white",borderwidth=0,cursor="hand2" )
    contacts_label.place(x=10,y=10,anchor="nw")
    contacts_label.bind("<Button-1>",lambda event: show_contacts())
    
    create_contact_label = tk.Label(f1, text="+  Create Contact ", font=("arial", 15), fg="black", bg="white",borderwidth=0, cursor="hand2",activebackground="white", relief="raised")
    create_contact_label.pack(padx=10, pady=80, anchor="w")
    create_contact_label.bind("<Button-1>", lambda event: create_contact())
    
    if len(contacts) == 0:
        text2 = tk.Label(f1,text="No contacts yet",font=("bold",18),bg="white",fg="black")
        text2.place(relx=0.5,rely=0.5,anchor="center")
    
    y_offset = 180  
    vertical_spacing = 70  

    for contact in contacts:
        contact_display = f"{contact['first_name']} {contact['surname']} ({contact['phone']})"
        contact_label = tk.Label(f1, text=contact_display, font=("arial", 22), fg="black", bg="white", borderwidth=0, anchor="w")
        contact_label.place(x=15, y=y_offset)

        fav_btn = tk.Button(f1, text="Add to Favorites", font=("arial", 15), fg="black", bg="lightpink", width=13)
        fav_btn.place(x=490, y=y_offset + 10)
        fav_btn.bind("<Button-1>", lambda event, c=contact: add_to_favorites(c))

        more_info_btn = tk.Button(f1, text="More Info", font=("arial", 15), fg="black", bg="lightgray", width=13, height=1)
        more_info_btn.place(x=680, y=y_offset + 10)
        more_info_btn.bind("<Button-1>", lambda event, c=contact: show_more_info(c))

        y_offset += vertical_spacing        
        
    

#function to create contacts dynamically:
def create_contact():
    global first_name_entry, surname_entry, phone_entry, company_entry, job_title_entry, email_entry, day_entry, month_entry, year_entry, notes_entry
    
    for widget in f1.winfo_children():
        widget.destroy()
    
    contact_frame = tk.Frame(f1, bg="white")
    contact_frame.pack(fill="both", expand=True, pady=15)
    
    tk.Label(contact_frame, text="First Name: ", font=("arial", 18), bg="white").place(x=35, y=15)
    first_name_entry = tk.Entry(contact_frame, width=45, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    first_name_entry.place(x=210, y=20)
    
    tk.Label(contact_frame, text="Surname: ", font=("arial", 18), bg="white").place(x=35, y=70)
    surname_entry = tk.Entry(contact_frame, width=45, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    surname_entry.place(x=210, y=75)
    
    tk.Label(contact_frame, text="Email Id: ", font=("arial", 18), bg="white").place(x=35, y=120)
    email_id_entry = tk.Entry(contact_frame, width=45, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    email_id_entry.place(x=210, y=125)
    
    tk.Label(contact_frame, text="Home Address: ", font=("arial", 18), bg="white").place(x=35, y=177)
    home_address_entry = tk.Entry(contact_frame, width=45, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    home_address_entry.place(x=210, y=179)
    
    tk.Label(contact_frame, text="Work Address: ", font=("arial", 18), bg="white").place(x=35, y=232)
    work_address_entry = tk.Entry(contact_frame, width=45, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    work_address_entry.place(x=210, y=233)
    
    
    combo = ttk.Combobox(contact_frame, values=["Algeria: +213", "Angola: +244", "Botswana: +267", "Burkina Faso: +226", "Egypt: +20", "Ghana: +233", "Kenya: +254", "Nigeria: +234", "South Africa: +27", "Afghanistan: +93", "China: +86", "India: +91", "Japan: +81", "South Korea: +82", "Saudi Arabia: +966", "Thailand: +66", "United Arab Emirates: +971",  "Austria: +43", "Belgium: +32", "France: +33", "Germany: +49", "Italy: +39", "Netherlands: +31", "Spain: +34", "United Kingdom: +44", "Canada: +1", "Mexico: +52", "United States: +1", "Australia: +61", "Fiji: +679", "New Zealand: +64", "Papua New Guinea: +675", "Argentina: +54", "Brazil: +55", "Chile: +56", "Colombia: +57", "Peru: +51", "Bahamas: +1-242", "Barbados: +1-246", "Jamaica: +1-876", "Trinidad and Tobago: +1-868", "Antarctica: +672", "Greenland: +299"], font=("arial", 12))
    combo.current(11)
    combo.place(x=35, y=290, width=180, height=30)
    
    tk.Label(contact_frame, text="Phone: ", font=("arial", 18), bg="white").place(x=250, y=288)
    phone_entry = tk.Entry(contact_frame, width=20, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    phone_entry.place(x=340, y=290)
    
    
    tk.Label(contact_frame, text="Day: ", font=("arial", 18), bg="white").place(x=35, y=355)
    day_entry = tk.Entry(contact_frame, width=5, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    day_entry.place(x=95, y=355)
    
    
    tk.Label(contact_frame,text="Month: ",font=("arial", 18), bg="white").place(x=180, y=355)
    month_entry = ttk.Combobox(contact_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], font=("arial", 12))
    month_entry.current(0)
    month_entry.place(x=265, y=355, height=30, width=180)
    
    
    tk.Label(contact_frame, text="Year: ", font=("arial", 18), bg="white").place(x=475, y=355)
    year_entry = tk.Entry(contact_frame, width=7, borderwidth=1, font=("arial", 16), bg="whitesmoke", fg="black")
    year_entry.place(x=550, y=355)
    
    
    tk.Label(contact_frame, text="Notes:", font=("arial", 18), bg="white").place(x=35, y=450)
    notes_entry = tk.Text(contact_frame, width=20, height=5, font=("arial", 14), fg="black", wrap="word", borderwidth=2,bg="whitesmoke")
    notes_entry.place(x=140, y=450)
    
    save_button = tk.Button(contact_frame, width=7, height=2, bg="tomato", fg="White", activebackground="white", text="Save", font=("arial", 12, "bold"), command=lambda: save_contact(first_name_entry.get(), surname_entry.get(), phone_entry.get(), home_address_entry.get(),work_address_entry.get(), email_id_entry.get(), day_entry.get(), month_entry.get(),year_entry.get(), notes_entry.get("1.0", "end-1c")))
    save_button.place(x=400, y=600)


#right side frame contents:
f1 = tk.Frame(root,bg="white",width=1100,height=900)
f1.pack(fill="both",padx=5,pady=30,expand=False,side="right")
f1.pack_propagate(False) 


#f1 image
script_dir = os.path.dirname(os.path.abspath(__file__))

#function to load the images dynamically:
def load_image(file_name):
    image_path = os.path.join(script_dir,file_name)
    return Image.open(image_path)

image = load_image("photo.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(f1, image=photo, borderwidth=0)
image_label.place(relx=0.5, rely=0.5, anchor="center")
image_label.image = photo

# contact() label
l1 = tk.Label(f1, bg="white", fg="black", width=80, height=2, text=f"Contacts ({len(contacts)})", font=("arial", 25), anchor="w")
l1.pack(padx=8, pady=0, side="top")

text = tk.Label(f1, text="No contacts yet", font=("bold", 18), bg="white", fg="black")
text.place(x=470, y=450)

#menu button
menu_btn = tk.Canvas(root,width=40,height=30,bg="whitesmoke",highlightthickness=0,bd=0,borderwidth=0)
menu_btn.pack(padx=20,pady=35,anchor="nw")

line1 = menu_btn.create_line(5,6,35,6, width=3,fill="black")
line2 = menu_btn.create_line(5,15,35,15, width=3,fill="black")
line3 = menu_btn.create_line(5,24,35,24, width=3,fill="black")

#main screen contacts image
image1 = os.path.join(os.getcwd(), "contacts.png")
image1 = Image.open(r"C:\Users\RUCHI\Desktop\python ruchi\Contact List\contacts.png")  
photo1 = ImageTk.PhotoImage(image1)
image1_label = tk.Label(root, image=photo1, borderwidth=0)
image1_label.place(x=75, y=25)
image1_label.image = photo1

l2 = tk.Label(root, fg="Black", font=("arial", 20), text="Contacts")
l2.place(x=145, y=35)

#SIDE BAR FRAME contents:
f2 = tk.Frame(root,width=525,bg="white",height=659)
f2.pack(padx=5,pady=0,anchor="w")
f2.pack_propagate(False)

#search bar:
search_bar = None

def add_search_bar():
    global search_bar
    search_bar = tk.Entry(f2,text="Search",width=31,font=("arial",17),bg="whitesmoke")
    search_bar.place(x=5,y=50,anchor="w")

    search_btn= tk.Button(f2,text="Search",font=("arial",12),bg="lightgray",fg="Black",activebackground="White",command=lambda:perform_search(search_bar.get()))
    search_btn.place(x=5,y=80)

    clear_btn = tk.Button(f2,text="Clear",font=("arial",12),bg="lightgray",fg="Black",activebackground="White",command=lambda: show_contacts())
    clear_btn.place(x=80,y=80)
    
def perform_search(search_query):
    if not search_query.strip():
        messagebox.showerror("Input Error","Search query cannot be empty!")
        return
    
    search_query = search_query.lower()
    
    filtered_contacts = [
        contact for contact in contacts
        if search_query in contact['first_name'].lower() or
           search_query in contact['surname'].lower() or
           search_query in contact['phone'].lower() or
           search_query in contact['email_id'].lower() 
    ]
    
    filtered_contacts_list(filtered_contacts)

def filtered_contacts_list(filtered_contacts=None):
    for widget in f1.winfo_children():
        widget.destroy()
        
    add_search_bar()
    
    if filtered_contacts is None:
        filtered_contacts = contacts
        
    if not filtered_contacts:
        error_label = tk.Label(f1,text="No contacts found!",font=("bold",18),bg="white",fg="black")
        error_label.place(relx=0.5,rely=0.5,anchor="center")
        
    else: 
        for contact in filtered_contacts:
            display = f"{contact['first_name']} {contact['surname']} ({contact['phone']})"
            filter_contact_label = tk.Label(f1, text=display, font=("arial", 22), fg="black", bg="white", borderwidth=0, anchor="w")
            filter_contact_label.pack(padx=15, pady=10, anchor="nw")
            
        more_info_btn = tk.Button(f1, text="More Info", font=("arial", 15), fg="black", bg="lightgray",width=13,height=1)
        more_info_btn.pack(anchor="ne", padx=80, pady=0)
        more_info_btn.bind("<Button-1>", lambda event, c=contact: show_more_info(c)) 
           
add_search_bar()

l3 = tk.Label(f2,text="+  Create Contact ",font=("arial",20),fg="black",bg="skyblue3",borderwidth=0,cursor="hand2",relief="raised")
l3.pack(padx=10,pady=150,anchor="w")
l3.bind("<Button-1>",lambda event: create_contact())


#function for dynamically getting current script's directory:
script_dir = os.path.dirname(os.path.abspath(__file__))

#function to load images dynamically:
def load_image(file_name):
    image_path = os.path.join(script_dir,file_name)
    return Image.open(image_path)

#contacts image:
image2 = load_image("profile.jpg")
photo2 = ImageTk.PhotoImage(image2)
image2_label = tk.Label(f2,image = photo2,borderwidth=0,height=35,bg="white")
image2_label.place(x=10,y=210)
image2_label.image = photo2

contacts_label = tk.Label(f2,text="Contacts",bg="white",fg="black",font=("arial",20),borderwidth=0,cursor="hand2")
contacts_label.place(x=43,y=210)
contacts_label.bind("<Button-1>",lambda event: show_contacts())

#frequent contacts image:
image3 = load_image("frequent.jpg")
photo3 = ImageTk.PhotoImage(image3)
image3_label = tk.Label(f2,image=photo3,borderwidth=0,height=35,bg="white")
image3_label.place(x=10,y=260)
image3_label.image = photo3

l5 = tk.Label(f2,text="Frequent Contacts",bg="white",fg="black",font=("arial",20),borderwidth=0,cursor="hand2")
l5.place(x=43,y=260)
l5.bind("<Button-1>",lambda event: fre_contacts())

#favorite contacts image:
image4 = load_image("heart.jpg")
photo4 = ImageTk.PhotoImage(image4)
image4_label = tk.Label(f2,image=photo4,borderwidth=0,height=35,bg="white")
image4_label.place(x=10,y=310)
image4_label.image = photo4

l6 = tk.Label(f2,text="Favorites",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
l6.place(x=43,y=310)
l6.bind("<Button-1>",lambda event: fav_contacts())

#recycle-bin image:
image5 = load_image("bin.jpg")
photo5 = ImageTk.PhotoImage(image5)
image5_label = tk.Label(f2,image=photo5,borderwidth=0,height=35,bg="white")
image5_label.place(x=10,y=365)
image5_label.image = photo5

l6 = tk.Label(f2,text="Recycle Bin",font=("arial",20),fg="black",bg="white",borderwidth=0,cursor="hand2")
l6.place(x=43,y=365)
l6.bind("<Button-1>",lambda event: recycle_bin())

root.mainloop()