# Download e Conversão de Vídeos

Este projeto permite baixar vídeos ou áudios de URLs usando `yt-dlp` e combinar arquivos de vídeo e áudio em um único arquivo usando `FFmpeg`.

## Funcionalidades

- **Download de Vídeo e Áudio**: Baixa o vídeo completo com áudio ou apenas o áudio de uma URL fornecida.
- **Conversão de Arquivo**: Combina arquivos de vídeo e áudio em um único arquivo.

## Pré-requisitos

Certifique-se de ter o Python 3.x e `FFmpeg` instalados em seu sistema.

- [Python](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/cesardmn/get_yt.git
   cd get_yt
   ```

2. Instale as dependências usando `pip`:

   ```bash
   pip install -r requirements.txt
   ```
### Uso

1. Execute o script Python:

   ```bash
   python main.py
   ```

2. Quando solicitado, insira a URL do vídeo.

3. Escolha entre:
   - **1**: Baixar apenas o áudio.
   - **2**: Baixar vídeo e áudio e combinar em um arquivo.

## Exemplo de Execução

```bash
URL do vídeo: 
https://www.youtube.com/watch?v=dQw4w9WgXcQ
Baixar apenas áudio (1) ou vídeo e áudio (2)? 
2
```

Se você escolher a opção **2**, o script baixará o vídeo e o áudio e, em seguida, criará um arquivo combinado.

## Contribuições

Se você deseja contribuir para o projeto, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_ com melhorias ou correções. Certifique-se de seguir as boas práticas e manter a consistência com o estilo do código existente.

## Licença

Este projeto é de propriedade de Cesar Dimi e está licenciado sob a [Licença MIT](LICENSE).

## Contato

Para mais informações, você pode entrar em contato através do [perfil de Cesar Dimi](https://cesardmn.github.io/).
