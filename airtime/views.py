from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions
import africastalking
import requests
import os
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def sendAirtime(request):
    # Set your app credentials
    username = os.environ.get('USERNAME')
    api_key = os.environ.get('API_KEY')

    # Initialize the SDK
    africastalking.initialize(username, api_key)

    # Get the airtime service
    airtime = africastalking.Airtime

    # Set phone_number in international format
    phone_number = '+254703616854'

    # Set The 3-Letter ISO currency code and the amount
    amount = "5"
    currency_code = "KES"

    try:
        # That's it, hit send, and we'll take care of the rest
        responses = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        print(responses)
    except Exception as e:
        print("Encountered an error while sending airtime: %s" % str(e))

    return Response({'message': 'Airtime sent successfully'})  # Add a response to indicate success

