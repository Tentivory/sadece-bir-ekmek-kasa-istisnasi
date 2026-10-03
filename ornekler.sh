#!/bin/sh
# Uc resmi ornek. Ciddi degildir.
python3 kasa_istisnasi.py --urun 1 --bahane ekmek --acil hayir --goz-temasi hayir
echo
python3 kasa_istisnasi.py --urun 3 --bahane "sadece bir ekmek" --acil evet --goz-temasi evet
echo
python3 kasa_istisnasi.py --urun 17 --bahane ekmek --acil evet --goz-temasi hayir
