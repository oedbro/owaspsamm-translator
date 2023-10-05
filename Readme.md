# Translator
A quick tool to translate the [OWASP SAMM core](https://github.com/owaspsamm/core) repository using google translate. Used as an easy way to create a translation. 

## Usage
```
usage: samm-translator.py [-h] [-l LANGUAGE] repositoryPath

A tool for translating OWASP SAMM

positional arguments:
  repositoryPath        Path to the root folder of the core OWASP SAMM repository

options:
  -h, --help            show this help message and exit
  -l LANGUAGE, --language LANGUAGE
                        The two letter language code to translate to
```

The output will be saved in a separate folder in the current folder. 