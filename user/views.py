
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from user.models import Users
from show_video.models import Video

# Create your views here.

#注册表单(表单模板和数据库模板)
class RegisterForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = "__all__"

#登录表单
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

def isOnline(req):
	if 'username' in req.session.keys():
		return True
	return False
#登录界面
def init(req):
	if req.method == 'POST':
		uf = LoginForm(req.POST)
		if uf.is_valid():
			un = uf.cleaned_data['username']
			pw = uf.cleaned_data['password']
			result = Users.objects.filter(username=un,password=pw)
			if result:
				req.session['username'] = un
				return HttpResponseRedirect('/list/')

	uf = LoginForm()
	return render(req,'login.html',{'uf':uf})
#主界面
def list_page(req):
	if isOnline(req) == False:
		return HttpResponseRedirect('/login/')
	return render(req,'list_page.html')

def register(req):
	if req.method == "POST":
		uf = RegisterForm(req.POST)
		#new_user = uf.save(commit=False)
		#print(new_user.username,new_user.password,new_user.name)
		#如果主键和已有数据重复这个条件就不成立
		if uf.is_valid():
			new_user = uf.save()
			uf = LoginForm()
			return render(req,'login.html',{'uf':uf})
		return HttpResponse('<html>用户名已存在！！！</html>')
	uf = RegisterForm()
	return render(req,'register.html',{'uf':uf})

#显示资源
def video(req):
	if isOnline(req) == False:
		return HttpResponseRedirect('/login/')
	if req.method == 'POST':
		result = Video.objects.all()
		#print(result)
		querylist = list()
		#转成列表传到前台
		for item in result:
			a = {'name':item.file,'date':item.date,'size':item.size,'v_id':item.v_id}
			querylist.append(a)
		return render(req,'list_page.html',{'queryset':querylist})
	return render(req,'list_page.html')

def novel(req):
	return render(req,'list_page.html')
