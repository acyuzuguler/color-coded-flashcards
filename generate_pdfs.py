import os 

google_chrome='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'

os.system(f"{google_chrome} --headless --print-to-pdf=flashcards.pdf --no-margins flashcards.html")
