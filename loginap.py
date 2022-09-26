from tkinter import *
root = Tk()
root.geometry("500x300")

Label(root, text="My Registration Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood= Label(root, text="Payment Mood")

# Packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

# Variable for installing date
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = IntVar
checkvalue = IntVar

name_entry = Entry(root, textvariable =namevalue)
phone_entry = Entry(root, textvariable=phonevalue)
gender_entry = Entry(root, textvariable=gendervalue)
emergency_entry = Entry(root, textvariable =emergencyvalue)
paymentmood_entry = Entry(root, textvariable =paymentmoodvalue)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
paymentmood_entry.grid(row=5, column=3)

# Creating Checkbox

checkbtn = Checkbutton(text="Add Member", variable = checkvalue)
checkbtn.grid(row=6, column=3)

root.mainloop()
