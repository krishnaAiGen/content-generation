from typing import Optional, Dict, Any
import asyncio
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL", "phi3")
        self.llm = Ollama(model=self.model, temperature=0)

    async def generate_text(self, prompt: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate text content based on the prompt and parameters using Ollama
        """
        try:
            final_prompt = prompt
            if parameters and "context" in parameters:
                final_prompt = f"Context: {parameters['context']}\n\nPrompt: {prompt}"
            
            output = self.llm.invoke(final_prompt, stop=['.'])
            
            return {
                "status": "success",
                "content": output,
                "parameters": parameters or {}
            }
        except Exception as e:
            return {
                "status": "error",
                "content": str(e),
                "parameters": parameters or {}
            }

    async def generate_audio(self, prompt: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate audio content based on the prompt and parameters
        """
        # TODO: Implement actual audio generation logic
        return {
            "status": "success",
            "content": f"Generated audio for prompt: {prompt}",
            "parameters": parameters or {}
        }

    async def generate_video(self, prompt: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate video content based on the prompt and parameters
        """
        # TODO: Implement actual video generation logic
        return {
            "status": "success",
            "content": f"Generated video for prompt: {prompt}",
            "parameters": parameters or {}
        } 