from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from openai import OpenAI

import credentials
from prompt import article_prompt, with_two_text

app = FastAPI()

base_url = credentials.base_url
api_key = credentials.api_key

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

client = OpenAI(
    base_url=base_url,
    api_key=api_key 
)

@app.post("/rewrite")
@limiter.limit("3/minute") 
async def rewrite_text(request: Request, text: str, text2:str = None):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        
        if text2:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages = [ 
                    {'role': 'user', 'content': with_two_text(text, text2)}],
                seed=1,

            )
            rewritten_text = response.choices[0].message.content
            
            return {"rewritten_text": rewritten_text}
        else:
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [ 
                {'role': 'user', 'content': article_prompt(text= text)}],
            seed=1,

        )
            rewritten_text = response.choices[0].message.content
            return {"rewritten_text": rewritten_text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

