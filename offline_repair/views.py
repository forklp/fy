from django.shortcuts import render
from . import models
from django.shortcuts import redirect
# Create your views here.
def repair_form(request):
    if request.method == 'POST':
        message = '报修成功'
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
        computerperipheral = request.POST['form-peripheral']
        computerdestroy = request.POST['form-destroy']
        computerdata = request.POST['form-data']
        try:
            computerserver = request.POST.getlist('form-server')
        except:
            computerserver = '无'
        try:
            computerreset = request.POST['form-reset']
        except:
            computerreset = '0'
        try:
            computerclear = request.POST['form-clear']
        except:
            computerclear = '0'
        computerdescription = request.POST['form-description']
        # server = ' '
        # server.join(computerserver)
        if computerreset == '1':
            computerreset = True
        else:
            computerreset = False
        if computerclear == '1':
            computerclear = True
        else:
            computerclear = False
        try:
            user = models.User.objects.get(user_name=username)
            computer = models.Computer.objects.create(computer_user=user, computer_name=computername, computer_get_code=computergetcode, computer_password=computerpassword, computer_peripheral=computerperipheral, computer_destroy=computerdestroy, computer_backups_data=computerdata, computer_server=computerserver, computer_is_reset=computerreset, computer_is_clear=computerclear,computer_description=computerdescription)
            computer.save()
        except:
            p = models.User.objects.create(user_name=username, user_sex=usersex, user_phone_first=userphone, user_phone_second=userphone2, user_address=useraddress, user_qq=userqq, user_id_card=userid, user_fy_vip=uservip)
            p.save()
            computer = models.Computer.objects.create(computer_user=p, computer_name=computername, computer_get_code=computergetcode, computer_password=computerpassword, computer_peripheral=computerperipheral, computer_destroy=computerdestroy, computer_backups_data=computerdata, computer_server=computerserver, computer_is_reset=computerreset, computer_is_clear=computerclear, computer_description=computerdescription)
            computer.save()

        return render(request, 'repair_form.html',{'message': message})
    else:
        return render(request, 'repair_form.html')


def index(request):
    return render(request, 'index.html')

def login(request):
    if 'name' in request.session:
        return redirect('/technician')
    else:
        if request.method == 'POST':
            username = request.POST['account']
            password = request.POST['password']
            try:
                technician = models.Technician.objects.get(technician_account=username)
                if technician.technician_password == password:
                    request.session['name'] = technician.technician_name
                    return redirect('/technician')
                message = '密码错误'
                return render(request, 'login.html', {'message': message})
            except:
                message = '账号不存在'
                return render(request, 'login.html', {'message': message})
        return render(request, 'login.html')

def technician(request):
    if 'name' in request.session:
        if request.method == 'POST':
            computeruser = request.POST['search']
            try:
                message = request.session['name']
                computer_user = models.User.objects.get(user_name=computeruser)
                computersearch = models.Computer.objects.filter(computer_user=computer_user)
                return render(request, 'technician.html', locals())
            except:
                message1 = '此机主不存在'
                message = request.session['name']
                computers = models.Computer.objects.all()
                return render(request, 'technician.html', locals())
        message = request.session['name']
        computers = models.Computer.objects.all()
        return render(request, 'technician.html', locals())
    return redirect('/login')


def computer(request, computerid):
    try:
        computer = models.Computer.objects.get(id=computerid)
        return render(request, 'computer.html', locals())
    except:
        return render(request, 'computer.html')

