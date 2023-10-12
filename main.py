import moviepy.editor
from pathlib import Path


directory_to_save = "audios"
path_list = Path(directory_to_save).glob("*.mp4")

for arquivo in path_list:
    print(arquivo)
    videoclip = moviepy.editor.VideoFileClip(str(arquivo))
    videoclip.audio.write_audiofile(f"{str(arquivo)}.mp3")
