# Program 4
# Create a program that will find and print the biggest number using only if-else statement
# Display the biggest number
# Display the output 

import tkinter as tk
from tkinter import messagebox

def start_clicked():
    app.destroy()
    def find_largest_number():
        # Get user input
        input_1 = entry1.get()
        input_2 = entry2.get()
        input_3 = entry3.get()

        # Check if all fields are non-empty
        if input_1 and input_2 and input_3:
            try:
                # Convert inputs to float
                input_1 = float(input_1)
                input_2 = float(input_2)
                input_3 = float(input_3)

                # Use if-else statements to find the largest number
                if input_1 >= input_2 and input_1 >= input_3:
                    result = f"The largest number is: {input_1}"
                elif input_2 >= input_1 and input_2 >= input_3:
                    result = f"The largest number is: {input_2}"
                else:
                    result = f"The largest number is: {input_3}"

                # Display the result using a messagebox
                messagebox.showinfo("Result", result)

            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers.")
        else:
            messagebox.showwarning("Warning", "Please enter values in all fields.")

    def reset_inputs():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)

    # Create the main window
    window = tk.Tk()
    window.title("Find Largest Number")

    # Create entry widgets for user input
    entry_frame = tk.Frame(window, pady=10)
    entry_frame.pack()

    label1 = tk.Label(entry_frame, text="Enter number 1:", font=("Cooper Black", 10), bg="#F8EFE4", fg="#FF005C")
    label1.grid(row=0, column=0, padx=5)
    entry1 = tk.Entry(entry_frame)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(entry_frame, text="Enter number 2:", font=("Cooper Black", 10), bg="#F8EFE4", fg="#FF005C")
    label2.grid(row=1, column=0, padx=5)
    entry2 = tk.Entry(entry_frame)
    entry2.grid(row=1, column=1)

    label3 = tk.Label(entry_frame, text="Enter number 3:", font=("Cooper Black", 10), bg="#F8EFE4", fg="#FF005C")
    label3.grid(row=2, column=0, padx=5)
    entry3 = tk.Entry(entry_frame)
    entry3.grid(row=2, column=1)

    # Create buttons
    calculate_button = tk.Button(window, text="Find Largest Number", command=find_largest_number, pady=10, font=("Cooper Black", 10), bg="#F8EFE4", fg="#3E630F")
    calculate_button.pack()


    # Start the Tkinter event loop
    window.mainloop()

# Create the main window
app = tk.Tk()
app.title("Start Button Example")

# Create a start button
start_button = tk.Button(
    app,
    command=start_clicked,
    text="Start!",
    font=("Cooper Black", 14),
    bg="#F8EFE4",
    fg="#ff9636",
)
start_button.pack(pady=100)


# Start the Tkinter event loop for the main window
app.mainloop()
