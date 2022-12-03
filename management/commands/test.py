from django.core.management.base import BaseCommand, CommandError
from accounts.models import rent_rem
from django.shortcuts import render , redirect


class Command(BaseCommand):
    def __init__(self):
        print("hope it works")
        f = open('C:/Users/Pratham/Desktop/t/test0.txt','w')
        f.close()
        r = rent_rem.objects.all()
        for i in r:
            print(i.dob)
        self.stdout.write("Unterminated line", ending='')