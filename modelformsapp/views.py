from django.shortcuts import render,redirect
from modelformsapp.forms import projectform
from modelformsapp.models import project
# Create your views here.
def index(request):
    return render(request,'modelformsapp/index.html')
def listprojects(request):
    projects = project.objects.all()
    return render(request,'modelformsapp/listprojects.html',{'projects':projects})
def addproject(request):
    if request.method=="POST":
        form=projectform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = projectform()
    return render(request,'modelformsapp/addproject.html',{'form':form})
def test(request):
    return render(request, 'test.html')

        
