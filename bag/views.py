from django.shortcuts import render


def view_bag(request):
    """A view to view items in checkout"""
    
    return render(request, 'bag/bag.html')
