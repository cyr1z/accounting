from django.db import models

# Create your models here.


class Account(models.Model):
    number = models.IntegerField(
        null=False,
        blank=False,
        primary_key=True,
        verbose_name='Рахунок'
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        verbose_name='Назва рахунку'
    )

    class Meta:
        verbose_name = 'Рахунок'
        verbose_name_plural = 'Рахунки'

    def __str__(self):
        return f'{self.number} {self.name}'


class SubAccount(models.Model):
    number = models.IntegerField(
        null=False,
        blank=False,
        primary_key=True,
        verbose_name='Рахунок'
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=40,
        verbose_name='Назва субрахунку'
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Рахунок'

    )

    class Meta:
        verbose_name = 'Субрахунок'
        verbose_name_plural = 'Субрахунки'

    def __str__(self):
        return f'{self.number} {self.name}'


class Department(models.Model):
    title = models.CharField(
        verbose_name='Назва',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Опис',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Відділ'
        verbose_name_plural = 'Відділи'

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(
        verbose_name="Ім'я",
        max_length=255
    )
    second_name = models.CharField(
        verbose_name='Прізвище',
        max_length=255
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=25,
        blank=True,
        null=True
    )
    position = models.CharField(
        verbose_name='Посада',
        max_length=255,
        blank=True,
        null=True
    )
    department = models.ForeignKey(
        Department,
        verbose_name='Відділ',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name='зображення',
        upload_to='employee',
        null=True,
        blank=True
    )

    @property
    def department_title(self):
        return self.department.title

    class Meta:
        verbose_name = 'Співробітника'
        verbose_name_plural = 'Співробітники'

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Responsible(models.Model):
    first_name = models.CharField(
        verbose_name="Ім'я",
        max_length=255
    )
    second_name = models.CharField(
        verbose_name='Прізвище',
        max_length=255
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=25,
        blank=True,
        null=True
    )
    position = models.CharField(
        verbose_name='Посада',
        max_length=255,
        blank=True,
        null=True
    )
    department = models.ForeignKey(
        Department,
        verbose_name='Відділ',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name='зображення',
        upload_to='employee',
        null=True,
        blank=True
    )

    @property
    def department_title(self):
        return self.department.title

    class Meta:
        verbose_name = 'Материально відповідальну особу',
        verbose_name_plural = 'Материально відповідальні особи'

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Card(models.Model):
    number = models.IntegerField(
        verbose_name='Інвентарний номер',
        unique=True,
        null=False,
        blank=False,
        primary_key=True
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        verbose_name='Рахунок',
        null=True,
        blank=True

    )
    sub_account = models.ForeignKey(
        SubAccount,
        on_delete=models.SET_NULL,
        verbose_name='Субрахунок',
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name='Назва',
        null=False,
        blank=False,
        max_length=255
    )

    image = models.ImageField(
        verbose_name='зображення',
        upload_to='cards',
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        verbose_name='Відділ',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    financially_responsible = models.ForeignKey(
        Responsible,
        verbose_name='Материально відповідальний',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        Employee,
        verbose_name='Користувач',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    manufacture_date = models.DateField(
        verbose_name='дата випуску',
    )
    acceptance_date = models.DateField(
        verbose_name='дата вводу до експлуатації',
    )

    count = models.IntegerField(
        verbose_name='Кількість',
        null=False,
        blank=False,
        default=1
    )

    start_price = models.FloatField(
        verbose_name='Первісна вартість грн.'
    )

    depreciation = models.FloatField(
        verbose_name='Знос, грн',
    )

    broken = models.BooleanField(
        default=False,
        verbose_name='Зламано чи застаріло',
    )
    cancel = models.BooleanField(
        default=False,
        verbose_name='Списано',
    )
    filed_for_cancellation = models.BooleanField(
        default=False,
        verbose_name='Подано на списання',
    )
    utilize = models.BooleanField(
        default=False,
        verbose_name='Утилізовано',
    )
    filed_for_utilize = models.BooleanField(
        default=False,
        verbose_name='Подано на утилізацію',
    )

    description = models.TextField(
        verbose_name='Опис',
        null=True,
        blank=True,
    )
    @property
    def responsible_name(self):
        if self.financially_responsible.first_name:
            return ' '.join((self.financially_responsible.first_name, self.financially_responsible.second_name))
        else:
            return None

    @property
    def residual_value(self):
        return round(self.start_price - self.depreciation, 2) if (self.start_price - self.depreciation) > 0 else 0

    @property
    def department_title(self):

        return self.department.title

    class Meta:
        verbose_name = 'Картку'
        verbose_name_plural = 'Картки одиниць обладнання'

    def __str__(self):
        return f'{self.number} {self.name[:40] + "..." if len(self.name) > 40 else self.name}'


class ComponentType(models.Model):
    name = models.CharField(
        verbose_name='Назва',
        null=False,
        blank=False,
        max_length=255
    )



    class Meta:
        verbose_name = 'Тип компонентів'
        verbose_name_plural = 'Типи компонентів'

    def __str__(self):
        return f'{self.name[:40] + "..." if len(self.name) > 40 else self.name}'


class Component(models.Model):

    name = models.CharField(
        verbose_name='Назва',
        null=False,
        blank=False,
        max_length=255
    )
    card = models.ForeignKey(
        Card,
        verbose_name='Картка',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    type = models.ForeignKey(
        ComponentType,
        verbose_name='Тип',
        on_delete=models.SET_NULL,
        blank=True,
        null=True

    )

    employee = models.ForeignKey(
        Employee,
        verbose_name='Користувач',
        on_delete=models.SET_NULL,
        blank=True,
        null=True

    )

    department = models.ForeignKey(
        Department,
        verbose_name='Відділ',
        on_delete=models.SET_NULL,
        blank=True,
        null=True

    )

    description = models.TextField(
        verbose_name='Опис',
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name='зображення',
        upload_to='cards',
        null=True,
        blank=True
    )

    @property
    def department_title(self):
        return self.department.title

    @property
    def number(self):
        return self.card.number

    @property
    def parent_name(self):
        return self.card.name

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненти'

    def __str__(self):
        return f'{self.number} {self.name[:40] + "..." if len(self.name) > 20 else self.name} {self.parent_name}'


class OperationLog(models.Model):

    card = models.ForeignKey(
        Card,
        verbose_name='Картка',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    operation_type = models.CharField(
        choices=[],
        max_length=255)

    document = models.FileField(
        verbose_name='Документ',
        blank=True,
        null=True
    )

    date = models.DateTimeField(
        verbose_name='дата',
    )

    description = models.TextField(
        verbose_name='Опис',
    )

    @property
    def number(self):
        return self.card.number

    @property
    def name(self):
        return self.card.name

    @property
    def type(self):
        return self.operation_type.title()

    class Meta:
        verbose_name = 'Операція'
        verbose_name_plural = 'Операції'

    def __str__(self):
        return f'{self.card.number} {self.card.name} {self.operation_type}'
