from django.shortcuts import render,get_object_or_404
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .choices import state_choices,bedrooms_choices,prices_choices
from .models import Listing
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings,
        }
    return render(request,"listings/listings.html",context)
def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={'listing':listing}
    return render(request,"listings/listing.html",context)
def search(request):
    listings_query=Listing.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            listings_query=listings_query.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            listings_query=listings_query.filter(city__iexact=city)
    # state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            listings_query=listings_query.filter(state__iexact=state)
    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            # LTE stands for less then or equalto and GLE stands for grater then or equal to
            listings_query=listings_query.filter(bedrooms__gte=bedrooms)
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            listings_query=listings_query.filter(price__lte=price)
    context={
        "state_choices":state_choices,
        "bedrooms_choices":bedrooms_choices,
        "prices_choices":prices_choices,
        "listings_query":listings_query,
        "values":request.GET 
    }
    return render(request,"listings/search.html",context)