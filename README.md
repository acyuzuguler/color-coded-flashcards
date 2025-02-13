# Color-coded Flashcards for German Nouns

196 ready-to-print flashcards for A1 German Nouns. The cards are color-coded based on the gender of the noun (der: blue, das: green, die: red). The nouns taken from [Einfach gut! Deutsch für die Integration A1.1](https://www.telc.net/fileadmin/user_upload/Downloads_Verlag/Einfach_gut/Wortschatzlisten/Einfach_gut_A1.1_Wortschatzliste_Deutsch.pdf). Some of the compound nouns are omitted (e.g., Kursbuch is omitted as Kurs and Buch are both included). Create a PR if I missed any important word from the list.

To re-generate htmls and pdfs, run:

```
python generate_htmls.py
python generate_pdfs.py
```

NOTE: generate_pdfs.py requires Chrome to be installed in your computer. You may need change its path in `generate_pdfs.py` based on your system.

To create physical flashcards, simply print the generated pdfs on A4 paper (double-side) using a color printer. 
