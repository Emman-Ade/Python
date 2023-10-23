"""
File: learnPython.py
Name: Emmanuel Adeniyi
Purpose: Show understanding of loops, user input, and operations
Date:October 15, 2023
Last Modified: October 15, 2023
"""

def main():
    sum_values = 0  # Initialize variables
    min_value = float('inf')  # Initialize min to positive infinity
    max_value = float('-inf')  # Initialize max to negative infinity

    #User input for how much grades to be entered
    num_values = int(input("Enter number of values: "))
    values = [0] * num_values

    #asking user to input the grade
    for i in range(num_values):  # Loop to input values
        value = int(input(f"Enter value ({i + 1} of {num_values}): "))
        values[i] = value
        sum_values += value  # Sum of all values

    #printing out each grade
    for i, value in enumerate(values):
        print(f"Index {i}: {value}")

    #Finding the max and min
    for i in range(num_values):
        if values[i] > max_value:
            max_value = values[i]  # Max of all values
            print(f"\nMaximum: {max_value} at index {i}")
        elif values[i] < min_value:
            min_value = values[i]  # Min of all values
            print(f"Minimum: {min_value} at index {i}")

    #Priting out the average, values over average, and values under average
    average = sum_values / num_values
    over_average = sum(1 for value in values if value > average)
    under_average = sum(1 for value in values if value < average)

    print(f"Average: {average:.4f}")
    print(f"Values over average: {over_average}")
    print(f"Values under average: {under_average}")

if __name__ == "__main__":
    main()