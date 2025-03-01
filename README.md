# Color-coded Flashcards for German Nouns

196 ready-to-print flashcards for A1 German Nouns. One side of the card is a German word, its article, and its plural, the other side is its English translation. The cards are color-coded based on the gender of the noun (der: blue, das: green, die: red). The nouns taken from [Einfach gut! Deutsch für die Integration A1.1](https://www.telc.net/fileadmin/user_upload/Downloads_Verlag/Einfach_gut/Wortschatzlisten/Einfach_gut_A1.1_Wortschatzliste_Deutsch.pdf). Some of the compound nouns are omitted (e.g., Kursbuch is omitted as Kurs and Buch are both included). Create a PR if I missed any important word from the list.

To re-generate htmls and pdfs, run:

```
python generate_htmls.py
python generate_pdfs.py
```

NOTE: generate_pdfs.py requires Chrome to be installed in your computer. You may need change its path in `generate_pdfs.py` based on your system.

To create physical flashcards:

1. In a terminal with Python installed, `pip install PyPDF2`
2. `python generate.py --paper A4`
3. Print the `flashcards.pdf` double-sided using a color printer on A4 papers (for durability, use a thick paper (e.g., [250 g/m2 craft card](https://www.digitec.ch/en/s1/product/mondi-colour-copy-250-gm-125-x-a4-printing-paper-8056471?dbq=1&supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PROD_CH_PMAX_M9_C4&campaignid=21038324335&adgroupid=&adid=&dgCidg=Cj0KCQiA_Yq-BhC9ARIsAA6fbAjLUwsRJ3sqWZfay-572L-aHPxdhreZ_-7hH8h0GobmH_SqTbyyo3saAindEALw_wcB&gad_source=1&gclid=Cj0KCQiA_Yq-BhC9ARIsAA6fbAjLUwsRJ3sqWZfay-572L-aHPxdhreZ_-7hH8h0GobmH_SqTbyyo3saAindEALw_wcB&gclsrc=aw.ds)) )
4. Cut the printed papers into flashcards using a hobby knife
