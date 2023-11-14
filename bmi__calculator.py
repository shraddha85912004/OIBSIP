from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('BMI Calculator')
root.geometry('400x300')
root.config(bg='pink')

def reset_entry():
    height.delete(0,'end')
    weight.delete(0,'end')
    age.delete(0,'end')

def calculate_bmi():
    kg = int(weight.get())
    m = int(height.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmiIndex(bmi)

def bmiIndex(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('BMI Calculator', 'something went wrong!')   


var = IntVar()

frame1 = Frame(root,bg="lightblue",padx=15, pady=15)
frame1.pack(expand=True)

age_label = Label(frame1,text="Enter Age (2 - 100)")
age_label.grid(row=1, column=1)

age = Entry(frame1, )
age.grid(row=1, column=2, pady=5)

gender_label = Label(frame1,text='Select Gender')
gender_label.grid(row=2, column=1)

frame2 = Frame(frame1)
frame2.grid(row=2, column=2, pady=5)

male_radioBTN = Radiobutton(frame2,text = 'Male',variable = var,value = 1)
male_radioBTN.pack(side=LEFT)

female_radioBTN = Radiobutton(frame2,text = 'Female',variable = var,value = 2)
female_radioBTN.pack(side=RIGHT)

height_label = Label(frame1,text="Enter Height (cm)  ")
height_label.grid(row=3, column=1)

weight_label = Label(frame1,text="Enter Weight (kg)  ",)
weight_label.grid(row=4, column=1)

height = Entry(frame1,)
height.grid(row=3, column=2, pady=5)

weight = Entry(frame1,)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame(frame1)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3,text='Calculate',command=calculate_bmi)
cal_btn.pack(side=LEFT)

reset_btn = Button(frame3,text='Reset',command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn = Button(frame3,text='Exit',command=lambda:root.destroy())
exit_btn.pack(side=RIGHT)

root.mainloop()
