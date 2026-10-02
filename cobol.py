# Analisador Lexico de Cobol
# Transforma de COBOL pra C 
# ^ acho que esse não precisa ainda? Qlqr coisa, oq estiver aqui é caminho já
# ^ por enquanto vamo só dizer se o arquivo lido é cobol valido ou não

# REGRAS DE PROJETO:
# TAB -> 2 espaços
# Evitar passar da coluna 80, 100 é limite real 
# nome de funcoes e vars em portugues
# Separem funções completamente diferentes com 2 \n, sub-funções relacionadas com 1
# variaveis declaradas no escopo usado. 1 \n entre elas e o codigo seguinte
# comentario faz como quiser.
# se quiser marcar algo pra fazer dps, comenta "[TODO]" naquela seção
# como escrever função e estilizar, tanto faz. Só não deixa feio demais tbm 
# Tentar não quebrar nos push, implementa uma coisa por vez e garante que roda 
# Não precisa estar completo, só não crashar ou dar erro 

# Ideia doq tem que fazer:
# 0. Primeiro só analisar lexicamente (retorna se é valido ou nn). Dps a gente mete o C
# 1. Ler o arquivo e conseguir discernir cada seção
#   -> Acho legal a gente dedicar cada um pra uma seção pra acelerar
# 2. Desenvolver a tabela hardcoded das palavras reservadas e tals 
# 3. O analisador de arvore la do chaim (aula mais recente) parece boa
#   referencia. 
#   -> ele mostra como funciona o codigo em C +/-
#   -> tbm mostrou que recursão à esquerda dá ruim, evitar com o truque dele

import time
import os
import sys
import argparse
from pathlib import Path
# imports malucos aqui


def read_file(input_file):
  # Lê o arquivo de cobol e salva oq for necessário em alguma variável.

  # Se quiserem, podemos fazer que ele lê enquanto analisa. 
  #   -> Acho que daí deixa de ser compilador e vira interpretador
  # Melhor salvar todo o texto em uma variavel e dps ir quebrando ela conforme
  #  analisa
  # Opinem.

  file = open(input_file, 'r')
  content = file.read()

  print(f"File \"{os.path.basename(input_file)}\" read. Contents:")
  print(content)

  file.close()


def start_lex():
  # Inicializa o analisador lexico, chama as funções necessárias para sua
  #  execução

  # Aqui a gente expande conforme necessário. 
  # Sub-funções ficam abaixo desta função.
  print("Sesbian")


def print_results(output_file):
  # Imprime os resultados em um arquivo separado.
  # Podemos colocar que ele tbm fala um resumo simples no terminal pra ajudar

  print(output_file)


# só para silenciar saídas se executar com "-q"
class NullDevice:
  def write(self, s):
    pass
  def flush(s):
    pass


def main():
  # aqui a gente coloca só o seguinte:
  # * ler arquivo de entrada com read_file()
  # * analisar lexicamente usando start_lex()
  #   * envolver o comando acima com try pra cuidar de exceções
  # * printar saida do jeito que for melhor, usando print_results()

  # pra funcionar os argumentos do arquivo
  parser = argparse.ArgumentParser(description="COBOL lexical interpreter")
  parser.add_argument("-i", "--input", type=str, help="COBOL input file")
  parser.add_argument("-o", "--output", type=str, help="Analysis output file")
  parser.add_argument("-q", "--quiet", action="store_true", help="Silence outputs")

  args = parser.parse_args()

  if args.quiet:
    sys.stdout = NullDevice()

  # ambos input_file e output_file tem um arquivo default caso não especifique
  if args.input:
    input_file = os.path.expanduser(f"./{args.input}")
  else:
    input_file = os.path.expanduser("./input.cbl")

  if args.output:
    output_file = os.path.expanduser(f"./{args.output}")
  else:
    output_file = os.path.expanduser("./output.txt")

#-- main de verdade --
  print("ANALISADOR MUITO MODERNO VERSÃO 39")
  read_file(input_file)
  try:
    start_lex()
  except:
    print("Deu exceção e deu ruim")
  print_results(output_file)


if __name__ == "__main__":
  main()

