import tkinter as tk
from tkinter import filedialog

class Application():
    def __init__(self):
        # Create text box for window
        self.text = tk.Text(root)
        self.text.grid()
        # Create save button
        self.button = tk.Button(root, text="Save", command=self.saveas)
        self.button.grid()
    
    # Save function
    def saveas(self):
        t = self.text.get("1.0", "end-1c")
        save_location = filedialog.asksaveasfilename()
        file1 = open(save_location, "w+")
        file1.write(t)
        file1.close()

# Start program
root =tk.Tk()
root.title("PyNote")
app = Application()
root.mainloop()