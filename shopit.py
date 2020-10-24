import webbrowser, sys, pyperclip

if len(sys.argv) > 1: #Check if command line arguments were passed
    addressAli = '-'.join(sys.argv[1:])
    addressAmazon = '+'.join(sys.argv[1:])
    addressAmericanas = '-'.join(sys.argv[1:])
else:
    addressAli = '-'.join(pyperclip.paste().split())
    addressAmazon = pyperclip.paste()
    addressAmericanas = pyperclip.paste()
    
webbrowser.open('https://pt.aliexpress.com/w/wholesale-' + addressAli + '.html')
webbrowser.open('https://www.amazon.com.br/s?k=' + addressAmazon)
webbrowser.open('https://www.americanas.com.br/busca/' + addressAmericanas)
