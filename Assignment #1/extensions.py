#Program that identifies and outputs the media type of a file based on its extension

#Lists of file extensions
image=[".gif",".jpg",".jpeg",".png"]
application=[".pdf",".zip"]
text=[".txt"]

x=input("File name: ")
x=x.lower() #Insensitive to uppercase
x=x.replace(" ","") #Insensitive to spaces

#Media types based on the extension
def extensions():

    #Combine all extensions into one list
    combine=image+application+text

    for ext in combine:

        if x.endswith(ext):
            if ext in image:
                a=ext.replace(".","image/")

            elif ext in application:
                a=ext.replace(".","application/")

            elif ext in text:
                a="text/plain"
        
            return (a)

    return "application/octet-stream"

print(extensions())