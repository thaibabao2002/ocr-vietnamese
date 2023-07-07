import os
import json
import base64
import requests

import numpy as np
import gradio as gr

from io import BytesIO
from OCR_VN.utils import parse_args
from OCR_VN.predict import TextSystem

def encode_b64_image(image, format="png"):
    """Encode a PIL image as a base64 string."""
    _buffer = BytesIO()  # bytes that live in memory
    image.save(_buffer, format=format)  # but which we write to like a file
    encoded_image = base64.b64encode(_buffer.getvalue()).decode("utf8")
    return encoded_image

args = parse_args()
model = TextSystem(args)

class PredictorBackend:
    """Interface to a backend that serves predictions.

    To communicate with a backend accessible via a URL, provide the url kwarg.

    Otherwise, runs a predictor locally.
    """

    def __init__(self, url=None):
        self.url = url
        if self.url is not None:
            self._predict = self._predict_from_endpoint
        else:
            self._predict = model.inference

    def run(self, image):
        if self.url is None:
            image = np.array(image)
        pred = self._predict(image)
        return pred

    def _predict_from_endpoint(self, image):
        encoded_image = encode_b64_image(image)
        payload = json.dumps({"image": encoded_image})
        response = requests.post(self.url, data=payload)
        pred = response.json()['pred']

        return pred

def make_frontend(
    fn,
):
    """Creates a gradio.Interface frontend for an image to text function."""
    examples_dir = "./images"
    example_fnames = [elem for elem in os.listdir(examples_dir) if elem.endswith(".jpg")]
    example_paths = [examples_dir + "/" + fname for fname in example_fnames]


    examples = [[str(path)] for path in example_paths]

    allow_flagging = "never"


    # build a basic browser interface to a Python function
    frontend = gr.Interface(
        fn=fn,  # which Python function are we interacting with?
        outputs=gr.components.Textbox(),  # what output widgets does it need? the default text widget
        inputs=gr.components.Image(type="pil",label="Image OCR"),
        title="📝 Text Recognizer",  # what should we display at the top of the page?
        examples=examples,  # which potential inputs should we provide?
        cache_examples=False,  # should we cache those inputs for faster inference? slows down start
        allow_flagging=allow_flagging,  # should we show users the option to "flag" outputs?
    )

    return frontend

def main():
    #lambda_url_local = "http://localhost:8080/2015-03-31/functions/function/invocations"
    predictor = PredictorBackend(url=None)
    frontend = make_frontend(
        predictor.run,
    )
    frontend.launch(
        server_name="0.0.0.0",  # make server accessible, binding all interfaces  # noqa: S104
        share=True,  # should we create a (temporary) public link on https://gradio.app?
    )
if __name__ == "__main__":
    main()