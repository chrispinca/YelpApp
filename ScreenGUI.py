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

        self.buttonHeight = 2
        self.buttonWidth = 20

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
        self.LoginButton = tk.Button(self.LoginFrame, text = "Login", command = self.login, height = 2, width = 20)
        self.LoginButton = self.LoginButton.grid(row = 2, column = 0, columnspan = 2, pady = 4)

    """
    Handles the event triggered by the login button
    """
    def login(self):
        userID = self.EntryUserID.get()
        print(userID)
        try:
            conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_cpinca;pwd=ba266eay2N3Edryt')
            print("Connection successful")
            self.createMainScreen()
        except pyodbc.Error as e:
            messagebox.showerror("Login Failed", f"Invalid Credentials")
        finally:
            if 'conn' in locals():
                conn.close()


    def createMainScreen(self):
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        self.SearchBusinessButton = tk.Button(self.LoginFrame, text="Search Businesses", command=self.searchBusiness, height = self.buttonHeight, width = self.buttonWidth)
        self.SearchBusinessButton.grid(row=0, column=0, padx=5, pady=5)

        self.SearchUsersButton = tk.Button(self.LoginFrame, text="Search Users", command=self.searchUsers, height = self.buttonHeight, width = self.buttonWidth)
        self.SearchUsersButton.grid(row=1, column=0, padx=5, pady=5)

        self.MakeFriendButton = tk.Button(self.LoginFrame, text="Make Friend", command=self.makeFriend, height = self.buttonHeight, width = self.buttonWidth)
        self.MakeFriendButton.grid(row=2, column=0, padx=5, pady=5)

        self.ReviewBusinessButton = tk.Button(self.LoginFrame, text="Review Business", command=self.reviewBusiness, height = self.buttonHeight, width = self.buttonWidth)
        self.ReviewBusinessButton.grid(row=3, column=0, padx=5, pady=5)

    def searchUsers(self):
        print("We searchin users")

    def makeFriend(self):
        print("We makin friends")

    def reviewBusiness(self):
        print("We reviewin businesses")


    def searchBusiness(self): 
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        orderByOptions = ["Name", "City", "Stars"]
        self.orderByVar = tk.StringVar()
        self.orderByVar.set("Select Option") 

        self.TitleLabel = tk.Label(self.LoginFrame, text = "Search Businesses", font = ("Arial, 16")) 
        self.TitleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        self.LabelSearch = tk.Label(self.LoginFrame, text="Minimum Stars (1-5): ")
        self.LabelSearch.grid(row=1, column=0, padx=5, pady=2)

        self.EntryMinStars = tk.Entry(self.LoginFrame)
        self.EntryMinStars.grid(row=2, column=0, padx=5, pady=2)

        self.LabelCityName = tk.Label(self.LoginFrame, text="Enter City Name: ")
        self.LabelCityName.grid(row=3, column=0, padx=5, pady=2)

        self.EntryCityName = tk.Entry(self.LoginFrame)
        self.EntryCityName.grid(row=4, column=0, padx=5, pady=2)

        self.LabelBusinessName = tk.Label(self.LoginFrame, text="Business Name: ")
        self.LabelBusinessName.grid(row=5, column=0, padx=5, pady=2)

        self.EntryBusinessName = tk.Entry(self.LoginFrame)
        self.EntryBusinessName.grid(row=6, column=0, padx=5, pady=2)

        self.LabelOrderBy = tk.Label(self.LoginFrame, text="Order By Dropdown:")
        self.LabelOrderBy.grid(row=7, column=0, padx=5, pady=2)

        self.orderByDropdown = tk.OptionMenu(self.LoginFrame, self.orderByVar, *orderByOptions)
        self.orderByDropdown.grid(row=8, column=0, padx=5, pady=2)

        self.SearchButton = tk.Button(self.LoginFrame, text="Search", command=self.searchForBusiness, height = self.buttonHeight, width = self.buttonWidth)
        self.SearchButton.grid(row=11, column=0, columnspan=4, pady=4)

        self.BackButton = tk.Button(self.LoginFrame, text="Back", command=self.createMainScreen)
        self.BackButton.grid(row=0, column=15, columnspan=2, padx=5, pady=4)

    def searchUsers(self): 
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        self.TitleLabel = tk.Label(self.LoginFrame, text = "Search Users", font = ("Arial, 16")) 
        self.TitleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        self.BackButton = tk.Button(self.LoginFrame, text="Back", command=self.createMainScreen)
        self.BackButton.grid(row=0, column=15, columnspan=2, padx=5, pady=4)

        self.LabelUserName = tk.Label(self.LoginFrame, text="Enter User Name: ")
        self.LabelUserName.grid(row=1, column=0, padx=5, pady=2)

        self.EntryUserName = tk.Entry(self.LoginFrame)
        self.EntryUserName.grid(row=2, column=0, padx=5, pady=2)

        self.LabelMinReviewCount = tk.Label(self.LoginFrame, text="Minimum Review Count: ")
        self.LabelMinReviewCount.grid(row=3, column=0, padx=5, pady=2)

        self.EntryMinReviewCount = tk.Entry(self.LoginFrame)
        self.EntryMinReviewCount.grid(row=4, column=0, padx=5, pady=2)

        self.LabelMinAvgStars = tk.Label(self.LoginFrame, text="Minimum Average Stars (1-5): ")
        self.LabelMinAvgStars.grid(row=5, column=0, padx=5, pady=2)

        self.EntryMinStars = tk.Entry(self.LoginFrame)
        self.EntryMinStars.grid(row=6, column=0, padx=5, pady=2)

        self.SearchButton = tk.Button(self.LoginFrame, text="Search", command=self.searchForUser, height = self.buttonHeight, width = self.buttonWidth)
        self.SearchButton.grid(row=11, column=0, columnspan=4, pady=4)

    
    def searchForBusiness(self):
        # Add logic to perform the search based on the entered criteria
        minStars = self.EntryMinStars.get()
        cityName = self.EntryCityName.get()
        businessName = self.EntryBusinessName.get()
        orderBy = self.orderByVar.get()
        print(f"Performing search with these options: {minStars} {cityName} {businessName}")
        print(f"Sorting by: {orderBy}")

        try:
            conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_cpinca;pwd=ba266eay2N3Edryt')
            cursor = conn.cursor()

            sqlQuery = f"""
                          SELECT business_id, name, address, city, stars 
                          FROM business 
                          WHERE stars >= {minStars} 
                          AND city LIKE '%{cityName}%' 
                          AND name LIKE '%{businessName}%' 
                          ORDER BY {orderBy}"""
            cursor.execute(sqlQuery)
            rows = cursor.fetchall()

            for row in rows:
                stars = f"STARS: {row.stars}"
                print(f"ID: {row.business_id}, NAME: {row.name}, ADDRESS: {row.address}, CITY: {row.city}, {stars}")
        except pyodbc.Error as e:
            messagebox.showerror("SQL ERROR")
        finally: 
            if 'conn' in locals():
                conn.close()

    def searchForUser(self):
        userName = self.EntryUserName.get()
        reviewCount = self.EntryMinReviewCount.get()
        #set default to 0
        minAvgStars = self.EntryMinStars.get()
        print(f"Performing search with these options: {userName} {reviewCount} {minAvgStars}")
        print(f"Sorting by name: ")

        try:
            conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_cpinca;pwd=ba266eay2N3Edryt')
            cursor = conn.cursor()

            sqlQuery2 = f"""
                          SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since
                          FROM user_yelp 
                          WHERE average_stars >= {minAvgStars} 
                          AND name LIKE '%{userName}%' 
                          AND review_count >= {reviewCount} 
                          ORDER BY name"""
            cursor.execute(sqlQuery2)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
        except pyodbc.Error as e:
            messagebox.showerror("SQL ERROR", f"An error occurred while querying the database: {str(e)}")
        finally: 
            if 'conn' in locals():
                conn.close()


if __name__ == "__main__":
    #creates the Tkinter root window and an instance of the ScreenGUI class
    root = tk.Tk()
    AppScreen = ScreenGUI(root)
    root.mainloop()