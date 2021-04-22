from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = list()
        # empty list,when we create an empty object to add post

    def __repr__(self):
        """return the values of the blog,this is a wrapper function
        this will represent the blog in our debugging process"""

        return "{} by {} ({} post{})".format(self.title,
                                             self.author, len(self.posts), "s" if len(self.posts) != 1 else "")
    #this means that put s in front of "post() if the length of post is not equal to one

    def create_post(self, title, content):
        #this method receives title,content and create post(s)
        """we not receiving a post object,we have to create it"""
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title":self.title,
            "author":self.author,
            "posts":[post.json() for post in self.posts]
        }
