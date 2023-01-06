from django.contrib.messages import constants as messages
from django.shortcuts import redirect,render
from fyyyapp.models import Contact
#from django.contrib.auth.models import User


# Create your views here.
def saveinfo(request):
    if request.method=='POST':
        FirstName=request.POST['firstname']
        LastName=request.POST['lastname']
        Email=request.POST['email']
        Phone=request.POST['phone']
        add=Contact(FirstName=FirstName,LastName=LastName,Email=Email,Phone=Phone)
        add.save()
    Data=Contact.objects.all()
    return render(request,'index.html',{'Data':Data})
    
def index(request):
    Data=Contact.objects.all()
    return render(request,'index.html',{'Data':Data})

def formupdate(request,id):
    if request.method=="POST":
        add=Contact.objects.get(id=id)
        add.FirstName=request.POST["firstname"]
        add.LastName=request.POST["lastname"]
        add.Email=request.POST["email"]
        add.Phone=request.POST["phone"]
        add.save()
        return redirect('index')
    
def edit(request,id):
    Data=Contact.objects.get(id=id)
    if request.method=='POST':
        messages.success(request,"Saved Changes")
    return render(request,'edit.html',{'Data':Data})
def delete(request,id):
    add=Contact.objects.get(id=id)
    add.delete()
    return redirect('index')
def search(request):
    query=request.GET["query1"]
    Data=Contact.objects.filter(Phone__icontains=query)
    params={'Data':Data}
    return render(request,'search.html',params)
