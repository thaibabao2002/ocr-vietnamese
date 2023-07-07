import cv2
import json
import base64
import requests

import numpy as np

from OCR_VN.predict import TextSystem
from OCR_VN.utils import parse_args

args = parse_args()
model = TextSystem(args)

def handler(event, context):
    """Provide main prediction API."""
    image = _load_image(event)
    if image is None:
        return {"statusCode": 400, "message": "neither image_url nor image found in event"}
    
    pred = model.inference(image)
    return {"pred": str(pred)}

def _load_image(event):
    event = _from_string(event)
    event = _from_string(event.get("body", event))

    image_url = event.get("image_url")
    if image_url is not None:
        print("INFO url {}".format(image_url))

        response = requests.get(image_url)
        image_data = response.content
        image = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
    else:
        encoded_img = event.get("image")
        print("INFO Loading image")
        if encoded_img is not None:
            image = base64.b64decode(encoded_img)
            image = np.frombuffer(image, dtype=np.uint8)
            image = cv2.imdecode(image, flags=1)
            print("INFO Loaded image")
            return image
        else:
            print("INFO Not valid image")
            return None

def _from_string(event):
    if isinstance(event, str):
        return json.loads(event)
    else:
        return event