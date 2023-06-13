# Tom & Jerry Classification 

### Description :
Detect the presence of characters 'tom' and 'jerry' in any given image
Tom and Jerry is an American animated media franchise and series of comedy short films created in 1940 by William Hanna and Joseph Barbera. Best known for its 161 theatrical short films by Metro-Goldwyn-Mayer, the series centers on the rivalry between the titular characters of a cat named Tom and a mouse named Jerry.

This is one of the famous cartoon shows, that we would have never missed watching during our childhood. Now, its time to use our deep learning skills to detect our favorite characters - Tom and Jerry in the images extracted from some of the shows.

## Dataset Source :
https://www.kaggle.com/datasets/balabaskar/tom-and-jerry-image-classification

## Steps:

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
<p>For Training we just use 3 epoch so the accuracy is not upto the marks if you want good accuracy add the epochs to 100 or 500</p>
<p>This is for just training</p>

```
python main.py
```

## Stage 04: Evaluation Pipeline
<p> Once Model is Trained check the model performance it will evaluate the model and save the result in <b> scores.json</b> </p>

```
python main.py
```

## Initializing DVC
<p> DVC Stands for Data Version Control , it help to track our model and run the stage wise if the pipeline is already run it skip and run the remining pipeline</p>
<p>To Use DVC we need any version control here we use GIT , To initilalize DVC </p>

```
dvc init
```
<p>To Run DVC </p>

```
dvc repro
```
<p> To Track the Model Pipeline </p>

```
dvc dag
```
<p>The Logs are stored in the <b>dvc.lock</b> file </p>

## Flask App Creation:

<p>To Check the Flask App run the below command in the terminal</p>

```
python app.py
```

<p> Check the Browser with localhost and the port is 8080 </p>

```
http://127.0.0.1:8080
```

<p> To Train the model using Flask</p>

```
http://127.0.0.1:8080/train
```

## AWS-CICD-Deployment-with-Github-Actions


1. Login to AWS console.
2. Create IAM user for deployment

## with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

```
1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2
```

## Policy:

```
1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 972510255763.dkr.ecr.us-east-1.amazonaws.com/tomjerry
```
