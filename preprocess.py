import bs4
import sys



def main():
    if len(sys.argv) != 2:
        return

    filename = sys.argv[1]
    data = preprocess(filename)
    with open(filename, 'w') as f:
        f.write(data)

def preprocess(filename):
    with open('./one_big.css', 'r') as f:
      css = f.read()

    with open('./one_big.js', 'r') as f:
      js = f.read()

    with open(filename, 'r') as f:
        data = f.read()
    html = bs4.BeautifulSoup(data, 'html.parser')
    data = html.find_all('div', attrs={'class': 'section'})[0]

    title = html.find('title').prettify()

    html_pretag = """
    <html class=" js flexbox flexboxlegacy canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers applicationcache svg inlinesvg smil svgclippaths">
    """

    css = '<style>' + css + '</style>'
    js = "<script>" + js + '</script>'
    html = html_pretag + title + css + data.prettify() + "</html>"
    return html

if __name__ == '__main__':
    main()
