from fatos import buscar_fato_aleatorio
from sistema import obter_info_sistema


def main():
    fato = buscar_fato_aleatorio()
    info = obter_info_sistema()

    resultado = {"Fato : ": fato, **info}
    print(resultado)


if __name__ == "__main__":
    main()
