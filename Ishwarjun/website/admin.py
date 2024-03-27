from django.contrib import admin
from .models import Campaign,CampaignImages
# Register your models here.

class campaignImage(admin.StackedInline):
    model=CampaignImages


@admin.register(Campaign)
class imgUpload(admin.ModelAdmin):
    inlines = [campaignImage]

    class Meta:
        model = Campaign


@admin.register(CampaignImages)
class PostProdImage(admin.ModelAdmin):
    pass
