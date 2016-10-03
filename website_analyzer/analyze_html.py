from bs4 import BeautifulSoup


def get_metas_contents(html):
    soup = BeautifulSoup(html.lower(), "lxml")
    metas = {}
    tmp_metas = soup.find_all("meta")
    for meta in tmp_metas:
        if meta.has_attr("name") and meta.has_attr("content"):
            metas[meta['name']] = meta['content']
    return metas
