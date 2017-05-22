from __future__ import unicode_literals

from django.db import models


	
class Area(models.Model):
	area = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/Area')
	def __unicode__(self):
		return "%s"%(self.area)

class Bar(models.Model):
	Username = models.CharField(max_length=50 , default = 'baruser')
	Password = models.CharField(max_length=50 , default = 'barpassword')
	Bar = 'Bar'
	Pub = 'Pub'
	CHOICES = ((Bar ,'Bar'),(Pub ,'Pub'))
	area = models.ForeignKey(Area , on_delete = models.CASCADE)
	category = models.CharField(max_length=10 , choices = CHOICES, default = Bar)
	name = models.CharField(max_length=50)
	content = models.CharField(max_length=5000)
	image1 = models.ImageField(upload_to='images/Bar' , blank=True)
	image2 = models.ImageField(upload_to='images/Bar' , blank=True)
	image3 = models.ImageField(upload_to='images/Bar' , blank=True)
	status = models.CharField(max_length=50  , blank=True)
	location = models.CharField(max_length=200)
	price = models.CharField(max_length=10 , blank=True , default = '$$$')
	phone = models.CharField(max_length=15 , blank=True)
	facebook = models.CharField(max_length=50 , blank=True)
	wifi = models.CharField(max_length=10 , blank=True , default = '-')
	googlemap = models.CharField(max_length=1000 , blank=True)
	promotion = models.CharField(max_length=200 , blank=True)
	happyhours = models.CharField(max_length=200 , blank=True)
	capacity = models.IntegerField(default = 30)
	def __unicode__(self):
		return "%s"%(self.name)


class Booking(models.Model):
	bar = models.ForeignKey(Bar , on_delete = models.CASCADE)
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	people =  models.CharField(max_length=2)
	TIME_CHOICES = (('19.00','19.00'),('19.30','19.30'),('20.00','20.00'),('20.30','20.30'),('21.00','21.00'))
	time = models.CharField(max_length=10 , choices = TIME_CHOICES )




class Drink(models.Model):
	TYPE_CHOICES = (('Wine', (
					('whitewine', 'White Wine'),
					('redwine', 'Red Wine'),
					('rosewine', 'Rose Wine'),
					('dessertwine', 'Dessert Wine'),
					('sparkling', 'Sparkling Wine'))),
    		   ('Spirits', (
    		   		('whisky', 'Whisky'),
    		   		('vodka', 'Vodka'),
    		   		('gin', 'Gin'),
    		   		('brandy', 'Brandy'),
    		   		('tequila', 'Tequila'),
    		   		('liqueur', 'Liqueur'),
    		   		('rum', 'Rum'),
    		   		('aperitif', 'Aperitif'))),
    		   ('Beer', (
    		   		('ale', 'Ale'),
    		   		('lager', 'Lager'),
    		   		('ipa', 'Ipa'),
    		   		('stouts', 'Stouts'),
    		   		('blondes', 'Blondes'),
    		   		('paleales', 'Pale Ales'),
    		   		('wheatbeer', 'Wheat Beer'),
    		   		('aleandporters', 'Ale and Porters'),
    		   		('whiskybourbonbarrelagedstouts', 'Whisky:Bourbon Barrel-Aged Stouts'),
    		   		('redalesambers', 'Red Ales:Ambers'),
    		   		('ryesandpumpkinales', 'Ryes and pumpkin Ales'),
    		   		('pilsners', 'Pilsners'),
    		   		('amberlager', 'Amber Lager'),
    		   		('bock', 'Bock'),
    		   		('dunkel', 'Dunkel'),
    		   		('schwarzbier', 'Schwarzbier'))),
			  )
	
	CATEGORY_CHOICES = (('Wine','Wine'),('Spirits','Spirits'),('Beer','Beer'))

	name = models.CharField(max_length=50)
	category = models.CharField(max_length=100 , choices = CATEGORY_CHOICES , default = 'Wine')
	typedrink = models.CharField(max_length=100 , choices = TYPE_CHOICES)
	image = models.ImageField(upload_to='images/Drink')
	content = models.CharField(max_length=2000 , default = "")
	price = models.DecimalField(max_digits=10, decimal_places=2 , default = 0)
