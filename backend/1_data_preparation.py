# Author : Jigesh Sheoran / sheoraninfosec / bug0x

import tranco
from homoglyphs import Homoglyphs
import pandas as pd

# Fetch top domains
t = tranco.Tranco(cache=True, cache_dir='.tranco')
latest_list = t.list()
top_domains = latest_list.top(10000)
pd.DataFrame(top_domains, columns=['domain']).to_csv('top_10k_domains.csv', index=False)

# Generate homoglyph variants [25]
hg = Homoglyphs(categories=('LATIN', 'CYRILLIC', 'GREEK', 'COMMON'))
#... (generation logic as previously detailed)...
