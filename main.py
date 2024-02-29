import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

urls = [
    ("ICSE 2024","https://dblp.org/db/conf/icse/icse2024.html","2024.04.14~2024.04.20"),
    ("TSE 2024","https://dblp.org/db/journals/tse/tse50.html",None),
    ("TOSEM 2024","https://dblp.org/db/journals/tosem/tosem33.html",None),
    ("RE 2023","https://dblp.org/db/conf/re/re2023.html",None),
    ("ASE 2023","https://dblp.org/db/conf/kbse/ase2023.html","2023.09.12~2023.09.14"),
    ("ICSE 2023","https://dblp.org/db/conf/icse/icse2023.html","2023.05.14~2024.04.20"),
    ("TSE 2023","https://dblp.org/db/journals/tse/tse49.html",None),
    ("TOSEM 2023","https://dblp.org/db/journals/tosem/tosem32.html",None),
    ("RE 2022","https://dblp.org/db/conf/re/re2022.html",None),
    ("ASE 2022","https://dblp.org/db/conf/kbse/ase2022.html","2022.10.10~2022.10.14"),
    ("ICSE 2022","https://dblp.org/db/conf/icse/icse2022.html","2022.05.08~2022.05.27"),
    ("TSE 2022","https://dblp.org/db/journals/tse/tse48.html",None),
    ("TOSEM 2022","https://dblp.org/db/journals/tosem/tosem31.html",None),
    ("RE 2021","https://dblp.org/db/conf/re/re2021.html",None),
    ("ASE 2021","https://dblp.org/db/conf/kbse/ase2021.html","2021.11.15~2021.11.19"),
    ("ICSE 2021","https://dblp.org/db/conf/icse/icse2021.html","2021.05.17~2021.06.02"),
    ("TSE 2021","https://dblp.org/db/journals/tse/tse47.html",None),
    ("TOSEM 2021","https://dblp.org/db/journals/tosem/tosem30.html",None),
    ("RE 2020","https://dblp.org/db/conf/re/re2020.html",None),
    ("ASE 2020","https://dblp.org/db/conf/kbse/ase2020.html","2020.09.21~2020.09.25"),
    ("ICSE 2020","https://dblp.org/db/conf/icse/icse2020.html","2020.06.24~2020.07.16"),
    ("TSE 2020","https://dblp.org/db/journals/tse/tse46.html",None),
    ("TOSEM 2020","https://dblp.org/db/journals/tosem/tosem29.html",None),
    ("RE 2019","https://dblp.org/db/conf/re/re2019.html",None),
    ("ASE 2019","https://dblp.org/db/conf/kbse/ase2019.html","2019.11.10~2022.11.15"),
    ("ICSE 2019","https://dblp.org/db/conf/icse/icse2019.html","2019.05.25~2019.05.31"),
    ("TSE 2019","https://dblp.org/db/journals/tse/tse45.html",None),
    ("TOSEM 2019","https://dblp.org/db/journals/tosem/tosem28.html",None),
    ("RE 2018","https://dblp.org/db/conf/re/re2018.html",None),
    ("ASE 2018","https://dblp.org/db/conf/kbse/ase2018.html","2018.09.03~2018.09.07"),
    ("ICSE 2018","https://dblp.org/db/conf/icse/icse2018.html",None),
    ("TSE 2018","https://dblp.org/db/journals/tse/tse44.html",None),
    ("TOSEM 2018","https://dblp.org/db/journals/tosem/tosem27.html",None),
    ("RE 2017","https://dblp.org/db/conf/re/re2017.html",None),
    ("ASE 2017","https://dblp.org/db/conf/kbse/ase2017.html","2017.10.29~2017.11.03"),
    ("ICSE 2017","https://dblp.org/db/conf/icse/icse2017.html",None),
    ("TSE 2017","https://dblp.org/db/journals/tse/tse43.html",None),
    ("TOSEM 2017","https://dblp.org/db/journals/tosem/tosem26.html",None),
    ("RE 2016","https://dblp.org/db/conf/re/re2016.html",None),
    ("ASE 2016","https://dblp.org/db/conf/kbse/ase2016.html",None),
    ("ICSE 2016","https://dblp.org/db/conf/icse/icse2016.html",None),
    ("TSE 2016","https://dblp.org/db/journals/tse/tse42.html",None),
    ("TOSEM 2016","https://dblp.org/db/journals/tosem/tosem25.html",None),
    ("RE 2015","https://dblp.org/db/conf/re/re2015.html",None),
    ("ASE 2015","https://dblp.org/db/conf/kbse/ase2015.html",None),
    ("ICSE 2015","https://dblp.org/db/conf/icse/icse2015.html",None),
    ("TSE 2015","https://dblp.org/db/journals/tse/tse41.html",None),
    ("TOSEM 2015","https://dblp.org/db/journals/tosem/tosem24.html",None),
    ("RE 2014","https://dblp.org/db/conf/re/re2014.html",None),
    ("ASE 2014","https://dblp.org/db/conf/kbse/ase2014.html",None),
    ("ICSE 2014","https://dblp.org/db/conf/icse/icse2014.html",None),
    ("TSE 2014","https://dblp.org/db/journals/tse/tse41.html",None),
    ("TOSEM 2014","https://dblp.org/db/journals/tosem/tosem23.html",None),
    ("RE 2013","https://dblp.org/db/conf/re/re2013.html",None),
    ("ASE 2013","https://dblp.org/db/conf/kbse/ase2013.html",None),
    ("ICSE 2013","https://dblp.org/db/conf/icse/icse2013.html",None),
    ("TSE 2013","https://dblp.org/db/journals/tse/tse40.html",None),
    ("TOSEM 2013","https://dblp.org/db/journals/tosem/tosem22.html",None),
]
if __name__=="__main__":
    txt = "# RE-Paper-list\n\n"
    for name,url,date in tqdm(urls):
        if date is None:
            t = f"## [{name}]({url})\n\n"
        else:
            t = f"## [{name}]({url}) ({date})\n\n"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"})
        soup = BeautifulSoup(r.text, 'lxml')
        papers = []
        t_extract = f"### requirements extraction\n"
        for entry in soup.find_all('li', class_='entry inproceedings'):
            title = entry.find('span', class_='title').text
            authors = [author.text for author in entry.find_all('span', itemprop='author')]
            url = entry.find('a')['href']
            first_author = authors[0] if authors else 'Unknown'
            found = "requirements" in title.lower() or "requirement" in title.lower() or "user review" in title.lower()
            found_extract = "extract" in title.lower() or "identify" in title.lower() or "mine" in title.lower() or "mining" in title.lower()
            item = f"- {title}.{first_author} et.al. [pdf]({url})\n"
            if found:
                t_extract +=item
        t+=t_extract
        txt +=t
    with open("paperlist.md",'w') as f:
        f.write(txt)
