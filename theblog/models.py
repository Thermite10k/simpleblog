from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.



class branch(models.Model):
	name = models.CharField(max_length=255)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))	
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, blank=True,null=True)
	facebook_url = models.CharField(max_length=255, blank=True,null=True)
	instagram_url = models.CharField(max_length=255, blank=True,null=True)



	def get_absolute_url(self):
		return reverse('show_profile_page', args=(str(self.id)))
		#return reverse('home')

	def __str__(self):
		return str(self.user)

class Post(models.Model):
	title = models.CharField(max_length=255)
	header_image = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	snippet = models.CharField( max_length=255)
	#body = models.TextField()
	title_tag = models.CharField(max_length=255)
	post_date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(branch, blank=True, null=True, on_delete=models.CASCADE)
	category2 = models.CharField( max_length=255, default="code")
	likes = models.ManyToManyField(User, related_name='bolg_posts')

	def total_likes(self):

		return self.likes.count()

	def __str__(self):
		return self.title + " | " + str(self.author) # what will be returned to the admin page

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)))	
		return reverse('home')


class Comment(models.Model): 
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	data_added = models.DateField(auto_now_add=True)
	return_id = models.CharField(max_length=500, default=0)
	def __str__(self):
		return '%s - %s' %(self.post.title, self.name)
	def get_absolute_url(self):
		return reverse('article-detail', args=(str(self.return_id)))	
