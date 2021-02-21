from ftplib import FTP_TLS
from ftplib import FTP

def uploadToFtp(filename):
    host = "88.122.218.102"  # adresse du serveur FTP
    user = "freebox"  # votre identifiant
    password = "7avril2001"  # votre mot de passe
    port = 49153
    ftps = FTP_TLS()
    ftps.connect(host, port)
    ftps.login(user, password)
    ftps.encoding = "utf-8"
    ftps.cwd("Disque dur")
    ftps.cwd("static")

    with open('/static/'+filename, "rb") as file:
        ftps.storbinary(f"STOR {filename}", file)
    ftps.quit()

