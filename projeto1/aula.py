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