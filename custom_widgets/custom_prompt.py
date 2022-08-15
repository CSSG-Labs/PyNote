import tkinter as tk


class CustomPrompt(tk.Toplevel):
    """
    custom prompt displaying some text and below it a row of option buttons
        
    Attributes
    ----------
    parent : 
        the prompt parent
    title : str
        the title of the prompt window
    text : str
        the text that will be showed in the center and invite the user to take an action
    text_options : list
        list of text for the buttons of the actions
    function_options: list
        list of functions for the buttons of the actions (must be the same length as text_options)
    close_on_click: Boot
        (Default True)
        If True the prompt autocloses after an option was chosen,
        if False otherwise

    Methods
    ----------
    function_handler(i) :
        NOT INTENDED TO BE USED OUTSIDE THE CLASS
        method to add to the given function (taken from the function_options list via index i)
            the functionality of closing if necessary the prompt window

    Example of usage
    ----------
    #Copy to see how the class functions
    root = tk.Tk()
    label = tk.Label(root, text="Just some text")
    #in the lambdas in the CustomPrompt object creation one can pass any function
    button = tk.Button(root, text="Click me", command=lambda: CustomPrompt(root, "a or averyverylongstring", "Test", ["Print a", "Print averyverylongstring"], [lambda: print("a"), lambda: print("averyverylongstring")]))
    button.pack()
    label.pack()
    root.mainloop()
    """
    def __init__(self, parent, title, text, text_options, functions_options, close_on_click=True):
        #initialization, argument check and fixing window size
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
    
    def function_handler(self, i):
        if(self.close_on_click):
            self.functions_options[i]()
            self.destroy()
        else:
            self.functions_options[i]()
