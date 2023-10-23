"""
File: consoles.py
Name: Emmanuel Adeniyi
Purpose: Show understanding of objects,classes, and inheritance
Date:October 22, 2023
Last Modified: October 23, 2023
"""
class console():
    # our super class containing our values shared between subclasses
    def __init__(self,company,name,release_date,sales):
        self.company = company
        self.name = name
        self.release_date = release_date

        #error handling if sales is inserted as a negative number
        if sales < 0:
            raise ValueError("Sales must be a positive number")
        self.sales = sales

        #returning a string that prints out this statement for all subclasses
    def __str__(self):
     return f"This is {self.company}'s {self.name} it released on {self.release_date} and sold {self.sales} million units"

#subclasses with all their unique information
class NintendoSwitch(console):
        def __init__(self):
            super().__init__("Nintendo","Nintendo Switch","March 3, 2017",129.5)

class Xbox360(console):
        def __init__(self):
            super().__init__("Microsoft","Xbox 360","November 22, 2005",85.73)

class NintendoWii(console):
        def __init__(self):
            super().__init__("Nintendo","Wii","November 18, 2006",101.6)

def main():
    #main method, creating an array to store all of our information and printing it out
    console = [NintendoSwitch(),Xbox360(),NintendoWii()]

    for c in console:
        print(c)

if __name__ == "__main__":
    main()