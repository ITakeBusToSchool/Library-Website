from django.contrib import admin


from .models import Author
from .models import Publisher
from .models import Document
from .models import Branch
from .models import Copy
from .models import Book
from .models import Reader
from .models import BorrowTransaction
from .models import Borrow
from .models import Chief_Editor
from .models import Reservation
from .models import Proceeding
from .models import Journal_Issue
from .models import Write
from .models import Descriptor
from .models import Issue_Editor
#from .models import Has
from .models import Reserve
from .models import Journal_Volume

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Document)
admin.site.register(Branch)
admin.site.register(Copy)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(BorrowTransaction)
admin.site.register(Borrow)
admin.site.register(Chief_Editor)
admin.site.register(Reservation)
admin.site.register(Proceeding)
admin.site.register(Journal_Issue)
admin.site.register(Write)
admin.site.register(Descriptor)
admin.site.register(Issue_Editor)
#admin.site.register(Has)
admin.site.register(Reserve)
#admin.site.register(Journal_Volume)
