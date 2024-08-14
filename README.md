
# Handwritten Word Recognition for Indian Languages using CRNN

Optical Character Recognition (OCR) technology has revolutionized the way we process and analyze written text. However, existing OCR algorithms have primarily been developed for English and other Western languages, leaving many non-Latin scripts, such as Indic languages, underrepresented. The goal is to develop an OCR algorithm specifically tailored for Indic languages. The algorithm will be designed to recognize and accurately process complex scripts, ligatures, and diacritical marks in Indic languages, and will be optimized for a variety of Indic languages and dialects. By doing so, this project seeks to enhance OCR technology for Indic languages.

> This project was a part of [ICDAR 2023 Competition on Indic Handwriting Text Recognition( IHTR 2023 )](https://ilocr.iiit.ac.in/ihtr/index.html). Consequently, the [dataset](https://ilocr.iiit.ac.in/ihtr/dataset.html) used for this project was sourced from the competition.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

Indic scripts present unique challenges for OCR (Optical Character Recognition) due to their complex and diverse characters. This project aimed to develop a robust model capable of recognizing handwritten text from 10 different Indic languages, utilizing deep learning techniques and advanced image preprocessing methods.

## Key Features

- **Preprocessing Techniques:** Image binarization, noise reduction, skew correction, and normalization.
- **Data Augmentation:** Techniques such as cropping, rotation, and scaling were applied to a corpus of 90K handwritten text images.
- **Model Architecture:** Combined the powerful feature extraction of VGG16 with the sequential modeling of a Bidirectional Long Short-Term Memory (BiLSTM) network.
- **Performance Metrics:** Evaluated using Character Recognition Accuracy (CRA), Word Recognition Accuracy (WRA), Precision, and Recall.

## [Dataset](https://ilocr.iiit.ac.in/ihtr/dataset.html) 

The dataset consisted of 90K handwritten word images from 10 different Indian languages. It was preprocessed to enhance OCR accuracy by removing noise, correcting skew, and normalizing the text size and orientation.

## Preprocessing

- **Binarization:** Converted images to black and white to simplify processing.
- **Noise Reduction:** Removed artifacts and unwanted elements to improve clarity.
- **Skew Correction:** Straightened skewed text lines for better recognition.
- **Normalization:** Standardized the shape and size of characters to enhance recognition accuracy.

## Model Architecture

The model used in this project is a CRNN_VGG16_BN, which merges:

- **VGG16:** Pre-trained on ImageNet, used for feature extraction.
- **BiLSTM:** Bidirectional Long Short-Term Memory network for sequential data processing.

This combination allows the model to effectively extract spatial features and handle the sequential nature of text.

## Training

The model was fine-tuned on the preprocessed dataset using:

- **Learning Rate:** ***0.01*** Optimized for best convergence.
- **Batch Size:** ***1024*** Adjusted to balance performance and memory usage.
- **Augmentation:** Techniques such as cropping, rotation, and scaling to improve generalization.

## Evaluation

The model's performance was evaluated using:

- **Character Recognition Rate (CRR):** Measures the percentage of correctly recognized characters.
- **Word Recognition Rate (WRR):** Measures the percentage of correctly recognized words.

## Results

The model achieved:

- **Character Recognition Rate (CRR):** Up to 90.42% CRR  for Devanagari, Tamil & Telugu
- **Word Recognition Rate (WRR):** Up to 51.5% for Devanagari, Tamil & Telugu.
- Secured **6th place** in the [IHTR competition](https://ilocr.iiit.ac.in/ihtr/leaderboard.html) for ICDAR 23 conference.

## Procedure

1. **Download Dataset**: Acquire the dataset from the IHTR website.
2. **Data Preprocessing**: Clean and organize the dataset to prepare it for training.
3. **Create Vocabulary**: Develop a vocabulary set from the dataset to train the model for various languages.
4. **Model Training**: Train the model, conducting up to 100 epochs for each language.
5. **Evaluation and Testing**: Assess and test the trained models to generate predictions.


## Installation and Usage

This project uses [docTR: Document Text Recognition](https://github.com/mindee/doctr) to Train and test model, hence consider following steps for installation.
```sh
git clone https://github.com/mindee/doctr.git
pip install -e doctr/.
pip install -e doctr/.[torch]
```
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Jaysharma2/Handwritten_Word_Recognition.git
   cd Handwritten_Word_Recognition
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the [dataset](https://ilocr.iiit.ac.in/ihtr/dataset.html)  and place it in the `data/` directory.

4. Train Command

To train the model using the open-source DocTR library and a CRNN model from scratch, provide the paths to your training and validation data along with other hyperparameters:

```bash
python doctr/references/recognition/train_pytorch.py crnn_vgg16_bn \
  --train_path path/to/train/data/ \
  --val_path path/to/validation/data/ \
  --vocab tamil \
  --epochs 100 \
  --b 1024 \
  --device 0 \
  --lr 0.01
```

5. Test Command

To test the trained model, use the following command:

```bash
python src/test.py \
  --data path/to/test/data/ \
  --lang telugu \
  --model ./models/crnn_vgg16_bn_telugu.pt
```

*Note: A sample test data folder named `test_samples` is available for reference.*

6.  Get Evaluation Results

To obtain evaluation results, run:

```bash
python src/get_results.py \
  --data path/to/validation/data/ \
  --lang telugu \
  --model ./models/crnn_vgg16_bn_telugu.pt
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
