from django.shortcuts import render, redirect
from post.models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404
from post.forms import PostCreateForm

# Create your views here.

def index(request):
	return render(request, 'base.html')

class PostView(View):

	def get(self, request):

		template_name = 'post.html'

		blogs = Blog.objects.all()

		context = {
			'blogs' : blogs,
		}


		return render(request, 'post.html', context)

class PostViewDetail(View):

	template_name = 'view_post_detail.html'

	def get(self, request, *args, **kwargs):
		blog = get_object_or_404(Blog, title__iexact = self.kwargs["title"])

		return render(request, self.template_name, context = {'blog': blog})

class PostCreate(View):
	
	def get(self, request):
		form = PostCreateForm()
		return render(request, 'post_create.html', context = {'form': form})

	def post(self,request):
		
		bound_form = PostCreateForm(request.POST, request.FILES)

		if bound_form.is_valid():
			new_title = bound_form.save()
			return redirect('post_view_url')		
# Я думаю что redirect связан как то с get_absolute_url потому что он находит путь через экземпляр класса 
		
		return render(request, 'post_create.html', context = {'form': bound_form})