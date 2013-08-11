from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')
	
def about(request):
    return render_to_response('index.html')
	
def blog(request):
	return render_to_response('blog.html', {'posts' : entries})
	
def projects(request):
	return render_to_response('projects.html')
	
def resume(request):
	return render_to_response('resume.html')
