import asyncio
import time
import re
from util import get_last_chat, write_command, press_key
from chatgpt import send_to_ai

# Пути к файлам CS2 - измени на свои
cs_path = "E:\\www\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log"
log_dir = "E:\\www\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log"
exec_dir = "E:\\www\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg\\message.cfg"

chat_delay = 3
user_last_command_time = {}

async def handle_chat():
    print("CS2 ChatGPT бот запущен...")
    
    while True:
        new_lines = get_last_chat(log_dir)

        if not new_lines:
            await asyncio.sleep(0.1)
            continue

        for line in new_lines:
            if '  [ALL] ' in line or '  [T] ' in line or '  [CT] ' in line:
                match = re.search(r'\[.*?\]\s(.*?)\s?(?:\[DEAD\])?:', line)
                if match:
                    username = match.group(1).strip()
                    data = line.split(': ', 1)
                    message = data[1].strip() if len(data) > 1 else ""
                    current_time = time.time()
                    if username in user_last_command_time:
                        time_since_last = current_time - user_last_command_time[username]
                        if time_since_last < chat_delay:
                            remaining_time = chat_delay - time_since_last
                            print(f"Игнорируем команду от '{username}', подожди {int(remaining_time)} сек.")
                            continue

                    user_last_command_time[username] = current_time
                    if message.startswith('!ask '):
                        question = message[5:].strip()  # Убираем "!ask "
                        if question:
                            print(f"[{username}] спрашивает: {question}")
                            await process_question(username, question)

        await asyncio.sleep(0.1)


async def process_question(username, question):
    try:
        write_command(f"say [AI] {username} спрашивает AI...")
        press_key()
        await asyncio.sleep(0.5)
        answer = await send_to_ai(question)
        
        if answer:
            max_length = 100
            if len(answer) > max_length:
                parts = [answer[i:i+max_length] for i in range(0, len(answer), max_length)]
                for i, part in enumerate(parts):
                    write_command(f"say [AI] {part}")
                    press_key()
                    await asyncio.sleep(1)
            else:
                write_command(f"say [AI] {answer}")
                press_key()
        else:
            write_command(f"say [AI] Ошибка: не удалось получить ответ")
            press_key()

    except Exception as e:
        print(f"Ошибка при обработке вопроса: {e}")
        write_command(f"say [AI] Ошибка: {str(e)[:50]}")
        press_key()


if __name__ == "__main__":
    print("CS2 ChatGPT бот запускается...")
    print("Используй команду: !ask <твой вопрос>")
    try:
        asyncio.run(handle_chat())
    except KeyboardInterrupt:
        print("\nБот остановлен.")
