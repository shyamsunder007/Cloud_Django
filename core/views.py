from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SignUpForm,BookForm
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
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user  # use your own profile here
            #print (request.FILES)
            #handle_uploaded_file(request.FILES['pdf'])
            candidate.save()
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'upload_book.html', {
        'form': form
    })
