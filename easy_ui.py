import eel

html_template = """
<!DOCTYPE html>
<html>

    <head>
        <title>EEL Basic Template</title>
        <script type="text/javascript" src="/eel.js"></script>
        <script src="./scripts.js"></script>
        <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
    </head>

    <body>
    
        <div id="root"></div>
    
    </body>

</html>
"""

class easyUI:

    def __init__(self):

        # create basic javascript template
        f = open('web/scripts.js', 'w')
        f.write("")
        f.close()

        # create basic css template
        f = open('web/style.css', 'w')
        f.write("")
        f.close()

        # create basic html template
        f = open('web/index.html', 'w')
        f.write(html_template)
        f.close()

        # start eel init
        eel.init("web")

    def launch(self):
        eel.start("index.html")

ui = easyUI()
ui.launch()