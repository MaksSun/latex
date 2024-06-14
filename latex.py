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
        with open('latetex_documets.tex', 'w', encoding='utf-8') as f:
            f.write(self.get_tex())

        import subprocess
        import os

        # Компиляция TeX-файла в PDF
        subprocess.run(['pdflatex', 'latetex_documets.tex'])

        # Компиляция TeX-файла в PDF
        subprocess.run(['pdflatex', 'latetex_documets.tex'])

        # Удаление временных файлов
        os.remove('latetex_documets.aux')
        os.remove('latetex_documets.log')
        os.remove('latetex_documets.tex')

    def default(self, title='', abstract='', fancyhead=''):
        self.add_head(r'\documentclass[12pt]{article}')
        self.add_head(r'\usepackage[T2A]{fontenc}')
        self.add_head(r'\usepackage[utf8]{inputenc}')
        self.add_head(r'\usepackage[left=3cm, right=1.5cm, top=2cm, bottom=2cm]{geometry}')
        self.add_head(r'\usepackage[english, russian]{babel}')
        self.add_head(r'\usepackage{fancyhdr}')

        self.add_title(f'\\title{{{title}}}')
        self.add_title(r'\author{Монгуш М.А. \thanks{Муниципальное автономное образовательное учреждение Лицей №1}}')
        self.add_title(r'\date{\today}')

        self.add_abstract(r'\begin{abstract}')
        self.add_abstract(f'{abstract}')
        self.add_abstract(r'\end{abstract}')

        self.add_fancyhead(r'\pagestyle{fancy}')
        self.add_fancyhead(f'\\fancyhead[R]{{{fancyhead}}}')
        self.add_fancyhead(r'\fancyhead[L]{Монгуш М.А.}')
        self.add_fancyhead(r'\fancyhead[C]{\today}')