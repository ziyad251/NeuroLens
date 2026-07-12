<div align="center">

# 🧠 Neuro Lens:An XAI Multimodal based Classifcation of Alzeimers using Deep Learning

### AI-Powered Alzheimer's Stage Classification & Explainable Medical Imaging Platform

An end-to-end healthcare AI application that analyzes brain MRI images using deep learning to classify Alzheimer's disease stages, visualize model attention using Grad-CAM, manage patient records, and generate downloadable medical reports.

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST_API-000000?style=for-the-badge&logo=flask&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<br>

**Deep Learning • Medical Imaging • Explainable AI • Full-Stack Development**

</div>

---

## 📌 Overview

**Alzheimer's MRI AI** is an end-to-end AI-powered medical imaging application designed to analyze brain MRI scans and classify them into different stages of Alzheimer's-related cognitive impairment.

The system integrates a trained **PyTorch deep learning model** with a **Flask REST API**, an interactive **Streamlit frontend**, and **MongoDB** for persistent patient and prediction data.

Beyond basic classification, the platform provides confidence and risk indicators, **Grad-CAM explainability**, patient history management, AI-assisted report generation, PDF export, and email delivery.

The application is designed as a complete demonstration of how a machine learning model can be integrated into a production-style full-stack application rather than existing only as a standalone notebook.

---

# ✨ Key Features

### 🧠 MRI-Based Alzheimer's Classification

Upload a brain MRI scan and classify it into one of four stages:

| Stage | Description |
|---|---|
| 🟢 **No Impairment** | No significant impairment detected |
| 🟡 **Very Mild Impairment** | Early or subtle signs of impairment |
| 🟠 **Mild Impairment** | Noticeable signs of cognitive impairment |
| 🔴 **Moderate Impairment** | More advanced signs of impairment |

---

### 🔍 Input Plausibility Screening

The application performs basic screening before model inference to reject obvious out-of-domain uploads.

This helps prevent clearly unrelated images from being directly passed to the MRI classification model.

> **Note:** The current screening mechanism is a preliminary safeguard. Clinical-grade deployment would require a separately trained and validated MRI/OOD detection model.

---

### 📊 Confidence & Risk Analysis

Every successful prediction provides:

- Predicted Alzheimer's stage
- Model confidence score
- Risk indicator
- Prediction metadata
- Timestamped prediction history

---

### 🔥 Grad-CAM Explainability

The system integrates **Gradient-weighted Class Activation Mapping (Grad-CAM)** to provide visual explanations of model predictions.

Grad-CAM generates a heatmap highlighting image regions that contributed most strongly to the model's decision.

This helps improve:

- Model interpretability
- Prediction transparency
- Visual understanding of model attention

---

### 📄 AI-Assisted Medical Reports

The platform can generate structured reports containing:

- Patient information
- Prediction result
- Confidence score
- Risk assessment
- AI-generated interpretation
- Prediction timestamp
- Relevant analysis information

Reports can be:

- Viewed inside the application
- Exported as PDF
- Sent through email

---

### 👤 Registration & Authentication Flow

The application follows a registration-first user experience.

Users provide:

- Full name
- Email
- Username
- Password
- Password confirmation

Application access is gated so that users follow the flow:

```text
Registration
     ↓
   Login
     ↓
    Home
     ↓
Patient Management
     ↓
MRI Upload & Prediction
     ↓
Prediction Results
     ↓
Reports & History
```

---

### 🗃️ Patient & Prediction Management

MongoDB is used to maintain application data such as:

- Patient records
- Prediction history
- Generated reports
- User-related application data

This allows users to maintain historical records instead of treating each MRI prediction as an isolated operation.

---

### 🌗 Modern Healthcare Dashboard

The Streamlit frontend provides a multi-page healthcare-oriented interface with:

- Dashboard navigation
- Dark and light themes
- Registration and login flow
- Patient management
- MRI upload interface
- Prediction visualization
- Reports and history

---

# 🏗️ System Architecture

```text
                         ┌───────────────────────┐
                         │         User          │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │  Streamlit Frontend   │
                         │                       │
                         │ • Registration        │
                         │ • Authentication      │
                         │ • Patient Dashboard   │
                         │ • MRI Upload          │
                         │ • Reports             │
                         └───────────┬───────────┘
                                     │
                                     │ HTTP / REST API
                                     ▼
                         ┌───────────────────────┐
                         │      Flask API        │
                         │                       │
                         │ • Request Handling    │
                         │ • Input Validation    │
                         │ • Prediction API      │
                         │ • Report Generation   │
                         └──────┬─────────┬──────┘
                                │         │
                  ┌─────────────┘         └─────────────┐
                  ▼                                     ▼
        ┌─────────────────────┐             ┌─────────────────────┐
        │   PyTorch AI Model  │             │       MongoDB       │
        │                     │             │                     │
        │ • MRI Inference     │             │ • Patients          │
        │ • Classification    │             │ • Predictions       │
        │ • Confidence        │             │ • Reports           │
        │ • Grad-CAM          │             │ • History           │
        └──────────┬──────────┘             └─────────────────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Prediction Results  │
        │                     │
        │ • Alzheimer's Stage │
        │ • Confidence Score  │
        │ • Risk Score        │
        │ • Grad-CAM          │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Report Services   │
        │                     │
        │ • AI Report         │
        │ • PDF Generation    │
        │ • Email Delivery    │
        └─────────────────────┘
```

---

# 🔄 Prediction Workflow

```text
MRI Image Upload
        │
        ▼
File Validation
        │
        ▼
Input Plausibility Screening
        │
        ├── Invalid / Obvious Non-MRI ──► Reject Upload
        │
        ▼
Image Preprocessing
        │
        ▼
PyTorch Model Inference
        │
        ▼
Alzheimer's Stage Classification
        │
        ├── No Impairment
        ├── Very Mild Impairment
        ├── Mild Impairment
        └── Moderate Impairment
        │
        ▼
Confidence & Risk Analysis
        │
        ▼
Grad-CAM Generation
        │
        ▼
Store Prediction in MongoDB
        │
        ▼
Generate Medical Report
        │
        ├── View Report
        ├── Download PDF
        └── Send via Email
```

---

# 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Programming Language** | Python |
| **Frontend** | Streamlit |
| **Backend** | Flask |
| **API Architecture** | REST API |
| **Machine Learning** | PyTorch |
| **Computer Vision** | Deep Learning / CNN |
| **Explainable AI** | Grad-CAM |
| **Database** | MongoDB |
| **Containerization** | Docker & Docker Compose |
| **Report Generation** | PDF |
| **Email Service** | SMTP |
| **Configuration** | Environment Variables |

---

# 📁 Project Structure

```text
alzheimers-app/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── app_pages/
│   │   ├── user_registration.py
│   │   ├── login.py
│   │   ├── home.py
│   │   └── ...
│   └── requirements.txt
│
├── models/
│   └── model.pth
│
├── scripts/
│   └── create_test_email.py
│
├── assets/
│   ├── screenshots/
│   │   ├── home.png
│   │   ├── registration.png
│   │   ├── login.png
│   │   ├── prediction.png
│   │   ├── gradcam.png
│   │   ├── results.png
│   │   └── report.png
│   │
│   └── demo.gif
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

> The exact internal folder structure may differ depending on the current implementation.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd alzheimers-app
```

---

## 2. Create the Environment File

Copy the example environment configuration:

### Windows

```bash
copy .env.example .env
```

### Linux / macOS

```bash
cp .env.example .env
```

Update the required configuration values inside `.env`.

---

# 🧠 Model Setup

The trained PyTorch model is required for prediction.

## Step 1: Place the Model

Copy your trained `.pth` model into:

```text
alzheimers-app/models/model.pth
```

The structure should look like:

```text
models/
└── model.pth
```

---

## Step 2: Configure the Model Path

Inside `.env`, set:

```env
MODEL_PATH=models/model.pth
```

---

## Step 3: Restart the Backend

After adding or replacing the model, restart the Flask backend so the model loader can use the configured file.

> If the model is missing, incompatible, or cannot be loaded, the API returns an error instead of generating a fake or demonstration prediction.

---

# 🗄️ Start MongoDB

Using Docker Compose:

```bash
docker compose up -d mongo
```

To check the running containers:

```bash
docker compose ps
```

---

# ⚙️ Start the Backend

Install the required backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the Flask backend:

```bash
python -m backend.app
```

The backend will be available at:

```text
http://localhost:5000
```

---

# 💻 Start the Frontend

Open another terminal and install the frontend dependencies:

```bash
pip install -r frontend/requirements.txt
```

Start the Streamlit application:

```bash
streamlit run frontend/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🐳 Docker Setup

The project includes Docker Compose configuration for supporting services.

Start MongoDB:

```bash
docker compose up -d mongo
```

Start the local Mailpit email service if configured:

```bash
docker compose up -d mailpit
```

---

# 🔌 API Reference

## MRI Prediction

```http
POST /api/predictions/predict
```

### Request

The endpoint accepts an MRI image using:

```text
multipart/form-data
```

### Processing

The backend:

1. Validates the uploaded file
2. Performs input plausibility screening
3. Loads the configured PyTorch model
4. Preprocesses the MRI image
5. Performs model inference
6. Calculates prediction confidence
7. Generates risk information
8. Creates Grad-CAM visualization
9. Stores prediction information
10. Returns the prediction result

---

# 📧 Email Configuration

The application supports sending generated reports through SMTP.

## Test Email

Generate test email credentials:

```bash
python scripts/create_test_email.py
```

Copy the generated credentials into your `.env` file and restart the backend.

---

## Local Email Testing with Mailpit

Start Mailpit:

```bash
docker compose up -d mailpit
```

The local inbox will be available on port:

```text
8025
```

---

## Gmail

For Gmail SMTP:

1. Enable two-step verification on your Google account.
2. Generate an App Password.
3. Configure the Gmail SMTP values in `.env`.
4. Restart the backend.

> Never commit email passwords, API keys, SMTP credentials, or other secrets to GitHub.

---

# 🔐 Environment Variables

Example configuration:

```env
MODEL_PATH=models/model.pth

MONGO_URI=your_mongodb_connection_string

SMTP_HOST=your_smtp_host
SMTP_PORT=your_smtp_port
SMTP_USERNAME=your_username
SMTP_PASSWORD=your_password
```

Create a safe `.env.example` containing only placeholder values.

---

# 🛡️ Security Practices

The repository should never contain:

- `.env` files
- Database credentials
- SMTP passwords
- API keys
- Private tokens
- Large trained model files containing sensitive or proprietary assets

Recommended `.gitignore` entries:

```gitignore
# Environment variables
.env
.env.*
!.env.example

# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Virtual environments
venv/
.venv/
env/
ENV/

# IDE
.vscode/
.idea/

# Model files
*.pth
*.pt
*.ckpt

# Internal development files
TODO.md
MODEL_PLACEMENT.md

# Uploads
uploads/
uploaded_files/
```

---

# ⚠️ Model & Input Validation

The application only performs predictions when a valid trained PyTorch `.pth` model is available.

If the configured model:

- Does not exist
- Cannot be loaded
- Is incompatible with the expected architecture
- Produces an inference error

the API returns an appropriate error instead of generating a placeholder result.

The application also includes basic input plausibility screening to reject obvious non-MRI images.

However, this should **not** be considered equivalent to a clinically validated out-of-distribution detection system.

A production-grade implementation should include:

- Dedicated MRI modality validation
- Out-of-distribution detection
- Model uncertainty estimation
- Confidence calibration
- External dataset validation
- Clinical validation

---

# 🗺️ Future Improvements

- [ ] Multimodal Alzheimer's analysis using MRI and clinical data
- [ ] Dedicated MRI validation model
- [ ] Advanced out-of-distribution detection
- [ ] Model confidence calibration
- [ ] Improved uncertainty estimation
- [ ] Longitudinal patient progression tracking
- [ ] Role-based authentication
- [ ] Doctor and administrator dashboards
- [ ] Cloud deployment
- [ ] Model monitoring and versioning
- [ ] Improved report customization
- [ ] External dataset validation
- [ ] Mobile-responsive interface

---

# 🧪 Research & Engineering Focus

This project explores the integration of several areas of software engineering and artificial intelligence:

- Medical image classification
- Deep learning inference
- Explainable AI
- Backend API development
- Database integration
- Full-stack application architecture
- Containerized development
- AI model deployment
- Automated report generation

The primary goal is to demonstrate how a trained machine learning model can be integrated into a complete application workflow.

---

# ⚕️ Medical Disclaimer

> **This project is intended strictly for educational, academic, and research purposes.**

The predictions, confidence scores, risk indicators, Grad-CAM visualizations, and generated reports produced by this application:

- Are **not medical diagnoses**
- Should **not be used for clinical decision-making**
- Should **not replace professional medical evaluation**
- Have not been established here as a clinically validated medical device

Any real-world medical deployment would require extensive clinical validation, regulatory review, security controls, privacy safeguards, and evaluation by qualified healthcare professionals.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/your-feature

# Commit your changes
git commit -m "feat: add your feature"

# Push the branch
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 👨‍💻 Author

**Mahammad Ziyad**

Computer Science & Engineering student focused on:

- Backend Development
- Cloud Technologies
- Generative AI
- Machine Learning

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a **⭐ star**.

<div align="center">

### Built with 🧠 AI, 🔥 PyTorch, 🐍 Python, and ☁️ modern software engineering

</div>
