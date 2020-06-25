# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 21:52:47 2015

@author: Michel
"""

####################
# simple buttons ###
####################

#from Tkinter import * #Tkinter in python 2.x, tkinter in python 3.x
#import sys
#
#print (sys.version)
#
#
## create the window
#root = Tk()
#
##modify root window
#root.title("Selection menu")
#root.geometry("200x100")
#
#app = Frame(root)
#app.grid()
##label = Label(app, text = "This is a label!")
##label.grid()
#
#button1 = Button(app, text = "This is a button")
#button1.grid()
#
#button2 = Button(app)
#button2.grid()
#button2.configure(text = "This will show text")
#
#button3 = Button(app)
#button3.grid()
#button3["text"] = "This will show up as well"
#
##kick off the event loop
#root.mainloop()
#

#####################################
### buttons as class and changing ###
#####################################

#from Tkinter import * #Tkinter in python 2.x, tkinter in python 3.x
#import sys
#
#print (sys.version)
#
#class Application(Frame):
#    """ GUI """
#    
#    def __init__(self, master):
#        """ Initialize the frame """
#        Frame.__init__(self, master)
#        self.grid()
#        self.button_clicks = 0 #count the number of button clicks
#        self.that_changed = 0
#        self.create_widgets()
#        
#    def create_widgets(self):
#        """ Create button(s) """
#        # first button
##        button1 = Button(self, text = "This is a button")
##        button1.grid()
##        
##        button2 = Button(self)
##        button2.grid()
##        button2.configure(text = "This will show text")
##        
##        button3 = Button(self)
##        button3.grid()
##        button3["text"] = "This will show up as well"
#        
#        self.button = Button(self)
#        self.button["text"] = "Total Clicks: 0"
#        self.button["command"] = self.update_count
#        self.button.grid()
#        
#        self.button2 = Button(self)
#        self.button2["text"] = "This is a var changer test"
#        self.button2["command"] = self.change_something
#        self.button2.grid()
#        
#    def update_count(self):
#        """ Increase """
#        self.button_clicks += 1
#        self.button["text"] = "Total Clicks: " + str(self.button_clicks)
#        
#    def change_something(self):
#        """ Change """
#        self.that_changed = 1
#        self.button2["text"] = "You selected this to be changed"
#        
#           
#root = Tk()
#root.title("Lazy buttons")
#root.geometry("200x85")
#
#app = Application(root)
#
#root.mainloop()

#######################
##### WRITTEN INPUT ###
#######################

from Tkinter import * #Tkinter in python 2.x, tkinter in python 3.x
import sys

print (sys.version)

class Application(Frame):
    """ GUI """
    
    def __init__(self, master):
        """ Initialize the frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create button(s) """
        
        self.instruction = Label(self, text = "Enter the password")
        
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W) # sticky -> Force to put the label to the W (west) side; so left
        
        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)
        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)
        
        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        
    def reveal(self):
        """ Display message based on the password typed in """
        content = self.password.get()
        
        if content == "password":
            message = "You have access to something special."
        else:
            message = "Access denied."
            
        self.text.delete(0.0, END) # delete previous message
        self.text.insert(0.0, message) #insert your message at position row 0, colomn 0
    
root = Tk()
root.title("Password")
root.geometry("250x150")
app = Application(root)

root.mainloop()

#####################
### Check buttons ###
#####################

#from Tkinter import * #Tkinter in python 2.x, tkinter in python 3.x
#import sys
#
#print (sys.version)
#
#class Application(Frame):
#    """ GUI """
#    
#    def __init__(self, master):
#        """ Initialize the frame """
#        Frame.__init__(self, master)
#        self.grid()
#        self.create_widgets()
#        
#    def create_widgets(self):
#        """ Create widgets for movie type choice """
#        Label(self, text = "Choose your favorite movie type").grid(row =0, column = 0, sticky = W)
#        
#        #instructions
#        Label(self, text = "Select all that apply:").grid(row = 1, column = 0, sticky = W)
#        
#        #comedy check button
#        self.comedy = BooleanVar()
#        Checkbutton(self, text = "Comedy", variable = self.comedy, command = self.update_text).grid(row = 2, column = 0, sticky = W)
#        
#        #drama check button
#        self.drama = BooleanVar()
#        Checkbutton(self, text = "Drama", variable = self.drama, command = self.update_text).grid(row = 3, column = 0, sticky = W)
#        
#        #comedy check button
#        self.adventure = BooleanVar()
#        Checkbutton(self, text = "Adventure", variable = self.adventure, command = self.update_text).grid(row = 4, column = 0, sticky = W)
#        
#        # Present the results
#        self.result = Text(self, width = 40, height = 5, wrap = WORD)
#        self.result.grid(row = 5, column = 0, columnspan = 3)
#        
#    def update_text(self):
#        """ Update text widget and display favorite movie types """
#        likes = ""
#        if self.comedy.get(): # Checks whether true or false, does not need self.comedy.get() == True
#            likes += "You like comedy. "
#        if self.drama.get():
#            likes += "You like drama. "
#        if self.adventure.get():
#            likes += "You like adventure. "
#        self.result.delete(0.0, END)
#        self.result.insert(0.0, likes)
#        
#root = Tk()
#root.title("Movie Chooser")
#app = Application(root)
#
#root.mainloop()

#####################
### Radio buttons ###
#####################

#from Tkinter import * #Tkinter in python 2.x, tkinter in python 3.x
#import sys
#
#print (sys.version)
#
#class Application(Frame):
#    """ GUI """
#    
#    def __init__(self, master):
#        """ Initialize the frame """
#        Frame.__init__(self, master)
#        self.grid()
#        self.create_widgets()
#        
#    def create_widgets(self):
#        """ Create widgets for movie type choice. """
#        Label(self,
#              text = "Choose your favorite type of movie"
#              ).grid(row = 0, column = 0, sticky = W)
#        Label(self,
#              text = "Selecting one:"
#              ). grid(row = 1, column = 0, sticky = W)
#              
#        #variable for single, favorite type of movie
#        self.favorite = StringVar() # you want a string
#        self.favorite.set(0) # set radio buttons empty at startup
#        
#        Radiobutton(self,
#                    text = "Comedy",
#                    variable = self.favorite,
#                    value = "comedy.",
#                    command = self.update_text
#                    ).grid(row = 2, column = 0, sticky = W)
#
#        Radiobutton(self,
#                    text = "Drama",
#                    variable = self.favorite,
#                    value = "drama.",
#                    command = self.update_text
#                    ).grid(row = 3, column = 0, sticky = W)
#                    
#        Radiobutton(self,
#                    text = "Adventure",
#                    variable = self.favorite,
#                    value = "adventure.",
#                    command = self.update_text
#                    ).grid(row = 4, column = 0, sticky = W)
#                    
#        self.result = Text(self, width = 40, height = 5, wrap = WORD)
#        self.result.grid(row = 5, column = 0, columnspan = 3)
#        
#    def update_text(self):
#        """Update the text area """
#        message = "Your favorite type of movie is "
#        message += self.favorite.get()
#        
#        self.result.delete(0.0, END)
#        self.result.insert(0.0, message)
#        
#root = Tk()
#root.title("Single movie chooser")
#app = Application(root)
#root.mainloop()
        