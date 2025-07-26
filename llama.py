# llama.py
import os, requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

def call_llama(prompt: str, temperature: float = 0.7, max_tokens: int = 1024) -> str:
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    res = requests.post(TOGETHER_API_URL, headers=headers, json=body)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]
