import yt_dlp
import subprocess
import os
import shutil
from typing import Tuple, Optional

# Constantes
REQUIRED_DIRS = ["tmp", "downloads"]
AUDIO_OPTION = "1"
VIDEO_OPTION = "2"

class ErroDownload(Exception):
    """Exceção personalizada para falhas no download"""
    pass

class ErroMerge(Exception):
    """Exceção personalizada para falhas na mesclagem de arquivos"""
    pass

def garantir_diretorios(diretorios: list) -> None:
    """Cria os diretórios necessários, se não existirem"""
    for diretorio in diretorios:
        try:
            os.makedirs(diretorio, exist_ok=True)
        except OSError as e:
            print(f"Erro ao criar o diretório {diretorio}: {e}")
            raise

def limpar_nome_arquivo(nome: str) -> str:
    """Remove caracteres problemáticos do nome do arquivo"""
    caracteres_invalidos = '<>:"/\\|?*'
    for char in caracteres_invalidos:
        nome = nome.replace(char, '_')
    return nome

def baixar_conteudo(url: str, apenas_audio: bool = False) -> Tuple[Optional[str], Optional[str]]:
    """
    Baixa o conteúdo da URL informada.

    Args:
        url: URL do vídeo
        apenas_audio: Define se será baixado somente o áudio

    Returns:
        Tupla contendo (caminho_video, caminho_audio)
    """
    ydl_opts = {
        "format": "bestaudio/best" if apenas_audio else "bestvideo+bestaudio/best",
        "outtmpl": "tmp/%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = limpar_nome_arquivo(info.get("title", "video"))
            extensao = info.get("ext", "mp4")

            print(f"\nBaixando: {titulo}")
            ydl.download([url])
            print("Download concluído com sucesso")

            if apenas_audio:
                return f"tmp/{titulo}.{extensao}", None
            else:
                return f"tmp/{titulo}.{extensao}", None
                
    except Exception as e:
        print(f"\nErro durante o download: {e}")
        raise ErroDownload(f"Falha ao baixar o conteúdo: {e}")

def mesclar_arquivos(video: str, audio: str) -> str:
    """
    Mescla arquivos de vídeo e áudio usando o FFmpeg.

    Args:
        video: Caminho do arquivo de vídeo
        audio: Caminho do arquivo de áudio

    Returns:
        Caminho do arquivo final mesclado
    """
    if not all(os.path.isfile(f) for f in [video, audio]):
        faltando = [f for f in [video, audio] if not os.path.isfile(f)]
        raise FileNotFoundError(f"Arquivos ausentes: {', '.join(faltando)}")

    arquivo_saida = video.replace(".mp4", "_mesclado.mp4")
    
    try:
        subprocess.run([
            "ffmpeg",
            "-y",
            "-i", video,
            "-i", audio,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-loglevel", "error",
            "-stats",
            arquivo_saida
        ], check=True)
        
        print(f"\nArquivo mesclado com sucesso: {arquivo_saida}")
        return arquivo_saida
        
    except subprocess.CalledProcessError as e:
        print(f"\nFalha na mesclagem com FFmpeg: {e}")
        raise ErroMerge("Falha ao mesclar vídeo e áudio")

def mover_para_downloads() -> None:
    """Move todos os arquivos da pasta 'tmp' para a pasta 'downloads'"""
    try:
        for arquivo in os.listdir("tmp"):
            origem = os.path.join("tmp", arquivo)
            destino = os.path.join("downloads", arquivo)
            
            if os.path.isfile(origem):
                shutil.move(origem, destino)
                
        print("\nTodos os arquivos foram movidos para a pasta 'downloads'")
        
    except Exception as e:
        print(f"\nErro ao mover arquivos: {e}")
        raise

def obter_entrada_usuario() -> Tuple[str, str]:
    """Solicita e valida entrada do usuário"""
    while True:
        url = input("\nDigite a URL do vídeo: ").strip()
        if url:
            break
        print("Por favor, insira uma URL válida")

    while True:
        opcao = input("\nEscolha uma opção:\n1 - Apenas áudio\n2 - Vídeo com áudio\n> ").strip()
        if opcao in (AUDIO_OPTION, VIDEO_OPTION):
            break
        print("Digite 1 ou 2")

    return url, opcao

def main() -> None:
    """Função principal de execução"""
    print("\nDownloader de YouTube")
    print("---------------------")
    
    try:
        url, opcao = obter_entrada_usuario()
        garantir_diretorios(REQUIRED_DIRS)
        
        if opcao == AUDIO_OPTION:
            print("\nBaixando apenas o áudio...")
            audio, _ = baixar_conteudo(url, apenas_audio=True)
        else:
            print("\nBaixando vídeo com áudio...")
            video, _ = baixar_conteudo(url)
        
        mover_para_downloads()
        
    except Exception as e:
        print(f"\nErro: {e}")
    finally:
        print("\nOperação finalizada")

if __name__ == "__main__":
    main()
