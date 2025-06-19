from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import LostItem, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView 
from .forms import newFoundForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user() #already authenticated, if return none it will execute the next else block
            login(request, user)
            return redirect("/")
        
    else:
        form = AuthenticationForm()

    return render(request,"login.html", {"form":form})

@login_required
def home(request):
    lost_items = LostItem.objects.all()
    print(lost_items)
    return render(request, 'home.html', {'lost_items': lost_items})

def logout_view(request):
    logout(request)
    return redirect("/login")

class newfound(FormView):
    template_name = 'newfound.html'
    form_class = newFoundForm
    success_url = '/'

    def form_valid(self, form):  #automatically called when form is submitted
        userProfile, created = UserProfile.objects.get_or_create(user=self.request.user)
        lostItem = LostItem(
            item_name = form.cleaned_data['item_name'],
            item_picture = form.cleaned_data['item_picture'],
            item_description = form.cleaned_data['item_description'],
            item_founder = userProfile,
            contactEmail = form.cleaned_data['contactEmail'],
            found_at = form.cleaned_data['found_at'],
            found_datetime = form.cleaned_data['found_datetime'],
            
        )
        lostItem.save()
        return super().form_valid(form)

    

