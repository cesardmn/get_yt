# Downloader Vídeo | Áudio do YouTube

## Visão Geral

Este script em Python oferece uma maneira prática de baixar vídeos ou áudios do YouTube e de outros sites suportados utilizando o `yt-dlp`, usando o `FFmpeg` para renderizar o arquivo final.

## Funcionalidades

- **Opções Flexíveis de Download**:
  - Baixar vídeo com áudio
  - Baixar somente o áudio
- **Gerenciamento Automático de Arquivos**:
  - Arquivos temporários são armazenados na pasta `tmp/`
  - Arquivos finais são movidos para a pasta `downloads/`
- **Preservação de Qualidade**:
  - Utiliza a melhor qualidade disponível por padrão
  - Mesclagem inteligente sem recodificação desnecessária

## Requisitos

- Python 3.7 ou superior  
- FFmpeg (deve estar no PATH do sistema)  
- Pacotes Python necessários (instale via `requirements.txt`)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/cesardmn/get_yt.git
   cd get_yt
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o FFmpeg está instalado e acessível:
   - **Windows**: Baixe em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione ao PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

## Uso

Execute o script:
```bash
python main.py
```

Siga as instruções:
1. Insira a URL do vídeo quando solicitado  
2. Escolha entre:
   - `1` para baixar apenas o áudio  
   - `2` para baixar vídeo com áudio  

Os arquivos baixados serão salvos na pasta `downloads/`.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
