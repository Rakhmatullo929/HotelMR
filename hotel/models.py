from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL, CASCADE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)
    created_by = models.ForeignKey(User, SET_NULL, null=True, blank=True, related_name='created_%(model_name)ss')
    updated_by = models.ForeignKey(User, SET_NULL, null=True, blank=True, related_name='updated_%(model_name)ss')

    class Meta:
        abstract = True
        ordering = ('id',)


class Type(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Room(BaseModel):
    type = models.ForeignKey(Type, CASCADE, 'type')
    amount_people = models.CharField(max_length=50)
    amount_bathroom = models.CharField(max_length=50)
    amount_bedroom = models.CharField(max_length=50)
    double_or_triple = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    photo_room = models.ImageField()
    photo_bedroom = models.ImageField()
    photo_bathroom = models.ImageField()

    def __str__(self):
        return f'{self.type}{self.amount_people}'


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Perfect'),
]


class Review(models.Model):
    user = models.ForeignKey(User, CASCADE)
    room = models.ForeignKey(Room, CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return self.user.username
