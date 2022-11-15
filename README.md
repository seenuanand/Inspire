# Inspire
Executing the Inspire  Automation Scripts

Packages
1. Selenium
2. Packaging
3. Behave

GitHub UR
https://github.com/seenuanand/Inspire

Accessing the Project 

Directly Clone the Project from Git Location
Create a Local Brnach

Can also Download as Zip
Extract and copy it to your shared location
Open the project in PyCharm

Login Credentials for the Application
UserName : srinivas.anand1@gmail.com
Password : Srinivas@12345

Execution
testPostBusinessProcess.py is a Vanila Script for analysing and it can be used as a Business Process Execution for Post Functionality
webDriverManagerCheck.py is a  Driver Manager Checking script to avoid downloading the Drivers (Not Implimented yet to functionality)

The above scripts can be executed directly from command prompt
C:/ProjectLocation/testPostBusinessProcess.py
Or
From PyCharm Terminal

Behave Implimentation
Feature File
createNewPost.feature
Step Definition : createNewPost.py
It can be executed directly from pycharm terminal with following commands
behave .\feature\createNewPost.feature     

You can also run 
verifyHomePage.feature
verifyLogin.feature 

CreatePostAndDelete.feature is still in working progress.

Please let me know if you need more info on srinivas.anand1@gmail.com

Note:  I am working on few more enhancement on framework like 
		Reading from Config Files
		Page Object Model
		Data Driven for functionality needed (As of now the data is fetched from feature file)
		Report Creations
