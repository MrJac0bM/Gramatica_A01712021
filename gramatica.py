import nltk
from nltk import CFG

# Definimos una gramática libre de contexto (CFG) en noruego que describe la estructura de oraciones compuestas
gramatica = CFG.fromstring("""
S -> Setning Setning_opt
Setning_opt -> Konj Setning Setning_opt | 
Setning -> HovedSetning Skilletegn_opt
Skilletegn_opt -> Skilletegn | 
HovedSetning -> Subjekt Predikat
Subjekt -> EnkelSubjekt Subjekt_opt
Subjekt_opt -> Konj Subjekt Subjekt_opt | 
EnkelSubjekt -> Pronomen | Art Substantiv | Substantiv | Art DetN | Art AdjE Substantiv | AdjE Substantiv 
Predikat -> Verb ObjektDel AdverbDel PPDel
ObjektDel -> Objekt | 
AdverbDel -> AdverbE | 
PPDel -> PP | 
Objekt -> EnkelObjekt Objekt_opt
Objekt_opt -> Konj Objekt Objekt_opt | 
EnkelObjekt -> Substantiv | Art Substantiv | Art AdjE Substantiv | 
PP -> Prep EnkelSubjekt
AdjE -> Adj AdjE_opt
AdjE_opt -> Konj AdjE | 
AdverbE -> Adv AdverbE_opt
AdverbE_opt -> Konj AdverbE | 

Pronomen -> "jeg" | "du" | "han" | "hun" | "vi" | "dere" | "de" | "meg" | "deg" | "ham" | "henne" | "det" | "oss" | "dere" | "dem"
Art -> "en" | "et" | "den" | "det" | "ei" | "et"
Substantiv -> "hund" | "katt" | "bok" | "skole" | "venn" | "familie" | "by" | "land" | "mat" | "vann" | "tid" | "bil" | "hus" | "jente" | "gutt" | "bord" | "stol" | "vindu" | "dør" | "telefon" | "sko" | "sokk" | "genser" | "jakke" | "bukse" | "parken" | "historie" | "skolen" | "boka" | "eple" | "solskinnet" | "varmen"
DetN -> "gutten" | "jenta" | "huset" | "bilen" | "barna" | "læreren"
Verb -> "spiser" | "leser" | "skriver" | "snakker" | "forstår" | "hører" | "ser" | "løper" | "sover" | "danser" | "synger" | "bygger" | "går" | "kommer" | "drikker" | "liker" | "tenker" | "sier" | "vasker" | "kjøper" | "åpner" | "lukker" | "spiller" | "lærer" | "underviser" | "møter" | "reiser" | "bor" | "finner" | "tar" | "elsker" | "hater"
Adj -> "stor" | "liten" | "rød" | "blå" | "gammel" | "ung" | "sterk" | "svak" | "vanskelig" | "lett" | "kaldt" | "gamle" | "lang"
Adv -> "fort" | "sakte" | "nøye" | "alltid" | "aldri" | "lykkelig" | "kanskje" | "ofte" | "sjeldent" | "snart" | "nå" | "hjemme" | "borte" | "der" | "hit" | "ut" | "inn" | "lenge" | "sammen" | "ennå" | "raskt"
Prep -> "i" | "på" | "med" | "til" | "under" | "over" | "ved" | "om" | "mellom" | "bak" | "foran" | "uten" | "etter" | "før" | "rundt" | "gjennom" | "langs" | "hos" | "mot"
Konj -> "og" | "men" | "fordi" | "eller" | "når" | "hvis" | "at" | "selv om" | "mens" | "derfor" | "så" | "enten" | "både" | "dessuten" | "likevel" | "som"
Skilletegn -> "." | "?" | "!" | "..." | "," | ":" | ";"
""")  

# Creamos un parser con la gramática definida usando ChartParser
parser = nltk.ChartParser(gramatica)

# Tokenizamos una oración de prueba que contiene conjunciones, adjetivos, objetos y adverbios
oracion = "en gamle hund og katt elsker solskinnet raskt og alltid , men hund hater varmen sakte .".split()

# Parseamos la oración para generar todos los árboles sintácticos posibles
trees = list(parser.parse(oracion))

# Mostramos los árboles generados o informamos si no se pudo generar ninguno
if trees:
    print(f"Árboles generados: {len(trees)}")
    for i, tree in enumerate(trees, 1):
        print(f"\nÁrbol {i}:")
        tree.pretty_print()  # Imprime el árbol sintáctico de manera visual
else:
    print("No se generaron árboles.")
