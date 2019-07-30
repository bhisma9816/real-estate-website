from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator= Paginator(listings,6)
    page=request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings':page_listings}

    return render(request,'listing/listings.html',context)

def listing(request ,listing_id):
    listing =get_object_or_404(Listing ,pk=listing_id)
    context = {'listing':listing}
    return render(request,'listing/listing.html',context)

def search(request):
    return render(request,'listing/search.html')
