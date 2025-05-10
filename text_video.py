import cv2
import numpy as np
from gtts import gTTS
from pydub import AudioSegment
import cohere
import os

# -- Cohere Key --
COHERE_API_KEY = "QzycWIpIZJi2YIBKdWJKsj8myKcRJtz6hdft7s2A"
co = cohere.Client(COHERE_API_KEY)

# -- Input Text --
prompt = "Explain how neural networks work in simple terms."

# 1. Summarize or stylize the input
response = co.generate(prompt=prompt, max_tokens=200)
text = response.generations[0].text.strip()
print("Text for video:", text)

# 2. Generate TTS audio
tts = gTTS(text)
audio_path = "output_audio.mp3"
tts.save(audio_path)

# 3. Get audio duration
audio = AudioSegment.from_mp3(audio_path)
duration_sec = audio.duration_seconds

# 4. Create video from text
width, height = 1280, 720
fps = 24
total_frames = int(duration_sec * fps)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_path = "output_video.mp4"
out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

font = cv2.FONT_HERSHEY_SIMPLEX

for _ in range(total_frames):
    frame = np.zeros((height, width, 3), np.uint8)
    wrapped = text[:150] + "..." if len(text) > 150 else text
    y0, dy = 100, 60
    for i, line in enumerate(wrapped.split('. ')):
        y = y0 + i*dy
        cv2.putText(frame, line.strip(), (50, y), font, 1.2, (255, 255, 255), 2)
    out.write(frame)

out.release()

# 5. Merge audio & video with ffmpeg (must be installed separately)
final_output = "final_output.mp4"
os.system(f"ffmpeg -y -i {video_path} -i {audio_path} -c:v copy -c:a aac {final_output}")

print("🔥 Video created:", final_output)
