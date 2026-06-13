from deep_translator import GoogleTranslator

while True:
    texto = input("O que você quer traduzir? ")
    
    if not texto:
        print("Por favor, digite uma frase")
        continue
    try:
        resultado = GoogleTranslator(target="en").translate(texto)
        break
    
    except Exception as erro:
        print(f"Erro ao tentar traduzir {erro}")

print(resultado)