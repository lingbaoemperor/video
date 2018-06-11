from django.shortcuts import render
from django.http import HttpResponse
from video.settings import BASE_DIR
from django.http import HttpResponseRedirect 
from django import forms
from show_video.models import Users,Video,User_Video
import datetime as dt

# Create your views here.
class UploadForm(forms.Form):
	video = forms.FileField()

def test(req):
	#return HttpResponse('<p>Hello World!!!</p>')
	return render(req,'main.html')

#进入开始界面
def init(req):
	if req.method == 'POST':
		if True:
			return HttpResponseRedirect('/list/')
	else:
		return render(req,'login.html')

def list_page(req):
	return render(req,'list_page.html')

def switch_to_upload(req):
	return HttpResponseRedirect('/upload/')

def upload(req):
	if req.method == 'GET':
		uf = UploadForm()
		return render(req,'upload_page.html',{'uf':uf})
	else:
		uf = UploadForm(req.POST,req.FILES)
		if uf.is_valid():
			#获取表单提交的模板信息
			myfile = uf.cleaned_data['video']
			video = Video()
			video.size = myfile.size
			video.date = dt.datetime.now()
			video.file = myfile
			video.save()
			#with open(BASE_DIR+'/media/img/'+myfile.name,'wb') as f:
			#	try:
			#		for chunk in myfile.chunks():
			#			f.write(chunk)
			#	finally:
			#		f.close()
		else:
			uf = UploadForm()
			return render(req,'upload_page.html',{'uf':uf})
		#return HttpResponse('OK!!!')
		return HttpResponseRedirect('/list/')

def play(req):
	return render(req,'play_video.html')
