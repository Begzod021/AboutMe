from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=111, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=111,blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.subject

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'