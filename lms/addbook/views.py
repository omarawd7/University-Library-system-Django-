from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import *
from .forms import CreateUserForm
#from .filters import OrderFilter


def demo (request):
    return render(request,'pages/index.html')
#index

def index (request):
    context={
        'books':Book.objects.all(),
    }
    return render(request,'pages/index.html',context)
#about
@login_required(login_url='login')
def about (request):
    return render(request,'pages/about.html')
#register

def Sign_Up (request):
   
    

        form= CreateUserForm()

        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('Log_in')



        context={'form':form}
        return render(request,'pages/Sign_Up.html',context)


  
        
#Log_In
def Log_in (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'username OR password is incorrect')
    context ={}
    return render(request,'pages/Log_in.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

    #username=request.POST.get('username')
    #password=request.POST.get('password')
    #data=log_in(username=username,password=password)
    #data.save()
    
#Search
@login_required(login_url='login')
def Search (request):
       if request.method=="POST":  
           title=request.POST.get('title') 
           author=request.POST.get('author')
           price=request.POST.get('price')
           pages=request.POST.get('pages')
           status=request.POST.get('status')
           bookobj=Book.objects.raw('select * from bo where title="'+title+'" and author="'+author+'" and price="'+price+'"and pages="'+pages+'"and status="'+status+'"')
           context={
              'Book':bookobj,
                   }           
           return render(request,'pages/Search.html',context)
       else:
            bookobj1=Book.objects.raw('select * from bo')
            context1={
              'Book':bookobj1,
                   }             
            return render(request,'pages/Search.html',context1)

 
#Books
@login_required(login_url='login')
def books (request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET :
       title=request.GET['search_name']
       if title:
           search = search.filter(title__icontains=title)
    

    context={
        'books':search,
    }
    return render(request,'pages/books.html',context)
