from django.shortcuts import render
from . import models
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