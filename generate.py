from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice
import os
import torch
import torchaudio

tts = TextToSpeech()

voices_dict = {}

# Choosing voice samples. Can be found under tortoise/voices
# It may take some time to download necesary files from HuggingFace for this engine to run so be patient
# You can also add your own voice audio samples to the tortoise/voices folder and work with that
voice_samples, chosen_voice_latents = load_voice("deniro")

# Read your story from a file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by paragraphs or double newlines
chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

# Generate and collect audio clips
all_clips = []
for i, chunk in enumerate(chunks):
    print(f"Generating audio for chunk {i+1}/{len(chunks)}...")

    # You can change the preset values here if you want faster but low quality output or slower and high quality output
    clip = tts.tts_with_preset(text=chunk, voice_samples=voice_samples, conditioning_latents=chosen_voice_latents, preset="fast")
    all_clips.append(clip)

# Concatenate all clips
combined = torch.cat(all_clips, dim=-1)

# Save final audio file in the "results" folder
os.makedirs("results", exist_ok=True)
torchaudio.save("results/final_output.wav", combined.squeeze(0).cpu(), 24000)
print("Audio saved to results/final_output.wav")
