
####################################

#Written By Chintan Pathak
#Summary: This is an example web scrapping using BeautifulSoup. The codes parses html content and print tags

#####################

from bs4 import BeautifulSoup

html =  """
                <html><head><title>Search Google</title></head>
                <p class="title"><b>Google Results</b></p>
                <p class="batch">Results obtained
                <a class="subject" href="http://www.google.com/search/R" id="prg2">R</a>,
                <a class="subject" href="http://www.google.com/search/Python" id="prg2">Python</a> and
                <a class="subject" href="http://www.google.com/search/C#" id="prg3">C#</a>;
                </p>
                <p class="title">...</p>
                </html>
                """

#You can also import html file and parse data
#soup = BeautifulSoup(open('sample.html')) 
soup = BeautifulSoup(html)

# extracts first <b> tag in html, prints tag value and type
def read_html():
    tag = soup.a
    print tag
    print type(tag)
    print tag.string
    print tag.attrs

# extracts and prints all elements in html
def extract_elements():
    for element in soup.extract():
        print element

def find_tags(tag_name="html"):
    return soup.find_all(tag_name)

def getParent(tag_name="html"):
    tags = []
    if tag_name != "html":
        tags = find_tags(tag_name)

    if len(tags) > 0:
        return tags[0].parent


#print find_tags('title')
#read_html()
#extract_elements()
print getParent('title')
