import yt_dlp
import subprocess
import os

# Função para garantir que o diretório 'media' exista
def ensure_media_directory():
    if not os.path.exists('media'):
        os.makedirs('media')

def download_content(url, download_audio=False):
    ensure_media_directory()  # Garantir que o diretório 'media' exista
    
    ydl_opts = {
        "format": "bestaudio/best" if download_audio else "bestvideo+bestaudio/best",
        "outtmpl": "media/%(title)s.%(ext)s",
        "noplaylist": True,  # Não baixar playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_title = info.get("title", "video")
        file_extension = info.get("ext", "mp4")  # Obter a extensão do arquivo

        print(f"Baixando: {video_title}")
        ydl.download([url])
        print(f"Download concluído: {video_title}")

        # Determinar o nome do arquivo de acordo com o tipo de download
        if download_audio:
            content_file = f"media/{video_title}.{file_extension}"
            return content_file, None
        else:
            video_file = f"media/{video_title}.mp4"
            audio_file = f"media/{video_title}.webm"  # ou o formato correspondente
            return video_file, audio_file

def convert_to_mp4(video_file, audio_file):
    # Gerar nome do arquivo final
    output_file = video_file.replace(".mp4", "_final.mp4")

    # Verificar se os arquivos existem
    if not os.path.isfile(video_file):
        print(f"Arquivo de vídeo não encontrado: {video_file}")
        return

    if not os.path.isfile(audio_file):
        print(f"Arquivo de áudio não encontrado: {audio_file}")
        return

    # Comando FFmpeg para combinar o vídeo e o áudio
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-i",
        video_file,  # Arquivo de vídeo
        "-i",
        audio_file,  # Arquivo de áudio
        "-c:v",
        "copy",  # Copiar o vídeo sem reencodificar
        "-c:a",
        "aac",  # Codificar o áudio em AAC
        "-b:a",
        "192k",  # Taxa de bits para o áudio
        "-preset",
        "fast",  # Usar preset rápido para melhorar a velocidade
        output_file,
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Arquivo final combinado criado: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar FFmpeg: {e}")

if __name__ == "__main__":
    video_url = input("URL do vídeo: \n")
    choice = input("Baixar apenas áudio (1) ou vídeo e áudio (2)? \n").strip().lower()

    if choice == "1":
        audio_file, _ = download_content(video_url, download_audio=True)
        if audio_file:
            print(f"Arquivo de áudio baixado: {audio_file}")
    elif choice == "2":
        video_file, audio_file = download_content(video_url)
        if video_file and audio_file:
            convert_to_mp4(video_file, audio_file)
    else:
        print("Escolha inválida. Por favor, escolha '1' para áudio ou '2' para vídeo e áudio.")
