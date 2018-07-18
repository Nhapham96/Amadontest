from django.shortcuts import render,HttpResponse,redirect
from apps.amadon.models import *
def index(req):
    context = {
        "items": Product.objects.all(), 
    } 
    return render(req,'amadon/index.html',context)
def buy(req,id):
    
    item = Product.objects.get(id=id)
    price =float(item.price)
    req.session['price']=price
    req.session['Quantity'] = req.POST['quantity']
    req.session['Total']= float(price) * float(req.session['Quantity'])
    if 'total' not in req.session:
        req.session['total'] = float(price) * float(req.session['Quantity'])
    else:
        req.session['total'] += float(price) * float(req.session['Quantity'])
    if 'total_Quantity' not in req.session:
        req.session['total_Quantity'] = int(req.session['Quantity'])
    else:
        req.session['total_Quantity'] = int(req.session['total_Quantity'])+ int(req.session['Quantity'])

    print(req.session['total'])
    return redirect('/reciept')
def reciept(req):
    context={
        'price':req.session['price'],
        'Quantity':req.session['Quantity'],
        'total': req.session['total'],
        'Total':req.session['Total'],
        'total_Quantity':req.session['total_Quantity']
    }

    return render(req,'amadon/reciept.html',context)
def reset(req):
    req.session.clear()
    return redirect('/')

