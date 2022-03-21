<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:41:22 2021

@author: José Carlos Costa
"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns 
from bs4 import BeautifulSoup
import requests
import re
from webdriver_manager.chrome import ChromeDriverManager

file = input('Digite o nome do arquivo com a distribuição dos verbos \n que você obteve no programa de extração lexical - Programa 2')

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://www.letras.ufmg.br/sistemas/verboweb_cliente/lista.php?lg=pt"
driver.get(url)


html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

verbos = soup.find_all('td')

verbos = '\n'.join([x.text for x in verbos])

verbos = re.sub(r"\d+\.\s", '', verbos)

verbos = verbos.replace('Ã§', 'ç')

verbos = list(verbos.splitlines())

driver.find_element_by_link_text('Abalar 1').click()

links_verbos = soup.find_all('a')
links_verbos = '\n'.join([str(x) for x in links_verbos])
links_verbos = '\n'.join(re.findall(r'(?<=\").+(?=\")', links_verbos))
links_verbos = [x for x in links_verbos.splitlines()]
del links_verbos[0]

nova_url = "http://www.letras.ufmg.br/sistemas/verboweb_cliente/"


from time import sleep

lista_verbos = []
aspecto_lista = []
sintagma_lista = []
papel_tematico_lista = []
classe_lista = []
exemplo_verbo_web_lista = []


for y in links_verbos:
    # driver.implicitly_wait(1)
    driver.get(nova_url + y)
    # sleep(1)
    estrutura_sintatica = driver.find_elements_by_css_selector('#opener4')
    if len(estrutura_sintatica) > 0:
        verbo_lema = driver.find_elements_by_tag_name('h3')
        # sleep(1)
        classe = driver.find_elements_by_css_selector('#opener1')
        papel_tematico = driver.find_elements_by_css_selector('#opener5')
        aspecto = driver.find_elements_by_css_selector('#opener7')
        exemplo_verbo_web = driver.find_element_by_tag_name('i').text
        for z in verbo_lema:
            lista_verbos.append(z.text)
        for c in classe:
            classe_lista.append(c.text)
        for w in aspecto:
            aspecto_lista.append(w.text)
        for k in estrutura_sintatica:
            sintagma_lista.append(k.text)
        for b in papel_tematico:
            papel_tematico_lista.append(b.text)
        for e in exemplo_verbo_web.splitlines():
            exemplo_verbo_web_lista.append(e)
    else:
        continue 
    
driver.close()

df.to_csv('verbo_web.csv')

import pandas as pd


lista_verbos = [x for x in lista_verbos if len(x)]

df = pd.DataFrame()
df['lema_verbo_web'] = lista_verbos
df['classe_verbo_web'] = classe_lista
df['aspecto_lexical'] = aspecto_lista
df['papel_tematico'] = papel_tematico_lista
df['estrutura_sintatica'] = sintagma_lista
df['exemplo_verbo_web'] = exemplo_verbo_web_lista
df['lema_verbo_web'] = df['lema_verbo_web'].apply(lambda x: re.sub(r'\d+', '', x))
df['lema_verbo_web'] = df['lema_verbo_web'].str.strip()
df['lema_verbo_web'] = df['lema_verbo_web'].str.lower()


df_verbos_cesq = pd.read_csv(file)

df_verbos_cesq.columns = ['verbos', 'frequencia', 'classificacao_nilc', 'lema',
       'lema_spacy', 'raiz_nltk', 'classificacao_verbal', 'syl_size',
       'infinitivo', 'gerundio', 'participio', 'pret_perf_ind', 'pret_imp_ind',
       'futuro_pret_ind', 'pres_indicativo', 'futuro_pres_ind',
       'pret_mais_perf_ind', 'pres_subj', 'imp_subj', 'imperativo',
       'futuro_subj']


df_verbos_cesq = df_verbos_cesq.drop_duplicates(subset = 'lema')

df_verbos_merged = df_verbos_cesq.merge(df, on = 'lema')



#exportação 

df_verbos_merged.to_excel('coral_verbo_web.csv')

=======
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:41:22 2021

@author: José Carlos Costa
"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns 
from bs4 import BeautifulSoup
import requests
import re
from webdriver_manager.chrome import ChromeDriverManager

file = input('Digite o nome do arquivo com a distribuição dos verbos \n que você obteve no programa de extração lexical - Programa 2')

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://www.letras.ufmg.br/sistemas/verboweb_cliente/lista.php?lg=pt"
driver.get(url)


html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

verbos = soup.find_all('td')

verbos = '\n'.join([x.text for x in verbos])

verbos = re.sub(r"\d+\.\s", '', verbos)

verbos = verbos.replace('Ã§', 'ç')

verbos = list(verbos.splitlines())

driver.find_element_by_link_text('Abalar 1').click()

links_verbos = soup.find_all('a')
links_verbos = '\n'.join([str(x) for x in links_verbos])
links_verbos = '\n'.join(re.findall(r'(?<=\").+(?=\")', links_verbos))
links_verbos = [x for x in links_verbos.splitlines()]
del links_verbos[0]

nova_url = "http://www.letras.ufmg.br/sistemas/verboweb_cliente/"


from time import sleep

lista_verbos = []
aspecto_lista = []
sintagma_lista = []
papel_tematico_lista = []
classe_lista = []
exemplo_verbo_web_lista = []


for y in links_verbos:
    # driver.implicitly_wait(1)
    driver.get(nova_url + y)
    # sleep(1)
    estrutura_sintatica = driver.find_elements_by_css_selector('#opener4')
    if len(estrutura_sintatica) > 0:
        verbo_lema = driver.find_elements_by_tag_name('h3')
        # sleep(1)
        classe = driver.find_elements_by_css_selector('#opener1')
        papel_tematico = driver.find_elements_by_css_selector('#opener5')
        aspecto = driver.find_elements_by_css_selector('#opener7')
        exemplo_verbo_web = driver.find_element_by_tag_name('i').text
        for z in verbo_lema:
            lista_verbos.append(z.text)
        for c in classe:
            classe_lista.append(c.text)
        for w in aspecto:
            aspecto_lista.append(w.text)
        for k in estrutura_sintatica:
            sintagma_lista.append(k.text)
        for b in papel_tematico:
            papel_tematico_lista.append(b.text)
        for e in exemplo_verbo_web.splitlines():
            exemplo_verbo_web_lista.append(e)
    else:
        continue 
    
driver.close()

df.to_csv('verbo_web.csv')

import pandas as pd


lista_verbos = [x for x in lista_verbos if len(x)]

df = pd.DataFrame()
df['lema_verbo_web'] = lista_verbos
df['classe_verbo_web'] = classe_lista
df['aspecto_lexical'] = aspecto_lista
df['papel_tematico'] = papel_tematico_lista
df['estrutura_sintatica'] = sintagma_lista
df['exemplo_verbo_web'] = exemplo_verbo_web_lista
df['lema_verbo_web'] = df['lema_verbo_web'].apply(lambda x: re.sub(r'\d+', '', x))
df['lema_verbo_web'] = df['lema_verbo_web'].str.strip()
df['lema_verbo_web'] = df['lema_verbo_web'].str.lower()


df_verbos_cesq = pd.read_csv(file)

df_verbos_cesq.columns = ['verbos', 'frequencia', 'classificacao_nilc', 'lema',
       'lema_spacy', 'raiz_nltk', 'classificacao_verbal', 'syl_size',
       'infinitivo', 'gerundio', 'participio', 'pret_perf_ind', 'pret_imp_ind',
       'futuro_pret_ind', 'pres_indicativo', 'futuro_pres_ind',
       'pret_mais_perf_ind', 'pres_subj', 'imp_subj', 'imperativo',
       'futuro_subj']


df_verbos_cesq = df_verbos_cesq.drop_duplicates(subset = 'lema')

df_verbos_merged = df_verbos_cesq.merge(df, on = 'lema')



#exportação 

df_verbos_merged.to_excel('coral_verbo_web.csv')

>>>>>>> 70de4aa70c66eb618a4af718c212ca9c516d9668
