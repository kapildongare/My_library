from django.shortcuts import render, HttpResponse, redirect
from .models import Book
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
# FBV---> Function Based Views

@login_required
def welcome_page(request): # this is always a http request
    return render (request, "welcome.html", {"today":datetime.datetime.now()})

@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)
    return render(request, "showbooks.html", {"all_books":books})

@login_required
def show_single_book(request, id):
    try:
        book_obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("This book does not exist")
    return render (request, "book_detail.html", {"book": book_obj})

@login_required
def add_single_book(request):
    if request.method == "POST":
        final_dict = request.POST
        book_name = final_dict.get("nm")
        book_price = final_dict.get("prc")
        book_qty = final_dict.get("qty")
        book_is_pub = final_dict.get("ispub")
   
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
        return redirect("show_books")
    
    elif request.method == "GET":
        return render(request, "addbook.html")

@login_required    
def update_single_book(request, id):
    book_obj = Book.objects.get(id=id)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        final_dict = request.POST
        book_name = final_dict.get("nm")
        book_price = final_dict.get("prc")
        book_qty = final_dict.get("qty")
        book_is_pub = final_dict.get("ispub")
    
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False

        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        return redirect("show_books")


#for hard delete
@login_required
def delete_single_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.delete()  
    return redirect("show_books")


#for soft delete
@login_required
def soft_delete_single_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = False   
    book_obj.save()
    return redirect("show_books")

def form_view(request):
    pass