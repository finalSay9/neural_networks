# OCR App — Learning Project

An app that extracts text from images (ID cards, receipts, books, documents) using classical CV preprocessing, OCR engines (Tesseract / EasyOCR), and a custom CRNN model trained on Google Colab.

This project is being built as a **learning exercise** — the goal is to understand each layer (preprocessing → OCR → post-processing) rather than just wire up a black-box pipeline.

---

## Project Status

- [ ] Preprocessing pipeline (OpenCV)
- [ ] Baseline OCR with Tesseract / EasyOCR
- [ ] Post-processing / structured field extraction
- [ ] Custom CRNN training (Colab)
- [ ] CRNN inference integrated into backend
- [ ] Frontend

---

## Architecture Overview

```mermaid
flowchart LR
    A[Client Upload] --> B[FastAPI Backend]
    B --> C[Preprocessing<br/>OpenCV]
    C --> D{OCR Engine}
    D -->|baseline| E[Tesseract]
    D -->|baseline| F[EasyOCR]
    D -->|custom, later| G[CRNN Model]
    E --> H[Post-processing<br/>Regex / Cleanup]
    F --> H
    G --> H
    H --> I[Structured Output<br/>JSON]
    I --> J[Client Response]
```

---

## Preprocessing Pipeline (Layer 2)

```mermaid
flowchart TD
    A[Raw Image] --> B[Grayscale Conversion]
    B --> C[Thresholding<br/>Otsu / Adaptive]
    C --> D[Noise Removal<br/>Blur / Morphology]
    D --> E[Deskew<br/>Hough Transform]
    E --> F[Contour Detection]
    F --> G[Perspective Transform<br/>Crop to Document]
    G --> H[Preprocessed Image<br/>ready for OCR]
```

---

## CRNN Model Flow (Layer 4)

```mermaid
flowchart LR
    A[Input Image<br/>fixed height] --> B[CNN<br/>Feature Extraction]
    B --> C[Feature Map<br/>sequence of columns]
    C --> D[Bidirectional LSTM<br/>Sequence Modeling]
    D --> E[CTC Decoder]
    E --> F[Predicted Text]
```

---

## Training Workflow (Colab-based)

```mermaid
sequenceDiagram
    participant Dev as You (local)
    participant Colab as Google Colab (GPU)
    participant Repo as training/ folder
    participant Backend as backend/app/models

    Dev->>Repo: Prepare dataset in training/dataset/
    Dev->>Colab: Open train_crnn.ipynb, upload/mount dataset
    Colab->>Colab: Train CRNN model
    Colab-->>Dev: Export trained weights (.h5 / .pt)
    Dev->>Backend: Copy weights into backend/app/models/
    Backend->>Backend: crnn_engine.py loads model for inference
```

---

## Request Flow (Runtime, once built)

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as FastAPI Backend
    participant P as Preprocessing
    participant O as OCR Engine
    participant Post as Post-processing

    U->>F: Upload image (ID / receipt / book page)
    F->>B: POST /ocr/upload
    B->>P: Run preprocessing pipeline
    P-->>B: Cleaned image
    B->>O: Run OCR (Tesseract / EasyOCR / CRNN)
    O-->>B: Raw extracted text
    B->>Post: Regex / NER extraction
    Post-->>B: Structured fields
    B-->>F: JSON response
    F-->>U: Display extracted data
```

---

## Folder Structure

```
ocr-app/
├── backend/            # FastAPI app: preprocessing, OCR engines, post-processing
├── frontend/            # UI (built later)
├── training/            # Colab notebooks + dataset, model export
├── sample_images/        # Test images: ids, receipts, books
├── docker-compose.yml
└── README.md
```

---

## Tech Stack

| Layer            | Tools                              |
|-------------------|-------------------------------------|
| Preprocessing      | OpenCV, Pillow                      |
| OCR (baseline)     | Tesseract, EasyOCR                   |
| OCR (custom)       | TensorFlow/Keras or PyTorch, CRNN, CTC loss |
| Post-processing     | Regex, spaCy (optional)               |
| Backend            | FastAPI, Uvicorn                     |
| Training           | Google Colab (GPU)                    |
| Deployment          | Docker, Docker Compose                |

---

## Running Locally

```bash
docker-compose up --build
```

Backend available at `http://localhost:8000`.
Health check: `GET /` → `{"status": "ok"}`

---

## Learning Notes

Research topics tracked as I go — see individual module docstrings and commit messages for what each piece does and why.