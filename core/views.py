from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
