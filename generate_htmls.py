from header import header, footer

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


def english_to_html_flashcards(data, color):
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
    for i in range(len(data), 18):
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + "white" + f""";'>
                <p class='german-single'><span class='article'> </span> </p>
                <p class='german-plural'> </p>
            </div>
        </div>
        """        

    return html_output
    # html_output += footer
    # with open(html_file_path, 'w') as html_file:
    #     html_file.write(html_output)

    # print(f"HTML code has been written to {html_file_path}")


def german_to_html_flashcards(data, color):
    # html_output = header

    html_output = ""
    # Add flashcards
    for row in data:
        article, german_noun, german_plural, _  = row
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + color + f""";'>
                <p class='german-single'><span class='article'>{article}</span> {german_noun}</p>
                <p class='german-plural'>{german_plural}</p>
            </div>
        </div>
        """
    
    for i in range(len(data), 18):
        html_output += """
        <div class='flashcard'>
            <div class='front' style='background-color: """ + "white" + f""";'>
                <p class='german-single'><span class='article'> </span> </p>
                <p class='german-plural'> </p>
            </div>
        </div>
        """        

    # html_output += footer
    # with open(html_file_path, 'w') as html_file:
    #     html_file.write(html_output)

    # print(f"HTML code has been written to {html_file_path}")

    return html_output

if __name__=="__main__":
    colors = {"der": "#a6d1ff", "die": "#ffcccb", "das": "#d0ffbc", "en": "white"}

    data = parse_text('wortschatz.txt')

    html_output = header
    for type in ["der", "die", "das"]:
        for cnt, i in enumerate(range(0, len(data[type]), 18)):
            html_output += german_to_html_flashcards(data[type][i:i+18], colors[type])
            html_output += english_to_html_flashcards(data[type][i:i+18], colors["en"])

    html_output += footer
    with open("flashcards.html", 'w') as html_file:
        html_file.write(html_output)