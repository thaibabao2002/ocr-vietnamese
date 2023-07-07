import os
import base64
import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"

image_path = "../images/098.jpeg"

with open(os.path.join(image_path), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

data = {
    #'image_url': "https://hpconnect.vn/wp-content/uploads/2019/10/muc-dich-cua-viec-ghep-chu-vao-anh.jpg",
    'image': encoded_string
}


result = requests.post(url, json=data).json()
print(result)