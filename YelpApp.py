import datetime
import tkinter as tk
from tkinter import messagebox
import secrets

import pyodbc


#Initializes the Screen for the GUI

class YelpApp:
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
        self.userID = self.EntryUserID.get()
        print(self.userID)

        try:
            #establishes connection to database
            self.conn = pyodbc.connect('driver={SQL Server};server=cypress.csil.sfu.ca;uid=s_cpinca;pwd=ba266eay2N3Edryt')
            print("Connection successful")
        except pyodbc.Error as e:
            #error message if it fails
            messagebox.showerror("Login Failed", f"Invalid Credentials")
        finally:
            if 'conn' in locals():
                self.conn.close()

        cursor = self.conn.cursor()
        sqlUserCheck = f"""
                    SELECT COUNT(*)
                    FROM user_yelp
                    WHERE user_id = '{self.userID}'
                    """
        cursor.execute(sqlUserCheck)
        count = cursor.fetchone()[0]
        print(count)

        if count > 0:
            self.createMainScreen()
            
    def createMainScreen(self):
        #clears the login frame and creates the main screen buttons
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

    def makeFriend(self):
        #clears the current frame and creates the Make Friend frame
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        self.TitleLabel = tk.Label(self.LoginFrame, text = "Make Friend", font = ("Arial, 16")) 
        self.TitleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        self.BackButton = tk.Button(self.LoginFrame, text="Back", command=self.createMainScreen)
        self.BackButton.grid(row=0, column=15, columnspan=2, padx=5, pady=4)

        self.LabelAddFriend = tk.Label(self.LoginFrame, text="Enter Their User ID To Add Friend: ")
        self.LabelAddFriend.grid(row=1, column=0, padx=5, pady=2)

        self.EntryAddUserID = tk.Entry(self.LoginFrame)
        self.EntryAddUserID.grid(row=2, column=0, padx=5, pady=2)

        self.AddFriendButton = tk.Button(self.LoginFrame, text="Add Friend", command=self.addFriend, height = self.buttonHeight, width = self.buttonWidth)
        self.AddFriendButton.grid(row=3, column=0, columnspan=4, pady=4)

    def searchBusiness(self): 
        #clears the frame and makes the Search Business frame
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        orderByOptions = ["Name", "City", "Stars"]
        self.orderByVar = tk.StringVar()
        self.orderByVar.set("Select Option") 

        self.TitleLabel = tk.Label(self.LoginFrame, text = "Search Businesses", font = ("Arial, 16")) 
        self.TitleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        self.LabelSearch = tk.Label(self.LoginFrame, text="Minimum Stars (0-5): ")
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

    def reviewBusiness(self):
        #clears the frame and creates the Review Business frame
        for widget in self.LoginFrame.winfo_children():
            widget.destroy()

        self.TitleLabel = tk.Label(self.LoginFrame, text = "Review Business", font = ("Arial, 16")) 
        self.TitleLabel.grid(row=0, column=0, columnspan=2, pady=10)

        self.BackButton = tk.Button(self.LoginFrame, text="Back", command=self.createMainScreen)
        self.BackButton.grid(row=0, column=15, columnspan=2, padx=5, pady=4)

        self.LabelReviewBusinessID = tk.Label(self.LoginFrame, text="Business ID: ")
        self.LabelReviewBusinessID.grid(row=1, column=0, padx=5, pady=2)

        self.EntryReviewBusinessID = tk.Entry(self.LoginFrame)
        self.EntryReviewBusinessID.grid(row=2, column=0, padx=5, pady=2)

        self.LabelRateStars = tk.Label(self.LoginFrame, text="Rate by Stars (1-5): ")
        self.LabelRateStars.grid(row=3, column=0, padx=5, pady=2)

        self.EntryRateStars = tk.Entry(self.LoginFrame)
        self.EntryRateStars.grid(row=4, column=0, padx=5, pady=2)

        self.AddReviewButton = tk.Button(self.LoginFrame, text="Review Business", command=self.addReview, height = self.buttonHeight, width = self.buttonWidth)
        self.AddReviewButton.grid(row=5, column=0, columnspan=4, pady=4)



    def searchUsers(self): 
        #clears the frame and makes the Search Users frame
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

        self.LabelMinAvgStars = tk.Label(self.LoginFrame, text="Minimum Average Stars (0-5): ")
        self.LabelMinAvgStars.grid(row=5, column=0, padx=5, pady=2)

        self.EntryMinStars = tk.Entry(self.LoginFrame)
        self.EntryMinStars.grid(row=6, column=0, padx=5, pady=2)

        self.SearchButton = tk.Button(self.LoginFrame, text="Search", command=self.searchForUser, height = self.buttonHeight, width = self.buttonWidth)
        self.SearchButton.grid(row=11, column=0, columnspan=4, pady=4)

    
    def searchForBusiness(self):
        #Performs the search based on the criteria entered
        minStars = self.EntryMinStars.get() or 'NULL'
        minStarsInt = int(minStars)
        #check that the correct star input was supplied
        if not 1 <= minStarsInt <= 5:
            messagebox.showerror("Stars must be between 1 and 5")

        cityName = self.EntryCityName.get() or ''
        businessName = self.EntryBusinessName.get() or ''
        orderBy = self.orderByVar.get()

        try:
            cursor = self.conn.cursor()
            sqlBusinessSearch = f"""
                          SELECT business_id, name, address, city, stars 
                          FROM business 
                          WHERE stars >= {minStars} 
                          AND city LIKE '%{cityName}%' 
                          AND name LIKE '%{businessName}%' 
                          ORDER BY {orderBy}"""
            cursor.execute(sqlBusinessSearch)
            rows = cursor.fetchall()

            if not rows:
                print("NO RESULTS MATCHING YOUR CRITERIA FOUND")
                messagebox.showerror("NO RESULTS MATCHING YOUR CRITERIA FOUND")
            else:
                for row in rows:
                    print(f"ID: {row.business_id}, NAME: {row.name}, ADDRESS: {row.address}, CITY: {row.city}, STARS: {row.stars}")
        except pyodbc.Error as e:
            messagebox.showerror("You must select SORT BY")
            messagebox.showerror("Could Not Find Business")
        finally: 
            if 'conn' in locals():
                self.conn.close()

    def searchForUser(self):
        #performs the search for user with the specified criteria
        userName = self.EntryUserName.get() or ''
        reviewCount = self.EntryMinReviewCount.get() or '0'
        minAvgStars = self.EntryMinStars.get() or ' 0'

        try:
            #executes sql query to find the search results
            cursor = self.conn.cursor()

            sqlUserSearch = f"""
                          SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since
                          FROM user_yelp 
                          WHERE average_stars >= {minAvgStars} 
                          AND name LIKE '%{userName}%' 
                          AND review_count >= {reviewCount} 
                          ORDER BY name"""
            cursor.execute(sqlUserSearch)
            rows = cursor.fetchall()

            if not rows:
                print("NO RESULTS MATCHING YOUR CRITERIA FOUND")
                messagebox.showerror("NO RESULTS MATCHING YOUR CRITERIA FOUND")
            else:
                for row in rows:
                    print(f"ID: {row.user_id}, NAME: {row.name}, REVIEW COUNT: {row.review_count}, USEFUL: {row.useful}, FUNNY: {row.funny}, COOL: {row.cool}, AVERAGE STARS: {row.average_stars}, SIGNUP DATE: {row.yelping_since}")
        except pyodbc.Error as e:
            messagebox.showerror("SQL ERROR", f"An error occurred while querying the database: {str(e)}")
        finally: 
            if 'conn' in locals():
                self.conn.close()

    def addFriend(self):
        #add a friend based on their userID
        friendID = self.EntryAddUserID.get()
        cursor = self.conn.cursor()
        #check that the user actually exists
        sqlUserCheck = f"""
                        SELECT *
                        FROM user_yelp
                        WHERE user_id = '{friendID}'
                        """
        cursor.execute(sqlUserCheck)
        userCheck = cursor.fetchone()

        #if the user exists, execute the sql query to add a friend
        if userCheck:
            try:
                cursor = self.conn.cursor()
                sqlAddFriend = f"""
                            INSERT INTO friendship (user_id, friend)
                            VALUES (
                                '{self.userID}',
                                '{friendID}'
                            )
                            """
                cursor.execute(sqlAddFriend)
                self.conn.commit()
                messagebox.showinfo("Success", "Friend added successfully!")
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Failed to add friend. Please try again.")
            finally: 
                if 'conn' in locals():
                    self.conn.close()

    #Creates a random id for the review
    def RandomReviewID(self):
        prefix = "cmpt354"
        randomString = secrets.token_hex(8)
        return f"{prefix}_{randomString[:6]}"

    #Add a review after supplying criteria
    def addReview(self):
        
        businessID = self.EntryReviewBusinessID.get()
        rateStars = self.EntryRateStars.get()
        rateStarsInt = int(rateStars)

        if 1 <= rateStarsInt <= 5:
            reviewID = self.RandomReviewID()
        else:
            print("Stars must be between  1 and 5")
            messagebox.showerror("Stars must be between  1 and 5")

        cursor = self.conn.cursor()
        #check that the business exists
        sqlUserCheck = f"""
                        SELECT *
                        FROM business
                        WHERE business_id = '{businessID}'
                        """
        cursor.execute(sqlUserCheck)
        userCheck = cursor.fetchone()

        #if business exists then execute query to add a review
        if userCheck:
            try:
                cursor = self.conn.cursor()
                #Insert review
                sqlAddReview = f"""
                          INSERT INTO review (review_id, user_id, business_id, stars, date)
                          VALUES ('{reviewID}', '{self.userID}','{businessID}','{rateStars}', GETDATE())
                          """
                cursor.execute(sqlAddReview)
                self.conn.commit()
                #update business after review
                sqlUpdateBusiness = f"""
                                UPDATE business
                                SET review_count = (SELECT COUNT(*) FROM Review WHERE business_id = '{businessID}')
                                WHERE business_id = '{businessID}'
                                """
                cursor.execute(sqlUpdateBusiness)
                self.conn.commit()
                messagebox.showinfo("Success", "Business Reviewed Successfully!")

            except pyodbc.Error as e:
                messagebox.showerror("Error", "Failed to review Business. Please try again.")
            finally: 
                if 'conn' in locals():
                    self.conn.close()
        else:
            messagebox.showerror("Error", "No Business with that ID exists")

if __name__ == "__main__":
    #creates the Tkinter root window and an instance of the YelpApp
    root = tk.Tk()
    AppScreen = YelpApp(root)
    root.mainloop()