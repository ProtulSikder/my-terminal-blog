from database import Database
import uuid, datetime


class Post(object):
    def __init__(self, author, title, content, blog_id, date=datetime.datetime.utcnow(), id=None):
        self.author = author
        self.title = title
        self.content = content
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'blog_id': self.blog_id,
            'id': self.id,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.findOne('posts', {'id': id})
        return cls(post_data['author'],
                   post_data['title'],
                   post_data['content'],
                   post_data['blog_id'],
                   post_data['date'],
                   post_data['id'])

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find('posts', {'blog_id': blog_id})]
