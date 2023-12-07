class Post:
    def __int__(self, post_message, post_author):
        self.message = post_message
        self.author = post_author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")
