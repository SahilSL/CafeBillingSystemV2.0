from tkinter import *
from tkinter import messagebox
import random
import os
import tempfile
import smtplib

# Functionality ---->
def clear():
    FrenchFriesEntry.delete(0,END)
    SandwichEntry.delete(0,END)
    BurgerEntry.delete(0,END)
    PizzaEntry.delete(0,END)
    DessertEntry.delete(0,END)
    PastaEntry.delete(0,END)
    ChickenTikkaEntry.delete(0,END)
    ChickenAngaraEntry.delete(0,END)
    PaneerTikkaEntry.delete(0,END)
    NoodlesEntry.delete(0,END)
    ManchurianEntry.delete(0,END)
    AlooTikkiEntry.delete(0,END)
    CocktailEntry.delete(0,END)
    MojitoEntry.delete(0,END)
    PepsiEntry.delete(0,END)
    SpriteEntry.delete(0,END)
    SodaEntry.delete(0,END)
    FrutiEntry.delete(0,END)
    ATFTaxEntry.delete(0,END)
    StarterTaxEntry.delete(0,END)
    drinksTaxEntry.delete(0,END)
    ATFPriceEntry.delete(0,END)
    StarterPriceEntry.delete(0,END)
    DrinksPriceEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    textarea.delete(1.0,END)

def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')

#create folder if not present
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        billcontent=textarea.get(1.0, END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(billcontent)
        file.close()
        messagebox.showinfo('success',f'Bill number {billnumber} is saved successfully')
        billnumber = random.randint(100, 1000)

billnumber=random.randint(100, 1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','All Customer Details Are Required !!!')
    elif ATFPriceEntry.get() == '' and StarterPriceEntry.get() == '' and DrinksPriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products are selected')
    elif ATFPriceEntry.get() == '0 Rs' and StarterPriceEntry.get() == '0 Rs' and DrinksPriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t      --- Cafe Bill ---\n')
        textarea.insert(END, f'\n Bill No.: {billnumber}\n')
        textarea.insert(END, f'\n Customer Name: {nameEntry.get()}')
        textarea.insert(END, f'\n Customer Phone Number: +91-{phoneEntry.get()}')
        textarea.insert(END, '\n=========================================================')
        textarea.insert(END, ' Product \t\t\t QTY \t\t\tPrice')
        textarea.insert(END, '\n=========================================================')
        if FrenchFriesEntry.get()!='0':
            textarea.insert(END, f'\n French Fries\t\t\t  {FrenchFriesEntry.get()}\t\t\t  {FrenchFriesPrice}')
        if SandwichEntry.get()!='0':
            textarea.insert(END, f'\n Sandwich\t\t\t  {SandwichEntry.get()}\t\t\t  {SandwichPrice}')
        if BurgerEntry.get()!='0':
            textarea.insert(END, f'\n Burger\t\t\t  {BurgerEntry.get()}\t\t\t  {BurgerPrice}')
        if PizzaEntry.get()!= '0':
            textarea.insert(END, f'\n Pizza\t\t\t  {PizzaEntry.get()}\t\t\t  {PizzaPrice}')
        if DessertEntry.get()!= '0':
            textarea.insert(END, f'\n Dessert\t\t\t  {DessertEntry.get()}\t\t\t  {DessertPrice}')
        if PastaEntry.get()!= '0':
            textarea.insert(END, f'\n Pasta\t\t\t  {PastaEntry.get()}\t\t\t  {PastaPrice}')

        if ChickenTikkaEntry.get()!= '0':
            textarea.insert(END, f'\n Chicken Tikka\t\t\t  {ChickenTikkaEntry.get()}\t\t\t  {ChickenTikkaPrice}')
        if ChickenAngaraEntry.get()!= '0':
            textarea.insert(END, f'\n Chicken Angara\t\t\t  {ChickenAngaraEntry.get()}\t\t\t  {ChickenAngaraPrice}')
        if PaneerTikkaEntry.get()!= '0':
            textarea.insert(END, f'\n Paneer Tikka\t\t\t  {PaneerTikkaEntry.get()}\t\t\t  {PaneerTikkaPrice}')
        if NoodlesEntry.get()!= '0':
            textarea.insert(END, f'\n Noodles\t\t\t  {NoodlesEntry.get()}\t\t\t  {NoodlesPrice}')
        if ManchurianEntry.get()!= '0':
            textarea.insert(END, f'\n Manchurian\t\t\t  {ManchurianEntry.get()}\t\t\t  {ManchurianPrice}')
        if AlooTikkiEntry.get()!= '0':
            textarea.insert(END, f'\n Aloo Tikki\t\t\t  {AlooTikkiEntry.get()}\t\t\t  {AlooTikkiPrice}')

        if CocktailEntry.get()!= '0':
            textarea.insert(END, f'\n Cocktail\t\t\t  {CocktailEntry.get()}\t\t\t  {CocktailPrice}')
        if MojitoEntry.get()!= '0':
            textarea.insert(END, f'\n Mojito\t\t\t  {MojitoEntry.get()}\t\t\t  {MojitoPrice}')
        if PepsiEntry.get()!= '0':
            textarea.insert(END, f'\n Pepsi\t\t\t  {PepsiEntry.get()}\t\t\t  {PepsiPrice}')
        if SpriteEntry.get()!= '0':
            textarea.insert(END, f'\n Sprite\t\t\t  {SpriteEntry.get()}\t\t\t  {SpritePrice}')
        if SodaEntry.get()!= '0':
            textarea.insert(END, f'\n Soda\t\t\t  {SodaEntry.get()}\t\t\t  {SodaPrice}')
        if FrutiEntry.get()!= '0':
            textarea.insert(END, f'\n Fruti\t\t\t  {FrutiEntry.get()}\t\t\t  {FrutiPrice}')
        textarea.insert(END, '\n---------------------------------------------------------')

        if ATFTaxEntry.get()!='0.0 Rs':
            textarea.insert(END, f'\n ATF Tax\t\t\t\t{ATFTaxEntry.get()}')
        if StarterTaxEntry.get()!='0.0 Rs':
            textarea.insert(END, f'\n Starter Tax\t\t\t\t{StarterTaxEntry.get()}')
        if drinksTaxEntry.get()!='0.0 Rs':
            textarea.insert(END, f'\n Drinks Tax\t\t\t\t{drinksTaxEntry.get()}')

        textarea.insert(END, f'\n\n Total Bill \t\t\t\t {totalbill}')
        textarea.insert(END, '\n---------------------------------------------------------')
        save_bill()

def send_email():
    #inside button of email button
    #pass: jzesztoeiklfgffk
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message=email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Successs','Bill emailed successfully', parent=root1) #parent=root1: to show message on same window
        except:
            messagebox.showerror('Error','Something went wrong!!! olease try later', parent= root1)
    if textarea.get(1.0, END)== '\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('sent gmail')
        root1.config(bg='cyan2')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1, text='SENDER', font=('arial',16,'bold'), bd=6, bg='cyan2', fg='black')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel=Label(senderFrame, text="Sender's Email", font=('arial',14,'bold'), bg='cyan2', fg='black')
        senderLabel.grid(row=0,column=0, padx=10, pady=8)

        senderEntry=Entry(senderFrame, font=('arial',14,'bold'), bd=2, width=23, relief = RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='cyan2', fg='black')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='cyan2', fg='black')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='cyan2', fg='black')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='cyan2', fg='black')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1, text='SEND', font=('arial', 16, 'bold'), width= 15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

    root1.mainloop()





def total():
    global FrenchFriesPrice
    global SandwichPrice
    global BurgerPrice
    global PizzaPrice
    global DessertPrice
    global PastaPrice

    global ChickenTikkaPrice
    global ChickenAngaraPrice
    global PaneerTikkaPrice
    global NoodlesPrice
    global ManchurianPrice
    global AlooTikkiPrice

    global CocktailPrice
    global MojitoPrice
    global PepsiPrice
    global SpritePrice
    global SodaPrice
    global FrutiPrice

    global totalbill

    # ATF Price Calculation
    FrenchFriesPrice = int(FrenchFriesEntry.get())*40
    SandwichPrice = int(SandwichEntry.get())*60
    BurgerPrice = int(BurgerEntry.get())*69
    PizzaPrice = int(PizzaEntry.get())*90
    DessertPrice = int(DessertEntry.get())*80
    PastaPrice = int(PastaEntry.get())*60

    TotalATFPrice = FrenchFriesPrice+SandwichPrice+BurgerPrice+PizzaPrice+DessertPrice+PastaPrice
    ATFPriceEntry.delete(0, END) # to update the value after changing the quantity
    ATFPriceEntry.insert(0, f'{TotalATFPrice} Rs')
    # TAX
    ATFTax = TotalATFPrice*0.12
    ATFTaxEntry.delete(0, END)
    ATFTaxEntry.insert(0, str(ATFTax) +' Rs')

    # Starter Price Calculation
    ChickenTikkaPrice = int(ChickenTikkaEntry.get())*120
    ChickenAngaraPrice = int(ChickenAngaraEntry.get())*140
    PaneerTikkaPrice = int(PaneerTikkaEntry.get())*100
    NoodlesPrice = int(NoodlesEntry.get())*70
    ManchurianPrice = int(ManchurianEntry.get())*80
    AlooTikkiPrice = int(AlooTikkiEntry.get())*70

    TotalStarterPrice = ChickenTikkaPrice+ChickenAngaraPrice+PaneerTikkaPrice+NoodlesPrice+ManchurianPrice+AlooTikkiPrice
    StarterPriceEntry.delete(0, END)
    StarterPriceEntry.insert(0, str(TotalStarterPrice) + ' Rs')
    StarterTax = TotalStarterPrice * 0.08
    StarterTaxEntry.delete(0, END)
    StarterTaxEntry.insert(0, str(StarterTax) + ' Rs')

    # Drinks Price Calculation
    CocktailPrice = int(CocktailEntry.get())*60
    MojitoPrice = int(MojitoEntry.get())*50
    PepsiPrice = int(PepsiEntry.get())*40
    SpritePrice = int(SpriteEntry.get())*40
    SodaPrice = int(SodaEntry.get())*30
    FrutiPrice = int(FrutiEntry.get())*50

    TotalDrinkPrice = CocktailPrice+MojitoPrice+PepsiPrice+SpritePrice+SodaPrice+FrutiPrice
    DrinksPriceEntry.delete(0, END)
    DrinksPriceEntry.insert(0, str(TotalDrinkPrice)+ ' Rs')
    DrinkTax = TotalDrinkPrice * 0.05
    drinksTaxEntry.delete(0, END)
    drinksTaxEntry.insert(0, str(DrinkTax) + ' Rs')

    #Total Bill
    totalbill=TotalATFPrice+TotalStarterPrice+TotalDrinkPrice+ATFTax+StarterTax+DrinkTax




#def save_bill():
#    global billnumbers
#    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
#    if result:
#        bill_content = textarea.get(1.0, END)
#        file = open(f'bills/ {billnumbers}.txt', 'w')
#        file.write(bill_content)
#        file.close()
#        billnumbers = random.randint(100, 1000)
#        messagebox.showinfo('Success', f'Bill No.{billnumbers} is saved successfully')


#billnumbers = random.randint(100, 1000)



# GUI ---->
root = Tk()

# Naming the tkinter Window frame ---->
root.title('CMF : Cafe Billing System - By SahilSL')

# size of window ---->
root.geometry('1340x680')

# window icon ---->
#root.iconbitmap('icon.ico')

# Title ---->
headingLabel=Label(root, text='Cafe Billing System', font=('times new roman', 30, 'bold')
                   , bg='cyan2', bd=10, relief=GROOVE)
# can also change font color as fg = 'gold'
# Different relief (border styles are GROOVE, FLAT, RIDGE, RAISED, SOLID)
headingLabel.pack(fill=X)
# fill=X is used to color whole area of heading including wide spaces


# Label Frame ---->
customer_detail_frame = LabelFrame(root, text=' Customer Details ', font=('times new roman', 15, 'bold')
                                   ,fg='midnight blue', bd=8, relief=GROOVE, bg='cyan2')
customer_detail_frame.pack(fill=X)

# Name Label ---->
# here we pass customer_detail_frame because it is under it
nameLabel = Label(customer_detail_frame, text='Name', font=('times new roman', 15, 'bold'), bg='cyan2', fg='red2')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry=Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)


# Phone Label ---->
phoneLabel = Label(customer_detail_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='cyan2', fg='red2')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)


# Bill Label ---->
billnumberLabel = Label(customer_detail_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='cyan2', fg='red2')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)


# Button ---->
searchButton = Button(customer_detail_frame, text='SEARCH', font=('arial', 12, 'bold'),bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

#=====================================================================================================================#

productsFrame = Frame(root)
productsFrame.pack()

# Class ATF
ATFFrame = LabelFrame(productsFrame, text=' ATF ', font=('times new roman', 15, 'bold'), fg='midnight blue', bd=8, relief=GROOVE, bg='cyan2')
ATFFrame.grid(row=0, column=0)

# Subclasses of ATF
FrenchFriesLabel = Label(ATFFrame, text='French Fries', font=('times new roman', 15, 'bold'), bg='cyan2', fg='red2')
FrenchFriesLabel.grid(row=0,column=0, pady=9, padx=10, sticky='w')
# sticky='w' means label starts from west side

FrenchFriesEntry = Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
FrenchFriesEntry.grid(row=0, column=1, pady=9, padx=10)
FrenchFriesEntry.insert(0, 0)  # this initially ahow zero in entry box

SandwichLabel=Label(ATFFrame, text='Sandwich', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
SandwichLabel.grid(row=1,column=0, pady=9, padx=10, sticky='w')

SandwichEntry=Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
SandwichEntry.grid(row=1, column=1, pady=9, padx=10)
SandwichEntry.insert(0, 0)

BurgerLabel=Label(ATFFrame, text='Burger', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
BurgerLabel.grid(row=2,column=0, pady=9, padx=10, sticky='w')

BurgerEntry=Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
BurgerEntry.grid(row=2, column=1, pady=9, padx=10)
BurgerEntry.insert(0, 0)

PizzaLabel=Label(ATFFrame, text='Pizza', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
PizzaLabel.grid(row=3,column=0, pady=9, padx=10, sticky='w')

PizzaEntry=Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
PizzaEntry.grid(row=3, column=1, pady=9, padx=10)
PizzaEntry.insert(0, 0)

DessertLabel=Label(ATFFrame, text='Dessert', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
DessertLabel.grid(row=4,column=0, pady=9, padx=10, sticky='w')

DessertEntry=Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
DessertEntry.grid(row=4, column=1, pady=9, padx=10)
DessertEntry.insert(0, 0)

PastaLabel=Label(ATFFrame, text='Pasta', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
PastaLabel.grid(row=5,column=0, pady=9, padx=10, sticky='w')

PastaEntry=Entry(ATFFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
PastaEntry.grid(row=5, column=1, pady=9, padx=10)
PastaEntry.insert(0, 0)


# Class Starter
StarterFrame=LabelFrame(productsFrame, text=' Starter ', font=('times new roman', 15, 'bold'),fg='midnight blue', bd=8, relief=GROOVE, bg='cyan2')
StarterFrame.grid(row=0, column=1)

ChickenTikkaLabel=Label(StarterFrame, text='Chicken Tikka', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
ChickenTikkaLabel.grid(row=0,column=0, pady=9, padx=10, sticky='w')

ChickenTikkaEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
ChickenTikkaEntry.grid(row=0, column=1, pady=9, padx=10)
ChickenTikkaEntry.insert(0, 0)

ChickenAngaraLabel=Label(StarterFrame, text='Chicken Angara', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
ChickenAngaraLabel.grid(row=1,column=0, pady=9, padx=10, sticky='w')

ChickenAngaraEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
ChickenAngaraEntry.grid(row=1, column=1, pady=9, padx=10)
ChickenAngaraEntry.insert(0, 0)

PaneerTikkaLabel=Label(StarterFrame, text='Paneer Tikka', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
PaneerTikkaLabel.grid(row=2,column=0, pady=9, padx=10, sticky='w')

PaneerTikkaEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
PaneerTikkaEntry.grid(row=2, column=1, pady=9, padx=10)
PaneerTikkaEntry.insert(0, 0)

NoodlesLabel=Label(StarterFrame, text='Noodles', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
NoodlesLabel.grid(row=3,column=0, pady=9, padx=10, sticky='w')

NoodlesEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
NoodlesEntry.grid(row=3, column=1, pady=9, padx=10)
NoodlesEntry.insert(0, 0)

ManchurianLabel=Label(StarterFrame, text='Manchurian', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
ManchurianLabel.grid(row=4,column=0, pady=9, padx=10, sticky='w')

ManchurianEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
ManchurianEntry.grid(row=4, column=1, pady=9, padx=10)
ManchurianEntry.insert(0, 0)

AlooTikkiLabel=Label(StarterFrame, text='Aloo Tikki', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
AlooTikkiLabel.grid(row=5,column=0, pady=9, padx=10, sticky='w')

AlooTikkiEntry=Entry(StarterFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
AlooTikkiEntry.grid(row=5, column=1, pady=9, padx=10)
AlooTikkiEntry.insert(0, 0)

# Drinks Starter
DrinksFrame=LabelFrame(productsFrame, text='Drinks', font=('times new roman', 15, 'bold'),fg='midnight blue', bd=8, relief=GROOVE, bg='cyan2')
DrinksFrame.grid(row=0, column=2)

CocktailLabel=Label(DrinksFrame, text='Cocktail', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
CocktailLabel.grid(row=0,column=0, pady=9, padx=10, sticky='w')

CocktailEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
CocktailEntry.grid(row=0, column=1, pady=9, padx=10)
CocktailEntry.insert(0, 0)

MojitoLabel=Label(DrinksFrame, text='Mojito', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
MojitoLabel.grid(row=1,column=0, pady=9, padx=10, sticky='w')

MojitoEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
MojitoEntry.grid(row=1, column=1, pady=9, padx=10)
MojitoEntry.insert(0, 0)

PepsiLabel=Label(DrinksFrame, text='Pepsi', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
PepsiLabel.grid(row=2,column=0, pady=9, padx=10, sticky='w')

PepsiEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
PepsiEntry.grid(row=2, column=1, pady=9, padx=10)
PepsiEntry.insert(0, 0)

SpriteLabel=Label(DrinksFrame, text='Sprite', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
SpriteLabel.grid(row=3,column=0, pady=9, padx=10, sticky='w')

SpriteEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
SpriteEntry.grid(row=3, column=1, pady=9, padx=10)
SpriteEntry.insert(0, 0)

SodaLabel=Label(DrinksFrame, text='Soda', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
SodaLabel.grid(row=4,column=0, pady=9, padx=10, sticky='w')

SodaEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
SodaEntry.grid(row=4, column=1, pady=9, padx=10)
SodaEntry.insert(0, 0)

FrutiLabel=Label(DrinksFrame, text='Fruti', font=('times new roman',15,'bold'), bg='cyan2', fg='red2')
FrutiLabel.grid(row=5,column=0, pady=9, padx=10, sticky='w')

FrutiEntry=Entry(DrinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
FrutiEntry.grid(row=5, column=1, pady=9, padx=10)
FrutiEntry.insert(0, 0)

#=======================================================================================================================

# Billing

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0,column=3, padx=10)

billareaLabel = Label(billframe, text='Bill',font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

Scrollbar = Scrollbar(billframe, orient=VERTICAL)
Scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=57, yscrollcommand=Scrollbar.set)
textarea.pack()

Scrollbar.config(command = textarea.yview)

#=======================================================================================================================

# Bill Menu
billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'),fg='midnight blue', bd=8, relief=GROOVE, bg='cyan2')
billmenuFrame.pack()

ATFPriceLabel = Label(billmenuFrame, text='ATF Price', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
ATFPriceLabel.grid(row=0,column=0, pady=6, padx=10, sticky='w')

ATFPriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
ATFPriceEntry.grid(row=0, column=1, pady=6, padx=10)

StarterPriceLabel = Label(billmenuFrame, text='Starter Price', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
StarterPriceLabel.grid(row=1,column=0, pady=6, padx=10, sticky='w')

StarterPriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
StarterPriceEntry.grid(row=1, column=1, pady=6, padx=10)

DrinksPriceLabel = Label(billmenuFrame, text='Drinks Price', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
DrinksPriceLabel.grid(row=2,column=0, pady=6, padx=10, sticky='w')

DrinksPriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
DrinksPriceEntry.grid(row=2, column=1, pady=6, padx=10)




ATFTaxLabel = Label(billmenuFrame, text='ATF Tax', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
ATFTaxLabel.grid(row=0,column=2, pady=6, padx=10, sticky='w')

ATFTaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
ATFTaxEntry.grid(row=0, column=3, pady=6, padx=10)

StarterTaxLabel = Label(billmenuFrame, text='Starter Tax', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
StarterTaxLabel.grid(row=1,column=2, pady=6, padx=10, sticky='w')

StarterTaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
StarterTaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinksTaxLabel = Label(billmenuFrame, text='Drinks Tax', font=('times new roman',14,'bold'), bg='cyan2', fg='red2')
drinksTaxLabel.grid(row=2,column=2, pady=6, padx=10, sticky='w')

drinksTaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
drinksTaxEntry.grid(row=2, column=3, pady=6, padx=10)


buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)


totalButton = Button(buttonFrame, text='TOTAL', font=('arial', 16, 'bold'), bg='red1', fg='white', bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=9)

billButton = Button(buttonFrame, text='GENERATE BILL', font=('arial', 16, 'bold'), bg='red1', fg='white', bd=5, width=15, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=8)

emailButton = Button(buttonFrame, text='EMAIL', font=('arial', 16, 'bold'), bg='red1', fg='white', bd=5, width=8, pady=10, command = send_email)
emailButton.grid(row=0, column=2, pady=20, padx=8)

printButton = Button(buttonFrame, text='PRINT', font=('arial', 16, 'bold'), bg='red1', fg='white', bd=5, width=8, pady=10, command = print_bill)
printButton.grid(row=0, column=3, pady=20, padx=8)

clearButton = Button(buttonFrame, text='CLEAR', font=('arial', 16, 'bold'), bg='red1', fg='white', bd=5, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=9)



root.mainloop()

