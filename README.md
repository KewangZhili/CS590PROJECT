# CS590 Project

## Overview

This project is designed for **concept prediction** and **caption generation** using a model trained on clinical images and captions. The project follows a modular approach, with steps for dataset preparation, concept detection, and caption prediction.

### Instructions

1. **Change Dataset Paths and Dependencies**  
   Update the paths in the code to match your local dataset and dependency paths.

2. **Training for Concept Prediction**  
   - Run the `train.py` file to train the model for concept prediction.
   - After training, use the obtained model to extract concepts associated with captions.

3. **Training for Caption Generation (CLIP-based Approach)**  
   - Open and execute `main.ipynb`.
   - The notebook includes steps to:
     - Calculate the similarity between captions and images.
     - Train the model.
     - Use the resulting `best.pt` file to generate captions for a new dataset, training dataset, or for metric collection.

### Project Workflow

Detailed explanations are provided in the comments of `main.ipynb` and additional documentation is available in the associated slides and paper.

### Project Phases

1. **Dataset Preparation**  
   Prepare and format datasets for use in the concept detection and caption generation phases.

2. **Concept Detection**  
   - This phase mirrors the process in the base paper and utilizes the provided BEiT transformer model for concept extraction.

3. **Caption Prediction**  
   - Use the trained model to generate captions based on the extracted concepts.

## Datasets

- **ROCOv2**: [ImageCLEF ROCO Medical Dataset](https://www.imageclef.org/2024/medical/caption)
- **Lumbar Spine Dataset**: [Lumbar Spine Dataset on Mendeley](https://data.mendeley.com/datasets/k57fr854j2/2)
