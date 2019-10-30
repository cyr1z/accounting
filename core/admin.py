from django.contrib import admin

from core.models import Employee, Department, Card, ComponentType, Component, \
                        Responsible, OperationLog, Account, SubAccount
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'department_title', 'position', 'phone')
    list_display_links = ('first_name', 'second_name')


@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'department_title', 'position', 'phone')
    list_display_links = ('first_name', 'second_name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)


@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'parent_name', 'department_title')
    list_display_links = ('number', 'name')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'department_title')
    list_display_links = ('number', 'name')


@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = ('operation_type', 'number', 'name')
    list_display_links = ('operation_type', 'number', 'name')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    list_display_links = ('number', 'name')


@admin.register(SubAccount)
class SubAccountAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    list_display_links = ('number', 'name')
