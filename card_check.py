import tkinter as tk

ls = []
odd_num = []

#Main Rectangle
root = tk.Tk()
root.geometry("300x300")
root.title("Credit Card Validator")

# Input Field
inp = tk.Entry(root, width=45, borderwidth=7)
inp.grid(row=0, columnspan=5, padx=10, pady= 10)


#Algoritm behind check button
def check():

    #Create list, Substract last number, reverse list
    ls = [int(_) for _ in inp.get()]
    last_digit = ls.pop()

    if ls[0] == 4 and len(ls) == 15:
        check_advisor["text"] = "VISA"
    elif ls[0] == 5:
        check_advisor["text"] = "MASTERCARD"
    elif check_valid["text"] == "INVALID":
        check_advisor["text"] = "NONE"

    ls.reverse()
    

    ls = [i*2 if j % 2 == 0 else i for j, i in enumerate(ls)]

    ls = [i-9 if i>9 else i for i in ls]

    list_sum = sum(ls)

    last_val = 10 - list_sum % 10

    if last_val == last_digit and len(ls) == 15:
        check_valid["text"] = "VALID"
        check_valid.configure(foreground="green")
    else:
        check_valid["text"] = "INVALID"
        check_valid.configure(foreground="red")

    print(ls)
    print(f"Length of list - {len(ls)}")
    print(list_sum)



#Clear Button fc
def clear():
    inp.delete(0, tk.END)
    ls.clear()
    odd_num.clear()
    check_valid["text"] = "-"
    check_valid.configure(foreground="black")
    check_advisor["text"] = "-"
    check_advisor.configure(fg="black")

#Check Button
check_btn = tk.Button(text="CHECK", font='Consolas', command=lambda: check())

#Clear Button
clear_btn = tk.Button(text='CLEAR', font='Consolas', command=lambda: clear())


#Check if the card is valid or not
check_valid_text = tk.Label(text="Card Status:", font='Consolas')
check_valid = tk.Label(text="-", font='Consolas')



#Check the card advisor
card_adv_text = tk.Label(text="Card Advisor: ", font='Consolas')
check_advisor = tk.Label(text="-", font='Consolas')


#Button grids
check_btn.grid(row=2, column=0,ipadx=20,ipady=15, columnspan=3)
clear_btn.grid(row=2, column=2,ipadx=20,ipady=15, columnspan=3)

# Static Text Grids
check_valid_text.place(x=20, y=150)
card_adv_text.place(x=20, y=200)


#Dynamic grids
check_valid.place(x=200, y=150)
check_advisor.place(x=200, y=200)



if __name__ == "__main__":
    root.mainloop()
