# OCR - Vietnamese
<details>
  <summary>Table Content</summary>

  1. [About Project](#about-project)
  2. [Detail](#detail)
  3. [Getting Started](#getting-started)
     - [Installation](#installation)
  4. [Train model](#trainmodel)
  5. [Inference ( Convert ONNX)](#infer)
  6. [Build and run docker](#build)
  7. [Using AWS Lamda for backend severless and  connect to gradio frontend ](#using)
  8. [Results](#results)

</details>

### About Project <a name="about-project"></a>
We developed an OCR project specifically designed for the Vietnamese language, following the MLOps process. Initially, we utilized the open-source paddleOCR and conducted testing on various models to ensure effective text detection and recognition. Throughout the training phase, we employed WandB to monitor parameters and preserve artifacts for the models at each step. Upon completion of model training, we selected the PPOCR_v3 model, which strikes a balance between accuracy and inference time for both text detection and recognition. Subsequently, we converted the two models to the ONNX format and packaged them together in a Docker image, which was then uploaded to AWS ECR for storage. We fetched the Docker image from ECR and deployed it on AWS Lambda, leveraging API Gateway to create an API for end users. This API is seamlessly connected to the Gradio Frontend, enabling users to receive the desired results.

![image](https://github.com/thaibabao2002/ocr-vietnamese/assets/76588198/607daac3-15b7-4ac5-b435-498119f0d264)



### Detail <a name="detail"></a>

Ocr-Vietnamese \
  | `OCR_VN:` \
  | ----- `predict.py`: Take input and return result \
  | ----- `utils.py`: Auxiliary function for file predict \
  | `Images`: Image  \
  | `Models:` \
  | +) `det_onnx` : Model Detection \
  | ----- `model_det.onxx` \
  | +) `rec_onnx` : Model Recognition  \
  | ----- `model_rec.onxx` \
  | `Serverless`: AWS Lamda \
  | ----- `lambda_function.py` \
  | ----- `test_lambda.py` \
  | `app.py`: Gradio \
  | `requirements.txt`: Libraries to download  \
    
### Getting Started <a name="getting-started"></a>
- Installation<a name = "installation"></a> :
    + conda create -n <name-of-env> python==3.10
    + pip install -r requirements.txt
### Train model <a name="trainmodel"></a>
  1. Text Detection :
  2. Text Recognition :
### Inference ( Convert ONNX) <a name="infer"></a>
  1. Colab :
### Build and run docker <a name="build"></a>
  1. Build and run docker
  2. Push Docker image to ECR
### Using AWS Lamda for backend severless and  connect to gradio frontend   <a name="using"></a>
### Results <a name="results"></a> :
![_-Text-Recognizer-Opera-2023-07-07-16-41-32](https://github.com/thaibabao2002/ocr-vietnamese/assets/106230362/aaace0f0-eb37-49e9-8171-c26ff8ea49c2)
