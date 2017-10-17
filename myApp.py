from model.post import Post
from database import Database
from model.blog import Blog
from menu import Menu

Database.initialize()
'''post = Post("nasir","This is a title","This is some content","123")

post.save_to_mongo()
print(post.from_mongo("b10108d4900e4b8ebe125ad9e1320b8d"))
print(post.from_blog(123))'''

'''blog = Blog("Protul","Sample Title","Description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())'''

menu = Menu()

menu.run_menu()