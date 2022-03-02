from django.db import models


class City(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('name', max_length=100, blank=False)
    description = models.TextField('description', blank=False)
    places = models.TextField('places_list', blank=False)
    photo = models.ImageField(upload_to='cities', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Guide(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('name', max_length=50, blank=False)
    surname = models.CharField('name', max_length=50, blank=False)
    birthdate = models.DateField('birthdate', blank=False)
    description = models.TextField('description', blank=False)
    photo = models.ImageField(upload_to='guides', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экскурсовод'
        verbose_name_plural = 'Экскурсоводы'


class Excursion(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField('name', max_length=100, blank=False)
    description = models.TextField('description', blank=False)
    date = models.DateField('date', blank=False)
    guide = models.ForeignKey(Guide, on_delete=models.RESTRICT)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'
