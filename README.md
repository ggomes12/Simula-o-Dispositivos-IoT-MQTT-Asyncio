# Simulação de Dispositivos IoT com MQTT e Asyncio

Este projeto simula dispositivos de uma casa inteligente que publicam dados em tópicos MQTT. Ele utiliza o protocolo MQTT para comunicação e a biblioteca `asyncio` para executar as tarefas de maneira assíncrona, permitindo que várias tarefas rodem simultaneamente sem bloquear a execução.

## Funcionalidades

- Simulação de dispositivos como geladeira, TV, portas e quarto, com dados gerados aleatoriamente.
- Publicação dos dados nos tópicos MQTT correspondentes.
- Gerenciamento dinâmico de tópicos, incluindo adição e remoção de tópicos aleatórios.
- Execução assíncrona utilizando `asyncio` para garantir alta performance e eficiência.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Paho MQTT**: Biblioteca cliente MQTT para Python.
- **Asyncio**: Biblioteca para programação assíncrona, permitindo execução concorrente sem bloqueios.
- **Broker MQTT**: O broker MQTT utilizado é o `broker.hivemq.com`, que é um broker público e gratuito.

## Como Funciona

O programa simula os seguintes dispositivos:
1. **Geladeira**: Publica dados como temperatura, consumo de energia e estado da porta.
2. **TV**: Publica dados sobre o estado da TV (ligada/desligada), canal, volume e o usuário que está controlando.
3. **Portas**: Publica dados sobre o estado de várias portas (aberta/fechada).
4. **Quarto**: Publica dados sobre a ocupação do quarto, temperatura e estado da luz.

Além disso, o código gerencia dinamicamente os tópicos, adicionando ou removendo tópicos aleatórios a cada execução.

## Instalação

### Requisitos
- Python 3.7 ou superior
- Biblioteca Paho MQTT
- Biblioteca Asyncio (já incluída no Python)

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
