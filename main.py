import user
import post

app_user_one = user.User("fgkhan@hotmail.com", "Nana", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("manager")
app_user_one.get_user_info()

posttt = post.Post("test", app_user_one.name)
posttt.get_post_info()