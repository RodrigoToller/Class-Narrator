from flask import Flask, render_template, request, send_file, jsonify, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Listar todos os arquivos de áudio na pasta static/audio
    audio_files = os.listdir('static/audio')
    audio_files = [f'audio/{file}' for file in audio_files if file.endswith('.mp3')]  # Somente arquivos .mp3
    return render_template('index.html', audio_files=audio_files)

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    texto = request.form.get('texto')
    titulo = request.form.get('titulo')

    # Depuração para ver os dados recebidos
    print(f"Texto recebido: {texto}")
    print(f"Título recebido: {titulo}")

    if texto and titulo:
        # Limpar o título para evitar caracteres inválidos
        titulo_limpo = "".join([c for c in titulo if c.isalnum() or c in (' ', '_')]).rstrip()
        
        # Criar o nome do arquivo a partir do título
        audio_file = f"static/audio/{titulo_limpo}.mp3"
        
        # Gerar o áudio
        tts = gTTS(text=texto, lang='pt')
        tts.save(audio_file)
        
        # Retornar a URL do áudio gerado
        audio_url = url_for('static', filename=f'audio/{titulo_limpo}.mp3')
        return jsonify({'audio_url': audio_url})
    
    return jsonify({'error': 'Texto ou título estão faltando'}), 400

if __name__ == "__main__":
    # Crie a pasta static/audio se ela não existir
    if not os.path.exists('static/audio'):
        os.makedirs('static/audio')
    
    # Executar o aplicativo Flask
    app.run(debug=True)
