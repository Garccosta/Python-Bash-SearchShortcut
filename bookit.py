import webbrowser, sys, pyperclip

if len(sys.argv) > 1: #Check if command line arguments were passed
 	address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #Use what is in the clipboard as search arguments

webbrowser.open('https://www.booking.com/searchresults.pt-br.html?ss=' + address)

