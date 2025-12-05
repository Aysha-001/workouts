from urllib.request import urlopen
import sys

def download():
    url = sys.argv[-1]
    #print(sys.argv)
    
    response = urlopen(url)
    content = response.read()

    #write the content
    if url.endswith("/"):
        base_name = "index.html"
    else:
        base_name = url.split('/')[-1]
    with open(base_name, 'wb' ) as file:
        file.write(content)


    print(f"{url} saved as {base_name}" )
    
download()