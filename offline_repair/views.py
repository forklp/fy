from django.shortcuts import render

# Create your views here.
def repair_form(request):
    if request.method == 'POST':
        try:
            username = request.POST['form-username']
            usersex = request.POST['form-sex']
            userphone = request.POST['form-phone']
            userphone2 = request.POST['form-phone2']
            useraddress = request.POST['form-address']
            userqq = request.POST['form-qq']
            userid = request.POST['form-idcard']
            uservip = request.POST['form-fyvip']
            computergetcode = request.POST['form-getcode']
            computername = request.POST['form-computer']
            computerpassword = request.POST['form-password']
        except:
            pass
    return render(request, 'repair_form.html')

def index(request):
    return render(request, 'index.html')