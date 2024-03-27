from django.shortcuts import render, HttpResponse
from .models import Campaign,CampaignImages
from datetime import date,datetime,timedelta
from django.utils import timezone

def home(request):
    # return HttpResponse('This is the my website')
    Campaigns = Campaign.objects.values()
    today = timezone.now().date()

    # Query objects with dates greater than or equal to today's date
    Campaigns = Campaign.objects.filter(campaign_date__gte=today)

    # If there are upcoming objects, get the most recent one
    if Campaigns.exists():
        # Sort the objects by date
        recent = Campaigns.order_by('campaign_date').first()
    else:
        # Handle case where there are no upcoming objects
        recent = None
    return render(request,'home.html',{'recent':recent})
def about(request):
    
    return render(request,'about.html')
def contact(request):
    
    return render(request,'contact.html')


def upcoming(request):
    
    return render(request,'upcoming.html')

def past_campaigns(request):
    
    return render(request,'work.html')

def campaign(request,cid):
    this_camp = Campaign.objects.filter(campaign_id=cid).values()
    photos = CampaignImages.objects.filter(prod=cid)
    data = {'campaign':this_camp[0],
            'campaign_id':cid}
    return render(request,'campaign.html')

