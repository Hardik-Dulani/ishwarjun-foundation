from django.db import models

# Create your models here.
class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=50)
    campaign_tagline = models.CharField(max_length= 500)
    campaign_venue = models.CharField(max_length=200,default="")
    desc = models.CharField(max_length=10000,default="")
    desc2 = models.CharField(max_length=10000,default='')
    campaign_date = models.DateField()
    campaign_image = models.FileField(upload_to="images/",default="")

    def __str__(self):
        return self.campaign_name
    



class CampaignImages(models.Model):
    prod = models.ForeignKey(Campaign, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    

