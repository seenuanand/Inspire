# Inspire
Executing the Inspire  Automation Scripts

Requirements
allure-behave==2.8.18
allure-python-commons==2.8.18
attrs==20.2.0
behave==1.2.6
iniconfig==1.1.1
packaging==20.4
parse==1.18.0
parse-type==0.5.2
pluggy==0.13.1
py==1.9.0
pyparsing==2.4.7
pytest==6.1.1
selenium==3.141.0
six==1.15.0
toml==0.10.1
urllib3==1.25.11


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
#Functionality
#Click on “Create Post”
#Verify the overlay pops up.
#Click on the "Choose Community" and choose a community you joined in Step 1.
#Click on the "Choose Topic" and choose any topic.
#Create a title in the title input field.
#Write some content in the body textarea.
#Click the "Privacy" dropdown menu and choose the "Inspire Friends" option
#Click Post
#Verify that your post shows up at the top of the lists of posts in your account by looking for the text you used to input. 

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

Functionality
#Click on “Create Post”
#Verify the overlay pops up.
#Click on the "Choose Community" and choose a community you joined in Step 1.
#Click on the "Choose Topic" and choose any topic.
#Create a title in the title input field.
#Write some content in the body textarea.
#Click the "Privacy" dropdown menu and choose the "Inspire Friends" option
#Click Post
#Verify that your post shows up at the top of the lists of posts in your account by looking for the text you used to input.     

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