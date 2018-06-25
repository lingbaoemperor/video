from django.shortcuts import render
from django.http import HttpResponse
from video.settings import BASE_DIR
from django.http import HttpResponseRedirect 
from django import forms
from show_video.models import Users,Video,User_Video
import datetime as dt
from show_video.models import Video
from django.contrib import messages
from user.models import Users
from show_video.models import User_Video
import os

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
			#获取用户实例,添加关联要用
			username = Users.objects.get(username=req.session['username'])
			print(username)
			if len(fname) == 2:
				#视频
				if fname[1] in ['webm','mp4','ogg','png','css','jpg']:
					#print(fname[1])
					video = Video()
					video.size = myfile.size
					video.date = dt.datetime.now()
					video.file = myfile
					video.save()
					#把用户和视频信息关联，同时保存，（add也可以，但多对一和多对多不一样）
					video.user_video_set.create(username=username)
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

#接受参数video
def play(req,video):
	#video文件编号
	query = Video.objects.filter(v_id=video)
	name = query[0].file
	name = str(name).split('.')[0]
	return render(req,'play_video.html',{'video_name':name})
def delete(req,id):
	if isOnline(req) == False:
		return HttpResponseRedirect('/login/')
	query = Video.objects.filter(v_id=id)
	path = str(query[0].file)
	query.delete()
	os.remove(BASE_DIR+'/media/'+path)
	return HttpResponseRedirect('/video/')

