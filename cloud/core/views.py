from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, CreateView
from .forms import SignUpForm,BookForm
from django.contrib.auth import login, authenticate
from .models import Book
# Create your views here.
from django.contrib import messages
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
            return redirect('login')
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
            print (request.FILES['file'])
            #handle_uploaded_file(request.FILES['pdf'])
            candidate.name=str("asd")+str(request.FILES['file'])
            candidate.save()
            form.save()
            print (candidate.name)
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'upload_book.html', {
        'form': form
    })

def book_list(request):
    books = Book.objects.filter(user=request.user)
    for book in books:
        x=book.file.url
        book.file=x.split("/")[-1]
    return render(request, 'book_list.html', {
        'books': books,
    })
    
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)

        book.delete()

    return redirect('book_list')


def share_book(request, file_key):
    return redirect('/media/books/pdfs/'+file_key)