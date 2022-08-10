import tkinter as tk
from tkinter import filedialog

root =tk.Tk()
root.title("PyNote")

# Create text box for window
text = tk.Text(root)
text.grid()

# Save function
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()

# Create save button
button = tk.Button(root, text="Save", command=saveas)
button.grid()

# Start program
root.mainloop()