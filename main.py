def main():
    from latex import Latex
    Latex = Latex()
    Latex.default()
    Latex.add_document('Проверка')

    Latex.create_pdf()


if __name__ == '__main__':
    main()
