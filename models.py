from django.contrib.admin.widgets import AdminTimeWidget
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    author_ID = models.CharField(max_length=100)
    author_name = models.CharField(max_length=250)

    class Meta:
        ordering = ('author_ID',)

# double underscorll means a string of representation of the object
    def __str__(self):
        return '%s, %s' % (self.author_ID, self.author_name)
         #return self.author_ID + '-' + self.author_name


class Publisher(models.Model):
    PublisherID=models.CharField(max_length=20,default='0')
    Publisher_Name=models.CharField(max_length=40)
    Publisher_Address=models.CharField(max_length=150)

    class Meta:
        ordering = ('PublisherID',)
    def __str__(self):
        return self.PublisherID + '-' + self.Publisher_Name + '-'+self.Publisher_Address

class Document(models.Model):
    DocID=models.CharField(max_length=20,default='0')
    Title=models.CharField(max_length=255)
    Publication_Date=models.CharField(max_length=20)
    PublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    class Meta:
        ordering = ('DocID',)
    def __str__(self):
        return self.DocID + '-' + self.Title+'-' + self.Publication_Date



class Branch(models.Model):
    LibID=models.CharField(max_length=20,default='0')
    Branch_Name = models.CharField(max_length=100)
    Branch_Location=models.CharField(max_length=100)
    class Meta:
        ordering = ('LibID',)
    def __str__(self):
        return self.LibID + '-' + self.Branch_Name  + '-'+self.Branch_Location

class Copy(models.Model):
    CopyNum = models.CharField(max_length=10,default='0')
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    LidID = models.ForeignKey(Branch, on_delete=models.CASCADE)

    Position = models.CharField(max_length=10)

    class Meta:
        ordering = ('CopyNum',)
    def __str__(self):
        return self.CopyNum+'-'+self.Position

class Book(models.Model):

    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=14)
    def __str__(self):
        return self.ISBN


    class Meta:
        ordering = ('ISBN',)


class Reader(models.Model):
    ReaderID = models.CharField(max_length=10)
    Type=models.CharField(max_length=10)
    Reader_Name=models.CharField(max_length=70)
    PhoneNum=models.CharField(max_length=15)
    Address=models.CharField(max_length=150)

    #user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #    on_delete=models.CASCADE,)

    def __str__(self):
        return self.ReaderID + '-' + self.Type+ '-' + self.Reader_Name+ '-' + self.PhoneNum+ '-' + self.Address
    class Meta:
        ordering = ('ReaderID',)

class BorrowTransaction(models.Model):
    BorNumber=models.CharField(max_length=20,default='0')
    Borrow_Date_Time=models.CharField(max_length=30)
    Return_Date_Time =models.CharField(max_length=30)
    ReaderID = models.ForeignKey(Reader, on_delete=models.CASCADE)
    CopyNum = models.ForeignKey(Copy, on_delete=models.CASCADE)

    def __str__(self):
        return self.BorNumber + '-' + self.Borrow_Date_Time+ '-' + self.Return_Date_Time
    class Meta:
        ordering = ('BorNumber',)


class Borrow(models.Model):
    copyNum = models.ForeignKey(Copy, on_delete=models.CASCADE)
    BorNumber = models.OneToOneField(BorrowTransaction, on_delete=models.CASCADE)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    LibID = models.ForeignKey(Branch, on_delete=models.CASCADE)
    ReaderID = models.ForeignKey(Reader, on_delete=models.CASCADE)

class Chief_Editor(models.Model):


    EditorID = models.CharField(max_length=20, default='0')
    Editor_Name = models.CharField(max_length=500)

    class Meta:
        ordering = ('EditorID',)

    def __str__(self):
        return self.EditorID + '-' + self.Editor_Name

class Reservation(models.Model):
    ResNumber=models.CharField(max_length=100,default='0')
    Reservation_Date_Time=models.CharField(max_length=40)
    ReaderID= models.ForeignKey(Reader, on_delete=models.CASCADE)
    copyNum = models.ForeignKey(Copy, on_delete=models.CASCADE)
    def __str__(self):
        return self.ResNumber+'-'+self.Reservation_Date_Time



class Proceeding(models.Model):
    Conference_date = models.CharField(max_length=30)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    Conference_Location = models.CharField(max_length=100)
    Conference_Chair = models.CharField(max_length=30)

    class Meta:
        ordering = ('Conference_date',)

    def __str__(self):
        return self.Conference_date+'-'+self.Conference_Location

class Journal_Issue(models.Model):
    Issue_Number=models.CharField(max_length=10)
    Scope=models.CharField(max_length=20)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.Issue_Number+'-'+self.Scope
    class Meta:
        ordering = ('Issue_Number',)

class Write(models.Model):
    AutherID=models.ForeignKey(Author, on_delete=models.CASCADE)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)


class Descriptor(models.Model):
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    Descriptor=models.CharField(max_length=100)

    def __str__(self):
        return self.Descriptor
    class Meta:
        ordering = ('Descriptor',)
class Issue_Editor(models.Model):
    Issue_Number = models.ForeignKey(Journal_Issue, on_delete=models.CASCADE)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    Editor_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.Editor_Name
    class Meta:
        ordering = ('Editor_Name',)
class Has(models.Model):
    #CopyNum = models.ForeignKey(Copy, on_delete=models.CASCADE)
    LidID = models.ForeignKey(Branch, on_delete=models.CASCADE)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)


class Reserve(models.Model):
    ReaderID = models.ForeignKey(Reader, on_delete=models.CASCADE)
    ResNumber = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    copyNum = models.ForeignKey(Copy, on_delete=models.CASCADE)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    LidID = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Journal_Volume(models.Model):
    Volume_Num = models.CharField(max_length=10)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    EditorID = models.ForeignKey(Chief_Editor, on_delete=models.CASCADE)
    def __str__(self):
        return self.Volume_Num

    class Meta:
        ordering = ('Volume_Num',)



'''class Journal_Volume1(models.Model):
    Volume_Num = models.CharField(max_length=10)
    DocID = models.ForeignKey(Document, on_delete=models.CASCADE)
    EditorID = models.ForeignKey(Chief_Editor, on_delete=models.CASCADE)'''

