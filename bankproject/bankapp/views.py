from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.shortcuts import render, redirect, get_object_or_404

from .form import PersonCreationForm
from .models import Person,Branch

# Create your views here.
def home(request):
    return render(request,'index.html')
# Login
def login(request):
    if request.method == "POST":
        username = request.POST['login_txt']
        password = request.POST['password_txt']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('button')
        else:
            messages.info(request, "invalid value")
            return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method == "POST":
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
               messages.info(request,"username Taken")
               return redirect('register')
            elif  User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def button(request):
    return render(request,'button.html')

# form code



def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'application accepted')
            return redirect('form')
        

    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})



