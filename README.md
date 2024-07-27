# Installing Python
### How to install python
1. Go to python.org/downloads/
2. Under the heading "Download the latest version of Python", click in the yellow box to download
3. Complete installation settings according to desired preferences

### Running a python program
1. Open python
2. Type  ***print("Hello World")***
3. Push enter and you should see "Hello World" as a result

# Learning Markdown
### What is Markdown?
Markdown is a type of lightweight markup language that can be used to add text to documents. In some ways Markdown is similar to HTML in terms of functionality because they both are used to add plaintext to doucuments. However, HTML is a more complicated language to learn whereas Markdown is simple and easy to use and easy to learn to use. 

### Markdown Guide
For general usage purposes, here are some of the rules to learn:
* Headings:
  * To create a heading put '#' in front of your text. Be sure to leave a space before you create your line of text.
  * To create a smaller heading put '##' in front of your text. Be sure to leave a space before you create your line of text.
  * To create a section heading, put '###' in front of your text. Be sure to leave a space before you create your line of text.
* Text:
  * To italicize text put "*" or "_" at the beginning and the end of your text. Do not leave any space.
  * To bold text put "**" or "__" at the beginning and the end of your text. Do not leave any space.
* Lists:
  * To create bullet points put "*" in front of your text. Be sure to leave a space before you create your line of text.
  * To create a numbered list put "1." in front of your text. Be sure to leave a space before you create your line of text.
 
  
# JSON Requests
### What are JSON Requests?
A JSON requests is a request made by a client to a server where data is being sent or received and is formatted as JSON (JavaScript Object Notation). It is a way for clients and servers to communciate with each other and it is commonly used in web development

### Creating a Web Scraper
When creating a Web Scraper in Python, it is necessary to use the lines "import requests" (which allows the program to make HTTP requests in Python) and "from bs4 import BeautifulSoup" (which imports "BeautifulSoup" that is used for parsing HTML documents). Make sure to install both if needed to run the program.

# Input Validation
### What is Input Validation?
Input Validation is used in programming to ensure that correct data is entered into a program. This can include checking the length of a variable, checking whether an input is within a certain range, checking whether an input is positive or negative, etc.

### Creating a Program to Validate User Input
Checking the length of a string is commonly used in websites where passwords are necessary. In general, the longer a password, the more secure it is. To test if an input is above a certain number of characters you can use the len() function that checks the length of a string and returns how many characters there are. Using if else statements it is simple to check whether or not a string has enough characters.

# Postman Calls
### What is a postman call?
Postman is an API platform for bulding and using APIs. A postman call allows a user to send API requests 

### Using Postman
Open Postman and navigate to the plus tab. From there, you will be able to choose the default method "GET" to grab information from your API using the link your program generates along with /get(yourfunction). For example, "http://127.0.0.1:5000/getBookmarks" returned "300 Bookmarks"

# Object Orientation
### Definitions
Object Oriented Programming (OOP) is a fundamental programming idea that involes classes and objects containing code that includes important ideas such as abstraction, polymorphism, amd encapsulation. The code is a set of data contained in fields instead of using a traditional logic based system.

### Example
One real life application and example of classes and objects is a menu item class. The class in the menu item case will have the characteristics and functions of a menu. In a simple example of object oriented programming, the menu item class will have two characterisitcs which is the name of the food and the price of the food. Then, instead of a user just creating a new item every time they want to add a food to a menu, they can create a menu item object that already has all the charactersitics of a class which is much simpler and saves time. The code can also be compiled more easily.

# YAML Files
### What is YAML
YAML (YAML Ain't Markup Language) is a human-readable data serialization language that is often used for writing configuration files. For example it can be used with docker for creating a docker-compose.yml file

### What is Docker?
Docker is a software with many uses. Focusing on it's similarities between virtual machines, it can be used for many of the same things. However, instead of running, for example, a linux machine in the cloud or on your machine using the machines own resources, you can run an ubuntu machine using your machine's resources in an isolated container.

# Hashing Algorithms
Hashing algorithms are mathematical functions that are one way only to make data unreadable. When something is hashed, the length of it is fixed making it impossible to work backwards. If one small change is made to some text (removing a letter or adding a letter) it does not just change one thing about the hash value, but completely changes the entire output of the hash function.

# DevOps Practices
