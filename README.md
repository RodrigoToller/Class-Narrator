
# Class Narrator

**Class Narrator** é uma aplicação web desenvolvida por Rodrigo da empresa **Class Solutions**, que converte textos em áudio. Ela utiliza Python e Flask no backend para processar o texto e gerar arquivos de áudio em formato MP3, com o auxílio da biblioteca Google Text-to-Speech (gTTS).

## 🚀 Funcionalidades

- Converte textos inseridos pelo usuário em arquivos de áudio (.mp3).
- Lista os áudios gerados, permitindo reprodução e download direto.
- Interface com estilo visual inspirado no Spotify.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem principal do projeto.
- **Flask**: Framework web para a criação do backend.
- **gTTS (Google Text-to-Speech)**: Biblioteca Python para converter texto em áudio.
- **HTML5, CSS3, e JavaScript**: Para a interface do usuário (frontend).
- **MediaElement.js**: Biblioteca JavaScript usada para personalizar os players de áudio.

## 📦 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- **Python 3.12**: [Download Python](https://www.python.org/downloads/)
- **pip**: O gerenciador de pacotes do Python. Ele geralmente vem junto com o Python, mas você pode verificar a instalação com o comando:

```bash
pip --version
```

## 🛠️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/class-narrator.git
cd class-narrator
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
# No Windows
python -m venv venv
venv\Scriptsctivate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências do projeto
Use o pip para instalar as bibliotecas necessárias que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não exista ainda, você pode criá-lo com o seguinte comando:

```bash
pip freeze > requirements.txt
```

Dependências principais:

- Flask: Framework web.
- gTTS: Biblioteca para converter texto em áudio.

Instale as dependências diretamente, se preferir:

```bash
pip install Flask gTTS
```

## 📂 Estrutura do Projeto

Certifique-se de que a estrutura de diretórios do seu projeto siga este formato:

```
/ (pasta raiz do projeto)
|-- app.py                # Código principal do servidor Flask
|-- requirements.txt       # Dependências do Python
|-- static/                # Arquivos estáticos (CSS, JS, etc.)
|   |-- css/
|       |-- style.css      # Estilos da aplicação
|-- templates/             # Templates HTML
|   |-- index.html         # Página principal da aplicação
```

## 🖥️ Executando o Servidor

Agora você pode rodar a aplicação localmente:

```bash
python app.py
```

Acesse a aplicação no navegador via [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 🎮 Uso

1. Abra a aplicação no navegador.
2. Insira o título e o texto que deseja converter em áudio.
3. Clique em "Converter para Áudio".
4. O áudio será gerado e listado na página com um player para pré-visualização e um link para download.

## 📂 Estrutura do Código

Aqui está uma visão geral das pastas e arquivos mais importantes no projeto:

```
/ (pasta do projeto)
|-- app.py                # Código principal do servidor Flask
|-- requirements.txt       # Dependências do Python
|-- static/                # Arquivos estáticos (CSS, JS, etc.)
|   |-- css/
|       |-- style.css      # Estilos da aplicação
|-- templates/             # Templates HTML
|   |-- index.html         # Página principal da aplicação
```

Descrição dos Arquivos:

- `app.py`: O arquivo principal da aplicação Flask, onde o backend é configurado.
- `requirements.txt`: Contém as dependências do projeto para instalação.
- `static/`: Diretório para os arquivos estáticos como CSS e JavaScript.
- `templates/`: Diretório onde os arquivos HTML são armazenados.

