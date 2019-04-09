from django.shortcuts import render
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from .forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    # HomeView = when visitor is NOT signed in
    template_name = 'splash.html'

    def get(self, request):
        return render(request, self.template_name)


class MainView(View):
    # MainView = when visitor is signed in
    template_name = 'logged_in_main.html'

    def get(self, request):
        return render(request, self.template_name, {'menu_active_item': 'home'})


class LoginView(View):
    template_name = 'signin.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting.')
            print(request.user)
            logout(request)
            return HttpResponseRedirect('/home')
            # { % url login % }
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # create a new entry in table 'logs'
                login(request, user)
                print('success login')
                # messages.success()
                return HttpResponseRedirect('/home')
            else:
                return HttpResponseRedirect('/register')
        return HttpResponse('This is Login view. POST Request.')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('already logged in. Redirecting.')
            print(request.user)
            return HttpResponseRedirect('')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to RegisterForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email,
                            first_name=firstname, last_name=lastname)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/signin')
        return HttpResponse('This is Register view. POST Request.')


# new_user = User.objects.create_user(username, email, password)
# new_user.is_active = False
# new_user.first_name = first_name
# new_user.last_name = last_name


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request.')
