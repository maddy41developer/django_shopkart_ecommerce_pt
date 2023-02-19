from django.http import  JsonResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
import random
from django.shortcuts import HttpResponse
 
def home(request):
  products=Product.objects.filter(trending=1)
  return render(request,"shop/index.html",{"products":products})
 
def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"shop/fav.html",{"fav":fav})
  else:
    return redirect("/")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")
 
 
 
 
def cart_page(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"shop/carts.html",{"cart":cart})
  else:
    return redirect("/")
 
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
 
 
 
def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)


 
def add_to_cart(request):
      if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
          data=json.load(request)
          product_qty=data['product_qty']
          product_id=data['pid']
          #print(request.user.id)
          product_status=Product.objects.get(id=product_id)
          if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
              return JsonResponse({'status':'Product Already in Cart'}, status=200)
            else:
              if product_status.quantity>=product_qty:
                Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                return JsonResponse({'status':'Product Added to Cart'}, status=200)
              else:
                return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
          return JsonResponse({'status':'Login to Add Cart'}, status=200)
      else:
        return JsonResponse({'status':'Invalid Access'}, status=200)
 
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
 
 
def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"shop/login.html")
 
def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
  return render(request,"shop/register.html",{'form':form})

def BuyNow(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      
  return render(request,"shop/products/BuyNow.html",{'form':form})

def buynow(request):
      #if(Category.objects.filter(name=cname,status=0)):
          #if(Product.objects.filter(name=pname,status=0)):
                #products=Product.objects.filter(name=pname,status=0).first()
                
      return render(request,"shop/products/BuyNow.html",)

     
 
 
def collections(request):
  category=Category.objects.filter(status=0)
  return render(request,"shop/collections.html",{"category":category})
 
def collectionsview(request,name):
  if(Category.objects.filter(name=name,status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,"shop/products/index.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('collections')
 
 
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/productdetails.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return ("/")
    messages.error(request,"No Such Catagory Found")
    return redirect('collections')

def final_page(request,pname):
      #if(Category.objects.filter(name=cname,status=0)):
          if(Product.objects.filter(name=pname,status=0)):
                 products=Product.objects.filter(name=pname,status=0).first()
                 return render(request,"shop/products/BuyNow.html",{"products":products})
          else:
            messages.error(request,"No Such Produtct Found")
            return ("/")
      #messages.error(request,"No Such Catagory Found")
      #return redirect('collections')

def carts(request):
      return render(request,'shop/carts.html')
      
def mobiles(request):
      return render(request,"shop/mobiles.html")

def menfashion(request):
      return render(request,"shop/menfashion.html")

def laptop(request):
      return render(request,"shop/laptop.html")

def kitchen(request):
      return render(request,"shop/kitchens.html")

def furnitures(request):
      return render(request,"shop/furnitures.html")

#laptops

def apple(request):
      return render(request,'shop/laptops/Apple_laptop.html')

def asus(request):
      return render(request,'shop/laptops/Asus_laptop.html')

def charger(request):
      return render(request,'shop/laptops/charger.html')

def earpod(request):
      return render(request,'shop/laptops/earpod.html')

def gionee(request):
      return render(request,'shop/laptops/Gionee.html')

def headphone(request):
      return render(request,'shop/laptops/headphone.html')

def Hp_15s(request):
      return render(request,'shop/laptops/Hp_15s_laptop.html')

def Hp_l(request):
      return render(request,'shop/laptops/Hp laptop.html')

def lenovo(request):
      return render(request,'shop/laptops/Lenovo laptop.html')

def otg(request):
      return render(request,'shop/laptops/otg.html')

#fashion

def bluestripped(request):
      return render(request,'shop/fashions/blue_stripped.html')

def cottonformal(request):
      return render(request,'shop/fashions/cotton_formal.html')

def formalpants(request):
      return render(request,'shop/fashions/formal_pants.html')

def formalshirts(request):
      return render(request,'shop/fashions/formal_shirts.html')

def fullsleeves(request):
      return render(request,'shop/fashions/full_sleeves.html')

def premiumshirts(request):
      return render(request,'shop/fashions/premium_shirts.html')

def printedpants (request):
      return render(request,'shop/fashions/printed_pants.html')

def roundneck(request):
      return render(request,'shop/fashions/round_neck_shirts.html')

def trackpants(request):
      return render(request,'shop/fashions/track_pants.html')

def cottonwhite(request):
      return render(request,'shop/fashions/cotton_white.html')
      



#mobiles

def apple13(request):
      return render(request,'shop/mobiles/apple_13.html')

def apple14(request):
      return render(request,'shop/mobiles/apple_14.html')

def moto(request):
      return render(request,'shop/mobiles/moto.html')

def oneplus(request):
      return render(request,'shop/mobiles/oneplus.html')

def oppo(request):
      return render(request,'shop/mobiles/oppo.html')

def realme(request):
      return render(request,'shop/mobiles/realme.html')

def redmi10 (request):
      return render(request,'shop/mobiles/redmi10.html')

def  redmi11(request):
      return render(request,'shop/mobiles/redmi11.html')

def  redmi12(request):
      return render(request,'shop/mobiles/redmi12.html')

def vivo(request):
      return render(request,'shop/mobiles/vivo.html')

#home

def aircoditioner(request):
      return render(request,'shop/furnitures/air_conditioner.html')

def aircooler(request):
      return render(request,'shop/furnitures/air_cooler.html')

def chair(request):
      return render(request,'shop/furnitures/chair.html')

def diningtable(request):
      return render(request,'shop/furnitures/dining_table.html')

def doublebed(request):
      return render(request,'shop/furnitures/double_bed.html')

def fan(request):
      return render(request,'shop/furnitures/fan.html')

def singlebed (request):
      return render(request,'shop/furnitures/singlebed.html')

def swingchair (request):
      return render(request,'shop/furnitures/swing_chair.html')

def tablefan(request):
      return render(request,'shop/furnitures/table_fan.html')

def writingtable(request):
      return render(request,'shop/furnitures/writing_table.html')

#kitchens

def bottles(request):
      return render(request,'shop/homes/bottles.html')

def box(request):
      return render(request,'shop/homes/box.html')

def chopper(request):
      return render(request,'shop/homes/chopper.html')

def cooker(request):
      return render(request,'shop/homes/cooker.html')

def juicer(request):
      return render(request,'shop/homes/juicer.html')

def kadai(request):
      return render(request,'shop/homes/kadai.html')

def maker(request):
      return render(request,'shop/homes/maker.html')

def rack(request):
      return render(request,'shop/homes/rack.html')

def tawa(request):
      return render(request,'shop/homes/tawa.html')

def tool(request):
      return render(request,'shop/homes/tool.html')


      

def checkout(request):
  if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/products/BuyNow.html")
  else:
    return redirect("/")

def placeholder(request):
      if request.user.is_authenticated:
            if request.method=="POST" :
                  neworder = Order()
                  neworder.user = request.user
                  neworder.fname = request.POST.get('fname')
                  neworder.lname = request.POST.get('lname')
                  neworder.email = request.POST.get('email')
                  neworder.phone = request.POST.get('phone')
                  neworder.address = request.POST.get('address')
                  neworder.city = request.POST.get('city')
                  neworder.state = request.POST.get('state')
                  neworder.country = request.POST.get('country')
                  neworder.pincode = request.POST.get('pincode')
                  neworder.payment_mode = request.POST.get('payment_mode')
                  neworder.total_price = request.POST.get('total_price')
                 
              
                  carts = Cart.objects.filter(user=request.user)
                  cart_total_price = 0
                  for item in carts:
                         cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
                         neworder.product=item.product.name,

                  neworder.total_price= cart_total_price
                  trackno = 'maddyshopkart' + str(random.randint(1111111,9999999))
                  while Order.objects.filter(tracking_no=trackno) is None:
                        trackno = 'maddyshopkart'+str(random.randint(1111111,9999999))

                  neworder.tracking_no  = trackno
                  neworder.save()

                  neworderitems = Cart.objects.filter(user=request.user)
                  for item in neworderitems:
                        OrderItem.objects.create(
                          order=neworder,
                          product=item.product.name,
                          price=item.product.selling_price,
                          quantity=item.product_qty
                    )

                        orderproduct = Product.objects.filter(id=item.product_id).first()
                        orderproduct.quantity = orderproduct.quantity - item.product_qty
                        orderproduct.save()
              
                  Cart.objects.filter(user=request.user).delete()
                  messages.success(request,"Your order has been placed successfully")
          
      else:
            return render('/')
           
      return render(request,"shop/thanks.html")
 
            
           
def buttonholder(request):
      if request.user.is_authenticated:
            if request.method=="POST" :
                  neworder = Order()
                  neworder.user = request.user
                  neworder.fname = request.POST.get('fname')
                  neworder.lname = request.POST.get('lname')
                  neworder.email = request.POST.get('email')
                  neworder.phone = request.POST.get('phone')
                  neworder.address = request.POST.get('address')
                  neworder.city = request.POST.get('city')
                  neworder.state = request.POST.get('state')
                  neworder.country = request.POST.get('country')
                  neworder.pincode = request.POST.get('pincode')
                  neworder.payment_mode = request.POST.get('payment_mode')
                  neworder.total_price = request.POST.get('price')
                  neworder.product=request.POST.get('product')
                  neworder.quantity=request.POST.get('quantity')

                  

                  neworder.save()
                  messages.success(request,"Your order has been placed successfully")  
            
      return render(request,"shop/thanks.html")