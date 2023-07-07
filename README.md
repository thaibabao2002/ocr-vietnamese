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
### Project Structure
Ocr-Vietnamese
│   backbone.py                   # Model configuration
|   export.py                     # UPDATED 10/2022: onnx weight with accompanying .npy anchors
│   hubconf.py                    # Pytorch Hub entrypoint
│   hybridnets_test.py            # Image inference
│   hybridnets_test_videos.py     # Video inference
│   train.py                      # Train script
│   train_ddp.py                  # DistributedDataParallel training (Multi GPUs)
│   val.py                        # Validate script
│   val_ddp.py                    # DistributedDataParralel validating (Multi GPUs)
│
├───encoders                      # https://github.com/qubvel/segmentation_models.pytorch/tree/master/segmentation_models_pytorch/encoders
│       ...
│
├───hybridnets
│       autoanchor.py             # Generate new anchors by k-means
│       dataset.py                # BDD100K dataset
│       loss.py                   # Focal, tversky (dice)
│       model.py                  # Model blocks
│
├───projects
│       bdd100k.yml               # Project configuration
│
├───ros                           # C++ ROS Package for path planning
│       ...
│
└───utils
    |   constants.py
    │   plot.py                   # Draw bounding box
    │   smp_metrics.py            # https://github.com/qubvel/segmentation_models.pytorch/blob/master/segmentation_models_pytorch/metrics/functional.py
    │   utils.py                  # Various helper functions (preprocess, postprocess, eval...)
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
