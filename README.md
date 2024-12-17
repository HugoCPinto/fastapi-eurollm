# FastAPI Euro LLM Integration

This project demonstrates how to integrate a pre-trained language model Euro LLM with **FastAPI** to 
build a web API that can generate text based on user input.

## Features

- **FastAPI-based web API** for interacting with the model.
- **Text generation** using a pre-trained language model (Euro LLM).
- **Endpoint** to generate custom responses based on input text.
- Supports logging during app startup for better monitoring.

---

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python 3.10+**

---

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### 2. Set up a Virtual Environment (optional but recommended)
```bash
python -m venv venv
```
Activate the virtual environment:
- windows:
```bash
venv\Scripts\activate
```
- linux:
```bash
source venv/bin/activate
```

### 3. Install the Required Dependencies
Run the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

This will install the following packages:

- fastapi: Web framework to build the API.
- uvicorn: ASGI server to run the FastAPI app.
- transformers: Hugging Face library to load and work with pre-trained models.
- torch: PyTorch library for deep learning and model inference.
- datasets: Hugging Face datasets library to load datasets if needed.
- accelerate: To efficiently handle large models.

## Running the application

### 1. Start the FastAPI Application
```bash
uvicorn main:app --reload
```
This will start the application on http://127.0.0.1:8000. The --reload flag allows automatic reloading of the app during development.

### 2. Access the Swagger API Documentation
Once the server is running, you can navigate to the following URL in your browser to access the Swagger UI (interactive API documentation):
```bash
http://127.0.0.1:8000/docs
```
