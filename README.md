## Handwritten Word Recognition for Indian Languages using CRNN

### Problem Statement

Optical Character Recognition (OCR) technology has revolutionized the way we process and analyze written text. However, existing OCR algorithms have primarily been developed for English and other Western languages, leaving many non-Latin scripts, such as Indic languages, underrepresented. The goal is to develop an OCR algorithm specifically tailored for Indic languages. The algorithm will be designed to recognize and accurately process complex scripts, ligatures, and diacritical marks in Indic languages, and will be optimized for a variety of Indic languages and dialects. By doing so, this project seeks to enhance OCR technology for Indic languages.

> This project was a part of [ICDAR 2023 Competition on Indic Handwriting Text Recognition( IHTR 2023 )](https://ilocr.iiit.ac.in/ihtr/index.html). Consequently, the [dataset](https://ilocr.iiit.ac.in/ihtr/dataset.html) used for this project was sourced from the competition.

<!-- This project uses [docTR: Document Text Recognition](https://github.com/mindee/doctr) -->

### Installation

This project uses [docTR: Document Text Recognition](https://github.com/mindee/doctr) to Train and test model, hence consider following steps for installation.
```sh
git clone https://github.com/mindee/doctr.git
pip install -e doctr/.
pip install -e doctr/.[torch]
pip install -r ./requirements.txt
```

