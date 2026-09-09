import logging


# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("execucao_bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


def processar_arquivo(caminho: str):
    try:
        # Abre o arquivo usando o gerenciador de contexto with
        with open(caminho, "r", encoding="utf-8") as arquivo:

            # Lê cada linha do arquivo
            for linha in arquivo:
                linha = linha.strip()

                # Registra cada linha lida
                logging.info(f"Linha lida: {linha}")

    except FileNotFoundError:
        # Registra erro caso o arquivo não seja encontrado
        logging.error(f"Arquivo não encontrado: {caminho}")

    finally:
        # Registra o término da tentativa de processamento
        logging.info("Término da tentativa de processamento.")


if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo: ")
    processar_arquivo(caminho)
