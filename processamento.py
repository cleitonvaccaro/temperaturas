def adicionar_media(dados: list) -> list:
    for item in dados:
        item["media"] = (item["max"] + item["min"]) / 2
    return dados