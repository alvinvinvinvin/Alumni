# Create your views here.
from datetime import datetime
import operator
import re

from django.core.mail import send_mail
from django.core.mail.message import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.template.context import RequestContext

from MSE_Alumni.models import *
from django.views.generic.edit import FormView
from .models import Attachment
from django.views.generic import ListView
from django.core.context_processors import request


def home(request):
    #send_mail('Subject here', 'Here is the message.','uwl.mse@gmail.com',['svenchen90@gmail.com','chen.gong@uwlax.edu'], fail_silently=False)
    '''
    subject, from_email = 'hello', 'uwl.mse@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p><p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['uwl_mse@yahoo.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    '''
    #admin_mail_verification(['svenchen90@gmail.com'], 'register')
    
    messages = Message.objects.all().order_by('-date')[0:3]
    
    return render(request, 'index.html',{'messages':messages })

'''
def signin(request):
    if request.method == 'POST':
        user = User.objects.filter(account=request.POST['account'],\
                                   password=request.POST['password'],\
                                   type=request.POST['type'])
        if len(user) == 0:
            return render(request, 'index.html')
        else :
            if request.POST['type'] == '0':
                request.session['user'] = user.get(account=request.POST['account'])
            else:
                alumni = Alumni.objects.filter(user=user.get(account=request.POST['account']))[0]
                print alumni.status
                if alumni.status == '1':
                    request.session['user'] = Alumni.objects.filter(user=user.get(account=request.POST['account']))[0]
            return render(request, 'index.html')
    else : 
        return render(request, 'index.html')
'''
    
def signout(request):
    request.session.flush()
    return redirect('/')


#Start of Alumnus functionality
def register(request):
    if request.method == 'POST':
        if len(User.objects.filter(account=request.POST['account'])) == 0:
            if request.POST['password'] == request.POST['password_confirm']:
                new_user = User(account = request.POST['account'],\
                                password = request.POST['password'],\
                                type = 1)
                new_user.save()
                
                new_alumni = Alumni(user = new_user,\
                                    first_name = request.POST['first_name'],\
                                    last_name = request.POST['last_name'],\
                                    email = request.POST['email'],\
                                    graduate_date = request.POST['graduate_date']+'-01',\
                                    gender = request.POST['gender'],\
                                    status =0)
                new_alumni.save()
                admin_mail_verification([request.POST['email']],'register')
                return redirect('/')
            else:
                return render(request, 'register.html') 
        else:
            return render(request, 'register.html')
    else:
        return render(request,'register.html')
    
def education_add(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        context={}
        context['education_list'] = Education_Exp.objects.filter(alumni_id = request.session['user'].id)
        if request.method == 'GET':
            return render(request,'education_add.html',context)
        else:
            new_education = Education_Exp(alumni=request.session['user'],\
                                          major=request.POST['major'],\
                                          start_date=request.POST['start_date']+'-01',\
                                          end_date=request.POST['end_date']+'-01',\
                                          school=request.POST['school'],\
                                          address=request.POST['address'],\
                                          city=request.POST['city'],\
                                          state=request.POST['state'],\
                                          zip=request.POST['zip'],\
                                          description=request.POST['description'])
            new_education.save()
            return redirect('/education_view/')
    else:
        return redirect('/')

def education_view(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        context={}
        context['education_list'] = Education_Exp.objects.filter(alumni_id = request.session['user'].id)
        
        if 'education_id' not in request.GET:
            return render(request,'education_view.html',context)
        else:
            education = Education_Exp.objects.get(id=request.GET['education_id'])
            context['education'] = education
            return render(request,'education_view.html',context)
    else:
        return redirect('/')
    
    
def education_update(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        Education_Exp.objects.filter(id=request.POST['education_id']).update(major=request.POST['major'],\
                                          start_date=request.POST['start_date']+'-01',\
                                          end_date=request.POST['end_date']+'-01',\
                                          school=request.POST['school'],\
                                          address=request.POST['address'],\
                                          city=request.POST['city'],\
                                          state=request.POST['state'],\
                                          zip=request.POST['zip'],\
                                          description=request.POST['description'])
        return redirect('/education_view/?education_id='+request.POST['education_id'])
    else:
        return redirect('/')

def working_add(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        context={}
        context['working_list'] = Working_Exp.objects.filter(alumni_id = request.session['user'].id)
        if request.method == 'GET':
            return render(request,'working_add.html',context)
        else:
            new_working = Working_Exp(alumni=request.session['user'],\
                                          title=request.POST['title'],\
                                          start_date=request.POST['start_date']+'-01',\
                                          end_date=request.POST['end_date']+'-01',\
                                          company=request.POST['company'],\
                                          address=request.POST['address'],\
                                          city=request.POST['city'],\
                                          state=request.POST['state'],\
                                          zip=request.POST['zip'],\
                                          description=request.POST['description'])
            new_working.save()
            return redirect('/working_view/')
    else:
        return redirect('/')
    
def working_view(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        context={}
        context['working_list'] = Working_Exp.objects.filter(alumni_id = request.session['user'].id)
        
        if 'working_id' not in request.GET:
            return render(request,'working_view.html',context)
        else:
            working = Working_Exp.objects.get(id=request.GET['working_id'])
            context['working'] = working
            return render(request,'working_view.html',context)
    else:
        return redirect('/')
    
def working_update(request):
    if 'user' in request.session and hasattr(request.session['user'], 'user'):
        Working_Exp.objects.filter(id=request.POST['working_id']).update(title=request.POST['title'],\
                                          start_date=request.POST['start_date']+'-01',\
                                          end_date=request.POST['end_date']+'-01',\
                                          company=request.POST['company'],\
                                          address=request.POST['address'],\
                                          city=request.POST['city'],\
                                          state=request.POST['state'],\
                                          zip=request.POST['zip'],\
                                          description=request.POST['description'])
        return redirect('/working_view/?working_id='+request.POST['working_id'])
    else:
        return redirect('/')

def search(request):
    context = {}
    if 'text_search' not in request.POST:
        all_alumnus = Alumni.objects.filter(status=1).order_by('graduate_date')
        context['alumnus'] = all_alumnus
        return render(request, 'alumni_search.html', context)
    else:
        context['alumnus'] = search_component(request.POST['text_search'])
        return render(request, 'alumni_search.html',context)
#End of Alumnus functionality


#Start of Admin functionality
def admin_search(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        context = {}
        context['list_year'] = getgraduationyears()
        
        if 'pending' in request.GET:
            context['pending'] = 1
            alumnus = Alumni.objects.filter(status=0).order_by('graduate_date')
        elif 'year' not in request.GET and 'text_search' not in request.GET:
            alumnus = Alumni.objects.filter(status=1).order_by('graduate_date')
        elif 'year' in request.GET and 'text_search' not in request.GET:
            alumnus = Alumni.objects.filter(graduate_date__year = request.GET['year'], status=1).order_by('graduate_date')
            context['year'] = int(request.GET['year'])
        elif 'year' not in request.GET and 'text_search' in request.GET:
            alumnus = search_component(request.GET['text_search'])
        else:
            alumnus = {}
        
        context['alumnus'] = alumnus
        return render(request, 'admin_search.html', context)
    else:
        return redirect('/')

#Email Notification
def admin_comfirmregistration(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        if request.GET['approve'] == '0':
            user_id = Alumni.objects.filter(id=request.GET['id'])[0].user.id
            
            admin_mail_verification([Alumni.objects.filter(id=request.GET['id'])[0].email], 'deny')
            
            Alumni.objects.filter(id=request.GET['id']).delete()
            User.objects.filter(id=user_id).delete()
        elif request.GET['approve'] == '1':
            Alumni.objects.filter(id=request.GET['id']).update(status=1);
            
            admin_mail_verification([Alumni.objects.filter(id=request.GET['id'])[0].email], 'approve')
        
        return redirect('/admin_search?pending')
    else:
        return redirect('/')
    
#Group management
def admin_groups(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        context = {}
        context['list_groups'] = Group.objects.all()
        
        if 'addgroup' in request.GET:
            context['alumnus'] = Alumni.objects.filter(status=1).order_by('graduate_date')
            context['tag'] = 'addgroup'
            return render(request, 'admin_group.html', context) 
        elif 'addgroup' in request.POST:
            new_group = Group(name = request.POST['groupname'])
            new_group.save()
            for member in request.REQUEST.getlist('to_add'):
                new_group.alumnis.add(Alumni.objects.filter(id=member)[0])
            
            return redirect('/admin_groups?addgroup=1')
        elif 'group_id' in request.GET:
            group = Group.objects.filter(id=request.GET['group_id'])[0]
            list_members = []
            for m in group.alumnis.all():
                list_members.append(m.id)
            condition = reduce(operator.and_, [~Q(id=me) for me in list_members]+[Q(status=1)])
            avaliable = Alumni.objects.filter(condition).order_by('graduate_date')
            context['group'] = group
            context['avaliable'] = avaliable
            return render(request, 'admin_group.html', context)
        elif 'addmembers' in request.POST:
            group = Group.objects.filter(id=request.POST['group_id'])[0]
            for member in request.REQUEST.getlist('to_add'):
                group.alumnis.add(Alumni.objects.filter(id=member)[0])
            return redirect('/admin_groups?group_id=' + str(group.id))
        elif 'removemembers' in request.POST:
            group = Group.objects.filter(id=request.POST['group_id'])[0]
            for member in request.REQUEST.getlist('to_remove'):
                group.alumnis.remove(Alumni.objects.filter(id=member)[0])
            return redirect('/admin_groups?group_id=' + str(group.id))
        else:
            return redirect('/admin_groups?addgroup')
    else:
        return redirect('/')
    
# Email 
def admin_mail_verification(list_to,type):
    from_email = 'uwl.mse@gmail.com'
    if type == 'register':
        subject = 'Notification from UWL-MSE Alumnus'
        content = '<p>Thank you for register at UWL-MSE Alumnus.</p><p>This is an response message.Please wait for administrator to verify your information!</p>'
    elif type == 'approve':
        subject = 'Notification from UWL-MSE Alumnus'
        content = '<p>Thank you for register at UWL-MSE Alumnus.</p><p>Congratulations!Your application of registration  has been approved!Y</p>'
    elif type == 'deny':
        subject = 'Notification from UWL-MSE Alumnus'
        content = '<p>Thank you for register at UWL-MSE Alumnus.</p><p>Sorry.Your application of registration has been denied!You can contact us if you have any question.</p>'
    else:
        return
    msg = EmailMultiAlternatives(subject, content, from_email, list_to)
    msg.attach_alternative(content, "text/html")
    msg.send()

def admin_mail_message(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        from_email = 'uwl.mse@gmail.com'
        subject = request.POST['subject']
        content = request.POST['content']
        list_to = []
        group = Group.objects.filter(id = request.POST['group_id'])[0]
        
        for alu in group.alumnis.all():
            list_to.append(alu.email)
            
        msg = EmailMultiAlternatives(subject, content, from_email, list_to)
        msg.send()
        return redirect('/admin_groups?group_id=' + str(group.id))
    else:
        return redirect('/')
    
def admin_view_profile(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        if 'alumni_id' in request.GET:
            alumni = Alumni.objects.filter(id = request.GET['alumni_id'])
            if len(alumni) == 0:
                return redirect('/') 
            else:
                return render(request, 'admin_alumniprofile.html',{'alumni' : alumni[0],\
                                                                   'education' : Education_Exp.objects.filter(alumni_id=request.GET['alumni_id']),\
                                                                   'working' : Working_Exp.objects.filter(alumni_id=request.GET['alumni_id'])})
        else:
            return redirect('/')
    else:
        return redirect('/')
         
    
#upload file

def admin_message(request):
    if request.method == 'POST':
        if request.FILES is None:
            form = DocumentForm(request.POST)
            new_message = Message(subject=request.POST['subject'],\
                                  date = datetime.now(),\
                                  abstract=request.POST['abstract'],\
                                  docfile = None)
            new_message.save()

            # Redirect to the document list after POST
            return redirect('/admin_message/')
        else:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                docfiles = request.FILES.getlist('docfile',False)
                if not docfiles:
                    new_message = Message(subject=request.POST['subject'],\
                                      date = datetime.now(),\
                                      abstract=request.POST['abstract'])
                elif len(docfiles) == 1:
                    new_message = Message(subject=request.POST['subject'],\
                                      date = datetime.now(),\
                                      abstract=request.POST['abstract'],\
                                      docfile1 = docfiles[0])
                elif len(docfiles) == 2:
                    new_message = Message(subject=request.POST['subject'],\
                                      date = datetime.now(),\
                                      abstract=request.POST['abstract'],\
                                      docfile1 = docfiles[0],\
                                      docfile2 = docfiles[1])
                elif len(docfiles) == 3:
                    new_message = Message(subject=request.POST['subject'],\
                                      date = datetime.now(),\
                                      abstract=request.POST['abstract'],\
                                      docfile1 = docfiles[0],\
                                      docfile2 = docfiles[1],\
                                      docfile3 = docfiles[2])
                new_message.save()
                    
                # Redirect to the document list after POST
                return redirect('/admin_message/')
            else:
                new_message = Message(subject=request.POST['subject'],\
                                      date = datetime.now(),\
                                      abstract=request.POST['abstract'])
                new_message.save()
                return redirect('/admin_message/')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    messages = Message.objects.all().order_by('date')

    # Render list page with the documents and the form
    return render(request, 'admin_message.html', {'messages': messages, 'form': form})

#Admin account management
def admin_account(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        accounts = User.objects.filter(type = '0').order_by('first_name')
        
        return render(request, 'admin_account.html', {'accounts':accounts})
    else:
        return redirect('/')
    
#Add new admin account
def admin_account_add(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        message = {}
        if request.method == 'POST':
            if len(User.objects.filter(account=request.POST['account'])) == 0:
                new_account = User(account = request.POST['account'],\
                                                password = request.POST['password'],\
                                                first_name = request.POST['first_name'],\
                                                last_name = request.POST['last_name'],\
                                                type = '0')
                new_account.save()
                return redirect('/admin_account/')
            else:
                message['message'] = 'Account already existed.'
                return render(request, 'admin_account_add.html',{'message':message})
        else:
            return render(request, 'admin_account_add.html')
    else:
        return redirect('/')
    
def admin_account_update(request):
    if 'user' in request.session and hasattr(request.session['user'], 'type'):
        message = {}
        response=HttpResponse()  
        response['Content-Type']="text/javascript"
        if request.method == 'GET':
            if 'account' not in request.GET:
                message['message'] = 'please select one account first.'
                return render(request,'admin_account.html',{'message':message})
            else:
                context = {}
                user = User.objects.get(account=request.GET['account'])
                context['user'] = user
                return render(request,'admin_account_update.html',{'context':context})
        elif request.method == 'POST':
            User.objects.filter(id=request.POST['account']).update(password=request.POST['password'],\
                                          first_name=request.POST['first_name'],\
                                          last_name=request.POST['last_name'])
            response.write('1')
        else:
            response.write('0')
    else:
        return redirect('/')
    return

def admin_account_delete(request):
    return
#AJAX
def ajax_signin(request):
    response=HttpResponse()  
    response['Content-Type']="text/javascript"
    
    user = User.objects.filter(account=request.POST['account'],\
                               password=request.POST['password'],\
                               type=request.POST['type'])
    if len(user) == 0:
        response.write('0')       
    else:
        if request.POST['type'] == '0':
            request.session['user'] = user.get(account=request.POST['account'])
        else:
            alumni = Alumni.objects.filter(user=user.get(account=request.POST['account']))[0]
            if alumni.status == '1':
                request.session['user'] = Alumni.objects.filter(user=user.get(account=request.POST['account']))[0]
                response.write('1')
            else:
                response.write('0')
    return response

def ajax_register(request):
    response=HttpResponse()  
    response['Content-Type']="text/javascript"
    
    validate1 = User.objects.filter(account=request.POST['account'])
    validate2 = Alumni.objects.filter(email=request.POST['email'])
    
    if len(validate1) == 0 and len(validate2) == 0:
        new_user = User(account = request.POST['account'],\
                        password = request.POST['password'],\
                        type = 1)
        new_user.save()
        
        new_alumni = Alumni(user = new_user,\
                            first_name = request.POST['first_name'],\
                            last_name = request.POST['last_name'],\
                            email = request.POST['email'],\
                            graduate_date = request.POST['graduate_date']+'-01',\
                            gender = request.POST['gender'],\
                            status =0)
        new_alumni.save()
        admin_mail_verification([request.POST['email']],'register')
        response.write('0')
    elif len(validate1) != 0 and len(validate2) == 0:
        response.write('1')
    elif len(validate1) == 0 and len(validate2) != 0:
        response.write('2')
    elif len(validate1) != 0 and len(validate2) != 0:
        response.write('3')
    else:
        response.write('-1')
    return response
    

# trivial
def search_component(text_search):
    list_input = text_search.split(' ')
    list_search = []
    
    for i in list_input:
        if i != '':
            list_search.append(i)        

    if len(list_search) != 0:
        years, others = getyearsfromarry(list_search)
        
        if len(years) == 0 and len(others) != 0:
            condition = reduce(operator.or_, [Q(first_name__icontains=f) for f in others]\
                               +[Q(last_name__icontains=l) for l in others])
            
        elif len(years) !=0 and len(others) != 0:
            condition1 = reduce(operator.or_, [Q(graduate_date__year=y) for y in years])
            condition2 = reduce(operator.or_, [Q(first_name__icontains=f) for f in others]\
                               +[Q(last_name__icontains=l) for l in others])
            condition = reduce(operator.and_, [condition1,condition2])
            print condition
        elif len(years) !=0 and len(others) == 0:
            condition = reduce(operator.or_, [Q(graduate_date__year=y) for y in years])
             
        condition = reduce(operator.and_, [condition,Q(status=1)])
        return Alumni.objects.filter(condition).order_by('graduate_date')
    else:
        return Alumni.objects.filter(status=1).order_by('graduate_date')
    
def getyearsfromarry(str_list):
    years = []
    others = []
    
    pattern = re.compile(r'\d')
    
    for s in str_list:
        match = pattern.match(s)
        if match:
            if len(s) == 4:
                years.append(s)
        else:
            others.append(s)
    return years, others

def getgraduationyears():
    years = []
    all = Alumni.objects.filter(status=1)
    for a in all:
        if a.graduate_date.year not in years:    
            years.append(a.graduate_date.year)
    years.sort(key=int)
    return years