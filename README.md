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
2. `python generate.py --paper A5`
3. Print the `flashcards.pdf` double-sided using a color printer on A5 papers (for durability, use a thick paper (e.g., [250 g/m2 craft card](https://www.coop-city.ch/de/papeterie/buerobedarf-buerogeraete/papier/briefumschlaege-karten/qualite-prix-doppelkarten-a6-25-stueck/p/4534346?gad_source=1&gclid=CjwKCAiAtsa9BhAKEiwAUZAszR_R4-CoRR7YQztJ9VP28TZbo16IrKX8TDMFKi7SfVojiM1b22ZIehoCn_gQAvD_BwE)) )
