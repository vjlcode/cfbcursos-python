num1 = num2 = res = 0
# escopo geral
canal = "CFB Cursos"


def cn():
    # escopo local
    curso = "Curso de Java"
    # declaração de variavel global
    global url
    url = "https://www.youtube.com/c/cfbcursos"
    print(canal + " - " + curso)
    
cn()

print(url)