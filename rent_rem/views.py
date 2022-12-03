from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth



# Create your views here.

# def index(request):
#     page = None
#     if home == "index":
#         page = 'index.html'  
#     if home == "home":
#         page = 'index.html'  
#     if home == "signup":
#         page = 'Signup.html'      
         
#     return render (request,'index.html')

def indexx(request):
    return render (request,'index.html')




# def generic(request):
#     if request.method == 'POST':
#         your_email = request.POST['your_Email']
#         phone = request.POST['your_Phone Number']
#         name = request.POST['Name']
#         age = request.POST['Age']
#         dob = request.POST['Date Of Birth']
#         rent = request.POST['Rent Amount']
#         due_date = request.POST['Due Date']
#         tenent_email = request.POST['Email']
#         tenent_phn = request.POST['Phone Number']
#         tmessage = request.POST['message']
        


#     return render (request,'generic.html')    