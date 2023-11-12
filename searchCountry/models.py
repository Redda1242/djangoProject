from django.contrib.gis.db import models

class Country(models.Model):
    # Country/area border as polygon(s)
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField(max_length=2)           # ISO 3166-1 Alpha-2 Country Code
    iso3 = models.CharField(max_length=3)           # ISO 3166-1 Alpha-3 Country Code
    un = models.PositiveSmallIntegerField()         # ISO 3166-1 Numeric-3 Country Code
    name = models.CharField(max_length=50)          # Name of country/area
    area = models.PositiveBigIntegerField()         # Land area, FAO Statistics (2002)
    pop2005 = models.PositiveBigIntegerField()      # Population, World Population Prospects (2005)
    region = models.PositiveSmallIntegerField()     # Macro geographical (continental region), UN Statistics
    subregion = models.PositiveSmallIntegerField()  # Geographical sub-region, UN Statistics
    lon = models.FloatField()                       # Longitude
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name