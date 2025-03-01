import argparse
import os
from header import get_header, footer
from PyPDF2 import PdfMerger

google_chrome='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'

def parse_text(txt_file):
    data = {"der": [], "die": [], "das": []}
    with open(txt_file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            fields = line.split(" ")
            fields = [f.replace("_", " ") for f in fields]
            article, german_noun, german_pl, english_noun = fields
            article = article.lower()
            german_noun = german_noun.lower().capitalize()
            german_pl = german_pl.lower().capitalize()
            english_noun = english_noun.lower()

            if article == 'der':
                data["der"].append((article, german_noun, german_pl, english_noun))
            elif article == 'die':
                data["die"].append((article, german_noun, german_pl, english_noun))
            elif article == 'das':    
                data["das"].append((article, german_noun, german_pl, english_noun))
            else:
                print(f"Invalid article: {article}")
                raise ValueError("Invalid article")
    return data


def english_to_html_flashcards(data, color, n_tiles):
    html_output = ""

    # Add flashcards
    for row in data:
        _, _, _, english_noun = row
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + color + f""";'>
                <p class='german-single'>{english_noun}</p>
            </div>
        </div>
        """

    for i in range(len(data), n_tiles):
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + "white" + f""";'>
                <p class='german-single'><span class='article'> </span> </p>
                <p class='german-plural'> </p>
            </div>
        </div>
        """      

    return html_output



def german_to_html_flashcards(data, color, n_tiles):
    html_output = ""

    # Add flashcards
    for row in data:
        article, german_noun, german_plural, _  = row
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + color + f""";'>
                <p class='german-single'><span class='article'>{article}</span> {german_noun}</p>
                <p class='german-plural'>{german_plural}</p>
                <div class="additional-text">A1</div>
            </div>
        </div>
        """

    for i in range(len(data), n_tiles):
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + "white" + f""";'>
                <p class='german-single'><span class='article'> </span> </p>
                <p class='german-plural'> </p>
            </div>
        </div>
        """      

    return html_output

colors = {"der": "#a6d1ff", "die": "#ffcccb", "das": "#d0ffbc", "en": "white"}
paper_sizes = {"A4": {"dims": (210, 297), "tile": (3,6)}, "A5": {"dims": (148, 210), "tile": (2,4)}, "A6": {"dims": (105, 148), "tile": (2,3)}}

if __name__=="__main__":
    argparser = argparse.ArgumentParser(description='Generate HTML flashcards from a text file')
    argparser.add_argument('--txt_file', type=str, default="wortschatz.txt")
    argparser.add_argument('--paper', type=str, default="A4")

    args = argparser.parse_args()

    data = parse_text(args.txt_file)

    page_dims = paper_sizes[args.paper]["dims"]
    tiles = paper_sizes[args.paper]["tile"]

    n_tiles = tiles[0]*tiles[1] 
    tile_size = (page_dims[0]/tiles[0], page_dims[1]/tiles[1])

    
    os.system("mkdir -p htmls")
    os.system("mkdir -p pdfs")

    os.system("rm -f htmls/**")
    os.system("rm -f pdfs/**")
    
    merger = PdfMerger()

    cnt = 0
    for type in ["der", "die", "das"]:
        for i in range(0, len(data[type]), n_tiles):
            html_output = get_header(tiles[0], tile_size, args.paper)
            html_output += german_to_html_flashcards(data[type][i:i+n_tiles], colors[type], n_tiles)
            html_output += footer

            html_file = "htmls/flashcards_"+args.paper+"_"+str(cnt)+"_de.html"
            pdf_file = "pdfs/flashcards_"+args.paper+"_"+str(cnt)+"_de.pdf"
            with open(html_file, 'w') as f:
                f.write(html_output)

            cmd = f"{google_chrome} --headless --print-to-pdf={pdf_file} --no-margins {html_file}"
            print(cmd)
            os.system(cmd)
            merger.append(open(pdf_file, 'rb'))

            en_data = data[type][i:i+n_tiles]
            mirrored_en_data = []
            for r in range(tiles[1]):
                for c in range(tiles[0]):
                    mirrored_ind = r*tiles[0]+tiles[0]-c-1
                    if mirrored_ind < len(en_data):
                        mirrored_en_data.append(en_data[mirrored_ind])
            html_output = get_header(tiles[0], tile_size, args.paper)
            html_output += english_to_html_flashcards(mirrored_en_data, colors["en"], n_tiles)
            html_output += footer

            html_file = "htmls/flashcards_"+args.paper+"_"+str(cnt)+"_en.html"
            pdf_file = "pdfs/flashcards_"+args.paper+"_"+str(cnt)+"_en.pdf"
            with open(html_file, 'w') as f:
                f.write(html_output)

            cmd = f"{google_chrome} --headless --print-to-pdf={pdf_file} --no-margins {html_file}"
            print(cmd)
            os.system(cmd)

            merger.append(open(pdf_file, 'rb'))

            cnt += 1

    with open("flashcards_"+args.paper+".pdf", "wb") as fout:
        merger.write(fout)

    os.system("rm -f pdfs/**")