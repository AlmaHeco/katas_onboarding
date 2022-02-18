
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("es un directorio no se puede leer")


if __name__ == '__main__':
    main()