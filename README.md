# Tom & Jerry Classification 

### Description :
Detect the presence of characters 'tom' and 'jerry' in any given image
Tom and Jerry is an American animated media franchise and series of comedy short films created in 1940 by William Hanna and Joseph Barbera. Best known for its 161 theatrical short films by Metro-Goldwyn-Mayer, the series centers on the rivalry between the titular characters of a cat named Tom and a mouse named Jerry.

This is one of the famous cartoon shows, that we would have never missed watching during our childhood. Now, its time to use our deep learning skills to detect our favorite characters - Tom and Jerry in the images extracted from some of the shows.

## Dataset Source :
https://www.kaggle.com/datasets/balabaskar/tom-and-jerry-image-classification

### Create and activate  new Python Environment:
```
conda create -p venv python==3.8 -y
``` 

```
conda activate venv/
```

### Install Neccessary Python Packages for this Project:

```
pip install -r requirements.txt
```

## Stage 01: Data Ingestion

<p>Dataset is zipped and stored in AWS S3 Bucket download the file and extract the file.</p>
<p>AWS credentials are stored in Environment Variable </p>
<p>Data Ingestion Is Created and Used in Pipeline to run </p>

```
python main.py
```

## Stage 02: Prepare Base Model
<p> For this image classification, we use transfer learning approach which is VGG16 first we download the model from keras and update the base weight for our use case and save the model
</p>

```
python main.py
```

## Stage 03: Training Pipeline
<p>For Training we just use 1 epoch so the accuracy is not upto the marks if you want good accuracy add the epochs to 100 or 500</p>
<p>This is for just training</p>

```
python main.py
```
