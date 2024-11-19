import random
import asyncio
import paho.mqtt.client as mqtt

# config do MQTT
BROKER = "broker.hivemq.com"
PORTA = 1883
TOPICOS = {
    "geladeira": "casa/geladeira",
    "tv": "casa/tv",
    "portas": "casa/portas",
    "quarto": "casa/quarto"
}

cliente = mqtt.Client()

# Callback para quando a conexão for estabelecida
def ao_conectar(cliente, userdata, flags, rc):
    print(f"Conectado com o código {rc}")
    for topico in TOPICOS.values():
        cliente.subscribe(topico)
        print(f"Inscrito no tópico {topico}")

# Callback para quando uma mensagem for recebida
def ao_receber_mensagem(cliente, userdata, msg):
    print(f"[Recebido no tópico {msg.topic}]: {msg.payload.decode()}")

# gera os dados aleatórios para cada dispositivo
async def geladeira():
    while True:
        temperatura = round(random.uniform(2.0, 8.0), 1)
        consumo = round(random.uniform(0.5, 1.5), 2)
        porta = random.choice(["fechada", "aberta"])
        dados = f"Temperatura: {temperatura}°C, Consumo: {consumo}kW, Porta: {porta}"
        cliente.publish(TOPICOS["geladeira"], dados)
        print(f"Enviado para {TOPICOS['geladeira']}: {dados}")
        await asyncio.sleep(random.uniform(1, 3))

async def tv():
    while True:
        estado = random.choice(["ligada", "desligada"])
        canal = random.choice(["ESPN2", "NationalGeographic", "AnimalPlanet", "History2"])
        volume = random.randint(0, 100)
        usuario = random.choice(["Guilherme", "Kelvin", "Gomes"])
        dados = f"Estado: {estado}, Canal: {canal}, Volume: {volume}, Usuário: {usuario}"
        cliente.publish(TOPICOS["tv"], dados)
        print(f"Enviado para {TOPICOS['tv']}: {dados}")
        await asyncio.sleep(random.uniform(1, 3))

async def portas():
    portas = ["Entrada", "Cozinha", "Quarto 1", "Quarto 2", "Quarto 3"]
    while True:
        porta = random.choice(portas)
        estado = random.choice(["aberta", "fechada"])
        dados = f"Porta: {porta}, Estado: {estado}"
        cliente.publish(TOPICOS["portas"], dados)
        print(f"Enviado para {TOPICOS['portas']}: {dados}")
        await asyncio.sleep(random.uniform(1, 3))

async def quarto():
    while True:
        ocupacao = random.choice(["ocupado", "desocupado"])
        pessoa = random.choice(["Guilherme", "Kelvin", "Gomes"]) if ocupacao == "ocupado" else "Ninguém"
        temperatura = round(random.uniform(15.0, 40.0), 1)
        luz = random.choice(["ligada", "desligada"])
        dados = f"Ocupação: {ocupacao} por {pessoa}, Temperatura: {temperatura}°C, Luz: {luz}"
        cliente.publish(TOPICOS["quarto"], dados)
        print(f"Enviado para {TOPICOS['quarto']}: {dados}")
        await asyncio.sleep(random.uniform(1, 3))

# ger. a inserção e remoção de tópicos aleatoriamente
async def gerenciar_topicos():
    while True:
        acao = random.choice(["adicionar", "remover"])
        
        if acao == "adicionar":
            novo_topico = f"casa/{random.choice(['cozinha', 'banheiro', 'sala', 'garagem'])}"
            if novo_topico not in TOPICOS.values():
                TOPICOS[random.choice(['cozinha', 'banheiro', 'sala', 'garagem'])] = novo_topico
                cliente.subscribe(novo_topico)
                print(f"Novo tópico adicionado: {novo_topico}")
        
        elif acao == "remover":
            if TOPICOS:
                topicos_atuais = list(TOPICOS.values())
                topico_remover = random.choice(topicos_atuais)
                if topico_remover != 'casa/geladeira':
                    del TOPICOS[next(key for key, value in TOPICOS.items() if value == topico_remover)]
                    print(f"Tópico removido: {topico_remover}")

        await asyncio.sleep(random.uniform(5, 10))

# lógica de inscrição e envio assíncrono
async def principal():
    cliente.on_connect = ao_conectar
    cliente.on_message = ao_receber_mensagem
    
    cliente.connect(BROKER, PORTA, 60)

    await asyncio.gather(
        asyncio.to_thread(cliente.loop_start),
        geladeira(),
        tv(),
        portas(),
        quarto(),
        gerenciar_topicos()
    )

if __name__ == "__main__":
    try:
        asyncio.run(principal())
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")

