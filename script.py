import os

links={
    "resume":"https://drive.google.com/file/d/1PFNn1DiG0Mtp7_XdDuHxldcxFdPjn0eF/view?usp=sharing",
    "github":"https://github.com/JivinVarghese",
    "marksheets":"https://drive.google.com/file/d/1n4O9l5DsgczCjBG-DpYJ8Qy-IP4MP8M2/view?usp=sharing",
    "aadhaarpanbirth":"https://drive.google.com/file/d/1Dqgt8rCwyLY3_NcR3rbxrZ76-fiG9pB6/view?usp=sharing",
    "linkedin":"https://www.linkedin.com/in/jivinvarghese/",


}


def createFileContent(url):
    
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirecting</title>
    <script>
        window.location.href="{}"
    </script>
    </head>
    <body>
        
    </body>
    </html>
    '''.format(url)

for k,v in links.items():
    f = open(f"{k}.html", "w")
    f.write(createFileContent(v))
    f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")

