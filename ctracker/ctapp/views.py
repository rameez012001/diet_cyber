from multiprocessing.sharedctypes import Value
from pickle import TRUE
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from matplotlib.style import context
import pandas as pd
import math as m
from django.urls import reverse
from django.db.models import Sum

from .models import fdata
def temp(x):
  return loader.get_template(x)



def index(request):
  df=pd.read_csv(r'ctapp\csv\foodchart.csv')
  findex=df.set_index('Food')

  template = temp('index.html')
  
  if request.GET.get('food'):
    q= request.GET['food']
    x1=findex.loc[q,'Calories']
    x2=findex.loc[q,'Protein']
    x3=findex.loc[q,'Fat']

    a = fdata(food=q,calories=x1,protein=x2,fat=x3)
    a.save()
  else:
      False 
  data = fdata.objects.all().values()
  
  # items = fdata.objects.all().aggregate(Sum('calories'))
  item= fdata.objects.all()
  totcal = sum(item.values_list('calories', flat=True))
  totpro = sum(item.values_list('protein', flat=True))
  totfat = sum(item.values_list('fat', flat=True))


  context = {
    'fdata': data,
    'cal':totcal,
    'pro':totpro,
    'fat':format(totfat,".1f")
  }
  return HttpResponse(template.render(context, request)) 

def deleteall(request):
  fdata.objects.all().delete()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = fdata.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))