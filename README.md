<img width="724" height="239" alt="image" src="https://github.com/user-attachments/assets/3359b63e-274b-470a-909a-57ecc660d46d" />

### ENGLISH
### first launch and setup
0. go to openrouter, get api key and paste it in chatgpt.py line 5
1. in main.py lines 8 9 10 change to your paths
2. in util.py line 28 change to your path
3. install dependencies:
cd "path to CS2ChatGPT folder"
pip install -r requirements.txt

4. create empty file "message.cfg":
"your_path_to_CS2\game\csgo\cfg\message.cfg"

5. cs2 properties -> launch options:
-condebug -conclearlog

6. in game console:
bind f5 "exec message"

### every launch

1. start cs2

2. powershell as administrator:
cd "path to CS2ChatGPT folder"
py main.py

launch completed

type in chat: "!ask your question"

### default settings (you can change in code)

- API: OpenRouter (GPT-4o-mini)
- message limit: 100 characters (don't change, cs2 chat limit)
- delay between requests: 3 seconds
- bind: F5 (you can change it in util.py)

---
### RUSSIAN
### первый запуск и настройка
0.заходишь на опенроутер, получаешь апи ключ и вставляешь его в chatgpt.py в 5 строку
1. в main.py строки 8 9 10 меняешь на свои
2. в util.py 28 строку поменяй на свой путь
3. установка зависимостей:
cd "путь к папке CS2ChatGPT"
pip install -r requirements.txt

4. создай пустой файл "message.cfg":
"твой_путь_к_CS2\game\csgo\cfg\message.cfg"

5.  свойства кс2 -> параметры запуска:
-condebug -conclearlog

6. в игре в консоли:
bind f5 "exec message"

### каждый запуск

1. запуск кс2

2. powershell от имени администратора:
cd "путь к папке CS2ChatGPT" 
py main.py

запуск завершен

пиши в чат: "!ask твой вопрос"

### настройки по дефолту(можешь поменять в коде)
- API: OpenRouter (GPT-4o-mini)
- лимит сообщения: 100 символов (не менять, лимит кс2 чата)
- задержка между запросами: 3 секунды
- бинд: F5 (можно поменять в util.py)
