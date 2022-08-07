from django.shortcuts import render,redirect, get_object_or_404
from website.models import Book
from .forms import BookAddForm
from django.contrib import messages
import symbl
import time
import requests
import json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile, File
from django.conf import settings
from django.http import HttpResponse
import os

# Create your views here.
def page2(request):
    return render(request, 'page2.html',{})

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Book added successfully")
            



            app_id = "597473436d506b356d4a415969777a76754b41356b7445753659385551516832"
            app_secret = "6e71415a673879304574415948594e4352764733324a586563745947493052724833783872476f314a2d48776574485574694f414b566d7767594f2d464c7a68"

            url = "https://api.symbl.ai/oauth2/token:generate"
            headers = {
                "Content-Type": "application/json"
            }
            request_body = {   
              "type": "application",
              "appId": app_id,
              "appSecret": app_secret
            }
            response = requests.post(url, headers=headers, json=request_body)
            #book = get_object_or_404(Book, pk=1)
            #path=book.file_path
            #print(str(path))
            print(response.json())


            print(response.json())
            l=response.json()
            print(l['accessToken'])
            access_token = l['accessToken']
            file_path = (r'C:\Users\srija\Downloads\sample_video_file.mp4')
            symblai_params = {
            #"name": "<NAME>"
            }
            headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "video/mp4"
            }
                 #file_path
            with open(file_path, "rb") as file:
             request_body = file.read()

             response = requests.request(
                method="POST", 
                url="https://api.symbl.ai/v1/process/video",
                params=symblai_params,
                headers=headers,
                data=request_body
                )
            print(response.json())
            a=response.json()
            conversationid= a['conversationId']
            jobid= a['jobId']

            access_token = access_token
            conversation_id = conversationid

            headers = {
                "Authorization": "Bearer " + access_token,
                "Content-Type": "application/json"
                }      
            


            response = requests.request(
                method="GET", 
                url="https://api.symbl.ai/v1/conversations/" + conversation_id + "/messages?sentiment=true",
                headers=headers
                )
            print(json.dumps(response.json(), indent=2))
            url = "https://api.symbl.ai/v1/conversations/messages"

            headers = {
            "Accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFVUTRNemhDUVVWQk1rTkJNemszUTBNMlFVVTRRekkyUmpWQ056VTJRelUxUTBVeE5EZzFNUSJ9.eyJodHRwczovL3BsYXRmb3JtLnN5bWJsLmFpL3VzZXJJZCI6IjQ3MjY5MzU5MTI0NDgwMDAiLCJpc3MiOiJodHRwczovL2RpcmVjdC1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiWXRzQ21QazVtSkFZaXd6dnVLQTVrdEV1Nlk4VVFRaDJAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vcGxhdGZvcm0ucmFtbWVyLmFpIiwiaWF0IjoxNjU5NzYxOTI2LCJleHAiOjE2NTk4NDgzMjYsImF6cCI6Ill0c0NtUGs1bUpBWWl3enZ1S0E1a3RFdTZZOFVRUWgyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.SsjhzVwWfaahkepUdFlrN-il4YW0CaOJZDz7eFv1l4McEef3DX4j4hrAT2lnlboAMsByiyaPaNHoij3nhDgqAmDyG6bTkIpQDTOLMFkr3o-YGQ5M3LV1nn3zo4gqgh6vIRgnO0Ki873yxnHEDCJXA-DoK7zuXuuehdbjjyGBEtcvb9dfI0Jw2ZvvHTt8Y2Q_XS_HBqH_x3jet5ybNzahAK2dlddM1Cb2udmOfKCjlXla2l2cDoVjnqPdbNwsgpSnJou0alqrStLOguU1_mVZ1l_236j0anMpR3ATYPfBkF4EZaw6WvovVUxiqjaXYTlEs33UFwKnRDH-69O5Z30wHQ"
            }

            response = requests.get(url, headers=headers)
            print(response.text)
            print(response)
            print(response.json())

            message=response.text 
            print(message)
            length= len(message[0])
            print(length)
            print(message[0:4])
            print(type(message[0:4]))
            data = response.json()

        # Iterating through the json
                # list      
          
            return redirect('home')
            
            #
            
    else:
        form = BookAddForm()
    return render(request, 'add_book.html', {'form': form})


def delete_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        #print(book.pdf)
        messages.success(request, "Book deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
def download(request):
    path = "tmp/text.txt"
    success = 2
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise "Http404"