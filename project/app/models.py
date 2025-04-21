from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.core.exceptions import *

class Kind(models.TextChoices):
    Buy = 'b', 'Куплю'
    Sell = 's', 'Продам'
    Change = 'c', 'Обмен'

class Rubric(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/app/rubric/{self.pk}/"
def validate_even(value):
    if value % 2 == 0:
        raise ValidationError(f"Число {value} четное")


class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.max_value = max_value
        self.min_value = min_value

class PolozitValueValidator:
    def __init__(self, value):
        if value >= 0:
            self.value = value

    def __call__(self, value):
        if value <= self.min_value or value >= self.max_value:
            raise ValidationError("Ваша цена вышла за диапазон")
class Bd(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Название", validators=[RegexValidator("^.{4,}$")])
    content = models.TextField(null=True,blank=True, verbose_name="Описание")
    price = models.FloatField(null=True,blank=True, verbose_name="Цена", default="Бесплатно", validators=[MinMaxValueValidator(min_value= 0, max_value= 1000), validate_even])
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def get_absolute_url(self):
        return f"/app/bb/{self.pk}/"
    def save(self, *args, **kwargs):
        if self.title == "Оружие":
            return ValidationError('Оружие запрещено')
        super().save(*args, **kwargs)

    def delete(self,*args, **kwargs):
        if self.title == "Мяч":
            return ValidationError('Нельзя удалить')
        super().save(*args, **kwargs)

    def title_and_price(self):
        if self.price:
            return f"Название: {self.title}, Цена: {self.price}"
        else:
            return f"Название: {self.title}"
    def title_and_content(self):
        if self.content:
            return f"Название: {self.title}, Описание: {self.content}"
        else:
            return f"Название: {self.title}"

    def price_and_published(self):
        if self.price:
            return f"Цена: {self.price}, Дата публикации: {self.published}"
        else:
            return f"Дата публикации: {self.published}"



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

