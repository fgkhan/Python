import user
import post


app_user_one = user.User("fgkhan@hotmail.com", "Nana", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("manager")
app_user_one.get_user_info()

new_post = post.Post("teset", app_user_one.name)
new_post.get_post_info()
