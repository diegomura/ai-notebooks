import os
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

print(TTS().list_models())

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

en_text="In a quaint little town nestled between rolling hills and dense forests, lived two friends named Sarah and David. They were inseparable since childhood, sharing laughter, dreams, and the occasional secret. One gloomy evening, the sky painted in shades of gray, they found themselves in Sarah's cozy living room, engrossed in conversation."

es_text='''Un hombre del pueblo de Neguá, en la costa de Colombia, pudo subir al alto cielo.
A la vuelta, contó. Dijo que había contemplado, desde allá arriba, la vida humana. Y dijo que somos un mar de fueguitos.
—El mundo es eso —reveló—. Un montón de gente, un mar de fueguitos.
Cada persona brilla con luz propia entre todas las demás. No hay dos fuegos iguales. Hay fuegos grandes y fuegos chicos y fuegos de todos los colores. Hay gente de fuego sereno, que ni se entera del viento, y gente de fuego loco, que llena el aire de chispas. Algunos fuegos, fuegos bobos, no alumbran ni queman; pero otros arden la vida con tantas ganas que no se puede mirarlos sin parpadear, y quien se acerca, se enciende.'''

tts.tts_to_file(
  text=es_text,
  speaker_wav=[
    os.path.join(os.getcwd(), 'tortoise-voices/rec.wav'),
  ],
  language="es",
  file_path="xtts-rec-es.wav"
)
