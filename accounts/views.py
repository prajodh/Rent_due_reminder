from typing import TypeAlias
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from .models import rent_rem


# Create your views here.

# def signup(request):
#     return render (request,'signup.html')


def signup(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=Username).exists():
                messages.error(request,'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already registered')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = Username,password = password1,first_name=Firstname,email=email,last_name=Lastname)
                user.save();
                return redirect ('login')
        
        else:
            messages.error(request,"passwords doesn't match!!")
            return redirect('signup')
     
    return render (request,'signup.html')          
       

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('logged in')
            tlist = rent_rem.objects.all()
            return render(request,'tenents.html',{'tlist':tlist,'username':username})
        else:
            messages.error(request,"invalid credentials")
            return redirect('login')    
    return render(request,"login.html")

def generic(request):
    tlist = rent_rem()
    if request.method == 'POST':
        tlist = rent_rem()
        tlist.username = request.POST['username']
        username = request.POST['username']
        tlist.name = request.POST['name']
        tlist.age = request.POST['age']
        tlist.dob = request.POST['dob']
        tlist.rent_amount = request.POST['rent_amount']
        tlist.due_date = request.POST['due_date']
        tlist.tenent_email = request.POST['tenent_email']
        tlist.tenent_phone = request.POST['tenent_phone']
        tphone = request.POST['tenent_phone']
        tlist.tmessage = request.POST['tmessage']
        if (len(tphone) > 10):
            messages.error(request,"Enter a valid phone number")
            return redirect ("generic")
        tlist.save();
        tlist = rent_rem.objects.all()
        
        return render (request,'tenents.html',{'username':username,'tlist':tlist})
        # for i in tlist:
        #     if i.username == username:
        #         print(i.username)
                
        #         return render (request,'tenents.html',{'username':username,'tlist':tlist})            
            # if i.username != username:
            #     print(i.username)
            #     messages.error(request,"Enter a valid username!!")
            #     return redirect('generic')
    return render(request,'generic.html')       

def tenents(request):
    if request.method == "POST":
        username = request.POST['username']
        return render(request,"tenents.html",{'username':username})   
        
         

    
    return render(request,"tenents.html")


