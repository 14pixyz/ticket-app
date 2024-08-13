from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone


class Company(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    tel = models.CharField(max_length=15)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(verbose_name='メールアドレス', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    company =  models.ForeignKey(Company, on_delete=models.PROTECT)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    max_seat = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    opening_time = models.TimeField(blank=False, null=False)
    closing_time = models.TimeField(blank=False, null=False)
    image = models.ImageField(null=True, default='noImage.png')
    web_site = models.URLField(null=True, blank=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    overview = models.TextField(blank=True, null=True) #公演概要
    company =  models.ForeignKey(Company, on_delete=models.PROTECT)


class Ticket(models.Model):
    seat_type = (
        ('free', '自由席'),
        ('reserved', '指定席'),
    )

    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    price = models.IntegerField(blank=False, null=False)
    type = models.CharField(max_length=10, choices=seat_type)
    area = models.CharField(max_length=150, blank=True, null=True)
    seat_number = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_reserved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)


class Customer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(verbose_name='メールアドレス')


class Reservation(models.Model):
    payment_choice = (
        ('bank', '銀行振込'),
        ('credit', 'クレジットカード決済'),
    )

    id = models.AutoField(primary_key=True, unique=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    people_num = models.IntegerField(blank=False, null=False)
    payment = models.CharField(max_length=20, choices=payment_choice)
    comment = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)