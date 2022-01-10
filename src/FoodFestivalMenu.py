from tkinter import *
from data import foods


root = Tk()
root.title("Mel's Food Festival")
root.geometry("800x500")
Label(root, text="Mel's Food Festival").grid(column=2, row=1, pady=50)

appetizerMenu = LabelFrame(root, padx=50, pady=50).grid(row=2, column=1)
mainMenu = LabelFrame(root, padx=50, pady=50).grid(row=2, column=1)
dessertMenu = LabelFrame(root, padx=50, pady=50).grid(row=2, column=1)

# Centering Frames
root.columnconfigure(0, weight=1)
root.columnconfigure(4, weight=1)

root.rowconfigure(7, weight=1)


Label(appetizerMenu, text="Appetizers").grid(column=1, row= 2)
for index, food_data in enumerate(foods.appe):
  Checkbutton(appetizerMenu, text=f"{food_data[0]}, ${food_data[1]}.00").grid(column=1, row=(index + 2) + 1, pady=5, padx=15)

Label(root, text="Main Course").grid(column=2, row= 2)
for index, food_data in enumerate(foods.main):
  Checkbutton(root, text=f"{food_data[0]}, ${food_data[1]}.00").grid(column=2, row=(index + 2) + 1, pady=5, padx=15)

Label(root, text="Desserts").grid(column=3, row= 2)
for index, food_data in enumerate(foods.dess):
  Checkbutton(root, text=f"{food_data[0]}, ${food_data[1]}.00").grid(column=3, row=(index + 2) + 1, pady=5, padx=15)

Button(root, text="Place Your Order").grid(column=2, row=6, pady=30)
root.mainloop()