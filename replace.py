import os

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('.html'):
            filepath = os.path.join(root, name)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                
                content = content.replace('<span>Задания</span>', '<span>Задания по номерам</span>')
                content = content.replace('>Задания</a>', '>Задания по номерам</a>')
                
                content = content.replace('<span>Варианты</span>', '<span>Варианты ЕГЭ</span>')
                content = content.replace('>Варианты</a>', '>Варианты ЕГЭ</a>')
                
                content = content.replace('<span>Панель</span>', '<span>Моя статистика</span>')
                content = content.replace('>Панель</a>', '>Моя статистика</a>')
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {filepath}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
