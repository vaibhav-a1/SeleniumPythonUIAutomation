import random
from datetime import date
from datetime import datetime, timedelta
import string
import time


def get_randome_name():
    randomname = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(10))
    return randomname

def get_campaign_successful_message(randomname):
    campaign_successful_message = f"Campaign {randomname} is saved"
    return campaign_successful_message

def get_current_date():
    current_date = date.today().strftime("%m/%d/%Y")
    return current_date

def get_current_time_pm():
    current_time = datetime.now().strftime("%H:%M")
    current_time_pm = current_time + " P"
    return current_time_pm

def get_future_date():
    current_date = datetime.now()
    futuredate = (current_date + timedelta(days=2)).strftime("%m/%d/%Y")
    return futuredate
