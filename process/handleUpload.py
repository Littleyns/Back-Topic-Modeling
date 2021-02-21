def handle_uploaded_file(f):
    import os
    cwd = os.getcwd()
    with open(cwd+'\process\Articles', 'w') as destination:
        destination.write(f)
with open('/','w') as destination:
    destination.write('lol.txt')
