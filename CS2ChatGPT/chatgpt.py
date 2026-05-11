import aiohttp
import asyncio

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "вставь сюда ключ"

async def send_to_ai(question):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com/cs2chatgpt", 
        "X-Title": "CS2 ChatGPT Bot" 
    }
    
    payload = {
        "model": "openai/gpt-4o-mini",  
        "messages": [
            {
                "role": "system",
                "content": "Ты полезный ассистент. Отвечай кратко и по делу, на том языке, на котором был задан вопрос. максимум 2-3 предложения."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                OPENROUTER_API_URL,
                headers=headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=15)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    answer = data['choices'][0]['message']['content'].strip()
                    return answer
                else:
                    error_text = await response.text()
                    print(f"Ошибка API: {response.status} - {error_text}")
                    return None
                    
    except asyncio.TimeoutError:
        print("Таймаут при запросе к API")
        return "Таймаут запроса"
    except Exception as e:
        print(f"Ошибка при запросе к AI: {e}")
        return None
