import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from datetime import date

price_list = [50,30,25]

def pay():
    global total_price
    if(customer_entry.get()==""):
        messagebox.showerror(title="Error",message="Please enter your name.")
    else:
        total_price = int(quntity1_combobox.get())*price_list[0]+int(quntity2_combobox.get())*price_list[1]+int(quntity3_combobox.get())*price_list[2]
        if(total_price==0):
            messagebox.showwarning(title="Error",message="Please select some dishes")
        else:
            name_label = ctk.CTkLabel(bill_frame,text=f'Customer Name: {customer_entry.get()}')
            name_label.place(x=0,y=100)
            price_label= ctk.CTkLabel(bill_frame,text=f'Total Price: {total_price} $')
            price_label.place(x=0,y=150)
            date_label = ctk.CTkLabel(bill_frame,text=f"Bill Date: {date.today()}")
            date_label.place(x=0,y=200)

def new():
    customer_entry.delete(0,END)
    quntity1_combobox.set(0)
    quntity2_combobox.set(0)
    quntity3_combobox.set(0)

def save():
    f=open(f"{customer_entry.get()} Bill","w")
    f.write(f"Customer Name: {customer_entry.get()}\n")
    f.write(f"Total Price: {total_price}$ \n")
    f.write(f"Bill Date: {date.today()}")
    messagebox.showinfo(title='Saved',message="Bill has been saved.")

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Cafe")
app.geometry("1000x400")
app.config(bg="#25283b")
app.resizable(False,False)


price_list = [50,30,25]
total_price = 0

bill_frame= ctk.CTkFrame(app,width=300,height=400,fg_color="#545457")
bill_frame.place(x=700,y=0)

menu_label = ctk.CTkLabel(app,text="Love Cafe",text_color="#FFFFFF",bg_color="#25283b")
menu_label.place(x=230,y=5)

img12 = PhotoImage(file=r"pasta.png")
img1 = img12.subsample(2, 2) 
img23 = PhotoImage(file=r"rice.png")
img2 = img23.subsample(2, 2) 
img43 = PhotoImage(file=r"sandwich.png")
img3  = img43.subsample(2, 2) 

img1_label = ctk.CTkLabel(app,image=img1,text='Seafood Pasta\n Price:50$',text_color="#FFFFFF",fg_color="#090b17",width=50,height=60,corner_radius=20,compound=TOP,anchor=N)
img1_label.place(x=30,y=70)

img2_label = ctk.CTkLabel(app,image=img2,text='Fried Rice\n Price:30$',text_color="#FFFFFF",fg_color="#090b17",width=50,height=60,corner_radius=20,compound=TOP,anchor=N)
img2_label.place(x=250,y=70)

img3_label = ctk.CTkLabel(app,image=img3,text='Sandwich\n Price:25$',text_color="#FFFFFF",fg_color="#090b17",width=50,height=60,corner_radius=20,compound=TOP,anchor=N)
img3_label.place(x=470,y=70)

quntity1_combobox = ctk.CTkComboBox(app,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3"),state="readonly")
quntity1_combobox.place(x=63,y=220)
quntity1_combobox.set(0)

quntity2_combobox = ctk.CTkComboBox(app,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3"),state="readonly")
quntity2_combobox.place(x=280,y=220)
quntity2_combobox.set(0)

quntity3_combobox = ctk.CTkComboBox(app,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3"),state="readonly")
quntity3_combobox.place(x=500,y=280)
quntity3_combobox.set(0)

customer_label = ctk.CTkLabel(app,text='Customer Name:',text_color="#FFFFFF",fg_color="#25283b")
customer_label.place(x=40,y=300)

customer_entry = ctk.CTkEntry(app,fg_color="#FFFFFF",text_color="#000000",border_color="#FFFFFF",width=200)
customer_entry.place(x=200,y=300)

pay_button = ctk.CTkButton(app,command=pay,text="Pay Bill",fg_color="#ad0c78",hover_color='#ad0c78',corner_radius=20,cursor="hand2")
pay_button.place(x=100,y=350)

save_button = ctk.CTkButton(app,command=save,text="Save Bill",fg_color="#ad0c78",hover_color='#ad0c78',corner_radius=20,cursor="hand2")
save_button.place(x=250,y=350)

new_button = ctk.CTkButton(app,command=new,text="New Bill",fg_color="#ad0c78",hover_color='#ad0c78',corner_radius=20,cursor="hand2")
new_button.place(x=400,y=350)


app.mainloop()