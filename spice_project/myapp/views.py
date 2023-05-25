from pyexpat.errors import messages

from allauth.socialaccount.models import SocialAccount
from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
from django.contrib import messages


def index(request):
    return render(request, './myapp/index.html/')


def base(request):
    cat_name = category.objects.all()
    context = {'category_list': cat_name}
    return render(request, './myapp/base.html', context)


def login(request):
    return render(request, './myapp/login.html')
def contact(request):
    return render(request, './myapp/contact.html')

def non_contact(request):
    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        c_s = contact_support(name=u_name, phone=phone, email=email, message=msg)
        c_s.save()
        cat_name = category.objects.all()
        context = {'category_list': cat_name}
        return render(request, './myapp/non_user_contact.html',context)
    else:
        cat_name = category.objects.all()
        context = {'category_list': cat_name}
        return render(request, './myapp/non_user_contact.html',context)
def non_about(request):
    cat_name = category.objects.all()
    context = {'category_list': cat_name}
    return render(request, './myapp/non_user_about.html',context)

def sign_up(request):
    cat_name = category.objects.all()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')


        #exists username
        if user_details.objects.filter(email=email):
            msg = {'msg1': 'username taken...!'}
            return render(request, './myapp/sign_up.html', msg)
        else:
            ud = user_details(fname=fname,lname=lname,phone=phone,email=email,password=password)
            ud.save()
            context = {'msg': 'User Registered'}
            return redirect(login)
    else:
        context = {'category_list': cat_name}
        return render(request, './myapp/sign_up.html', context)


#
from django.http import HttpResponse
import json
def google_auth_callback(request, format=None):
    social_account = SocialAccount.objects.get(user=request.user, provider='google')
    print(social_account)
    u = user_details(email=social_account)
    u.save()
    request.session['user_name'] = u.email
    print(request.session['user_name'])
    print(u.email)
    # result = google_auth_callback(social_account)  # Call the function with the appropriate parameter
    # return JsonResponse({'result': result})
    # return JsonResponse(google_auth_callback(social_account))
    return redirect(user_home)



def user_home(request):
    items_details = item.objects.all()
    cat_name = category.objects.all()
    ud = user_details.objects.filter(email=request.session['user_name'])
    id = user_details.objects.get(email=request.session['user_name'])
    qs = review.objects.filter(user=id)
    my_count = qs.count()

    #category
    t = item.objects.filter(category='1').order_by('-id')
    s = item.objects.filter(category='2').order_by('-id')
    d = item.objects.filter(category='3').order_by('-id')
    c = item.objects.filter(category='4').order_by('-id')
    if request.method == 'POST':
        item_search = request.POST.get('item_name')
        im_l = item.objects.filter(item_name__icontains=item_search)

        context1 = {'items': im_l}
        return render(request, './myapp/user_search_item_view.html', context1)
    context = {'items': items_details,'category_list': cat_name, 'uname': ud,
               'my_count': my_count,
               'tea': t, 'spice': s, 'dry_fruits': d, 'chocolate': c}
    return render(request, './myapp/user_home.html', context)


def user_search_item_view(request):
    name = request.GET.get('item_name')
    a = item.objects.filter(item_name__icontains=name)
    return render(request, './myapp/user_search_item_view.html', {'items': a})


def autocomplete(request):
    if 'term' in request.GET:
        qs = item.objects.filter(item_name__isstartswith=request.GET.get("term"))
        titles = list()
        for product in qs:
            titles.append(product.item_name)
        return JsonResponse(titles, safe=False)
    return render(request, './myapp/search.html')


def login(request):
    cat_name = category.objects.all()
    if request.method == 'POST':
        un = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        # ul = userlogin.objects.filter(username=', password='123', user_type='admin')
        ub = user_details.objects.filter(email=un, password=pwd)
        # user_type = userlogin.objects.filter(user_type = 'user')
        # if len(ul) == 1:
        #     return redirect('http://127.0.0.1:8000/admin/')
        # g= user_details.objects.filter(email=u)

        if len(ub) == 1:
            request.session['user_name'] = ub[0].email
            request.session['user_id'] = ub[0].id
            return redirect(user_home)
        else:
            context = {'msg1': 'Invalid username and password...!', 'category_list': cat_name}
            return render(request, './myapp/login.html', context)

    else:
        context = {'category_list': cat_name}
        return render(request, './myapp/login.html', context)


def logout(request):
    try:
        del request.session['user_name']

        del request.session['user_id']
    except:
        return redirect(login)
    else:
        return redirect(login)

def index(request):
    items_details = item.objects.all().order_by('-id')

    cat_name = category.objects.all()
     #category
    t = item.objects.filter(category='1').order_by('-id')
    s = item.objects.filter(category='2').order_by('-id')
    d = item.objects.filter(category='3').order_by('-id')
    c = item.objects.filter(category='4').order_by('-id')
    context = { 'tea': t, 'spice': s, 'dry_fruits': d, 'chocolate': c,'items': items_details, 'category_list': cat_name}

    return render(request, './myapp/index.html/', context)
def contact_supporting(request):
    cat_name = category.objects.all()
    if request.method == 'POST':
        u_name=request.POST.get('u_name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        msg = request.POST.get('message')
        c_s = contact_support(name=u_name, phone=phone, email=email,message=msg)
        c_s.save()
        return redirect(contact_supporting)
    else:
        ud = user_details.objects.filter(email=request.session['user_name'])
        context = {'uname': ud, 'category_list': cat_name}
        return render(request, 'myapp/contact.html',context)



def product_page(request):
    cat_na = category.objects.all()
    # product id
    id = request.GET.get('id')
    t = item.objects.filter(id=int(id))

    # for category
    cat_id = request.GET.get('cat_id')
    cat_name = category.objects.get(id=cat_id)
    related = item.objects.filter(category=cat_name)
    for i in related:
        print(i.item_name)

    # review
    r = item.objects.get(id=int(id))
    rev = review.objects.filter(item_name=r).order_by('-id')[:3]
    context = {'items': t, 'review': rev, 'related': related, 'category_list': cat_na}
    return render(request, './myapp/product_page.html', context)



def user_product_page(request):
    ud = user_details.objects.filter(email=request.session['user_name'])

    # product id
    id = request.GET.get('id')
    t = item.objects.filter(id=int(id))

    # for category
    cat_id = request.GET.get('cat_id')
    cat_name = category.objects.get(id=cat_id)
    related = item.objects.filter(category=cat_name)
    for i in related:
        print(i.item_name)
    c_name = category.objects.all()

    # review
    r = item.objects.get(id=int(id))
    rev = review.objects.filter(item_name=r).order_by('-id')[:3]
    qs = review.objects.filter(item_name=r)
    my_count = qs.count()

    total = review.objects.filter(item_name=r).aggregate(Avg('rate'))['rate__avg']
    round_num = round(total, 1)
    if request.method == 'POST':
        # REVIEW
        rev_desp = request.POST.get('review')
        user = request.session['user_name']
        star = request.POST.get('rating')
        ud = user_details.objects.get(email=user)
        review_details = review(user=ud, item_name=r, review_desp=rev_desp, rate=star)
        review_details.save()
        ################

        r = item.objects.get(id=int(id))
        rev = review.objects.filter(item_name=r).order_by('-id')[:3]
        qs = review.objects.filter(item_name=r)
        my_count = qs.count()
        ud = user_details.objects.filter(email=request.session['user_name'])


        c_name = category.objects.all()
        context1 = {'uname': ud,'review': rev, 'related': related, 'items': t, 'category_list': c_name, 'my_count': my_count, 'round_num' :round_num}
        return render(request, './myapp/user_product_page.html', context1)

    context = {'uname': ud,'items': t, 'review': rev, 'related': related, 'category_list': c_name, 'my_count': my_count, 'round_num' :round_num}
    return render(request, './myapp/user_product_page.html', context)


def category_item(request):
    ud = user_details.objects.filter(email=request.session['user_name'])
    cat_id = request.GET.get('cat_id')
    cat = category.objects.get(id=cat_id)
    cat_items = item.objects.filter(category=cat)
    cat_name = category.objects.all()
    context = {'category_item': cat_items, 'category_list': cat_name, 'uname': ud}
    return render(request, './myapp/category_item.html', context)

def base_category(request):
    cat_id = request.GET.get('id')
    cat = category.objects.get(id=cat_id)
    cat_items = item.objects.filter(category=cat)
    cat_name = category.objects.all()
    context = {'category_item': cat_items, 'category_list': cat_name}
    return render(request, './myapp/base_category.html', context)


def all_review(request):
    id = request.GET.get('id')
    it = item.objects.filter(id=int(id))
    r = item.objects.get(id=int(id))
    rev = review.objects.filter(item_name=r).order_by('-id')
    total = review.objects.filter(item_name=r).aggregate(Avg('rate'))['rate__avg']
    for i in rev:
        print(i.rate)
        rate_count = i.rate
        # all_plus =
    round_num = round(total, 1)
    print(round_num)
    avg = total / 5.0
    print(avg)

    context = {'review': rev, 'items': it, }
    return render(request, './myapp/all_review.html', context)


from django.shortcuts import get_object_or_404, redirect





def user_profile(request):
    cat_name = category.objects.all()
    id = request.session['user_name']
    user = user_details.objects.filter(email=id)
    context = {'category_list': cat_name,'profile': user}
    return render(request, './myapp/user_profile.html', context)

def user_address_view(request):
    cat_name = category.objects.all()
    id = request.GET.get('id')
    user = user_details.objects.filter(id=int(id))
    context = {'category_list': cat_name,'profile': user}
    return render(request, './myapp/user_address_view.html', context)


def user_address_edit(request):
    cat_name = category.objects.all()
    if request.method == 'POST':
        user = request.session['user_name']
        up = user_details.objects.get(email=user)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        pin = request.POST.get('pin')
        state = request.POST.get('state')
        address = request.POST.get('address')

        up.fname = fname
        up.lname = lname
        up.phone = phone
        up.address = address
        up.state = state
        up.pin = pin
        up.save()
        details = user_details.objects.filter(email=request.session['user_name'])
        context = {'category_list': cat_name,'profile': details}
        return redirect(user_profile)
    else:
        cat_name = category.objects.all()
        id = request.GET.get('id')
        user = user_details.objects.get(id=int(id))
        context = {'category_list': cat_name,'x': user}
    return render(request, './myapp/user_address_edit.html', context)

def user_login_details_view(request):
    cat_name = category.objects.all()
    id = request.session['user_name']
    user = user_details.objects.filter(email=id)
    context = {'category_list': cat_name,'profile': user}
    return render(request, './myapp/user_login_details_view.html', context)

def user_change_email(request):

    if request.method == 'POST':
        user = request.session['user_name']
        up = user_details.objects.get(email=user)
        email = request.POST.get('email')
        up.email = email
        up.save()
        return redirect(login)

    else:
        cat_name = category.objects.all()
        id = request.session['user_name']
        user = user_details.objects.get(email=id)
        context = {'category_list': cat_name,'x': user}
        return render(request, './myapp/user_change_email.html', context)

def user_change_password(request):
    cat_name = category.objects.all()
    if request.method == 'POST':
        user = request.session['user_name']
        up = user_details.objects.get(email=user)
        old_p = up.password
        old_pass = request.POST.get("old_password")
        new_pass = request.POST.get("new_password")

        if old_pass != old_p:
            msg = {'category_list': cat_name,'msg1': 'Old password is incorrect'}
            return render(request, './myapp/user_change_password.html', msg )
        else:
            up.password = new_pass
            up.save()
            return redirect(login)
    return render(request, './myapp/user_change_password.html')

def about(request):
    cat_name = category.objects.all()

    ud = user_details.objects.filter(email=request.session['user_name'])
    context = {'uname': ud, 'category_list': cat_name}
    return render(request, 'myapp/about.html', context)

##contact#######
def contact(request):
    cat_name = category.objects.all()
    ud = user_details.objects.filter(email=request.session['user_name'])
    context = {'category_list': cat_name, 'uname': ud}
    return render(request, 'myapp/contact.html', context)


######=====checkout, add to cart, mycart, wishlist ==========###########################

def addtocart(request):
    id = request.GET.get('id')

    product_obj = item.objects.get(id=int(id))
    # check if the cart exists
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart_obj = cart.objects.get(id=cart_id)
        product_in_cart = cart_obj.cartproduct_set.filter(item=product_obj)
        # item already exist in cart
        if product_in_cart.exists():
            cartproduct = product_in_cart.last()
            cartproduct.quantity += 1
            cartproduct.subtotal += product_obj.item_rate
            cartproduct.save()
            cart_obj.total += product_obj.item_rate
            cart_obj.save()
        else:
            cartproduct = CartProduct.objects.create(cart=cart_obj, item=product_obj, rate=product_obj.item_rate,
                                                     quantity=1, subtotal=product_obj.item_rate)
            cart_obj.total += product_obj.item_rate
            cart_obj.save()
    else:
        # user_id = request.session['user_name']
        up = user_details.objects.get(email=request.session['user_name'])
        cart_obj = cart(customer=up, total='0')
        cart_obj.save()
        request.session['cart_id'] = cart_obj.id
        print("new cart")
        cp = CartProduct.objects.create(cart=cart_obj, item=product_obj, rate=product_obj.item_rate, quantity=1,
                                        subtotal=product_obj.item_rate)
        cart_obj.total = float(cart_obj.total) + float(product_obj.item_rate)
        cart_obj.save()
    # context={'msg': 'added'}

    it = request.GET.get('id')
    t = item.objects.filter(id=int(it))
    # for category
    cat_id = request.GET.get('cat_id')
    cat_name = category.objects.get(id=cat_id)
    related = item.objects.filter(category=cat_name)
    r = item.objects.get(id=int(id))
    rev = review.objects.filter(item_name=r).order_by('-id')[:3]
    qs = review.objects.filter(item_name=r)
    my_count = qs.count()

    ud = user_details.objects.filter(email=request.session['user_name'])
    context = {'uname': ud,'items': t, 'related': related, 'review': rev, 'my_count': my_count}
    messages.success(request, "Successfully added to your cart")
    return render(request, 'myapp/user_product_page.html', context)


def mycart(request):
    cat_name = category.objects.all()
    ud = user_details.objects.filter(email=request.session['user_name'])

    user_id = request.session['user_name']
    up = user_details.objects.get(email=user_id)
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart1 = cart.objects.get(id=cart_id)
    else:
        cart1 = None
    context = {'category_list': cat_name,'uname': ud,'cart': cart1, 'u': up}
    return render(request, 'myapp/mycart.html', context)


def managecart(request, id):
    print("im in manage cart")
    action = request.GET.get("action")
    cp_obj = CartProduct.objects.get(id=id)

    cart_obj = cp_obj.cart
    if action == "inc":
        cp_obj.quantity += 1
        if cp_obj.quantity > cp_obj.item.opng_stock:
            messages.error(request, "Out of Stock")
            return redirect('/my-cart')
        cp_obj.subtotal += cp_obj.rate
        cp_obj.save()
        cart_obj.total += cp_obj.rate
        cart_obj.save()
    elif action == "dcr":
        cp_obj.quantity -= 1
        cp_obj.subtotal -= cp_obj.rate
        cp_obj.save()
        cart_obj.total -= cp_obj.rate
        cart_obj.save()
        if cp_obj.quantity == 0:
            cp_obj.delete()


    elif action == 'rmv':
        cart_obj.total -= cp_obj.subtotal
        cart_obj.save()
        cp_obj.delete()
    else:
        pass

    return redirect('/my-cart')


def emptycart(request):
    cart_id = request.session.get("cart_id", None)
    cart1 = cart.objects.get(id=cart_id)
    cart1.cartproduct_set.all().delete()
    cart1.total = 0
    cart1.save()
    return redirect('/my-cart')


from .forms import checkoutform


def checkout(request):
    user_id = request.session['user_name']
    user = user_details.objects.get(email=user_id)
    # for i in user:
    #     e = i.email
    cart_id = request.session.get("cart_id")
    cart_obj = cart.objects.get(id=cart_id)
    form = checkoutform(request.POST)
    if request.method == "POST":
        # order_status = "Order recived"
        address = request.POST.get("address")
        state = request.POST.get('state')
        pin=request.POST.get('pin')
        mobile = request.POST.get("Contact")
        total = request.POST.get("total")

        new_order = Order_address.objects.create(cart=cart_obj, customer=user, address=address, mobile=mobile,state=state,pin=pin,
                                          total=total)
        new_order.save()

        cart_products = cart_obj.cartproduct_set.all()
        for cart_product in cart_products:
            item = cart_product.item
            item.opng_stock -= cart_product.quantity
            item.save()
        return redirect(confirm_payment)
    else:
        context = {'cart': cart_obj, 'form': form, 'user': user}
        return render(request, 'myapp/checkout.html', context)

import os
import stripe

stripe.api_key = 'sk_test_51MzR0qSDsHoB6h4XS89hryuFO2ZLs4EGe6bs44P45Pq1pYzw1FbxRGwfHU1kcz13dX9qi9RFj2PDlFn56vF51rOe00Stz4HfFt'


#
# @app.route('checkout_session', methods=['POST'])
def checkout_session(request):
    cart_id = request.session['cart_id']
    cart_obj = cart.objects.get(id=cart_id)
    print(cart_obj.customer)

    u = user_details.objects.get(email=request.session['user_name'])
    # for i in u:
    #     name=i.fname

    order_address = Order_address.objects.filter(customer=u)
    for i in order_address:
        cart_obj = i.cart
        user = i.customer
        address = i.address
        mobile = i.mobile
        state = i.state
        pin = i.pin
        total = i.total

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': cart_obj.customer,
                },
                'unit_amount': cart_obj.total * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/pay_success',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
    )
    user_address = Orders.objects.create(cart=cart_obj, customer=user, address=address, mobile=mobile,state=state,pin=pin,
                                          total=total, order_status='order processing')
    user_address.save()

    del request.session['cart_id']
    return redirect(session.url, code=303)


# success
def pay_success(request):
    return render(request, './myapp/pay_success.html')


# cancel
def pay_cancel(request):
    return render(request, './myapp/pay_cancel.html')


def add_to_wishlist(request):
    id = request.GET.get('id')
    product_obj = item.objects.get(id=int(id))
    obj = item.objects.filter(id=int(id))
    w = wishlist.objects.filter(item= product_obj)
    up = user_details.objects.get(email=request.session['user_name'])
    for i in obj:
        rate = i.item_rate
        pic = i.item_pic
        category_name = i.category
    if w.exists():
        return redirect(wishlist_view)
    else:
        wishlist_obj = wishlist(item=product_obj, user=up, rate=rate, item_pic=pic, category_name=category_name)
        wishlist_obj.save()
        return redirect(wishlist_view)


def wishlist_view(request):
    cat_name = category.objects.all()
    ud = user_details.objects.filter(email=request.session['user_name'])
    up = user_details.objects.get(email=request.session['user_name'])
    wishlist_obj = wishlist.objects.filter(user=up)
    context = {'uname': ud,'category_list': cat_name, 'wishlist_obj': wishlist_obj}
    return render(request, './myapp/wishlist.html', context)


def delete_wishlist(request):
    id = request.GET.get('id')
    product_obj = wishlist.objects.get(id=int(id))
    product_obj.delete()
    return redirect(wishlist_view)

def user_order_status(request):
    up = user_details.objects.get(email=request.session['user_name'])
    u = user_details.objects.filter(email=request.session['user_name'])
    print(up.email)
    user_d = Orders.objects.filter(customer=up).order_by('-id')
    for i in user_d:
        print(i.customer)
        print(i.total)

    # C =
    context = {'order_status': user_d, 'uname': u}
    return render(request, './myapp/user_order_status.html', context)


def confirm_payment(request):
    user_id = request.session['user_name']
    user = user_details.objects.get(email=user_id)
    cart_id = request.session['cart_id']
    cart_obj = cart.objects.get(id=cart_id)
    print(cart_obj.total)

    context = {'cart': cart_obj, 'user': user}
    return render(request, 'myapp/confirm_payment.html', context)

#
def cancel_order(request):
    id = request.GET.get('id')
    od = Orders.objects.get(id=id)
    s = 'request for cancel'
    od.cancel_request = s
    od.save()
    # return redirect(user_order_status)
    return render(request, 'myapp/cancel_order.html')

def invoice(request):
    id=request.GET.get("id")
    ord = Orders.objects.filter(id=id)
    # for i in ord:
    #     cu = i.cart
    c = Orders.objects.get(id=id)
    cr = c.cart

    cart_obj = CartProduct.objects.filter(cart=cr)
    print('from cart obj', cart_obj)
    for i in cart_obj:
        item=i.item
        print(item)


    context = {'order_status': ord, 'items': cart_obj }
    return render(request, 'myapp/invoice.html', context)
