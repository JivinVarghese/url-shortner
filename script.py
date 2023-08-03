import os

links={
    "resume":"https://drive.google.com/file/d/1TCgEaAQdyZ9icV2uduWvFi6G7mk7thI5/view?usp=sharing",
    "linkedin":"https://www.linkedin.com/in/haydencordeiro/",
    "github":"https://github.com/haydencordeiro",
    "cert":"https://drive.google.com/drive/folders/1w0mwb4AjFmX9Vk-_lQLk_F1lB1kBkPzC?usp=sharing",
    "vaccine":"https://drive.google.com/file/d/1m_Vjm2RYgU3Cw6LUJvvlB2ZN-TQV2Dxl/view?usp=sharing",
    "certificates":"https://drive.google.com/drive/folders/1w0mwb4AjFmX9Vk-_lQLk_F1lB1kBkPzC?usp=sharing",
    "marksheets":"https://drive.google.com/file/d/1A1NP0Xd0sWpnIBZtvLbMHG9M9Esxy-Kn/view?usp=sharing",
    "aadharpanbirth":"https://drive.google.com/file/d/1sz1-alDLg6w6JeCylwSFR_MT5xDyrVEd/view?usp=sharing",
    "assdfrec":"https://mega.nz/folder/bKBEBDKR#7-I6nZdMl9xzzjkYrZVH3g",
    "sem7":"https://mega.nz/folder/PawUALSY#XudA6PFfm34RqRYavnz-yg",
    "sem72":"https://drive.google.com/drive/folders/1MkhH6xJ3ug_Fo7cKsFL-WECCBAVhgEVQ",
    "zenscape":"https://play.google.com/store/apps/details?id=com.Teknack.Zenscape&hl=en_IN&gl=US",
    "gre":"https://mega.nz/folder/6bRCVZyK#fJ0wI9IUUP2p3Ypgtsmcdg",
    "ielts":"https://mega.nz/folder/DfIgkDLA#7st_w2l6QKSiyj8m1Zi6JQ",
    "meet":"https://meet.google.com/sac-kfod-ipt",
    "zoom":"https://us04web.zoom.us/j/7661382898?pwd=Z01xa05kcE9OR2ZVKzFEUDZZWWFXZz09",
    "ruvin":"https://meet.google.com/jbz-agyh-oym",
    "jivin":"https://meet.google.com/kgg-nyxj-gyb",
    "comps":"https://www.appsheet.com/start/c3eb0069-1b16-4590-8b4b-68f06960fde1",
    "dc":"https://docs.google.com/document/d/1ramBKCWW8Y8RnIO57yMoF8qQq2JxUhGyqE4_GW7E684/edit?usp=drivesdk",
    "transmission":"http://192.168.0.109:9091/transmission/web/",
    "nas":"http://192.168.0.102/ui/plugins",
    "whatsapp: "https://wa.me/917039964659"

}


def createFileContent(name,url):
    analytics=""" 
    """
    
    return analytics+'''
<meta charset=UTF-8><meta content="IE=edge"http-equiv=X-UA-Compatible><meta content="width=device-width,initial-scale=1"name=viewport><title>Redirecting to {}</title><script>window.location.href="{}"</script>
    '''.format(name,url)

for k,v in links.items():
    if k not in ["404"]:
        print(k)
        f = open(f"{k}.html", "w")
        f.write(createFileContent(k,v))
        f.close()

os.system("git add .")
os.system('git commit -m "updated links"')
os.system("git push -f")



    
