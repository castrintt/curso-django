# include recebe uma string -> onde voce vai indicar o nome do app e o nome do arquivo que tem os arquivos onde voce vai importar


# como o caminho (path) onde usamos o include esta como '' quer dizer que ele está na rota default

# se voce quiser adicionar varias rotas filhas usando include na rota hipotetica sobre, voce faria assim

# from django.urls import path, include

# urlpatterns =[
#     path('sobre/', include('detalhes.urls'))
# ]


# dentro de uma função em views temos que criar todo um arquivo html

# para isso o django nos ajuda com o render que importando de django.shortcuts
# dessa forma

from django.shortcuts import render
from django.urls import URLPattern

# agora como usamos o render?

# dentro das funções faremos o seguinte
# primeiro retornaremos o render

def home(request):
    return render()

# render recebe alguns parametros(no minimo2), são eles, a request e o caminho do arquivo html, desas forma

def home(request):
    return render(request, 'arquivo.html')

# estamos dizendo para o django renderizar na função(rota) home o arquivo html (e para isso ele faz uma request)

# porem o django ainda não sabe que existe esse arquivo, tanto que quando voce tenta acessar essa rota, vai te retornar um erro

# TemplateDoesNotExist

# para falar para o django que ele deve buscar esse arquivo(ou avisar ele que esse arquivo existe)
# devemos ir para o arquivo settings.py, localizado na pasta mestre(na pasta onde usamos o comando django-admin startproject nome_pasta)

# dentro do arquivo settings.py temos os aplicativos instalados
#que é basicamente uma lista com os arquivos que temos instalados

# por padrao ele ja vem assim


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# agora nós precisamos avisa para ele que existe tbm os apps
# para isso vamos indicar dentro dessa lista o nome do arquivo que usamos para criar o app (python manage.py startapp nome_app)


# dessa forma


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nome_arquivo_aqui'
]


# E PRONTO!! o django agora entende que temos um app 

# DEVEMOS FAZER ISSO PARA TODOS OS APPS QUE CRIARMOS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nome_arquivo_aqui'
    'nome_arquivo_aqui2'
    'nome_arquivo_aqui3'
    'nome_arquivo_aqui4'
    'nome_arquivo_aqui5'

    ...
]



# PARA INDICARMOS PAR AO DJANGO ONDE BUSCAR TEMPLATES VAMOS USAR O MESMO ARQUIVO SETTINGS.PY

# NELE VAMOS ACHAR UMA LISTA CHAMADA --> TEMPLATES

# por padrao ela vem com essa estrutura

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# nota que dentro de templates temos um dicionario, contante uma chave 'DIRS' que recebe uma lista como valor

# é dentro desse arquivo que vamos informar em que pastas ele deve buscar
# OBS -->  podemos colocar quantas pastas quisermos

# suponha que temos uma pasta chamada base_templates

# onde temos templates onde queremos que o django busque pra gente

# basta usar a seguinte sintaxe dentro de DIRS

# sintaxe: 

 # BASE_DIR / 'base_templates',

# entao ficaria assim

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

            BASE_DIR / 'base_templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# dessa forma estamos indicando o caminho da pasta onde ele deve buscar templates


# PARA EVITARMOS CONFLITOS DE NOMES NO DJANGO DEVEMOS CRIAR UMA ESTRUTURA DE PASTAS ESPECIFICAS

# dentro da pasta recipes ( onde criamos o app ), nós criamos a pasta templates e jogamos nosso html la, porem como existe outra pasta chamada base_templates e dentro dela tem o mesmo arquivo home.html
# o django rederiza por ordem oque esta dentro de:

    # 'DIRS': [

    #         BASE_DIR / 'base_templates',
    #     ],

# puxando assim o arquivo incorreto

# para resolver isso, dentro da pasta templates (dentro de recipes) nós vamos criar outra pasta COM O MESMO NOME DA PASTA APPS

# dessa forma teriamos

# recipes      # pasta app
# ---templates
#--------recipes     # pasta de template apps
#------------home.html

# assim o django entende qual arquivo rederizar!

# LEMBRANDO QUE O NOME DA PASTA DEVE SER O MESMO DO APP

# suponha que temos o app chamada nomes
# a estrutura ficaria assim

# home
# ----templates
# -------home
#-----------arquivo.html


# DEPOIS DESSE PROCESSO DENTRO DO ARQUIVO settings.py

# vamos voltar dentro do arquivo onde estamos criando a view

# que estava dessa forma:

from django.shortcuts import render
from django.http import HttpResponse as response


def home(request):
    return render(request, 'home.html')

def contato(request):
    return response('CONTATO 1')

def sobre(request):
    return response('SOBRE 1')


# para que  o django não erre, ou seja, não busque o arquivo home.html na pasta errada
# nós só vamos indicar para ele assim

def home(request):
    return render(request,'recipes/home.html')

    # só indicamos que esta dentro da pasta recipes

# por isso é EXPLICITAMENTE necesssario colocar a nome da pasta dentro de templates igual ao nome da pasta app



__________________________________________

# aula 2 

# se voce apertar control click no render

# voce tem todos os parametros que ele aceita

def render(
    request, template_name, context=None, content_type=None, status=None, using=None
)

# uma requesta, nome do template, context,contant_type, status e using

# vamos entender cada um desses parametros de render

# o primeiro é o context

# podemos passar dentro do context um dicionario por exemplo

def home(request):
    return render(request,'nome_ap/template.html', context={
        # passando uma chave nome com valor igor

        'name': 'igor'
    })

# podemos acessar esse parametro dentro do nosso template (html) da seguinte forma
# sintaxe {{ chave }}

# logo dentro do template teriamos 

# passando o dado (como se fosse um dado dinamico em vue js, entre 2 chaves)
# sintaxe : {{ dado }}

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1>Temos um titulo</h1>
#     <h2>
#         {{ name }} # {{ dado }}
#     </h2>

# </body>
# </html>

# segue imagem_________________


# podemos alterar manualmente o status da solicitação com o parametro status
# podemos fazer uma aplicação ter o status 404 de error por exemplo

def home(request):
    return render(request,'app/template.html', status=200)



# retorna um status 200 para a request(solicitação)


def home(request):
    return render(request,'app/template.html', status=404)

# retorna um status 200 para a request


# OBS:  dentro de templates  podemos fazer if, for e varias outras coisas de forma dinamica, como no exemplo do context




# VOLTANDO A CONFIGURAÇÕES EM SETTINGS.py
# onde se encontra a variavel TEMPLATES, mais especifico na lista dentro dela chamada "DIRS":[

# ]

# nos indicamos o caminho para onde o django busca templates para serem rederizados

# passamos com a seguinte sintaxe

# 'DIRS': [
#     BASE_DIR / 'nome_da_pasta'/ 'nome_outra_pasta (se houver)'

# ]

# no nosso caso estamos trabalhando com a pasta teste chamada base_templates, onde configuramos dentro das rotas, que o django não deveria usar esse arquivo e sim o arquivo home que esta dentro de templates na pasta recipes

# para isso usamos a sintaxe de pastas dentro das urls

# -->

urlpatterns = [

    path('','recipes/home.html') #dessa forma
]

# pense agora que dentro do mesmo arquivo recipes temos outra pasta de templates chamada
# templates_teste
# e dentro dela temos um arquivo home.html

# como indicamos para o django que ele deve usar esse caminho??

# VAMOS NO ARQUIVO SETTINGS da pasta root do projeto (chamada projeto nesse caso)

# na variavel TEMPLATES
# na lista DIRS dentro dela

# 'DIRS':[ 
#     BASE_DIR / 'recipes' / 'templates_teste'
#             #/ pasta / pasta
# ]

# para rederizar esse arquivo teremos que fazer o seguinte dentro urls.py

def contato(request):
    return render(request,'temp/temp.html')

# sendo que a estrutura de pastas esta assim

# recipes
# -----templates
# -----------recipes
# ----------------home.html
# -----templates_teste
# ------------temp
# ----------------temp.html


# AUlA 3
