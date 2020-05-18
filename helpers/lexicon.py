import pandas as pd
import re

hostility = ['ass-hat', 'assbag', 'assbite', 'asscock', 'assface', 'asshat', 'asshead', 'asshole', 'assshit', 'asswipe',
             'awalt', 'b!tch', 'b17ch', 'b1tch', 'bad fuck', 'balls', 'banging', 'bastard', 'beastiality', 'beat',
             'beaver', 'bi+ch', 'biatch', 'big butt', 'bitch', 'bitch ass', 'bitcher', 'bitchers', 'bitches',
             'bitchtits', 'bite me', 'blockhead', 'blockheads', 'boang', 'bogan', 'bogans', 'bottom-feeder',
             'brotherfucker', 'butterhead', 'butterheads', 'buttface', 'byatch', 'cause pain', 'chav', 'chavs',
             'cheese eating surrender monkey', 'cheese eating surrender monkies', 'clitface', 'cock knob', 'cockbite',
             'cockblocker', 'cockhead', 'cockmaster', 'cockmongler', 'cocknose', 'cocknugget', 'conchuda', 'conchudas',
             'coochie', 'coochy', 'crotchrot', 'cum bubble', 'cum guzzler', 'cum jockey', 'cum tart', 'cumdumpster',
             'cumquat', 'cumqueen', 'cumslut', 'cunt', 'cunt rag', 'cuntass', 'cuntface', 'cuntfuck', 'cunthole',
             'cuntlick', 'cunts', 'cuntslut', 'demonrats', 'dick beaters', 'dick for brains', 'dick weasel', 'dick wod',
             'dickbag', 'dickbrain', 'dickface', 'dickless', 'dicktickler', 'dickwad', 'dickweed', 'dingo fucker',
             'dingo fuckers', 'dipshit', 'dipstick', 'douche', 'douchebag', 'dum ass', 'dumb fuck', 'dumbass',
             'dumbbitch', 'dumbfuck', 'eat me', 'eat pussy', 'entrap', 'ewalt', 'extort', 'fastfuck', 'fatass',
             'felcher', 'feltcher', 'finger fucker', 'fingerfuckers', 'fist fuck', 'fistfucker', 'footfucker', 'fucka',
             'fuckable', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbuddy', 'fucker', 'fuckers', 'fuckersucker',
             'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead', 'fuckher', 'fuckina', 'fuckingbitch',
             'fuckit', 'fuckknob', 'fuckpig', 'fucktard', 'fuckup', 'fuckwhore', 'fuckyou', 'gangbanger', 'gash',
             'gashes', 'greaseball', 'harm', 'hate', 'hayseed', 'hick', 'hicks', 'hillbilly', 'ho', 'hoar', 'hoare',
             'hoe', 'hoer', 'hoes', 'honkey', 'honky', 'hoodrat', 'hoodrats', 'hore', 'hos', 'hurt', 'hussy', 'idiot',
             'idiots', 'intimidate', 'jackass', 'kunt', 'l3i+ch', 'l3itch', 'lardass', 'libtards', 'limpdick', 'menace',
             'milf', 'minge', 'mock', 'mocks', 'moron', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz',
             'mothafucked', 'mothafucker', 'mothafuckers', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked',
             'motherfucker', 'motherfuckers', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muthafecker',
             'muthafuckker', 'mutherfucker', 'nutsack', 'paleface', 'palefaces', 'panooch', 'peckerwood', 'pindick',
             'pohm', 'pohms', 'poor white trash', 'pu55i', 'pu55y', 'punish', 'pusse', 'pussi', 'pussie', 'pussies',
             'pussy', 'pussys', 'pusy', 'queerhole', 'redneck', 'rednecks', 'rentafuck', 'retard', 'retarded',
             'russellite', 'russellites', 'scag', 'scags', 'scumbag', 'seppo', 'seppos', 'sheepfucker', 'sheepfuckers',
             'shit kicker', 'shit kickers', 'shitface', 'shithead', 'shitspitter', 'skag', 'skags', 'skank',
             'skank bitch', 'skank fuck', 'skank whore', 'skanky', 'skanky bitch', 'skanky whore', 'skullfuck', 'slag',
             'slags', 'slit', 'slits', 'slut', 'slut wear', 'slut whore', 'slutbag', 'sluts', 'slutt', 'slutting',
             'slutty', 'slutwhore', 'smear', 'snatch', 'son-of-a-bitch', 'spermbag', 'sub human', 'sub humans',
             'suckme', 'suckmytit', 'tard', 'terrorize', 'threaten', 'thrust', 'titfucker', 'titfuckin', 'trailertrash',
             'trisexual', 'turd', 'tw4t', 'twat', 'twathead', 'twats', 'twatty', 'twatwaffle', 'twobitwhore', 'twunt',
             'twunter', 'wanker', 'wasp', 'wasps', 'waspy', 'white trash', 'whitey', 'whities', 'whoar', 'whore',
             'whore from fife', 'whore from fifes', 'whorefucker', 'whores', 'williewanker', 'wuss', 'yankee']

flipping = ['beta', 'normie', 'overthrow', 'prevail', 'vanquish']

sexual_violence = ['cherry popper', 'clitfuck', 'cock block', 'cock carousel', 'cock tease', 'conquer', 'gangbang',
                   'gangbanged', 'gangbangs', 'incest', 'infiltrate', 'insest', 'lolita', 'molest', 'molestation',
                   'pound', 'rape', 'sodomise']

patriarchy = ['amog', 'betabuxx', 'compel', 'oblige', 'omega', 'overwhelm', 'subjugate', 'suppress']

belitting = ['b00bs', 'becky', 'big ass', 'bint', 'bints', 'bird', 'birds', 'boob', 'boobies', 'boobs', 'booobs',
             'boooobs', 'booooobs', 'booooooobs', 'camel toe', 'chesticles', 'cock waffle', 'dumb', 'dumbass', 'f4nny',
             'failure', 'fanny', 'fannyflaps', 'female', 'femoid', 'fho', 'fugly', 'funfuck', 'muff', 'pearlnecklace',
             'peehole', 'pissflaps', 'poon', 'poonani', 'poontang', 'pornprincess', 'pua', 'puntang', 'puss',
             'pussylips', 'roastie', 'shit heel', 'shit heels', 'short fuck', 'skin flute', 'smv', 'snowflake',
             'spermhearder', 'spermherder', 'stacy', 't1tt1e5', 't1tties', 'tittie', 'titties', 'titty', 'tittyfuck',
             'unfuckable', 'va-j-j']

stoicism = ['blackops2cel', 'blackpill', 'chad', 'cope', 'cuck', 'currycel', 'fakecel', 'friendless', 'fuel', 'gymcel',
            'handholdless', 'heightcel', 'hugless', 'hypergamy', 'jbw', 'jfl', 'kissless', 'kthhfv', 'ldar',
            'looksmatch', 'looksmaxx', 'meeks', 'mogs', 'redpill', 'ricecel', 'rope', 'touchless', 'truecel', 'tyrone',
            'volcel', 'wagecel', 'wristcel']


def count_words(categories, text):
    returnv = []

    for words in categories:

        words = [r'\b' + re.escape(word) + r'\b' for word in words]

        occ = len(re.findall("(" + "|".join(words) + ")", text, re.IGNORECASE))

        if occ == 0:
            returnv.append(0)
            continue

        n_words = len(text.split(" "))
        if n_words == 0:
            returnv.append(0)
            continue
        returnv.append(occ / n_words)

    return returnv


def load_hatebase():
    return list(pd.read_csv("/data/savvas/incels/filtered-hatewords-savvas.csv")["vocabulary_stemmed"].values)
