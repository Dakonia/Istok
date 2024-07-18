from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    consent_to_data_processing = models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')
    
    # Второстепенные поля для нашей лояльности пока их не трогаем 
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', null=True, blank=True)
    surname = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    gender = models.CharField(max_length=3, choices=[('man', 'Мужской'), ('wom', 'Женский')], verbose_name='Ваш пол', default=None, null=True )
    email = models.EmailField(verbose_name='Почта', null=True, blank=True, unique=True)
    has_children = models.CharField(max_length=3, choices=[('yes', 'Да'), ('no', 'Нет')], verbose_name='Наличие детей', default=None, null=True)
    renovation_plan = models.CharField(max_length=100, verbose_name='Планируется ли ремонт?', choices=[
        ('already_ongoing', 'Уже идет'),
        ('starting_soon', 'Скоро приступаем'),
        ('within_half_year', 'В течение полугода'),
        ('within_year', 'В течение года'),
    ], default=None,  null=True)
    ren_planned = models.CharField(max_length=3, choices=[('yes', 'Да'), ('no', 'Нет')], verbose_name='Планируется ли ремонт', default=None, null=True)
    renovation_location = models.ManyToManyField('RenovationLocation', verbose_name='Где планируется ремонт?', blank=True)
    subscription_consent = models.BooleanField(default=False, verbose_name='Согласие на рассылку')

class RenovationLocation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Место ремонта')

    def __str__(self):
        return self.name
    

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('bathroom', 'Ванная'),
        ('wardrobe', 'Гардероб'),
        ('racks', 'Стеллажи'),
        ('hallways', 'Прихожие'),
        ('kitchen', 'Кухни'),
        ('dresser', 'Комоды'),
        ('children', 'Детские'),
    ]

    name = models.CharField(max_length=100, verbose_name='Категории', choices=CATEGORY_CHOICES, default=None, null=True)
    
    def image_upload_to(instance, filename):
        return f'images/{instance.name}/{filename}'
    
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.get_name_display()
    


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена со скидкой', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    
    def main_image_upload_to(instance, filename):
        return f'images/{instance.category.name}/{filename}'

    main_image = models.ImageField(upload_to=main_image_upload_to, verbose_name='Главное изображение')
    additional_images = models.ManyToManyField('ProductImage', related_name='products_with_additional_images', blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    def image_upload_to(instance, filename):
        return f'images/{instance.product.category.name}/{filename}'

    product = models.ForeignKey(Product, related_name='additional_images_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return f"Изображение для {self.product.name}"
    



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)

class BonusProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bonus_points = models.DecimalField(max_digits=10, decimal_places=2)

