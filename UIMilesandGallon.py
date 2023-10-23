import tkinter as tk
"""
File: UIMilesandGallon.py
Name: Emmanuel Adeniyi
Purpose: Show use of Python GUI and how to make applications for users
Date:October 21, 2023
Last Modified: October 22, 2023
"""
class UIMilesandGallon:

    def __init__(self, root):
        self.root = root
        #setting or title
        root.title("MPG Calc")

        # Creating labels for miles and gallons
        miles_label = tk.Label(root, text="Miles:")
        gallons_label = tk.Label(root, text="Gallons:")
        #results label that will change depending on calculate_mpg method
        self.results_label = tk.Label(root, text="")

        # Create entry widgets
        self.miles_entry = tk.Entry(root)
        self.gallons_entry = tk.Entry(root)

        # Create a button that you press so you can calculate it
        calculate_button = tk.Button(root, text="Calculate", command=self.calculate_mpg)

        # Pack widgets using grid layout
        miles_label.grid(row=0, column=0)
        self.miles_entry.grid(row=0, column=1)
        gallons_label.grid(row=1, column=0)
        self.gallons_entry.grid(row=1, column=1)
        calculate_button.grid(row=2, column=0, columnspan=2)
        self.results_label.grid(row=3, column=0, columnspan=2)

    def calculate_mpg(self): #method that determines the calculatation
        #error handling
        try:
            mile = float(self.miles_entry.get())
            gallon = float(self.gallons_entry.get())

            if mile >= 0 and gallon >= 0:
                mpg = mile / gallon
                self.results_label.config(text=f"Miles Per Gallons: {mpg:.2f}")
            else:
                self.results_label.config(text="Miles and gallons cannot be negative")
        except ValueError:
            self.results_label.config(text="Invalid input. Please enter numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UIMilesandGallon(root)
    root.mainloop()