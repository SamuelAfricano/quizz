import random
import pathlib
from funcoes import questoes, pega_resposta, fazer_pergunta
from string import ascii_lowercase

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_PERGUNTAS = 10
QUESTIONS_PATH = pathlib.Path(__file__).parent / "perguntas.Toml"



def run_quiz():
	perguntas = questoes(
		QUESTIONS_PATH, num_questoes=NUM_PERGUNTAS
	)

	
	num_perguntas_corretas = 0
	for num, pergunta in enumerate(perguntas, 1):
		print(f"\nPergunta {num}: ")
		num_perguntas_corretas += fazer_pergunta(pergunta)
		pontuacao_total = num_perguntas_corretas * 10

	print(f"\nPontuação total -> {pontuacao_total}%")
	print(f'\nNúmero total de perguntas certas -> {num_perguntas_corretas}')
	print(f'\nNúmero total de perguntas  -> {num}')

if __name__ == '__main__':
	run_quiz()