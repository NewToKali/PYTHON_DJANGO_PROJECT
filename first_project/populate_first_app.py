import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic,Users
from faker import Faker

fakegen = Faker()

topics= ['Search', 'Social', 'Marketplace','News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        
        top= add_topic()
        
        fake_url= fakegen.url()
        fake_date= fakegen.date()
        fake_name= fakegen.company()
        fake_first_name= fakegen.name().split(" ")[0]
        fake_last_name= fakegen.name().split(" ")[1]
        fake_email= fakegen.email()
        
        webpge= Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        user= Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name,email=fake_email)[0]
        acc_rec= AccessRecord.objects.get_or_create(name=webpge,date= fake_date)[0]

if __name__ == '__main__':
    print("populating the tables")
    populate()
    print("complete")