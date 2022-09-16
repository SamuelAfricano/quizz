"""Este modulo guarda as perguntas dos app """

import pathlib
import random

from string import ascii_lowercase
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from colorama import init, Fore, Back, Style
from enum import IntEnum
init()

def questoes(path, num_questoes):
	info_topico = tomllib.loads(path.read_text())
	topicos = {
		topico["label"]: topico["pergunta"] for topico in info_topico.values()
	}
	topico_label = pega_resposta(
		pergunta="Escolha um tópico para começarmos",
		alternativas=sorted(topicos),
	)[0]
	perguntas = topicos[topico_label]
	num_questoes = min(num_questoes, len(perguntas))
	return random.sample(perguntas, k=num_questoes)

def fazer_pergunta(perguntas):
	resposta_correcta = perguntas["respostas"]
	alternativas = perguntas["respostas"] + perguntas["alternativas"]
	alternativas_baralhada = random.sample(alternativas, k=len(alternativas))
	
	resposta = pega_resposta(pergunta=perguntas["pergunta"], 
							alternativas=alternativas_baralhada,
							num_escolha=len(resposta_correcta),
							dica=perguntas.get("dica"),
							)

	if correcto := (set(resposta) == set(resposta_correcta)):
		print(Fore.GREEN + 'Correcto!.' + Style.RESET_ALL)
	else:
		resposta_plural = " é" if len(resposta_correcta) == 1 else "são"
		print( Fore.RED + "\n- ".join([f"Erraste, resposta  {resposta_plural}:  "] + resposta_correcta) +  Style.RESET_ALL)
	
	if "explicacao" in perguntas:
		print(Fore.YELLOW + f"\nExplicação: \n{perguntas['explicacao']}" + Style.RESET_ALL)

	return 1 if correcto else 0

		
def pega_resposta(pergunta, alternativas, num_escolha=1, dica=None):
	print(f"{pergunta} ?")
	alternativas_etiquetadas = dict(zip(ascii_lowercase, alternativas))
	if dica:
		alternativas_etiquetadas["?"] = "dica"

	for label, alternativa in alternativas_etiquetadas.items():
		print(Fore.BLUE + f"  {label}) {alternativa}"+ Style.RESET_ALL)

	while True:
		plural = "" if num_escolha == 1 else f"s (escolha {num_escolha})"
		resposta = input(f"\nEscolha{plural}: ")
		respostas = set(resposta.replace(",", " ").split())

		if dica and "?" in respostas:
			print(Fore.YELLOW + f"\nDica -> {dica}" + Style.RESET_ALL)
			continue

		if len(respostas) != num_escolha:
			plural = "" if num_escolha == 1 else "s, separada por vírgula"
			print(Fore.YELLOW + f"Por Favor escolhe {num_escolha} alternativa{plural}" + Style.RESET_ALL)
			continue

		if any(
			(invalida := resposta) not in alternativas_etiquetadas
			for resposta in respostas
		):
			print(
				Fore.YELLOW,
				f"{invalida!r} não é uma resposta válida. "
				f"Por Favor escolha {', '.join(alternativas_etiquetadas)}"
				+ Style.RESET_ALL
			)
			continue

		return [alternativas_etiquetadas[resposta] for resposta in respostas]
