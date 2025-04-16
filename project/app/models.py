from django.db import models
from django.contrib.auth.models import User

class Kind(models.TextChoices):
    Buy = 'b', 'Куплю'
    Sell = 's', 'Продам'
    Change = 'c', 'Обмен'

class Rubric(models.Model):
    name = models.CharField(max_length=100)
class Bd(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(null=True,blank=True, verbose_name="Описание")
    price = models.FloatField(null=True,blank=True, verbose_name="Цена", default="Бесплатно")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
 #   KINDS=(
 #       ('КУплю-продам',
 #           ('b','Куплю'),
 #           ('s', 'Продам'),),
 #      ('Обмен',
 #       ('c', 'Обменяю'),)
 #   )
 #   kind=models.CharField(max_length=1, default="b", choices=KINDS)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Объявления"
        verbose_name = "Объявления"
        ordering = ["-published"]
#        index_together = ['title', 'published']
#        constraints = (
 #           models.CheckConstraint(
 #           check=models.Q(price__gt=0) & models.Q(price__lte=1000),
 #           name='board_price_check',)
 #       )

class Passport(models.Model):
    country=models.CharField(max_length=100)
    user=models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name=models.CharField(max_length=30)
class Machine(models.Model):
    name=models.CharField(max_length=30)
    spares=models.ManyToManyField(Spare)

#Человек
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


# Ребёнок
class Child(Person):
    school = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name, self.school


# Мороженое
class IceCream(models.Model):
    vkus = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.vkus, self.price



class Kiosk(models.Model):
    location = models.CharField(max_length=200)
    ice_creams = models.ManyToManyField(IceCream)
    def __str__(self):
        return self.location, self.ice_creams