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
   git clone git@github.com:ggomes12/Simula-o-Dispositivos-IoT-MQTT-Asyncio.git
   cd Simula-o-Dispositivos-IoT-MQTT-Asyncio
   ```
2. Instale as dependências:
   ```bash
   pip install paho-mqtt
   ```
3. Execute o script Python:
   ```bash
   python3 simulador_iot.py
   ```

O programa irá se conectar ao broker MQTT público e começar a publicar dados simulados para os tópicos configurados.


## Estrutura do Código

O código principal está dividido nas seguintes partes:

### 1. Configuração do Cliente MQTT

O cliente MQTT é configurado para conectar ao broker e se inscrever em vários tópicos, como:

- `casa/geladeira`
- `casa/tv`
- `casa/portas`
- `casa/quarto`

### 2. Callbacks

- **`ao_conectar`**: Função chamada quando o cliente se conecta ao broker MQTT. Nessa função, o cliente se inscreve nos tópicos definidos para receber mensagens.
  
- **`ao_receber_mensagem`**: Função chamada quando uma mensagem é recebida em um dos tópicos nos quais o cliente está inscrito. Nessa função, você pode definir o comportamento a ser executado ao receber uma mensagem de determinado tópico.

### 3. Funções Assíncronas

- **`geladeira`**: Publica dados simulados da geladeira, como temperatura, consumo de energia e estado da porta (aberta ou fechada).
  
- **`tv`**: Publica dados simulados sobre a TV, incluindo seu estado (ligada/desligada), canal, volume e usuário que está controlando a TV.
  
- **`portas`**: Publica dados simulados sobre o estado das portas da casa, como se estão abertas ou fechadas.
  
- **`quarto`**: Publica dados simulados sobre o quarto, incluindo se está ocupado, a temperatura e o estado da luz.

- **`gerenciar_topicos`**: Gerencia a adição e remoção dinâmica de tópicos MQTT, permitindo que novos tópicos sejam criados ou excluídos ao longo da execução do programa.

### 4. Função Principal

A função **`principal`** configura o cliente MQTT, estabelece a conexão com o broker e inicia a execução das funções assíncronas. Essas funções são responsáveis por simular os dados dos dispositivos e publicá-los nos tópicos MQTT. A execução assíncrona é utilizada para garantir que as publicações ocorram simultaneamente sem bloqueio, permitindo que o código rode de forma eficiente.

---

## Exemplo de Saída

Ao rodar o código, você verá mensagens como as seguintes no terminal:


![Testes do simulador](images/imagem.jpg)
