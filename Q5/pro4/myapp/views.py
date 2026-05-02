from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ReviewForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product=product)

    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=pk)

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })