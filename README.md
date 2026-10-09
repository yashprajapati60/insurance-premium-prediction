# Insurance Premium Prediction

A machine learning project that combines a trained Random Forest model with FastAPI and Streamlit to build a simple prediction application.

I built this project to understand how a machine learning model can be integrated into a working application rather than just running predictions inside a Jupyter Notebook.

## What this project does

- Trains a Random Forest model using scikit-learn.
- Saves the trained model for reuse.
- Uses FastAPI to create a prediction endpoint.
- Uses Streamlit to provide a simple interface for user input.
- Connects the frontend and backend through HTTP requests.

## Tech Stack

- **Python** — Core development
- **Pandas & NumPy** — Data handling
- **Scikit-learn** — Model training and preprocessing
- **FastAPI** — REST API
- **Streamlit** — Frontend
- **Requests** — API communication
- **Jupyter Notebook** — Model experimentation

## Project Structure

```text
insurance-premium-prediction/
├── app.py              # FastAPI backend
├── frontend.py         # Streamlit interface
├── main.py             # Additional Python code
├── model.ipynb         # Model training notebook
├── requirements.txt    # Dependencies
└── README.md
```

The trained model (`model.pkl`) and dataset (`insurance.csv`) are required locally if they are not included in the repository.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yashprajapati60/insurance-premium-prediction.git
cd insurance-premium-prediction
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure the trained model file is available at the path expected by the backend.

### 4. Start the API

```bash
uvicorn app:app --reload
```

FastAPI documentation: http://127.0.0.1:8000/docs

### 5. Start the frontend

Open another terminal and run:

```bash
streamlit run frontend.py
```

Open the local URL shown in the terminal to use the application.

## How it works

1. The user enters the required information in Streamlit.
2. The frontend sends a request to the FastAPI backend.
3. The backend passes the input to the trained model.
4. The prediction is returned and displayed in the frontend.

## What I learned

- Training and saving a machine learning model with scikit-learn.
- Loading a saved model for inference.
- Building REST APIs with FastAPI.
- Connecting a frontend to a backend using HTTP requests.
- Organizing a machine learning project beyond the notebook stage.

## Future Improvements

- Evaluate the model on a suitable test dataset and document its performance.
- Add automated tests and better error handling.
- Explore model explainability and deployment.

## Author

**Yashkumar Prajapati**

GitHub: [@yashprajapati60](https://github.com/yashprajapati60)

