# Author : Jigesh Sheoran / sheoraninfosec / bug0x
# Last Updated : 11 September, 2025

HOMOGLYPH_MAP = {
    # Mathematical Bold Capital Letters
    "𝐀": "A", "𝐁": "B", "𝐂": "C", "𝐃": "D", "𝐄": "E", "𝐅": "F", "𝐆": "G",
    "𝐇": "H", "𝐈": "I", "𝐉": "J", "𝐊": "K", "𝐋": "L", "𝐌": "M", "𝐍": "N",
    "𝐎": "O", "𝐏": "P", "𝐐": "Q", "𝐑": "R", "𝐒": "S", "𝐓": "T", "𝐔": "U",
    "𝐕": "V", "𝐖": "W", "𝐗": "X", "𝐘": "Y", "𝐙": "Z",
    "𝐚": "a", "𝐛": "b", "𝐜": "c", "𝐝": "d", "𝐞": "e", "𝐟": "f", "𝐠": "g",
    "𝐡": "h", "𝐢": "i", "𝐣": "j", "𝐤": "k", "𝐥": "l", "𝐦": "m", "𝐧": "n",
    "𝐨": "o", "𝐩": "p", "𝐪": "q", "𝐫": "r", "𝐬": "s", "𝐭": "t", "𝐮": "u",
    "𝐯": "v", "𝐰": "w", "𝐱": "x", "𝐲": "y", "𝐳": "z",

    # Mathematical Italic Capital Letters
    "𝐴": "A", "𝐵": "B", "𝐶": "C", "𝐷": "D", "𝐸": "E", "𝐹": "F", "𝐺": "G",
    "𝐻": "H", "𝐼": "I", "𝐽": "J", "𝐾": "K", "𝐿": "L", "𝑀": "M", "𝑁": "N",
    "𝑂": "O", "𝑃": "P", "𝑄": "Q", "𝑅": "R", "𝑆": "S", "𝑇": "T", "𝑈": "U",
    "𝑉": "V", "𝑊": "W", "𝑋": "X", "𝑌": "Y", "𝑍": "Z",
    "𝑎": "a", "𝑏": "b", "𝑐": "c", "𝑑": "d", "𝑒": "e", "𝑓": "f", "𝑔": "g",
    "ℎ": "h", "𝑖": "i", "𝑗": "j", "𝑘": "k", "𝑙": "l", "𝑚": "m", "𝑛": "n",
    "𝑜": "o", "𝑝": "p", "𝑞": "q", "𝑟": "r", "𝑠": "s", "𝑡": "t", "𝑢": "u",
    "𝑣": "v", "𝑤": "w", "𝑥": "x", "𝑦": "y", "𝑧": "z",

    # Mathematical Bold Italic
    "𝑨": "A", "𝑩": "B", "𝑪": "C", "𝑫": "D", "𝑬": "E", "𝑭": "F", "𝑮": "G",
    "𝑯": "H", "𝑰": "I", "𝑱": "J", "𝑲": "K", "𝑳": "L", "𝑴": "M", "𝑵": "N",
    "𝑶": "O", "𝑷": "P", "𝑸": "Q", "𝑹": "R", "𝑺": "S", "𝑻": "T", "𝑼": "U",
    "𝑽": "V", "𝑾": "W", "𝑿": "X", "𝒀": "Y", "𝒁": "Z",
    "𝒂": "a", "𝒃": "b", "𝒄": "c", "𝒅": "d", "𝒆": "e", "𝒇": "f", "𝒈": "g",
    "𝒉": "h", "𝒊": "i", "𝒋": "j", "𝒌": "k", "𝒍": "l", "𝒎": "m", "𝒏": "n",
    "𝒐": "o", "𝒑": "p", "𝒒": "q", "𝒓": "r", "𝒔": "s", "𝒕": "t", "𝒖": "u",
    "𝒗": "v", "𝒘": "w", "𝒙": "x", "𝒚": "y", "𝒛": "z",

    # Mathematical Script Letters (Fraktur, Double-Struck, Sans-serif, etc.)
    "𝒜": "A", "𝒞": "C", "𝒟": "D", "𝒢": "G", "ℋ": "H", "𝒥": "J", "𝒦": "K",
    "𝒩": "N", "𝒪": "O", "𝒫": "P", "𝒬": "Q", "𝒮": "S", "𝒯": "T", "𝒰": "U",
    "𝒱": "V", "𝒲": "W", "𝒳": "X", "𝒴": "Y", "𝒵": "Z",
    "𝒶": "a", "𝒷": "b", "𝒸": "c", "𝒹": "d", "ℯ": "e", "𝒻": "f", "ℊ": "g",
    "𝒽": "h", "𝒾": "i", "𝒿": "j", "𝓀": "k", "𝓁": "l", "𝓂": "m", "𝓃": "n",
    "ℴ": "o", "𝓅": "p", "𝓆": "q", "𝓇": "r", "𝓈": "s", "𝓉": "t", "𝓊": "u",
    "𝓋": "v", "𝓌": "w", "𝓍": "x", "𝓎": "y", "𝓏": "z",

    # Add other ranges (Fraktur, Double-struck, Sans-serif bold/italic, etc.)
    # from your table here...
}

def contains_homoglyph(text: str) -> bool:
    return any(ch in HOMOGLYPH_MAP for ch in text)

def normalize_homoglyphs(text: str) -> str:
    """Replace homoglyphs with their ASCII equivalent"""
    return "".join(HOMOGLYPH_MAP.get(ch, ch) for ch in text)
