from django.shortcuts import render, redirect
from .models import Listing
from.forms import *

# create, retrive, update, delete, list features we need to implement

def listing_list(request):
    listings = Listing.objects.all()

    context = {
        'listings' : listings
    }
    return render(request, 'listings.html', context)

def listing_retrive(request, pk):
    listing = Listing.objects.get(id = pk)

    context = {
        'listing' : listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)         # used when we are uploading images/other files
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ListingForm()

    context = {
        'form':form,
    }
    return render(request, 'create.html', context)

def listing_update(request, pk):
    listing = Listing.objects.get(id = pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)     # used during uploading images/files
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        'form':form
    }
    return render(request, 'update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id = pk)
    listing.delete()
    return redirect('/')

