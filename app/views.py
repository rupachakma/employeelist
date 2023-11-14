from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from app.forms import AddForm, LoginForm,SignupForm, UpdateProfileForm, UserupdateForm
from app.models import Employee

# Create your views here.
def signuppage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request.POST,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("homepage")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

def homepage(request):
    employee = Employee.objects.all()
    return render(request,"home.html",{'employee':employee})

def addpage(request):
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AddForm()
    return render(request,"add.html",{'form':form})

def updatepage(request,id):
    if request.method == "POST":
        employee = Employee.objects.get(id=id)
        form = AddForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        employee = Employee.objects.get(id=id)
        form = AddForm(instance=employee)
    return render(request,"update.html",{'form':form})

def deletepage(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('homepage')


def update_profile(request):
    if request.method == 'POST':
        user_form = UserupdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
          
            return redirect(to='update_profile')
    else:
        user_form = UserupdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
    