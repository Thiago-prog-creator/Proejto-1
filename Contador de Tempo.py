import time
from datetime import datetime

nome = input("Qual seu nome? ")

print(f"\nOlá {nome}! Vou contar seu tempo no PC hoje.")
print("Pressione CTRL+C quando for sair...\n")

try:
    
    inicio = time.time()
    data = datetime.now().strftime("%d/%m/%Y")
    
    
    while True:
       time.sleep(1)

except KeyboardInterrupt:   
    fim = time.time()
    tempo_total = fim - inicio
    horas = int(tempo_total // 3600)
    minutos = int((tempo_total % 3600) // 60)      
    with open("tempo.txt", "a") as arquivo:
        arquivo.write(f"{data} - {nome} ficou {horas}h{minutos}m no PC\n")
    print(f"\nVocê ficou {horas}h{minutos}m hoje!")
    print("Salvei no arquivo 'tempo.txt'. Até amanhã!")
