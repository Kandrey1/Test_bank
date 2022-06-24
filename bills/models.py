from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Клиент')

    class Meta:
        verbose_name = "Клиент"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Organization(models.Model):
    client_name = models.CharField(max_length=250, verbose_name='Клиент')
    organization = models.CharField(max_length=250, verbose_name='Организация')

    class Meta:
        unique_together = ('organization', 'client_name')
        verbose_name = "Организации"
        ordering = ["id"]

    def __str__(self):
        return "Организация = " + str(self.organization) + " \t Клиент = " + str(self.client_name)


class Bills(models.Model):
    organization_client = models.CharField(max_length=250, verbose_name='Организация')
    account_number = models.IntegerField(verbose_name='Номер счета')
    balance = models.IntegerField(verbose_name='Баланс')
    date = models.CharField(max_length=250, verbose_name='Дата')                 # !!!!!!!!!!!!!!!!!!!!!!!!!!

    class Meta:
        unique_together = ('organization_client', 'account_number')
        verbose_name = "Счета"
        ordering = ["id"]

    def __str__(self):
        return "Организация = " + str(self.organization_client) + "\t № Счета = " + str(self.account_number) + "\t Баланс = " + str(self.balance)
