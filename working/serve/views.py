from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import data
from .serializers import dataSerializer
from .forms import enteryForm
from django.views.generic import TemplateView
# Create your views here.
def ToDo(request):
	return render(request,'serve/ToDo.html')
class datalist(APIView ):

	def get(self,request):
		Data = data.objects.all()
		serializer=dataSerializer(Data,many=True)
		return Response(serializer.data)
	def post(self):
		pass


class EnterView(TemplateView):
	template_name='serve/enter_data.html'

	def get(self,request):
		form=enteryForm()
		return render(request,self.template_name,{'form':'form'})
	def post(self,request):
		form=enteryForm[request.POST]
		if form.is_valid():

			Topic=cleaned_data['Topic']
			Level=cleaned_data['Level']
			Question=cleaned_data['Question']
			Answer=cleaned_data['Answer']

			form.save()

			return redirect('ToDo/')
		args={'form':form,'Topic':Topic,'Level':'Level','Questions':'Question','Answer':'Answer'}
		return render(request,self.template_name,args)