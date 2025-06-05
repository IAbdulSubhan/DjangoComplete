from django.shortcuts import render
from books.models import Book
def home(request):
    return render(request, 'base.html')

def books(request):
    books = Book.objects.all()
    print(books)
    context={"books" : books}
    return render(request, 'books/books.html', context)


def newbook(request):
    context = { }
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        price = request.POST.get("price")
        book_image = request.FILES.get("book_image")

        Book.objects.create(
            name = name,
            author = author,
            price = price,
            book_image = book_image
        )

        return redirect("books")

    return render(request, 'books/newbook.html', context)