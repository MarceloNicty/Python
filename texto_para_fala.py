# -*- coding: utf-8 -*-
from gtts import gTTS

# Texto a ser convertido em fala
text = "Olá, bom dia!"

# Criar um objeto gTTS com o idioma português do Brasil
tts = gTTS(text=text, lang='pt-br')

# Salvar o áudio em um arquivo
file_path = "ola_bom_dia_br.mp3"
tts.save(file_path)

print(f"Áudio salvo com sucesso como {file_path}")
