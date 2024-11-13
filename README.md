# CS590PROJECT

NOTE:Change the paths to the datasets and the dependencies accordingly
RUN train.py file to train for concept prediction and generate and use the obtained model to extract the concepts associated with captions
RUN main.ipynb file (clip based approach) to train the model to :
  a)Firstly find the similarity of captions to the images
  b)Train the models
  c)Use the obtained best.pt file to generate captions for new dataset/ for train dataset/ metric collection

The modular flow of the code is presented in the comments of the main.ipynb file and explanation is detailed in the slides and in the paper
Steps:
1.Preparing the dataset
2.Concept Detection phase is similar to base paper,utilising their code(Uses BEiT transformer)
3.Caption Prediction


Datasets:
ROCOv2:https://www.imageclef.org/2024/medical/caption
Lumbar Spine:https://data.mendeley.com/datasets/k57fr854j2/2
