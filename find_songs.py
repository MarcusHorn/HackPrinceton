#!/usr/bin/env python

import random

from boltons.strutils import singularize


# SYNONYMS = json.load('synonyms.json')
# START_TIMES = json.load('times/start.json')
# END_TIMES = json.load('times/end.json')


SYNONYMS = {
    "arthur": ["aardvark"],
    "raining": ["rain"],
    "rainy": ["rain"],
    "dogs": ["dog"],
    "loving": ["love"],
    "sunny": ["sun"],
    "happy": ["joyful"],
    "sad": ["unhappy"],
    "angry": ["worried"],
    "worry": ["worried"],
    "bee": ["bees"],
    "frogs": ["frog"],
    "cold": ["winter"],
    "hot outside": ["summer"],
    "student": ["studying"],
    "study": ["studying"],
    "test tomorrow": ["studying"],
    "pens": ["pen"],
    "pencils": ["pencil"],
    "exam": ["test"],
    "quiz": ["test"],
    "broke up": ["break up"],
    "dump": ["break up"],
    "I left": ["I cheated"],
    "love": ["admire"],
    "cute": ["good looking"],
    "hot": ["good looking"],
}



PROOF_ON_CONCEPT = True


def synonyms(word):
    """
    Find all valid synonyms for a word
    """
    return SYNONYMS.get(word, [])


class WordToSongs(dict):
    def __missing__(self, key: str):
        for synonym in synonyms(key):
            if synonym in self:
                self[key] = self[synonym]
                return self[synonym]
        raise KeyError('%s' % repr(key))


word_to_song = WordToSongs()

if PROOF_ON_CONCEPT:
    word_to_song.update(
        {
            ("aardvark",): ["b53WaK71sMM"],
            ("banana",): ["PDd8shcLvHI"],
            ("cat",): ["LTunhRVyREU"],
            ("cat", "dog"): [],
            ("cloud",): ["VyotcwmZE3w"],
            ("dog",): ["Qkuu0Lwb5EM"],
            ("fruit", "love"): [],
            ("pencil",): ["WCK5Cq5j0jk"],
            ("rain",): ["g4flAZEgtjs"],
            ("ronaldo",): ["bTk5ZcL0XZ4"],
            ("sun",): ["TiCxqhu9cio"],
            ("doodle", "yankee"): ["IzRhFH5OyHo"]
            ("joyful",): ["1z6XJp8Dctg"]
            ("unhappy",): ["nVjsGKrE6E8"]
            ("worried",): ["L3HQMbQAWRc"]
        }
    )


def all_subsets(seq):
    """
    Return all possible subsets.
    """
    if len(seq) == 0:
        return [[]]
    rest_all_subsets = all_subsets(seq[1:])
    return rest_all_subsets + [[seq[0]] + elem for elem in rest_all_subsets]


def find_song(phrase: str) -> str:
    """
    Find the song related to the word/string
    """
    if phrase == "":
        return random.choice(list(word_to_song.values()))[0]

    words = [singularize(word.strip().lower())
             for word in phrase.strip('"\'').split()]

    cleaned = sorted((tuple(sorted(subset)) for subset in all_subsets(words)),
                     key=len,
                     reverse=True)

    for group in cleaned:
        try:
            return word_to_song[group][0]
        except KeyError:
            continue
