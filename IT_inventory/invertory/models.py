from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Statuses(models.Model):
    title = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.title


class Nomenclature(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.ForeignKey('Statuses', on_delete=models.CASCADE, null=True)
    place = models.ForeignKey('Places', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Employees(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey('Places', on_delete=models.CASCADE, null=True)
    position = models.ForeignKey('Positions', on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(blank=True, null=True)
    home_address = models.CharField(max_length=150, blank=True, null=True)
    # fixing_date = models.DateTimeField()
    # nomenclature = models.ForeignKey('Nomenclature', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

# class Docs(models.Model):
#     doc = models.ForeignKey('Docs_type', on_delete=models.PROTECT, null=True)
#     # doc_number = models.IntegerField()
#     doc_date = models.DateTimeField(auto_now_add=True)



class Registry(models.Model):
    document = models.ForeignKey('Docs_type', on_delete=models.CASCADE, null=True)
    nomenclature = models.ForeignKey('Nomenclature', on_delete=models.CASCADE, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, null=True)
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.nomenclature


class Departments(models.Model):
    title = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.title



class Positions(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Docs_type(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# class Amortization(models.Model):
#     book_value = models.DecimalField(max_digits=15, decimal_places=2)
#     lifetime = models.IntegerField()
#     nomenclature = models.OneToOneField('Nomenclature', on_delete=models.CASCADE, null=True)


class Nomenclature_Report(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.ForeignKey('Statuses', on_delete=models.CASCADE, null=True)
    place = models.ForeignKey('Places', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title