from django.db import models


class Reference(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    class Meta:
        abstract = True


class Document(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    number = models.PositiveIntegerField()
    deleted = models.BooleanField()

    class Meta:
        abstract = True


class Account(Reference):
    pass

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"

    def __str__(self):
        return self.name


class MoneyIncome(Document):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    sum = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Поступление денег"
        verbose_name_plural = "Поступления денег"

    def __str__(self):
        return f"Поступление денег {self.number} от {self.date:%d.%m.%Y}"
