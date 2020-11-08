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





# Create your models here.
class HouseOfRepsBills(models.Model):
    title_of_bill = models.TextField(db_column='title_of_bill', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='date', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True, null=True)  # Field name made lowercase.
    chamber = models.TextField(db_column='chamber', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='status', blank=True, null=True)  # Field name made lowercase.
    stage_of_bill = models.TextField(db_column='stage_of_bill', blank=True, null=True)  # Field name made lowercase.
    portfolio = models.TextField(db_column='portfolio', blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='summary', blank=True, null=True)  # Field name made lowercase.
    link_to_bill = models.TextField(db_column='link_to_bill', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'hrepsbills'










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
