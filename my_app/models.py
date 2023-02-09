# models = Database
from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # Trick, dass wir das ausgeschriebene Wort angezeigt bekommen statt "ObjectId(1)" oder so
    def __str__(self):
        return '{}'.format(self.search)

    # Trick, dass "Searches" angezeigt wird statt "Searchs"
    class Meta:
        verbose_name_plural = 'Searches'