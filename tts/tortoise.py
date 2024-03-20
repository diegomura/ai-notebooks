import os
from TTS.api import TTS

tts = TTS("tts_models/en/multi-dataset/tortoise-v2")

# cloning `lj` voice from `TTS/tts/utils/assets/tortoise/voices/lj`
# with custom inference settings overriding defaults.
# tts.tts_to_file(text="Hello, my name is Manmay , how are you?",
#                 file_path="output.wav",
#                 voice_dir="path/to/tortoise/voices/dir/",
#                 speaker="lj",
#                 num_autoregressive_samples=1,
#                 diffusion_iterations=10)

# Using presets with the same voice
tts.tts_to_file(text="In a quaint little town nestled between rolling hills and dense forests, lived two friends named Sarah and David. They were inseparable since childhood, sharing laughter, dreams, and the occasional secret. One gloomy evening, the sky painted in shades of gray, they found themselves in Sarah's cozy living room, engrossed in conversation.",
                file_path="./output.wav",
                voice_dir=os.path.join(os.getcwd(), 'tortoise-voices'),
                speaker="daniel",
                preset="ultra_fast")
