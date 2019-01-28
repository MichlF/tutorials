try:
    from Tkinter import * #Tkinter in python 2.x
except:
    from tkinter import * #tkinter in python 3.x
    
import sys

print (sys.version)

class Application(Frame):
    """ 
    Creates the GUI for the EEG analysis menu 
    """

    def __init__(self, master):
        """ 
        Initialize the frame
        """
        
        Frame.__init__(self, master)
        self.grid()
        self.create_window()
        
    def combine_funcs(*funcs):
        """ 
        Combines several functions (or function calls) in one function
        Currently does not handle functions containing individual arguments (not tested)
        
        Arguments
        ------
        - any number of functions formatted as e.g.: (func1, func2, func3)
        
        Returns
        ------
        - combined function consisting of all input functions
        """
        
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
        
    def create_window(self):
        """ 
        Creates the widgets
        """
        
        # predefine input vars
        self.ana_chosen = IntVar() 
        self.subjects_chosen = StringVar()
        self.runs_chosen = StringVar()
        self.combine_analyses = IntVar()
        self.run_preprocessing = IntVar()
        self.run_main = IntVar()
        self.ana_chosen.set(1)
        self.subjects_chosen.set('None')
        self.runs_chosen.set('None')
        self.combine_analyses.set(0) #set radio buttons empty at startup
        self.run_preprocessing.set(0)
        self.run_main.set(0)
        
        self.font_header = "Verdana 10 bold"
        self.font_regular = "Verdana 10"
        
        # create labels (text)
        Label(self,
              text = "Choose your analysis (all mandatory):", font = self.font_header
              ).grid(row = 0, column = 0, sticky = W, pady = 7)
        Label(self,
              text = "Analysis ID?", font = self.font_regular
              ). grid(row = 1, column = 0, sticky = W)
        Label(self,
              text = "Which subjects? (e.g. '2,4,5')", font = self.font_regular
              ).grid(row = 2, column = 0, sticky = W)
        Label(self,
              text = "Which runs/sessions? (e.g. '1,3')", font = self.font_regular
              ). grid(row = 3, column = 0, sticky = W)
        Label(self,
              text = "Select one (all optional, default 'No'):", font = self.font_header
              ). grid(row = 4, column = 0, sticky = W, pady = 7)
        Label(self,
              text = "Run runs/sessions combined?", font = self.font_regular
              ).grid(row = 5, column = 0, sticky = W)
        Label(self,
              text = "Run preprocessing?", font = self.font_regular
              ).grid(row = 6, column = 0, sticky = W)
        Label(self,
              text = "Run the main analysis?", font = self.font_regular
              ). grid(row = 7, column = 0, sticky = W)
        Label(self,
              text = "Current selection:", font = self.font_regular + ' italic'
              ).grid(row = 8, column = 0, sticky = W, pady = 10)
        
        # create text input windows
        self.ana_chosen = Entry(self)
        self.ana_chosen.grid(row = 1, column = 1, sticky = W, columnspan = 2)
        self.submit_button = Button(self,
                                    text = "Submit", font = self.font_regular, command = self.update_text
                                    ).grid(row = 1, column = 2, columnspan = 1, sticky = W+E, padx = 5)
        
        self.subjects_chosen = Entry(self)
        self.subjects_chosen.grid(row = 2, column = 1, sticky = W)
        self.submit_button = Button(self,
                                    text = "Submit", font = self.font_regular, command = self.update_text
                                    ).grid(row = 2, column = 2, columnspan = 2, sticky = W+E, padx = 5)

        self.runs_chosen = Entry(self)
        self.runs_chosen.grid(row = 3, column = 1, sticky = W)
        self.submit_button = Button(self,
                                    text = "Submit", font = self.font_regular, command = self.update_text
                                    ).grid(row = 3, column = 2, columnspan = 2, sticky = W+E, padx = 5)
        
        # create radiobuttons        
        Radiobutton(self,
                    text = "Yes", font = self.font_regular,
                    variable = self.combine_analyses, value = 1, command = self.update_text
                    ).grid(row = 5, column = 1, sticky = E)
        Radiobutton(self,
                    text = "No", font = self.font_regular,
                    variable = self.combine_analyses, value = 0, command = self.update_text
                    ).grid(row = 5, column = 2, sticky = W)
        Radiobutton(self,
                    text = "Yes", font = self.font_regular,
                    variable = self.run_preprocessing, value = 1, command = self.update_text
                    ).grid(row = 6, column = 1, sticky = E)
        Radiobutton(self,
                    text = "No", font = self.font_regular,
                    variable = self.run_preprocessing, value = 0, command = self.update_text
                    ).grid(row = 6, column = 2, sticky = W)
        Radiobutton(self,
                    text = "Yes", font = self.font_regular,
                    variable = self.run_main, value = 1, command = self.update_text
                    ).grid(row = 7, column = 1, sticky = E)
        Radiobutton(self,
                    text = "No", font = self.font_regular,
                    variable = self.run_main, value = 0, command = self.update_text
                    ).grid(row = 7, column = 2, sticky = W)

        # create text window
        self.text = Text(self, width = 60, height = 7, wrap = WORD)
        self.text.grid(row = 9, column = 0, columnspan = 3)
        
        # create some other buttons
        
        self.debug_mode = Button(self, text = "Debug Mode", font = self.font_regular, command = self.exit_window_2debug)
        self.debug_mode.grid(row = 10, column = 0, sticky = W, pady = 10, padx = 5)
        
        self.exit_button = Button(self, text = "Save and Start", font = self.font_regular)
        self.exit_button["command"] = self.exit_window
        self.exit_button.grid(row = 10, column = 2, sticky = E, pady = 10, padx = 5)
        
    def exit_window(self):
        """ 
        Exits the GUI to start analysis 
        """
        
        self.debug_mode = 0
        self.ana_number = self.ana_chosen.get()
        self.subjects = [int(n) for n in self.subjects_chosen.get().split(',')]
        self.run_number = [int(n) for n in self.runs_chosen.get().split(',')]
        self.combined_run = self.combine_analyses.get()
        self.step_preprocess = self.run_preprocessing.get()
        self.step_main = self.run_main.get()    
        
        self.master.destroy()
        
    def exit_window_2debug(self):
        """ 
        Exits the GUI to start analysis with debug parameters (defined in session batch script)
        """
        
        self.debug_mode = 1
        self.master.destroy()
        
    def update_text(self):
        """
        Updates the status window to the most recent choice input(s)
        Note: In the current version the status window remains blank until a choice/input is provided. This should be fixed at some point.
        """
        
        fb_ana_chosen = self.ana_chosen.get()
        fb_subjects_chosen = self.subjects_chosen.get()
        fb_runs_chosen = self.runs_chosen.get()
        fb_combine_analyses = 'not combined'
        fb_run_preprocessing = 'No preprocessing'
        fb_run_main = 'no main analysis'
        
        if self.combine_analyses.get() == 1:
            fb_combine_analyses = 'combined'
        if self.run_preprocessing.get() == 1:
            fb_run_preprocessing = 'Preprocessing'
        if self.run_main.get() == 1:
            fb_run_main = 'the main analysis'
            
        message = 'You have chosen '
        message += 'analysis ' + fb_ana_chosen + ' for subject(s) ' + fb_subjects_chosen + ' each with run(s)/session(s) ' + fb_runs_chosen + '.' + ' Their run(s)/session(s) will be ' + fb_combine_analyses + '.' + ' ' + fb_run_preprocessing + ' and ' + fb_run_main + ' will be executed.'
        
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
          
root = Tk()
root.title("EEG analysis")

app = Application(root)

root.mainloop()

print app.debug_mode, type(app.debug_mode)
if app.debug_mode == 0:
    print app.ana_number, type(app.ana_number)
    print app.subjects, type(app.subjects)
    print app.run_number, type(app.run_number)
    print app.combined_run, type(app.combined_run)
    print app.step_preprocess, type(app.step_preprocess)
    print app.step_main, type(app.step_main)