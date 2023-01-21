from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages



# Create your views here.
def home(request): 
    context={'name':'harry','course':'python'}
    return render(request,'home.html')
    
    
def about(request):
    return render(request,'about.html')
    
def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        
        print(name,email,phone)
        ins = Contact(name=name,email=email,phone=phone)
        ins.save()

    if request.method =='POST':
        messages.success(request,'You are Successfully Enrolled in our Codehunt courses')\
        
    
    return render(request,'contact.html')

 



   

def project(request):
    return render(request,'project.html')
    


