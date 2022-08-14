import tkinter as tk

"""
creates custom prompt displaying some text and below it a row of option buttons
"""
class CustomPrompt(tk.Toplevel):
    def __init__(self, parent, title, text, text_options, functions_options, close_on_click=True):
        #initialization and argument check and also fixing its size
        tk.Toplevel.__init__(self, parent)
        if(isinstance(text_options, list) and isinstance(functions_options, list)):
            if(len(text_options) != len(functions_options)):
                raise Exception("text_options and functions_option should have the same length")
        else:
            raise Exception("text_options and functions_options should both be lists")
        self.resizable(False, False)

        self.close_on_click = close_on_click
        self.functions_options = functions_options

        self.title(title)

        #body of the window
        self.label = tk.Label(self, text=text)
        self.bottom_frame = tk.Frame(self)
        i = 0
        while(i<len(text_options)):
            button = tk.Button(self.bottom_frame, text=text_options[i], command=lambda j=i: self.function_handler(j))
            button.pack(pady=(0, 15), padx=15, side="left")
            i = i+1
        self.label.pack(pady=15, side="top")
        self.bottom_frame.pack(side="bottom")

        self.mainloop()
    
    #as the pop prompt may be closable this handler exists to do so
    def function_handler(self, i):
        if(self.close_on_click):
            self.functions_options[i]()
            self.destroy()
        else:
            self.functions_options[i]()

# testing program
if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="Just some text")
    #in the lambdas in the CustomPrompt object creation one can pass any function
    button = tk.Button(root, text="Click me", command=lambda: CustomPrompt(root, "a or vabalabadabdab", "Test", ["Print a", "Print vabalabadabdab"], [lambda: print("a"), lambda: print("vabalabadabdab")]))
    button.pack()
    label.pack()
    root.mainloop()
