from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# superuser  login : admin
# psswd : admin


# Create your views here.
def index(request):
    # IF WE WANT THE USER TO ENTER ONLY AFTER LOGIN
   if request.user.is_anonymous:
       return redirect("/login")
   return render(request,"index.html")
    # return HttpResponse("this is homepage")
        # agar strings ko return karna hai to use HttpResponse
        # ideally we should use templates 

# def home(request):
    
#     messages.success(request,"this is a test mssg")
#     return render(request , "index.html")

def menu(request):
    current_user = request.user
    user_name = current_user.username
    # print(user_name)
    context = {'user_name' : user_name}
    return render(request , 'menu.html' , context)
    # return render(request , "menu.html")

def about(request):
    current_user = request.user
    user_name = current_user.username
    context = {'user_name' : user_name}
    return render(request , 'about.html' , context)
    # return render(request , "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        #creating an obj contact
        contact = Contact(name=name,email=email , phone=phone , desc=desc , date = datetime.today())
        contact.save()
        
        messages.success(request , "Your message has been sent")
        
    current_user = request.user
    user_name = current_user.username
    context = {'user_name' : user_name}    
    return render(request,"contact.html",context)

def loginuser(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        user = authenticate(username=username , password = password)
        if user is not None:
            # A backend authenticated the credentials
            login(request , user)
            message = f'Welcome , {username} !'
            messages.success(request , message)
            return redirect('/home')
        
        else:
            return render(request , "login.html")  

    return render(request , "login.html")

# @login_required
# def index(request):
#     current_user = request.user
#     user_name = current_user.username
#     # print(user_name)
#     context = {'user_name' : user_name}
#     return render(request , 'index.html' , context)

# @login_required
def home(request):
    current_user = request.user
    user_name = current_user.username
    # print(user_name)
    context = {'user_name' : user_name}
    return render(request , 'index.html' , context)

def logoutuser(request):
    logout(request)
    return redirect("/")

def handleSignUp(request):
    if request.method == "POST":
        # get the post parameters
        username = request.POST.get('username' )
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #Check for errorneous inputs
        
        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.name = name

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        
        myuser.save()
        messages.success(request , "Your account has been successfully created")
        return render(request , "login.html")
    else:
        # return HttpResponse("404-notfound")
        return render(request , "signup.html")
    


# def styles(request):
#     return render(request , "styles.css")