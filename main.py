from website_analyzer.web import get_browser, get_html
from website_analyzer.analyze_html import get_metas_contents


if __name__ == '__main__':
    url = "http://bezerba.ma/offres/consulter/145-Cours%20de%20soutien%20comptabilit%C3%A9%20et%20contr%C3%B4le%20de%20gesti/"
    html = get_html(get_browser(), url)
    metas = get_metas_contents(html)
    print(metas)
