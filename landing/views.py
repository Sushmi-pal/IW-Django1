from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogView,AuthorName
from .forms import BlogViewForm
class HomePageView(TemplateView):
    template_name = 'landing/home.html'

def blogpage(request):
    data=BlogView.objects.all()
    return render(request,'landing/blog.html',{'data':data})

def authdesc(request,author_id):
    print(author_id)
    desc=AuthorName.objects.get(id=author_id)
    desc=get_object_or_404(AuthorName,id=author_id)
    return render(request,'landing/authdescription.html',{'desc':desc})

def detailblog(request,id):
    print(id)
    # de=BlogView.objects.get(id=id)
    de=get_object_or_404(BlogView,id=id)
    return render(request,'landing/detail.html',{'de':de})

def Create(request):
    if request.method=='POST':
        form=BlogViewForm(request.POST)
        if form.is_valid():
            print('Form is valid',form.cleaned_data)
            form.save()
            return redirect('/landing/blog/')
        else:
            print('Invalid')
    else:
        form=BlogViewForm()
    return render(request,'landing/create.html',{'form':form})

def BlogTry(request):
    return render(request,'landing/blogtry.html')
