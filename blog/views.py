from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.context_processors import csrf
from django.template.loader import render_to_string

from blog.models import Blog 
# Create your views here.

BLOGS_NUM_PAGES = 10

def bloghome(request):
	all_blogs = Blog.get_blogs()
	paginator = Paginator(all_blogs, BLOGS_NUM_PAGES)
	blogs = paginator.page(1)
	from_blog = -1
	if blogs:
		from_blog = blogs[0].id


	return render(request, 'blog/blog.html', {
		'blogs': blogs, 
		'from_blog': from_blog,
		'page': 1,
		})

def createBlog(request):
	
	last_blog = request.POST.get('last_blog')
	user = request.user
	csrf_token = (csrf(request)['csrf_token'])
	blog = Blog()
	blog.user = user

	title = request.POST['title']
	blog.title = title
	content = request.POST['content']
	content = content.strip()

	if len(content):
		blog.content = content[:255]
	blog.save()
	
	html = _html_feeds(last_blog, user, csrf_token)
	import pdb; pdb.set_trace()
	return HttpResponse(html)

    
def remove(request):
	try:

		blog_id = request.POST.get('blog')
		blog = Blog.objects.get(pk=blog_id)
		blog.delete()
		#import pdb; pdb.set_trace()
		return HttpResponse()

	except Exception:
		return HttpResponseBadRequest()
        


def _html_feeds(last_blog, user, csrf_token, blog_source='all'):

    blogs = Blog.get_blog_after(last_blog)
    import pdb; pdb.set_trace()
    if blog_source != 'all':
        blogs = blogs.filter(user__id=blog_source)
    html = ''
    for blog in blogs:
        html = '{0}{1}'.format(html,
                               render_to_string('blog/blog_item.html',
                                                {
                                                    'blog': blog,
                                                    'user': user,
                                                    'csrf_token': csrf_token
                                                    }))