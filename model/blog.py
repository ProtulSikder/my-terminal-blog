import uuid
from model.post import Post
import datetime
from database import Database

class Blog(object):
    def __init__(self,author,title,description,id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title:")
        content = input("Enter post:")
        date = input("Enter date or leave for today(ddmmyyyy):")
        post = Post(self.author,title,content,self.id,datetime.datetime.strptime(date,"%d%m%Y"))

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert('blogs',self.json())

    def json(self):
        return {
            'author' : self.author,
            'title' : self.title,
            'description' : self.description,
            'id' : self.id
        }

    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.findOne('blogs',{'id' :id})

        return cls(blog_data['author'],
                    blog_data['title'],
                    blog_data['description'],
                    blog_data['id'])
