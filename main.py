import moviepy.editor
import re
from pathlib import Path


directory_to_save = "audios"
path_list = Path(directory_to_save).glob("*.mp4")

for arquivo in path_list:
    print(arquivo)
    nome = str(arquivo).split('audios/')[1].split('.mp4')[0]
    videoclip = moviepy.editor.VideoFileClip(str(arquivo))
    videoclip.audio.write_audiofile(f"audios/{nome}.mp3")
