# https://regex-generator.olafneumann.org/

import re

def use_regex(input):
    pattern = re.compile(r"Pressure = ([+-]?(?=\\.\\d|\\d)(?:\\d+)?(?:\\.?\\d*))(?:[eE]([+-]?\\d+))?")
    return pattern.search(input, re.IGNORECASE)