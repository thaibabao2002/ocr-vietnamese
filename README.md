# OCR - Vietnamese
<details>
  <summary>Table Content</summary>

  1. [About Project](#about-project)
  2. [Getting Started](#getting-started)
     - [Installation](#installation)
  3. [Structure](@structure)
  4. [Results](#results)

</details>

### About Project <a name="about-project"></a>
-
### Detail 

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
### Train model 
  1. Text Detection :
  2. Text Recognition
### Inference ( Convert ONNX)
  1. Colab :
### Build and run docker
  1. Build and run docker
  2. Push Docker image to ECR
### Using AWS Lamda for backend severless and  connect to gradio frontend 
### Results <a name="results"></a> :
![_-Text-Recognizer-Opera-2023-07-07-16-41-32](https://github.com/thaibabao2002/ocr-vietnamese/assets/106230362/aaace0f0-eb37-49e9-8171-c26ff8ea49c2)
