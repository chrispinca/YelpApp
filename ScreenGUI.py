import tkinter as tk
from tkinter import messagebox

import pyodbc

"""
Initializes the Screen for the GUI
"""

class ScreenGUI:
    def __init__(self, root):
        #saves the root window and then sets the window title
        self.root = root
        self.root.title("Yelp App")

        #gets the user screen width and height and sets the app width and height
        UserScreenWidth = self.root.winfo_screenwidth()
        UserScreenHeight = self.root.winfo_screenheight()

        AppScreenWidth = 500
        AppScreenHeight = 500

        #calculates the centred x and y positions for the user's screen
        xPos = (UserScreenWidth - AppScreenWidth) // 2
        yPos = (UserScreenHeight - AppScreenHeight) // 2 

        #creates the frame for the login screen 
        self.LoginFrame = tk.Frame(self.root, width = AppScreenWidth, height = AppScreenHeight)
        self.LoginFrame.pack(padx = 15, pady = 15)

        #centers the window on the users screen
        self.root.geometry(f"{AppScreenWidth}x{AppScreenHeight}+{xPos}+{yPos}")

        #creates the label and entry for the userID
        self.LabelUserID = tk.Label(self.LoginFrame, text = "User ID:")
        self.LabelUserID.grid(row = 0, column = 0, padx = 5, pady = 2)
        
        self.EntryUserID = tk.Entry(self.LoginFrame)
        self.EntryUserID.grid(row = 0, column = 1, padx = 5, pady = 2)

        #creates the login button
        self.LoginButton = tk.Button(self.LoginFrame, text = "Login", command = self.login)
        self.LoginButton = self.LoginButton.grid(row = 2, column = 0, columnspan = 2, pady = 4)

    """
    Handles the event triggered by the login button
    """
    def login(self):
        userID = self.EntryUserID.get()
        print(userID)

if __name__ == "__main__":
    #creates the Tkinter root window and an instance of the ScreenGUI class
    root = tk.Tk()
    AppScreen = ScreenGUI(root)
    root.mainloop()