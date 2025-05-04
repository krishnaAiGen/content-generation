# Content Generation API

A FastAPI-based service for generating different types of content (text, audio, video) using AI. This API provides a unified interface for various content generation tasks, currently focusing on text generation using Ollama's Phi-3 model.

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Ollama**: Local LLM framework for running AI models
- **Phi-3**: Microsoft's lightweight language model for text generation
- **LangChain**: Framework for developing applications powered by language models
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server for running FastAPI applications
- **JWT**: JSON Web Tokens for authentication
- **Passlib**: Password hashing library

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- Security headers (XSS, CSRF, etc.)
- Rate limiting (to be implemented)
- Input validation
- Error handling

## Project Structure

```
content-generation/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and endpoints
│   ├── security.py          # Authentication and security utilities
│   └── services/
│       ├── __init__.py
│       └── ai_service.py    # AI service implementation
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

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

3. Set up Ollama:
```bash
# Install Ollama (if not already installed)
# Visit https://ollama.ai/download for installation instructions

# Pull the Phi-3 model
ollama pull phi3
```

4. Configure environment variables:
```bash
# Create a .env file with:
OLLAMA_MODEL=phi3
SECRET_KEY=your-secure-secret-key  # Generate a secure random string
```

5. Run the API:
```bash
python app/main.py
```

The API will be available at `http://localhost:8000`

## Authentication

### Login

To obtain an access token:

```bash
curl -X POST "http://localhost:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=admin123"
```

Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

### Using the Token

Include the token in the Authorization header for all protected endpoints:

```bash
curl -X POST "http://localhost:8000/get_content" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
     -H "Content-Type: application/json" \
     -d '{
         "content_type": "text",
         "prompt": "Write a short story about a robot"
     }'
```

## API Endpoints

### POST /token
- Authenticates user and returns JWT token
- Required for accessing protected endpoints

### POST /get_content

Generates content based on the specified type and parameters.

#### Request Body
```json
{
    "content_type": "text|audio|video",
    "prompt": "Your content generation prompt",
    "parameters": {
        // Optional parameters specific to the content type
    }
}
```

#### Content Types and Methods

1. **Text Generation** (`content_type: "text"`)
   - Uses Ollama's Phi-3 model
   - Supports additional context through parameters
   - Stops generation at periods (`.`)
   - Example parameters:
     ```json
     {
         "context": "Additional context for the generation"
     }
     ```

2. **Audio Generation** (`content_type: "audio"`)
   - Currently a placeholder implementation
   - Will be implemented in future versions

3. **Video Generation** (`content_type: "video"`)
   - Currently a placeholder implementation
   - Will be implemented in future versions

## Security Headers

The API includes the following security headers:
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Strict-Transport-Security: max-age=31536000; includeSubDomains
- Content-Security-Policy: default-src 'self'

## Error Handling

The API returns appropriate error responses for:
- Invalid credentials (401 Unauthorized)
- Invalid content types (400 Bad Request)
- Server errors (500 Internal Server Error)
- Invalid parameters
- Inactive users (400 Bad Request)

## Development

### Adding New Content Types

To add a new content type:
1. Add a new method in `AIService` class
2. Update the `get_content` endpoint in `main.py`
3. Add appropriate parameters and validation

### Environment Variables

Create a `.env` file with:
```
OLLAMA_MODEL=phi3
SECRET_KEY=your-secure-secret-key  # Generate a secure random string
```

## Future Enhancements

1. Implement audio generation using appropriate AI models
2. Implement video generation capabilities
3. Add rate limiting and authentication
4. Add support for more LLM models
5. Implement caching for frequently requested content
6. Add database support for user management
7. Implement role-based access control
8. Add API key management
9. Implement request logging and monitoring
