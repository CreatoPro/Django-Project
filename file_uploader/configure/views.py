from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.http import request
import boto3
import tkinter as tk
from tkinter import filedialog
import dropbox
import json
import requests
import os

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def aws_uploader(file_path):
    try:
        root = tk.Tk()
        root.withdraw()

        file_path= filedialog.askopenfile().name
        file_name = os.path.basename(file_path)

        s3_client = boto3.client('s3')

        response = s3_client.upload_file(file_path ,'my-bucket-7653854310', file_name  )
        print(response)
        print("Uploaded")
        return HttpResponse("Upload Sucess")
    except:
        return HttpResponse("Upload Failed, Retry")
    
def dropbox_uploader(computer_path):
    try:
        root = tk.Tk()
        root.withdraw()
        computer_path= filedialog.askopenfile().name
        file_name = os.path.basename(computer_path)
        dropbox_access_token= "9ugkmnZ-p0EAAAAAAAAAAar1vl1eaSbxNyzNOjIvh9GGx-kPvZZBQSoVfu-JpZRf"    #Enter your own access token
        dropbox_path= f"/pythonuploader16073/{file_name}"
        

        client = dropbox.Dropbox(dropbox_access_token)
        print("[SUCCESS] dropbox account linked")

        client.files_upload(open(computer_path, "rb").read(), dropbox_path)
        print("[UPLOADED] {}".format(file_name))
        return HttpResponse("Upload Sucess")
    except:
        return HttpResponse("Upload Failed, Retry")
    


def googledrive_upload(file_path):
    

    try:
        root = tk.Tk()
        root.withdraw()

        file_path= filedialog.askopenfile().name
        file_name = os.path.basename(file_path)


        headers = {"Authorization": "Bearer ya29.a0ARrdaM_muE9yyX8AqWhSnvStcs34eULe4AHwBwJc1QhX6ILDRK0m8sDeZXQhOYBR9Z3Leiq1nV2654HBuVLWjKXllzuWIJnVnAvSjlopsnh_YUtTOXAgMIHEiQFIKBYN94DLpNOHwFhHzh3h1ozOlxop4WzW"}
        para = {
            "name": file_name,
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open(file_path, "rb")
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        print(r.text)
        print("Uploaded")
        return HttpResponse("Upload Sucess")
    
    except:
        return HttpResponse("Upload Failed, Retry")