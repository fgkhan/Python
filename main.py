from user import User
from post import Post


app_user_one = User("fgkhan@hotmail.com", "Nana", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("manager")
app_user_one.get_user_info()

new_post = Post('Test', app_user_one.name)
new_post.get_post_info()
