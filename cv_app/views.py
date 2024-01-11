from django.shortcuts import render
from .models import information
from django.http import HttpResponse
from django.template import loader
import io
import pdfkit

def home(request):
    info = information.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        university = request.POST.get('university','')
        previouswork = request.POST.get('previouswork','')
        info_cv = information(name=name,email=email,phone=phone,summary=summary,university=university,previouswork=previouswork)        
        info_cv.save()
    return render(request, 'home.html',{'info':info})


def createpdf(request, id):

    info = information.objects.get(pk=id)
    

    # get the template html
    template = loader.get_template('templatepdf.html')
    #info to render on html
    html = template.render({'info':info})
    #options pdf kit
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    #configuration to start the convertion
    config = pdfkit.configuration(wkhtmltopdf=r'C:\wkhtmltox\bin\wkhtmltopdf.exe')

    #convert html to pdf
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    #customazing convertion
    response = HttpResponse(pdf,content_type='application/pdf')
    # configuration https://stackoverflow.com/questions/27673870/cant-create-pdf-using-python-pdfkit-error-no-wkhtmltopdf-executable-found
    response ['Content-Disposition'] ='attachment'
    return response
