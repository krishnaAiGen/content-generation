# Content Generation API

A FastAPI-based service for generating different types of content (text, audio, video) using AI.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
python app/main.py
```

The API will be available at `http://localhost:8000`

## API Usage

### Endpoint: POST /get_content

Request body:
```json
{
    "content_type": "text|audio|video",
    "prompt": "Your content generation prompt",
    "parameters": {
        // Optional parameters specific to the content type
    }
}
```

Example:
```bash
curl -X POST "http://localhost:8000/get_content" \
     -H "Content-Type: application/json" \
     -d '{"content_type": "text", "prompt": "Generate a story about a magical forest"}'
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
