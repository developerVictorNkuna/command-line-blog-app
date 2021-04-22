#system test is type of test that is going to test through your system

from unittest import  TestCase
from unittest.mock import  patch
from blog import  Blog
from post import  Post
import app

#patch let us patch ,something,like vehicle tire,that has punture to be patched

#patch the print function,install number of helper b4 it



class AppTest(TestCase):
    """this is part of  system """

    def setup(self):
        """ setup is function inside a test case ,the setup   will run before each test """
        blog = Blog("Test","Test Author")
        app.blogs = {"Test":blog}

    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            with patch("app.ask_create_blog") as mocked_ask_create_blog:

                app.menu()
                # self.assertIsNotNone(app.blogs["Test Create Blog"])

            #with patch("app.ask_create_blog") as mocked_ask_create_blog:

                # mocked_input.side_effect = ('c','Test Create Blog','Test Author','q')
                # app.menu()


                # self.assertIsNotNone(app.blogs["Test Create Blog"])
                mocked_ask_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input',return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        """assuming that print  blogs gets called"""

        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input",return_value="q"):
                app.menu()
                mocked_print_blogs.assert_called()



    def test_print_blogs(self):
        #blog = Blog("Test", "Test Author")
        # we setting up the dictionary equal to blog
        #app.blogs = {"Test": blog}

        # we have created a context manager,whatever the result  builtins.print=mocked_print
        """module.modify.function_to_be_patched"""
        with patch("builtins.print") as mocked_print:
            #blog = app.blogs["Test"]
            # what the result of print is now called mocked_print
            # patch recieves a modules
            app.print_blogs()
            # the above line calls print,from our app,with unit test it allows to seee if the module was called or not
            mocked_print.assert_called_with('-Test by Test Author (1 post)')

            # allows us to test if the blog is created or not

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('Test','Test Author')
            """side_effect are dependencies or  things that...
            change other things in the system environment,such as 
            
            class,file on fs,or values in the database,the piece of code ,
            is doing lot of things,is not pure function(same arg,same output,or return values)
            
            """
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        #blog =  Blog("Test",'Test Author')
        #app.blogs = {"Test":blog}

        with patch('builtins.input',return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs["Test"]
        blog.create_post("Test Post","Test Content")

        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[1])
            #this line above checks/assert that is called witth blog.posts


    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print ='''---Post title---Post content'''
        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)
    def test_ask_create_post(self, blog=None):
        # post = Post('Post title', 'Post content')
        # app.blogs ={"Test":blog}
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('Test','Test Title','Test Content')
            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title,'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content,'Test Content')
            #self.assertEqual(blog.posts[0].title,"Test Title")
            #self.assertEqual(blog.posts[0].content,"Test Content")


