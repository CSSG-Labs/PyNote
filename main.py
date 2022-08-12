import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("PyNote")

        # Create menu bar
        self.menuBar = tk.Menu(self.master)
        fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.master.config(menu=self.menuBar)
        fileMenu.add_command(label="New", command=None)
        fileMenu.add_command(label="Open", command=None)
        fileMenu.add_command(label="Save", command=None)
        fileMenu.add_command(label="Save as...", command=self.saveas)
        self.menuBar.add_cascade(label="File", menu=fileMenu)

        # Create text box for window
        self.text = tk.Text(self)
        self.text.pack(side="top")

        self.pack()

    # Save function
    def saveas(self):
        t = self.text.get("1.0", "end-1c")
        saveLocation = filedialog.asksaveasfilename()
        if(saveLocation != ''):
            file1 = open(saveLocation, "w+")
            file1.write(t)
            file1.close()

# Start program
root = tk.Tk()
app = Application(root)
app.mainloop()
