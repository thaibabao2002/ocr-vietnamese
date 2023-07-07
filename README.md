# OCR - Vietnamese
<details>
  <summary>Table Content</summary>

  1. [About Project](#about-project)
  2. [Detail](#detail)
  3. [Getting Started](#getting-started)
     - [Installation](#installation)
  4. [Structure](#structure)
  5. [Train model](#trainmodel)
  6. [Inference ( Convert ONNX)](#infer)
  7. [Build and run docker](#build)
  8. [Using AWS Lamda for backend severless and  connect to gradio frontend ](#using)
  9. [Results](#results)

</details>

### About Project <a name="about-project"></a>
-
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
  | ----- `model_strdent.onxx` \
  | `Serverless`: AWS Lamda \
  | ----- `lambda_function.py` \
  | ----- `test_lambda.py` \
  | `app.py`: Gradio \
  | `requirements.txt`: Libraries to download  \
    
### Getting Started <a name="getting-started"></a>
- Installation<a name = "installation"></a> :
    + Requirments.txt
### Structure <a name="structure"></a>
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
