from django.contrib import admin
#Импорт из приложения
from products.models import Product, ProductsCategory

#Регистрация БД в админке
admin.site.register(Product)
admin.site.register(ProductsCategory)
