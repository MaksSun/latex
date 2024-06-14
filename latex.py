class Latex:
    def __init__(self):
        self.tex_document = []
        self.head_list = []
        self.title = []
        self.function = []
        self.abstract = []
        self.document = []
        self.fancyhead = []

        self.document.insert(0, r'\begin{document}')
        self.document.insert(1, r'\maketitle')
        self.document.insert(2, self.abstract)
        self.document.insert(3, self.fancyhead)
        self.document.insert(len(self.document), r'\end{document}')

        self.tex_document.insert(0, self.head_list)
        self.tex_document.insert(1, self.title)
        self.tex_document.insert(2, self.function)
        self.tex_document.insert(3, self.document)

    def get_tex_tex(self):
        return self.tex_document

    def get_tex(self):
        tex = ''
        for mass_doc in self.tex_document:
            for mass_tex in mass_doc:
                if type(mass_tex) != list:
                    tex += str(mass_tex) + '\n'

                if type(mass_tex) == list:
                    for mass_tex_doc in mass_tex:
                        tex += str(mass_tex_doc) + '\n'
        return tex

    def add_head(self, addheader):
        self.head_list.append(addheader)

    def add_title(self, addtitle):
        self.title.append(addtitle)

    def add_abstract(self, addabstract):
        self.abstract.append(addabstract)

    def add_fancyhead(self, addfancyhead):
        self.fancyhead.append(addfancyhead)

    def add_document(self, documented):
        self.document.insert(len(self.document) - 1, documented)

    def create_pdf(self):
        # Запись TeX-кода в файл
        with open('teaching_geometry.tex', 'w', encoding='utf-8') as f:
            f.write(self.get_tex())

        import subprocess
        import os

        # Компиляция TeX-файла в PDF
        subprocess.run(['pdflatex', 'teaching_geometry.tex'])

        # Компиляция TeX-файла в PDF
        subprocess.run(['pdflatex', 'teaching_geometry.tex'])

        # Удаление временных файлов
        os.remove('teaching_geometry.aux')
        os.remove('teaching_geometry.log')
        os.remove('teaching_geometry.tex')


if __name__ == '__main__':
    Latex = Latex()
    Latex.add_head(r'\documentclass[12pt]{article}')
    Latex.add_head(r'\usepackage[T2A]{fontenc}')
    Latex.add_head(r'\usepackage[utf8]{inputenc}')
    Latex.add_head(r'\usepackage[left=3cm, right=1.5cm, top=2cm, bottom=2cm]{geometry}')
    Latex.add_head(r'\usepackage[english, russian]{babel}')
    Latex.add_head(r'\usepackage{fancyhdr}')

    Latex.add_title(r'\title{}')
    Latex.add_title(r'\author{Монгуш М.А. \thanks{Муниципальное автономное образовательное учреждение Лицей №1}}')
    Latex.add_title(r'\date{\today}')

    Latex.add_abstract(r'\begin{abstract}')
    Latex.add_abstract(r'')
    Latex.add_abstract(r'\end{abstract}')

    Latex.add_fancyhead(r'\pagestyle{fancy}')
    Latex.add_fancyhead(r'\fancyhead[R]{}')
    Latex.add_fancyhead(r'\fancyhead[L]{Монгуш М.А.}')
    Latex.add_fancyhead(r'\fancyhead[C]{\today}')

    print(Latex.get_tex_tex())

    print(Latex.get_tex())

    Latex.create_pdf()
