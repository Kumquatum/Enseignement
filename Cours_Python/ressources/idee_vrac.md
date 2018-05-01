
## Idee de nom

- Python pour la bioinformatique

## Certitudes

- Fait en Python 3.6

## Long brainstorming 


Base de python a mettre en relation avec le cours deja disponible de l'ULAVAL

- [cours en ligne](https://python.gel.ulaval.ca/login/)


Partie cours: 

- accord/rappel des bases:
    * python core: var, type, transtypage, string format, portee des variables, commentaires, help()
    * structures et operations de base: list, dict, set, tuple
        - notation [a:b:c] pour les listes: slice, reverse, ...
        - raccourcis d'operateurs d'ensemble: &, ~, |, -, ^
        - built-in: len, any, all, enumerate, map, zip, filter, sorted, range
        - built-in math: sum, max, min, pow, round, abs, complex, divmod
        - comprehension de list/dict
    * POO:
        - OO base: encapsulation, heritage, polymorphisme
        - built-in: type(), isinstance(), issubclass(), super()
        - difference entre "classe" et "objet/instance": @staticmethod
        - surcharge des operateurs "object": __str__, __init__, __lg/le/gt/ge/ne/eq__, __contains__, __and__, __xor__, __or__, ...
    * Exceptions
    
- python avance:
    * rappel pep: 1, 8, 20, 257
    * python, ipython, bpython, cpython, cython, ....
    * chaining operators [lien](https://stackoverflow.com/questions/101268/hidden-features-of-python#101945)
    * generateurs, lambda, iter(), next(): [lien](http://www.dabeaz.com/coroutines/)
    * pack/unpack args: *args, **kwargs
    * content management: with, __enter__, __exit__
    * (suppl.) decorateurs [lien](https://stackoverflow.com/questions/101268/hidden-features-of-python#101447)
    * (suppl.) multithreading & multiprocessing (GIL)
    * (suppl.) python synchrone & asynchrone
    
- outils pour la bioinfo:
    * lib python utiles:
        - standard/systeme: time, os/os.path, sys (argparse ?)
        - standard/recherche: re, [regex debugging](https://stackoverflow.com/questions/101268/hidden-features-of-python#143636)
        - standard/math: math, fraction, random 
        - ext/affichage: tqdm
        - ext/reseau: requests
    * interactions I/O: 
        - fichiers: csv, tsv, json
        - base de donnees: relationnelles, NoSQL
    * framework:
        - scientific/math: numpy, scipy, sympy
        - analyse: anaconda, bioconda, biopython, pandas
        - notebook: jupyter
        - visualisation: mathplotlib, bokeh, plotly, seaborn

- application problematique bioinfo :
    * Reverse complement
    * Parsing formats de données classiques : Fasta, FastQ, Bed, ...
    * Statistique exploratoire de base
    * Cartographie Qtl
    * Interogation de Blast / NCBI
    * Construction base de donnée d'annotation
    * Visualisation de reseaux (biologie des systemes, reseaux d'inhibition activation, coexpression, ...)
    * Pipeline d'outils, ex [lecture donnees] > [normalisation] > {[analyse 1], [analyse 2]} > [concatenation resultats] > [visualisation]
    * 

