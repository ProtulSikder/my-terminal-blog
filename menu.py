from model.blog import Blog
from database import Database

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name:")
        self.user_blog = None

        if self._user_has_account():
            print("Welcome back {}".format(self.user))

        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.findOne('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title:")
        description = input("Enter blog description:")
        blog = Blog(self.user,title,description)

        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read or write(W/R):")

        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for visiting our blog.")

    def _list_blogs(self):
        blogs = Database.find('blogs',{})

        for blog in blogs:
            print("ID:{}, Title:{}, Author: {}".format(blog['id'],blog['title'],blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the id of the blog you'd like to read:")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()

        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['date'],post['title'],post['content']))