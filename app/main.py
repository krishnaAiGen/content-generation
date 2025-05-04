from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.ai_service import AIService

app = FastAPI(title="Content Generation API")
ai_service = AIService()

class ContentRequest(BaseModel):
    content_type: str
    prompt: str
    parameters: Optional[dict] = None

@app.post("/get_content")
async def get_content(request: ContentRequest):
    try:
        if request.content_type == "text":
            return await ai_service.generate_text(request.prompt, request.parameters)
        elif request.content_type == "audio":
            return await ai_service.generate_audio(request.prompt, request.parameters)
        elif request.content_type == "video":
            return await ai_service.generate_video(request.prompt, request.parameters)
        else:
            raise HTTPException(status_code=400, detail="Invalid content type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001) 