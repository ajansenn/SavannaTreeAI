# Savanna Tree AI
![](https://github.com/ajansenn/SavannaTreeAI/blob/main/TreeDetectron2.png)

### Access the data
The Savanna Tree AI baseline dataset is published at [Zenodo](https://doi.org/10.5281/zenodo.7094916). The mosaics are also are published at [Geonadir](https://geonadir.com).

### Setting up your desktop
Follow the steps below to install this repository on your dekstop.

* Install [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/)
* Install [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2019.10-Windows-x86_64.exe)
  * Choose All Users
* Install [Git Desktop](https://desktop.github.com/)
* Open Git Desktop and clone https://github.com/ajansenn/Kakadutree.git
* Open Anaconda Prompt, cd to folder with cloned repository and [create conda environment] using the code below(https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment#local):
```
conda env create -f environment.yml
conda env list
conda activate savannatreeai
conda install notebook ipykernel
ipython kernel install --user
```

### Image Classification with Azure Custom Vision
Download the mosaic and shape files from [Zenodo](https://doi.org/10.5281/zenodo.7094916). Use the Raster to Custom Vision Jupyter notebook to clip images at the dimension of the bounding box and upload images (with labels) to Azure Custom Vision service.

CustomVision.ai in Microsoft Azure is used for image labeling and model training. 

* Create a [CustomVision.ai project](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/get-started-build-detector)

In Anaconda:

* Change directory to savannatreeai:
```
cd savannatreeai
```
* Start the [Jupyter Notebook app](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html):
```
jupyter notebook
```

### Object detection and instance segmentation with Azure Machine Learning

Download the 1024x1024 training and validation datasets from [Zenodo](https://doi.org/10.5281/zenodo.7094916). 

Deploy notebooks and dataset in [Azure Machine Learning Studio](https://azure.microsoft.com/en-gb/products/machine-learning/#features). 

### Contact

For more information contact:
* [Andrew Jansen](mailto:andrew.jansen@environment.gov.au), Supervising Scientist
* [Steve van Bodegraven](mailto:Steve.VanBodegraven@microsoft.com), Microsoft



