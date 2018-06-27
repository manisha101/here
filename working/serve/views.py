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
		return render(request,self.template_name,{'form':form})
	def post(self,request):
		form=enteryForm(request.POST)
		if form.is_valid():

			# topic=cleaned_data['topic']
			# level=cleaned_data['level']
			# question=cleaned_data['question']
			# answer=cleaned_data['answer']

			form.save()

			return redirect('enter')
		args={'form':form,'Topic':topic,'Level':level,'Questions':question,'Answer':answer}
		return render(request,self.template_name,args)