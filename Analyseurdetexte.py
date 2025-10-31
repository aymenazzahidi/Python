import string

def nettoyer_texte(texte):
    texte_nettoye = ""
    for c in texte:
        if c not in string.punctuation:
            texte_nettoye += c
    return texte_nettoye.lower()


def separer_mots(texte):
    texte = nettoyer_texte(texte)
    return texte.split()


def separer_phrases(texte):
    for p in ['!', '?']:
        texte = texte.replace(p, '.')
    phrases = texte.split('.')
    return phrases


def frequence_mots(mots):
    freq = {}
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1
    return freq


def longueur_moyenne_mots(mots):
    total = 0
    for mot in mots:
        total += len(mot)
    if len(mots) == 0:
        return 0
    return total / len(mots)


def mots_plus_moins_utilises(freq):

    valeurs = list(freq.values())
    max = max(valeurs)
    min = min(valeurs)
    plus = []
    moins = []
    for m in freq:
        if freq[m] == max:
            plus.append(m)
        if freq[m] == min:
            moins.append(m)
    return plus, moins


def detection_palindromes(mots):
    palindromes = []
    for m in mots:
        if (len(m) > 2 and m == m[::-1]):
            palindromes.append(m)
    return palindromes


def nombre_phrases(phrases):
    return len(phrases)


def longueur_phrases(phrases):
    longueurs = []
    for phrase in phrases:
        mots = separer_mots(phrase)
        longueurs.append(len(mots))
    return longueurs


def ponctuation_utilisee(texte):
    ponctuations = set()
    for c in texte:
        if c in ['!', '?','.']:
            ponctuations.add(c)
    return ponctuations


def statistiques_par_type_mot(mots):
    stats = {"majuscule": 0, "minuscule": 0, "numerique": 0}
    for m in mots:
        if m.isupper():
            stats["majuscule"] += 1
        elif m.islower():
            stats["minuscule"] += 1
        elif m.isdigit():
            stats["numerique"] += 1
    return stats

def top_10_mots(freq):
    items = list(freq.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:10]


def phrases_plus_longues(phrases):
    max_len = 0
    for p in phrases:
        n = len(separer_mots(p))
        if n > max_len:
            max_len = n
    longues = []
    for p in phrases:
        if len(separer_mots(p)) == max_len:
            longues.append(p)
    return longues


def diversite_vocabulaire(mots):
    uniques = set(mots)
    if len(mots) == 0:
        return 0
    return len(uniques) / len(mots)


def patterns_repetitifs(mots):
    repetitifs = []
    uniques = set(mots)
    for m in uniques:
        compteur = 0
        for mot in mots:
            if mot == m:
                compteur += 1
        if compteur > 3:
            repetitifs.append(m)
    return repetitifs