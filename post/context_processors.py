from post.models import Blog

def last_blog(request):#категории товаров

	last_post = Blog.objects.all().first()

	return { 'last_post' : last_post }
