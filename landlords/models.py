from django.db import models
class LandLord(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    nat_id=models.CharField(max_length=8,primary_key=True)
    passport=models.ImageField()
    phone_number=models.IntegerField()
    def __str__(self) -> str:
        return self.first_name+' '+self.last_name
class House(models.Model):
    COUNTY_LOCATION=[
        ('01',' Mombasa'),
        ('02',' Kwale'),
        ('03',' Kilifi'),
        ('04',' Tana River'),
        ('05',' Lamu'),
        ('06',' Taita/Taveta'),
        ('07',' Garissa'),
        ('08',' Wajir'),
        ('09',' Mandera'),
        ('10',' Marsabit'),
        ('11',' Isiolo'),
        ('12',' Meru'),
        ('13',' Tharaka-Nithi'),
        ('14',' Embu'),
        ('15',' Kitui'),
        ('16',' Machakos'),
        ('17',' Makueni'),
        ('18',' Nyandarua'),
        ('19',' Nyeri'),
        ('20',' Kirinyaga'),
        ('21',' Muranga'),
        ('22',' Kiambu'),
        ('23',' Turkana'),
        ('24',' West Pokot'),
        ('25',' Samburu'),
        ('26',' Trans Nzoia'),
        ('27',' Uasin Gishu'),
        ('28',' Elgeyo/Marakwet'),
        ('29',' Nandi'),
        ('30',' Baringo'),
        ('31',' Laikipia'),
        ('32',' Nakuru'),
        ('33',' Narok'),
        ('34',' Kajiado'),
        ('35',' Kericho'),
        ('36',' Bomet'),
        ('37',' Kakamega'),
        ('38',' Vihiga'),
        ('39',' Bungoma'),
        ('40',' Busia'),
        ('41',' Siaya'),
        ('42',' Kisumu'),
        ('43',' Homa Bay'),
        ('44',' Migori'),
        ('45',' Kisii'),
        ('46',' Nyamira'),
        ('47',' Nairobi City'),
    ]
    TYPE=[
        ('SR','Single Room'),
        ('BS','Bed-Sitter'),
        ('OB','One Bedroom'),
        ('TB','Two Bedroom'),
        ('AP3','Apartment - 3 Bedroom'),
        ('AP4','Apartment -4 Bedroom'),
        ('GH','Guest House'),
    
    ]
    name=models.CharField(max_length=70)
    county=models.CharField(max_length=70,choices=COUNTY_LOCATION)
    rent_per_month=models.IntegerField()
    house_type=models.CharField(max_length=100,choices=TYPE)
    landlord=models.ForeignKey(LandLord,on_delete=models.CASCADE)
class TimeStamps(models.Model):
    created_time=models.DateTimeField(auto_now=True)
    edited_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True
class Clout(models.Model):
    content=models.TextField()
    house=models.ForeignKey(House,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now=True)
    edited_time=models.DateTimeField(auto_now_add=True)



