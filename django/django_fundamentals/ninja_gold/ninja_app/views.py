from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz


def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    context = {
        'activities':request.session['activities']
    }
    return render(request, "index.html", context)

def process_money(request):
    if request.method == 'POST':
        # SETUP
        mygold = request.session['gold'] # save gold in session so amt doesn't reset to $0
        activities = request.session['activities']
        location = request.POST['location']     
        # My LOCATION stuff   
        if location == 'farm':
            goldthisturn = round(random.random() * 10 + 10) # earn 10-20 Gold
        elif location == 'cave':
            goldthisturn = round(random.random() * 5 + 5)
        elif location == 'house':
            goldthisturn = round(random.random() * 3 + 2)
        else:
            # do casino stuff
            winorlose = round(random.random()) 
            if winorlose == 1:
                goldthisturn = round(random.random() * 50)
            else:           
                goldthisturn = (round(random.random() * 50) * -1)       
        # Every turn stuff
        date_format='%m/%d/%Y %H:%M:%S %Z' # Create DATE!
        date = datetime.now(tz=pytz.utc) # setting time to now and  Timezone to UTC
        date = date.astimezone(timezone('US/Pacific')) # sets TZ to US Pacific('US/Pacific'))
        mytime = date.strftime(date_format) # displays time
        
        mygold += goldthisturn # add goldthisturn to mygold
        request.session['gold'] = mygold
        
        if goldthisturn >= 0:
            str = f"Earned {goldthisturn} gold from the {location} Yay!!! ({mytime})" # Activities is a lists: Create string for list & Populate string w/ variables
        else:
            goldthisturn *= -1
            str = f"Entered a {location} and Lost {goldthisturn} gold... Ouch... ({mytime})"
        activities.insert(0, str) # save string to sessions
        request.session['activities'] = activities
    return redirect("/")