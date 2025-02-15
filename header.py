header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards</title>
    <style>

.flashcards {
    display: grid;
    grid-template-columns: repeat(#NUM_COLS, 1fr);
    grid-gap: 0px;
}
.flashcard {
    width: #WIDTHcm;
    height: #HEIGHTcm;
    position: relative;
}
body {
    margin: 0;
    padding: 0;
}
.flashcard .front, .flashcard .back {
    width: 100%;
    height: 100%;
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid #ccc;
    box-sizing: border-box;
}
.flashcard .german-single {
    font-family: 'Verdana';
    font-size: 1.6em;
    letter-spacing: 0.02em;
    text-align: center;
    width: 100%;
    font-weight: bold;
}
.flashcard .german-plural {
    font-family: 'Verdana';
    font-size: 1.2em;
    text-align: right;
    position: absolute;
    bottom: 10px;
    right: 10px;
    font-weight: normal;
    font-style: italic;
}
.flashcard .english {
    font-family: 'Verdana';
    font-size: 1.2em;
    text-align: center;
    width: 100%;
    font-weight: normal;
}
.article {
    font-size: 0.8em;
}
@media print {
    @page { size: 21cm 29.7cm;margin: 0; }
    body { margin: 0cm; }
}
    </style>



</head>
<body>
    <div class='flashcards'>
    """

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class='flashcards'>
    """

def get_header(n_columns, tile_size, paper):
    return header.replace("#PAGE_TYPE", paper).replace("#NUM_COLS", str(n_columns)).replace("#WIDTH", str(tile_size[0]/10)).replace("#HEIGHT", str(tile_size[1]/10))
    return header.format(n_columns, tile_size[0]/10, tile_size[1]/10, paper)

footer = """
    </div>
</body>
</html>
    """