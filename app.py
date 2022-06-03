from helpers.createQuery import *
from helpers.welcome import *


welcome()
print("Enter Username")
username = input("Username: ")
print("Enter Password")
password = input("Password: ")
def login():
    run_query("SELECT username, password FROM user WHERE username=? and password=?", [username, password])
login()
def blog_interface_loop():
    pass

print("What would you like to do in Bloggie today?")

# Choices for creating new post, viewing all posts, and exiting
print("To create a new Post: " + "Enter 1")
print("To view all Posts: " + "Enter 2")
print("To Exit Select: " + "Enter 3")

while True:
    selection = input("Select here: ")
    
    #Choice # one is to make a new post (insert query)
    if selection == "1":
        
        content = input("Enter Content here: ")
        def createPost():
            post = run_query("INSERT INTO blog_post (username, content) VALUE (?,?)", [username, content])
            print(post)
        createPost()

    #Choice # two is to view all posts (select query)
    elif selection == "2":
        
        def viewPosts():
            viewPosts = run_query("SELECT username, content from blog_post")
            print(viewPosts)
        viewPosts()
    #Choise #3 is to exit the loop
    elif selection == "3":
        exit()
