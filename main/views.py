

from django.shortcuts import render,redirect
from django.http import HttpResponse


import time
import tinytuya
class Outlet:


    def __init__(self,key,ip,local_key):
        self.key=key
        self.ip=ip
        self.local_key=local_key
    def status(self):
        d=tinytuya.OutletDevice(self.key,self.ip,self.local_key)
        d.set_version(3.3)
        data=d.status()
        return data["dps"]["1"]
        
    def turn_on(self):
        d = tinytuya.OutletDevice(self.key, self.ip, self.local_key)
        d.set_version(3.3)
        d.turn_on()
    def turn_off(self):
        d = tinytuya.OutletDevice(self.key, self.ip, self.local_key)
        d.set_version(3.3)
        d.turn_off()





# Create your views here.

def home(response):
    return render(response,"main/home.html",{})

# def outlet(response):
#     return HttpResponse("coming soon")

def socket(response):
    socket=Outlet("bf9616a76586eba918hgs2","10.0.1.31","d1c5d8102db020f8")
    return render(response,"main/gniazdko.html",{"socket":socket})

# def random(response):
#     return render(response,"main/home.html",{})

def on(response):
    
    socket=Outlet("bf9616a76586eba918hgs2","10.0.1.31","d1c5d8102db020f8")
    socket.turn_on()
    return render(response,"main/gniazdko.html",{"socket":socket})
def off(response):
    
    socket=Outlet("bf9616a76586eba918hgs2","10.0.1.31","d1c5d8102db020f8")
    socket.turn_off()
    return render(response,"main/gniazdko.html",{"socket":socket})
def zdjecia(response):
    return render(response,"main/zdjecia.html",{})