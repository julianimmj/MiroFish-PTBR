import os
import re
from deep_translator import GoogleTranslator
import time

# Padrão para encontrar texto com caracteres chineses
CHINESE_PATTERN = re.compile(r'[\u4e00-\u9fff]+')

def translate_text(text):
    """Traduz o texto de chinês para português usando Google Translate."""
    try:
        # Extrair apenas a parte chinesa/texto (ignorando formatações ao redor se possível)
        # Por segurança, vamos usar o tradutor direto
        translator = GoogleTranslator(source='zh-CN', target='pt')
        translated = translator.translate(text)
        time.sleep(0.5)  # Evitar rate limit
        return translated
    except Exception as e:
        print(f"Erro ao traduzir '{text}': {e}")
        return text

def process_file(filepath):
    """Lê um arquivo, encontra strings com caracteres chineses, traduz e salva."""
    print(f"\nProcessando: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Encontrar todas as sequências de texto que contêm chinês
    # Vamos usar regex para encontrar o conteúdo dentro de aspas simples ou duplas,
    # ou comentários preenchidos com chinês.
    
    # 1. Encontrar o que parece ser texto chinês
    # Uma abordagem mais segura é encontrar cada linha que tenha caracteres chineses
    lines = content.split('\n')
    new_lines = []
    translations_made = 0
    
    for i, line in enumerate(lines):
        if CHINESE_PATTERN.search(line):
            # Encontrou chinês na linha
            # Vamos tentar isolar as partes entre aspas ou comentários
            
            # Se for comentário ou docstring simples, podemos traduzir a linha
            if line.strip().startswith('#'):
                chinese_part = line.strip()[1:].strip()
                if CHINESE_PATTERN.search(chinese_part):
                    translated = translate_text(chinese_part)
                    line = line.replace(chinese_part, translated)
                    translations_made += 1
            else:
                # Para strings no código (dentro de aspas duplas)
                matches = re.finditer(r'"([^"\\]*(?:\\.[^"\\]*)*)"', line)
                for match in matches:
                    string_content = match.group(1)
                    if CHINESE_PATTERN.search(string_content):
                        # Evitar traduzir chaves JSON misturadas
                        translated = translate_text(string_content)
                        line = line.replace(f'"{string_content}"', f'"{translated}"')
                        translations_made += 1
                
                # Para strings no código (dentro de aspas simples)
                matches_single = re.finditer(r"'([^'\\]*(?:\\.[^'\\]*)*)'", line)
                for match in matches_single:
                    string_content = match.group(1)
                    if CHINESE_PATTERN.search(string_content):
                        translated = translate_text(string_content)
                        line = line.replace(f"'{string_content}'", f"'{translated}'")
                        translations_made += 1
                        
        new_lines.append(line)

    if translations_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"  OK: {translations_made} traduções aplicadas.")
    else:
        print("  Nenhuma tradução feita (ou apenas triplas aspas - ignoradas provisoriamente).")
    
    return translations_made

def main():
    backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
    total_translations = 0
    
    for root, dirs, files in os.walk(backend_dir):
        for filename in files:
            if filename.endswith('.py') and 'site-packages' not in root:
                filepath = os.path.join(root, filename)
                total_translations += process_file(filepath)
                
    print(f"\nConcluído! Total de traduções aplicadas: {total_translations}")

if __name__ == "__main__":
    main()
