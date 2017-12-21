from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#
from django.http import HttpResponse

from .models import Author
from .models import Publisher
from .models import Document
from .models import Book
from .models import Copy
from .models import Branch
from .models import Journal_Issue
from .models import Issue_Editor
from django.views import generic
from .models import Reader
from .models import Borrow

def index(request):

    templates = 'library/index.html'
    num_authors = Author.objects.all().count() ;
    num_Publisher = Publisher.objects.all().count();
    num_Doc = Document.objects.all().count();
    num_Book = Book.objects.all().count();
    num_Copy = Copy.objects.all().count();
    num_Branch = Branch.objects.all().count();
    num_Journal_Issue = Journal_Issue.objects.all().count();
    num_Issue_Editor = Issue_Editor.objects.all().count();
    num_visits = request.session.get('num_visits', 0)

    request.session['num_visits'] = num_visits + 1

    return render(
        request , 'library/index.html',
        context={'num_authors' : num_authors, 'num_Publisher' : num_Publisher,
                     'num_Doc' : num_Doc, 'num_Book ' : num_Book ,
                 'num_Issue_Editor': num_Issue_Editor,
                     'num_Copy': num_Copy,'num_Branch': num_Branch,
                 'num_Journal_Issue': num_Journal_Issue,'num_visits' : num_visits}, )


def staff(request):
    return render(request,'library/staff.html')

def reader222(request):
    return render(request,'library/reader222.html')
def reader(request):
    return render(request,'library/reader.html')
def reader2111(request):
    templates = 'library/reader2111.html'

    query = request.GET.get('q')
    print(query)
    results = Document.objects.filter(DocID__icontains=query)
    print(results)
    context = {
        'results': results,
    }
    print(context)
    return render(request, templates, context)


def reader212(request):
    return render(request,'library/reader212.html')


#def reader2111(request):
    #return render(request, 'library/reader2111.html')



#def reader2112(request):
    #return render(request, 'library/reader2112.html')

def reader2112(request):
    return render(request, 'library/reader2121.html')

def UpdateDocument(request):
    query1=request.GET.get('a')
    query2=request.GET.get('b')
    query3=request.GET.get('c')

    insert=Publisher(PublisherID=query1,Publisher_Name=query2,Publisher_Address=query3)
    q=query1
    insert.save()
    #print (insert)
    context={
        'q':q,
    }
    #take=Publisher.objects.filter(PublisherID__icontains=query1)
    return render(request, 'library/UpdateDocument.html', context)

def successfullyinsert(request):
    query1=request.GET.get('a')
    query2=request.GET.get('b')
    query3 = request.GET.get('c')
    insert=Document(DocID=query1,Publication_Date=query2,PublisherID=query3)

    insert.save()
    return render(request, 'library/successfullyinsert.html')
def reader2121(request):
    templates = 'library/reader2121.html'
    query = request.GET.get('q')
    print (query)
    result1 = Reader.objects.filter(ReaderID__icontains=query)

    print (result1)

    context = {
        'result1': result1,

    }
    print (context)
    return render(request, templates, context)



