from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"name: {self.name}, code: {self.code}"

class Address(models.Model):
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    street = models.CharField(max_length=50)

    def __str__(self):
        return f"city: {self.city}, street: {self.street}, postc:{self.postcode}"
    
class Author(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # one to one relation
    address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"f_name:{self.first_name}, l_name:{self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # money ot one relation
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    country=models.ManyToManyField(Country,null=False)
    slug = models.SlugField(
        default="",
        blank=True,
        null=False,
        db_index=True,
    )

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}, Rating: {self.rating},author: {self.author},Rating: {self.rating},slug: {self.slug}"
