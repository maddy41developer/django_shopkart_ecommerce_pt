from django.urls import path
from . import views
 
urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('BuyNow',views.buynow,name="BuyNow"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('checkout',views.checkout,name='checkout'),
    path('placeholder',views.placeholder,name='placeholder'),
    path('collections/<str:cname>/<str:pname>',views.final_page,name="final_page"),
    path('buttonholder',views.buttonholder,name='buttonholder'),
    path('carts',views.carts,name='carts'),
   
   
    path('mobiles', views.mobiles,name='mobiles'),
    path('menfashion',views.menfashion,name='menfashion'),
    path('furnitures',views.furnitures,name='furnitures'),
    path('laptop',views.laptop,name='laptop'),
    path('kitchen',views.kitchen,name='kitchen'),

    #Laptops
    path("apple",views.apple,name="apple"),
    path("asus",views.asus,name="asus"),
    path("charger",views.charger,name="charger"),
    path("earpod",views.earpod,name="earpod"),
    path("gionee",views.gionee,name="gionee"),
    path("headphone",views.headphone,name="headphone"),
    path("hp_15s",views.Hp_15s,name="hp_15s"),
    path("hp_l",views.Hp_l,name="hp_l"),
    path("lenovo",views.lenovo,name="lenovo"),
    path("otg",views.otg,name="otg"),
    
    #fashion
    path("blue",views.bluestripped,name="blue"),
    path("cottonformal",views.cottonformal,name="cottonformal"),
    path("fpants",views.formalpants,name="fpants"),
    path("fshirts",views.formalshirts,name="fshirts"),
    path("fsleeves",views.fullsleeves,name="fsleeves"),
    path("pshirts",views.premiumshirts,name="pshirts"),
    path("ppants",views.printedpants, name="ppants"),
    path("rneck",views.roundneck,name="rneck"),
    path("tpants",views.trackpants,name="tpants"),
    path("cwhite",views.cottonwhite,name="cwhite"),
    
    #mobiles
    path("apple13",views.apple13,name="apple13"),
    path("apple14",views.apple14,name="apple14"),
    path("moto",views.moto,name="moto"),
    path("oneplus",views.oneplus,name="oneplus"),
    path("oppo",views.oppo,name="oppo"),
    path("realme",views.realme,name="realme"),
    path("redmi10",views.redmi10, name="redmi10"),
    path("redmi11",views.redmi11,name="redmi11"),
    path("redmi12",views.redmi12,name="redmi12"),
    path("vivo",views.vivo,name="vivo"),

    #homes
    path("airconditioner",views.aircoditioner,name="aircoditioner"),
    path("aircooler",views.aircooler,name="aircooler"),
    path("chair",views.chair,name="chair"),
    path("diningtable",views.diningtable,name="diningtable"),
    path("doublebed",views.doublebed,name="doublebed"),
    path("fan",views.fan,name="fan"),
    path("singlebed",views.singlebed, name="singlebed"),
    path("swingchair",views.swingchair,name="swingchair"),
    path("tablefan",views.tablefan,name="tablefan"),
    path("writingtable",views.writingtable,name="writingtable"),

    #kitchens
    path("bottles",views.bottles,name="bottles"),
    path("box",views.box,name="box"),
    path("chopper",views.chopper,name="chopper"),
    path("cooker",views.cooker,name="cooker"),
    path("juicer",views.juicer,name="juicer"),
    path("kadai",views.kadai,name="kadai"),
    path("maker",views.maker, name="maker"),
    path("rack",views.rack,name="rack"),
    path("tawa",views.tawa,name="tawa"),
    path("tool",views.tool,name="tool"),


  

]