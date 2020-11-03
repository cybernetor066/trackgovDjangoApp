from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    firstname = models.CharField(db_column='FIRSTNAME', max_length=200)
    lastname = models.CharField(db_column='LASTNAME', max_length=200)
    useremail = models.EmailField(unique=True, db_column='USEREMAIL', max_length=200)
    username = models.CharField(primary_key=True, db_column='USERNAME', max_length=200)
    password = models.CharField(db_column='PASSWORD', max_length=200)
    datereg = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'registered_users'



# Remove the firstname and lastname from the models







# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#     birth_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']

# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']
