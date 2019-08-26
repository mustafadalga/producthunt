from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Votes
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone

def home(request):
    products=Product.objects.all().order_by('vote').reverse()
    if len(products)>0:
        votes=Votes.objects.values('product').annotate(total_votes=Count('product'))
        context={
            'products':products,
            'votes':votes
        }
        return render(request,'products/home.html',context)
    else:
        context={
            'error':'Henüz yayınlanmış Ürün bulunmamaktadır.'
        }
        return render(request, 'products/home.html', context)


@login_required(login_url='/accounts/login')
def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST.get('icon', True) and request.POST.get('image', True):
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.vote = 1
            product.hunter = request.user
            product.save()
            messages.success(request, 'Ürününüz başarılı bir şekilde eklendi!')
            return redirect('/products/' + str(product.id))
        else:
            messages.error(request, 'Lütfen boş alan bırakmayınız!')
            return redirect('create')
    else:
        return render(request, 'products/create.html')


def detay(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    vote=Votes.objects.filter(product=product_id).count()

    context={
        'product':product,
        'vote':vote,
    }
    return render(request,'products/detay.html',context)

@login_required(login_url='/accounts/login')
def upvote(request,product_id):
    if request.method == "POST":
        if Votes.objects.filter(product_id=product_id,user=request.user).exists():
            messages.error(request,'Bu ürüne zaten oy vermişsiniz')
            return redirect('/products/'+str(product_id))
        else:
            product=get_object_or_404(Product,pk=product_id)
            product.vote+=1
            product.save()
            vote=Votes()
            vote.product=get_object_or_404(Product,pk=product_id)
            vote.user=User.objects.get(id=request.user.id)
            vote.save()
            messages.success(request,'Bu ürüne oy verme işlemi başarılı')
            return redirect('/products/'+str(product_id))

