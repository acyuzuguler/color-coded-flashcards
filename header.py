
header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards</title>
    <link rel="stylesheet" href="../styles_{}.css">
</head>
<body>
    <div class='flashcards'>
    """

footer = """
    </div>
</body>
</html>
    """


def get_header(n_columns, tile_size, paper):
    return header.format(paper)
