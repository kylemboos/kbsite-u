from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')
	
def about(request):
    return render_to_response('index.html')
	
def blog(request):
	return render_to_response('blog.html')
	
def post(request):
	path = request.path_info
	pathwords = path.split('/')
	for word in pathwords:
		if "post" in word:
			return render_to_response(word)
	
def projects(request):
	return render_to_response('projects.html')
	
def resume(request):
	return render_to_response('resume.html')


def mabout(request):
		return render_to_response('m_index.html')
		
def mprojects(request):
		return render_to_response('m_projects.html')
		
def mblog(request):
		return render_to_response('m_blog.html')
		
def mpost(request):
	path = request.path_info
	pathwords = path.split('/')
	for word in pathwords:
		if "post" in word:
			return render_to_response(word)
