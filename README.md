# Garbage Detection and Sorting System

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dataset](#dataset)
6. [Demo](#demo)
7. [Target Audience](#target-audience)
8. [Contributions](#contributions)

---

## 1. Introduction

This project implements an AI-powered garbage detection and sorting system using the YOLOv8 model for precise waste classification. The system is designed to enhance waste sorting efficiency and promote sustainable waste management practices.

## 2. Features

- Real-time garbage detection and classification
- Supports six categories: cardboard, plastic, glass, paper, metal, and biodegradable waste
- User-friendly interface using Streamlit
- Easy integration with camera systems for live detection
- Scalable and adaptable for various environments

## 3. Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/binguliki/Garbage-Detection.git
   cd Garbage Detection
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Click the "Start Camera" button to begin the live detection.
3. The system will display detected objects and their classifications in real-time.
4. Click the "Stop Camera" button to stop the live feed.

## 5. Dataset

- **Description**: The dataset includes images of various waste types, categorized into cardboard, plastic, glass, paper, metal, and biodegradable waste.
- **Source**: [Waste Sorting Dataset](https://universe.roboflow.com/material-identification/garbage-classification-3/dataset/2) (Replace with actual source)
- **Preprocessing**: Images are resized, normalized, and augmented for better training performance.

## 6. Demo


https://github.com/binguliki/Garbage-Detection/assets/138435877/93d97fac-1a72-4a7d-981f-b0ff597bcc0d


## 7. Target Audience

- **Municipal Waste Authorities**: Streamline waste sorting processes, reduce contamination, and improve overall efficiency.
- **Recycling Facilities**: Automate sorting, enhance recycling rates, and separate materials more effectively.
- **Large Businesses**: Improve waste management practices, minimize waste generation, and optimize recycling efforts.

## 8. Contributions

We welcome contributions to improve the project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## 9. Contributors

Thanks to the following people who have contributed to this project:

- [SurajPhani-github](https://github.com/SurajPhani-github)


