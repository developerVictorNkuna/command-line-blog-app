import unittest
from unittest import TestCase

# from ....blog_app.post import Post
from post import Post


# from blog_app.post import  Post
class PostTest(TestCase):
    """each test suite is a class,it always 
    has to inherit from PostTest(unittest.TestCase)"""



    def test_create_post(self):
        """
        if the test succeeds will pass ,else otherwise fails

        """

        p = Post("Test", "Test Content")  # Post(title,Content)
        # we can use tesCaseAPI=self.assertEqual("title","title")
        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)
        # if one change the object post,init method the test will fail



    # create a test for the dictionary json created in the post

    def test_json(self):
        p = Post("Test", "Test Content")
        expected = {"title": "Test", "content": "Test Content"}

        self.assertDictEqual(expected, p.json())

if __name__ == "__main__":
    print("Executed successfully")
    unittest.main()
