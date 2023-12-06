from user import User
from post import Post


app_user_one = User("fgkhan@hotmail.com", "Nana", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("manager")
app_user_one.get_user_info()


new_postt = Post("On a secret message", app_user_one.name)
new_postt.get_post_info()
