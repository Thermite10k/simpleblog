from django.shortcuts import render, get_object_or_404
from .models import Post, branch, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # List a queryset return all, query set in to data base but brings detailes of a single data
from .forms import PostForm, UpdateForm, AddCategoryForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	paginate_by = 4
	model = Post
	template_name = 'home.html'
	#ordering = ['-id']
	ordering = ['-post_date']


	def get_context_data(self, *args, **kwargs):
		num = 0
		for p in Post.objects.all():
			num = num + 1
		num = int(num/4)	
		pgz = "a" * num
		cat_menu = branch.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs )
		context["cat_menu"] = cat_menu
		context["pgz"] = pgz
		return context


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self,*args, **kwargs):
		cat_menu = branch.objects.all()
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True
		total_likes = stuff.total_likes()  #the function
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs )
		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = ('title', 'author', 'body', 'title_tag')


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = "__all__"


	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		form.instance.name = self.request.user.username
		form.instance.return_id = self.kwargs['pk']
		return super().form_valid(form)



class UpdatePostView(UpdateView):
	model = Post
	form_class = UpdateForm
	template_name = 'update_post.html'
	#fields = ('title', 'body', 'title_tag')


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = branch
	form_class = AddCategoryForm
	template_name = 'add_category.html'
	def get_context_data(self, *args, **kwargs):
		cat_menu = branch.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs )
		context["cat_menu"] = cat_menu
		return context

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category__name__contains=cats.replace('-',' '))
	cat_menu = branch.objects.all()
	#context = super(CategoryView, self).get_context_data(*args, **kwargs )
	#context["cat_menu"] = cat_menu

	return render(request, 'categories.html', {
		'cats': cats.title().replace('-',' '),
		'category_posts': category_posts,
		'cat_menu': cat_menu
		})
	



def CategoryListView(request):
	cat_menu_list = branch.objects.all()


	return render(request, 'category_list.html', {

		'cat_menu_list': cat_menu_list
		})
	
def LikeView(request, pk):

		post = get_object_or_404(Post, id=request.POST.get("post_id"))
		liked = False
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
			liked = False
		else:	
			post.likes.add(request.user)
			liked = True
		return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))