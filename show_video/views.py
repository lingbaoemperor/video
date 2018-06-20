from django.shortcuts import render
from django.http import HttpResponse
from video.settings import BASE_DIR
from django.http import HttpResponseRedirect 
from django import forms
from show_video.models import Users,Video,User_Video
import datetime as dt
from show_video.models import Video
from django.contrib import messages

# Create your views here.
class UploadForm(forms.Form):
	video = forms.FileField()

def isOnline(req):
	if 'username' in req.session.keys():
		return True
	return False
#上传
def upload(req):
	if isOnline(req) == False:
		return HttpResponseRedirect('/login/')
	if req.method == 'POST':
		#接受上传,只用了表单模型，手动创建一条数据实例保存
		uf = UploadForm(req.POST,req.FILES)
		if uf.is_valid():
			#获取表单提交的模板信息
			myfile = uf.cleaned_data['video']
			fname = myfile.name.split('.')
			print(fname)
			if len(fname) == 2:
				#视频
				if fname[1] in ['webm','mp4','ogg']:
					print(fname[1])
					video = Video()
					video.size = myfile.size
					video.date = dt.datetime.now()
					video.file = myfile
					video.save()
					return HttpResponseRedirect('/list/')
				#文本
				elif fname[1] in ['zip','txt','rar']:
					#novel = Novel()
					#novel.size = 1
					#novel.date = dt.datetime.now()
					#novel.file =myfile
					#novel.save()
					return HttpResponseRedirect('/list/')
			return render(req,'upload_page.html',{'uf':uf,'error':'注意文件格式！！！'})
	#加载登录界面
	uf = UploadForm()
	return render(req,'upload_page.html',{'uf':uf})

def play(req,video):
	#video文件编号
	query = Video.objects.filter(v_id=video)
	name = query[0].file
	name = str(name).split('.')[0]
	return render(req,'play_video.html',{'video_name':name})

def play_test(req):
	if isOnline(req) == False:
		return render(req,'login.html')
	if req.method == "POST":
		if 'video_name' not in req.POST.keys():
			print('aaa!!!')
		vn = req.POST['video_name']
		return render(req,'play_video.html',{'video_name':vn})
