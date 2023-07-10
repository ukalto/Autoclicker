import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Python AutoClicker")


# Create the text fields with labels
text1_label = tk.Label(root, text="Text 1:")
text1_label.grid(row=0, column=0)

text1 = tk.Entry(root)
text1.grid(row=0, column=1)

text2_label = tk.Label(root, text="Text 2:")
text2_label.grid(row=1, column=0)

text2 = tk.Entry(root)
text2.grid(row=1, column=1)

text3_label = tk.Label(root, text="Text 3:")
text3_label.grid(row=2, column=0)

text3 = tk.Entry(root)
text3.grid(row=2, column=1)

text4_label = tk.Label(root, text="Text 4:")
text4_label.grid(row=3, column=0)

text4 = tk.Entry(root)
text4.grid(row=3, column=1)

text5_label = tk.Label(root, text="Text 5:")
text5_label.grid(row=4, column=0)

text5 = tk.Entry(root)
text5.grid(row=4, column=1)

# Create the radio buttons
radio_label = tk.Label(root, text="Choose an option:")
radio_label.grid(row=5, column=0)

radio_var = tk.StringVar()
radio_var.set("Option 1")

radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio1.grid(row=5, column=1)

radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio2.grid(row=5, column=2)

# Create the integer field with label
int_label = tk.Label(root, text="Enter an integer:")
int_label.grid(row=6, column=0)

int_var = tk.IntVar()

int_field = tk.Entry(root, textvariable=int_var)
int_field.grid(row=6, column=1)

# Create the buttons
button1 = tk.Button(root, text="Button 1")
button1.grid(row=7, column=0)

button2 = tk.Button(root, text="Button 2")
button2.grid(row=7, column=1)

button3 = tk.Button(root, text="Button 3")
button3.grid(row=7, column=2)

# Start the main event loop
root.mainloop()
