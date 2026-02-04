# ASCII-Images
An updated program of a previous project which converts image pixels to ASCII character art. This program is updated with a functional UI written in HTML, CSS and JavaScript. Backend logic is handled by FastAPI and Python as the programming language.

## Prerequisites
- Python 3.10+
- pip (included with Python)

## How to Use
1. **Create a virtual environment**:
```bash
python -m venv venv
```

2. **Activate the virtual environment**:`

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

3. Install all the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application
To start the development server, run:
```bash
python -m uvicorn app:app --reload
```

The application will be available at `http://127.0.0.1:8000`

### Deactivating the Virtual Environment
When you are done, deactivate the virtual environment:
```bash
deactivate
```