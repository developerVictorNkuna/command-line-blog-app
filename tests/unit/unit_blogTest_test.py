from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_blog(self):
        b = Blog("Test","Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts) #make sure that the list are the same

    def test_repr(self):
        """the __repr__ method must return our blog number(0 posts)
        """
        b = Blog("Test","Test Author")
        b2 = Blog("My Day","Victor")

        self.assertEqual(b.__repr__(),"Test by Test Author (0 posts)")
        self.assertEqual(b2.__repr__(),"My Day by Victor (0 posts)")


    def test_repr_multiple_posts(self):

        b = Blog("Test","Test Author")
        b.posts = ["test"]

        b2 = Blog("My Day","Victor")
        b2.posts=["test","another"]

        self.assertEqual(b.__repr__(),"Test by Test Author (1 post)")
        self.assertEqual(b2.__repr__(),"My Day by Victor (2 posts)")


