from blog import Blog

MENU_PROMPT = input(
    "Enter 'c' to create a blog,'1' to list blogs,'r' to read one blog,'p' to create a post or 'q' to quit:\n")
POST_TEMPLATE ='''---{}---{}'''
blogs = dict()  # blog_name :Blog Object
"""this is a dictionary of blogs,mapping blog name:blog_object,we can easily fund dictionary by its name"""


# this create a brand new dictionary blogs ={} ,but is the same as creating set
# this is dictionary maps,blogName,and avail blog
# the app is not the thing that interact with another,is view inside our blog management system
def menu():
    """this menu is UI that will allow the users to create blogs,"""

    # show the user avaible blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit the  blog content system

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != "q":

        if selection == "c":
            ask_create_blog()
        elif selection == 1:
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)


def ask_create_blog():
    """this function ask the user to create a blog i he/she press c"""

    title = input("Enter your blog title:\n")
    author = input("Enter your name:\n")
    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Enter the blog title you want to read:\n")
    print_posts(blogs[title])



def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    """this function creates a new blog"""
    blog_name = input("Enter the  blog title you want to write a post in:\n")
    title = input("Enter your post title:\n")
    content = input("Enter your post content:\n")

    blogs[blog_name].create_post(title, content)


def print_blogs():
    # print the availble blogs
    for key, blog in blogs.items():  # same as (key:blog_name,value:Blog,(blog_name,Blog))
        """for both the key(blog_name),value("blog_object)"""

        # print("I am printing to the console,but i will be patched in the system test")
        # key:blogName and blog:blog
        # we cannot extract the value directly because printed values are in the console
        print("-{}".format(blog))
