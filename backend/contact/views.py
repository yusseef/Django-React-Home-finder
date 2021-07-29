from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request, format=None):
        data = self.request.data
        try:
            send_mail(
                data['subject'],
                'Name:' 
                + data['name'] 
                + '\nEmail:' 
                + data['email']
                +'\n\nMessage: \n'
                +data['message'],
                'realstateapp22@gmail.com',
                ['realstateapp22@gmail.com'],
                fail_silently=False
            )
            contact = Contact(name=data['name'], email = data['email'], subject = data['subject'], message = data['message'])
            contact.save()
            return Response({'success': 'message was sent succesfully'})
        except:
            return Response({'error':"Message faild to send"})