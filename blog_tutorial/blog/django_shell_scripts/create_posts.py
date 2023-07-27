from blog.models import Post
from django.contrib.auth.models import User

# we can create a post for a author
posts = Post.objects.all().last()
posts.title

user = User.objects.get(id=1)

# we can define the author like this
post = Post(
    title='new_blog_post_1',
    content='here is the content of the blog',
    author=user
)
post.save()

# we can also use the author_id to define the post's author
post = Post(
    title='new_blog_post_2',
    content='here is the content of the blog',
    author_id=user.id
)
post.save()

# We can view all of the users and posts
Post.objects.all()

# we can use the post_set method to create do the above
user = User.objects.get(id=1)

user.post_set.all()

user.post_set.create(
    title='new_blog_3',
    content='Created using the post_set method!'
)

user.post_set.all()

