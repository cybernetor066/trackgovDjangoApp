from django.db import models
from django.urls import reverse

# Create your models here.
class UserRegistration(models.Model):
    useremail = models.EmailField(unique=True, db_column='USEREMAIL', max_length=200)
    username = models.CharField(primary_key=True, db_column='USERNAME', max_length=200)
    password = models.CharField(db_column='PASSWORD', max_length=200)
    datereg = models.DateTimeField()
    class Meta:
        # managed = False
        db_table = 'registered_users'


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

    # def get_absolute_url(self):
    #     return reverse('trackgovApp:dashboardbilldetail', args=[str(self.id)])
    class Meta:
        # managed = False
        db_table = 'hrepsbills'

class HrepsPoliticiansInfo(models.Model):
    name = models.TextField(db_column='name', blank=True, null=True)  # Field name made lowercase.
    elec_div = models.TextField(db_column='elec_div', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    position = models.TextField(db_column='position', blank=True, null=True)  # Field name made lowercase.
    party = models.TextField(db_column='party', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.TextField(db_column='phone_number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address = models.TextField(db_column='email_address', blank=True, null=True)  # Field name made lowercase.
    twitter = models.TextField(db_column='twitter', blank=True, null=True)  # Field name made lowercase.
    facebook = models.TextField(db_column='facebook', blank=True, null=True)  # Field name made lowercase.
    bio_link = models.TextField(db_column='bio_link', blank=True, null=True)  # Field name made lowercase.
    profile_picture = models.TextField(db_column='profile_picture', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        # managed = False
        db_table = 'hrepsMembers'


class HrepsVotePatterns(models.Model):
    title = models.TextField(db_column='title', blank=True, null=True)  # Field name made lowercase.
    div_no = models.TextField(db_column='div_no', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    question = models.TextField(db_column='question', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='date', blank=True, null=True)  # Field name made lowercase.
    outcome = models.TextField(db_column='outcome', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    politician_name = models.TextField(db_column='politician_name', blank=True, null=True)  # Field name made lowercase.
    party = models.TextField(db_column='party', blank=True, null=True)  # Field name made lowercase.
    ayes_vote = models.TextField(db_column='ayes_vote', blank=True, null=True)  # Field name made lowercase.
    noes_vote = models.TextField(db_column='noes_vote', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        # managed = False
        db_table = 'hrepsVotePatterns'













