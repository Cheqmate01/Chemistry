from django.db import models

# Create your models here.
class Element(models.Model):
    name                = models.CharField(max_length=100)
    symbol              = models.CharField(max_length=3)
    atomic_number       = models.PositiveIntegerField()
    atomic_weight       = models.CharField(max_length=50)
    density             = models.CharField(max_length=50)
    melting_point       = models.CharField(max_length=20)
    boiling_point       = models.CharField(max_length=20)
    phase               = models.CharField(max_length=50)
    group               = models.PositiveIntegerField(null=True, blank=True)
    period              = models.PositiveIntegerField(null=True, blank=True)
    CATEGORY_CHOICES    = [
        ('noble gas', 'Noble Gas'),
        ('alkali metal', 'Alkali Metal'),
        ('alkaline earth metal', 'Alkaline Earth Metal'),
        ('metalloid', 'Metalloid'),
        ('halogen', 'Halogen'),
        ('transition metal', 'Transition Metal'),
        ('post-transition metal', 'Post-Transition Metal'),
        ('lanthanide', 'Lanthanide'),
        ('actinide', 'Actinide'),
        ('non metal', 'Non Metal')
    ]
    category            = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='alkali metal')

    def __str__(self):
        return self.name + ' (' + self.symbol + ')'
