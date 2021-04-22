from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        """this blog will have a posts in it"""
        #this NOT A UNIT TEST CODE,INTEGRATION TEST
        b =Blog("Test","Test Author")
        b.create_post("Test Post","Test Content")

        self.assertEqual(len(b.posts),1)
        #test that the len(post) is one ,
        # it test everything you have to test


        self.assertEqual(b.posts[0].title,"Test Post")
        #test the first post in the blog is Test Post
        self.assertEqual(b.posts[0].content,"Test Content")




    def test_json_no_posts(self):
        b = Blog("Test","Test Author")
        expected = {"title":"Test","author":"Test Author","posts":[]}
        # b.create_post("Test Post", "Test Content")

        self.assertDictEqual(expected,b.json())





        def test_json(self):
            b =Blog("Test","Test Author")
            b.create_post("Test Post","Test Content")

            expected = {
                "title":"Test",
                "author":"Test Author",
                "posts": [
                    {
                        "title":"Test Post",
                        "content":"Test Content"
                    }
                ]
            }
        self.assertDictEqual(expected,b.json())