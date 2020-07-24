from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator



def allBlogs(req):
	objects = Blog.objects.all()
	# objects = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	p = Paginator(objects,4)
	
	page_number = req.GET.get('page')
	page_obj = p.get_page(page_number)
	

	return render(req,'allBlogs.html',{'page_obj':page_obj})