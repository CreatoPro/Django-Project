from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import dropbox
import json
import tkinter as tk
from tkinter import filedialog
import requests
import boto3
import awscli
# Create your views here.

from django.http import HttpResponse

def s3_upload(file_path):
    root = tk.Tk()
    root.withdraw()

    file_path= filedialog.askopenfile().name

    s3_client = boto3.client('s3')

    response = s3_client.upload_file(file_path ,'my-bucket-7653854310', 'sample.jpg' )
    print(response)



def upload_dropbox(computer_path):
    # dropbox_access_token= "UErlsp4uNE4AAAAAAAAAAfUN5onvPKJNlyS8ulmwcQa8LEpoRm3rUZAt4LOJSk5N"    #Enter your own access token
    # dropbox_path= "/pythonuploader16073/sample.jpg"
    # computer_path='./sample.jpg'
    # # computer_path='F:\Python projects\Python-Projects\File Uploader\sample.jpg'
    # # {"site":"dropbox", "file_location":"sample.jpg"}
    # client = dropbox.Dropbox(dropbox_access_token)
    # print("[SUCCESS] dropbox account linked")

    # client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    # print("[UPLOADED] {}".format(computer_path))

    root = tk.Tk()
    root.withdraw()


    dropbox_access_token= "9ugkmnZ-p0EAAAAAAAAAAar1vl1eaSbxNyzNOjIvh9GGx-kPvZZBQSoVfu-JpZRf"    #Enter your own access token
    dropbox_path= "/pythonuploader16073/sample.jpg"
    computer_path= filedialog.askopenfile()

    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")

    client.files_upload(open(computer_path.name, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path.name))

def uplod_gdrive(file_path):
    file_path= filedialog.askopenfile()



    headers = {"Authorization": "Bearer ya29.a0ARrdaM_Dt_vsmLjdsCD2pBF5-aNBsEnZ9vRMhNPBkuu_sbq8y5HafUvuONE5CxTwUmCqHpf_c0Z5y0nVpQLMpu_NVb-9RR1cXfx0xDhpwyRzo3C-G_EC6B8bw1RE6yb-TqP-d3mAVyykvmxVzQX4Vk8q_DhT"}
    para = {
        "name": 'sample.jpg',
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file_path.name, "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)

def index(request):
    return HttpResponse("Hello, world. You're at the views.py file.")



@api_view(["POST"])
def upload(request):
    data=request.data
    print("the file location is",data["file_location"])
    if (data["site"]=="s3"):
        s3_upload(data["file_location"])
        print("s3")
    elif(data["site"]=="Onedrive"):
        print("Onedrive")
    elif(data["site"]=="drive"):
        uplod_gdrive(data['file_location'])
        print("drive")
    elif(data["site"]=="dropbox"):
        upload_dropbox(data["file_location"])
        print("dropbox")
    else:
        print("Invalid Request")


    print("the file location is",data["file_location"])
    return Response('200')