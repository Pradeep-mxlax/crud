from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	cart_add_form = CartAddProductForm()
	return render(
		request,
		'catalog/product_list.html',
		{
			'category': category,
			'categories': categories,
			'products': products,
			'cart_add_form': cart_add_form,
		},
	)


def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug, available=True)
	cart_add_form = CartAddProductForm()
	return render(request, 'catalog/product_detail.html', {'product': product, 'cart_add_form': cart_add_form})
