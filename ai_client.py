
from config import Config
import os

class AIClient:
    def __init__(self, api_key: str = None):
        try:
            from google import genai
        except Exception as e:
            raise RuntimeError("google-genai package not installed. Run: pip install google-genai") from e

        self.genai = genai
        key = api_key or Config.GOOGLE_API_KEY
        if not key:
            raise ValueError("GOOGLE_API_KEY not set in environment or passed to AIClient.")

        try:
            genai.configure(api_key=key)
        except Exception:
            pass

        self.model = Config.GOOGLE_MODEL

    def chat(self, prompt: str, model: str = None, temperature: float = None, max_tokens: int = None) -> str:
        model = model or self.model
        temperature = temperature if temperature is not None else Config.DEFAULT_TEMPERATURE
        max_tokens = max_tokens or Config.DEFAULT_MAX_TOKENS

        try:
            client = self.genai.Client()
        except Exception as e:
            return f"Error initializing Gemini client: {e}"

        try:
            response = client.models.generate_content(
                model=model,
                contents=[prompt],
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        except Exception as e:
            return f"Error calling Gemini model '{model}': {e}"

        if hasattr(response, "text") and response.text:
            return response.text
        if hasattr(response, "outputs") and response.outputs:
            out0 = response.outputs[0]
            if hasattr(out0, "content") and out0.content:
                content = out0.content
                if isinstance(content, (list, tuple)) and len(content) > 0:
                    first = content[0]
                    if isinstance(first, dict) and "text" in first:
                        return first["text"]
                    if hasattr(first, "text"):
                        return first.text
                    return str(first)
                return str(content)
            return str(out0)
        if hasattr(response, "candidates") and response.candidates:
            cand = response.candidates[0]
            return getattr(cand, "content", getattr(cand, "text", str(cand)))
        return str(response)
