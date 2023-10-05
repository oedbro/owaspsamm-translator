#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import yaml

from deep_translator import GoogleTranslator

LANGUAGE = ""

def main():
	parser = argparse.ArgumentParser(description="A tool for translating OWASP SAMM")

	parser.add_argument('-l', '--language', default='sv', help="The two letter language code to translate to")
	parser.add_argument('path', metavar='repositoryPath', help="Path to the root folder of the core OWASP SAMM repository")

	args = parser.parse_args()
	# print(args)

	LANGUAGE = args.language

	modell_path = f"{args.path}/model"

	# print(modell_path)
	for file in walker(modell_path):
		print (file)
		content = readYaml(file)
		if content != None:
			translated_content = translateYaml(content)
			writeYaml(file, translated_content)
			# print("done")
		# break

def writeYaml(file, content):
	# print("write")
	# print(content)
	with open(f"./{LANGUAGE}/{file}", 'w+', encoding='utf-8') as f:
		yaml.dump(content, f, allow_unicode=True)



def readYaml(file):
	with open(file, 'rb') as f:
		content = f.read()
		try:
			parsed_yaml = yaml.safe_load(content)
			#translated_yaml = translateYaml(parsed_yaml)
			# print(translated_yaml)
			return(parsed_yaml)

		except yaml.YAMLError as e:
			print(e)
			raise e



def walker(path):
	for dirpath in os.listdir(path):
		for file in os.listdir(f"{path}/{dirpath}/"):
			yield f"{path}/{dirpath}/{file}"
	# yield f"{path}/answer_sets/A.yml"


def translateYaml(parsed_yaml):
	result = {}
	for header in parsed_yaml:
		if header in ["dependencies", "relatedActivities", "number", "stream", "level", "id", "type", "value", "model", "name", "color", "logo", "order", "practice", "maturitylevel", "assingee", "shortName", "progress", "letter", "metrics", "results"]:
			# print("if")
			result[header] = parsed_yaml[header] if parsed_yaml[header] != None else " "
		elif isinstance(parsed_yaml[header], list):
				result[header] = []
				# print(parsed_yaml[header])
				for i in parsed_yaml[header]:
					if not isinstance(i, str) and i != None:
						tmp = i
						if i['text'] == True:
							i['text'] = "Yes"
						elif i['text'] == False:
							i['text'] = "No"
						tmp['text'] = translate(i['text'])
						result[header] += [tmp]
					else:
						result[header] += [translate(i)]
		else:
				result[header] = translate(parsed_yaml[header])
			
	return result

def translate(original):
	if original == None or original == "":
		return ""
	# print(f"Original: \n{original}\n")
	try:
		lines = original.splitlines()
	except AttributeError as e:
		lines = original
	# print(f"Lines: \n{lines[0]}\n")

	if isinstance(lines, str):
		lines = [lines]

	resultlines = GoogleTranslator(source='en', target=LANGUAGE).translate_batch(lines)
	#resultlines = lines
	result = "\n".join(resultlines)
	# print(f"result:\n{result}\n\n")
	return result

if __name__ == '__main__':
	main()
