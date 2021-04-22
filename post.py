class Post:
    def __init__(self, title, content):
        """
        __init__= is a constructor function/method  that
        ... initialize the object Post
        to define attributes/properties of the object
        """

        self.title = title
        self.content = content


    def json(self):
        """this dic represent our post stored in our db"""
        return {
            "title": self.title,
            "content": self.content,
            "posts": [post.json() for post in self.posts ]

        }

# #create a test for the dictionary json
#
#
# def json_test(self):
#     p = Post("Test","Test Content")
#     expected ={"title":"Test","content":"Test Content"}
#
#
#     self.assertDictEqual(expected,p.json())