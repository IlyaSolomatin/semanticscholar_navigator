from semanticscholar import SemanticScholar

sch = SemanticScholar()

doi = '5cff8ca46e3c6abb807e5a7be4d6c0f8760b84aa'  # example paper
top_refs = 20 # adjust as needed
top_cits = 10

paper = sch.get_paper(doi)

print("\'{title}\', {auth} {year} ({ncit}), {doi}".format(title=paper['title'], 
                                                          auth=", ".join([i['name'] for i in paper['authors']]),
                                                          year=paper['year'], 
                                                          ncit=paper['citationCount'],
                                                          doi=paper['paperId']
                                                        ))
refs = sorted(paper['references'], key=lambda x: x['citationCount'] if x['citationCount'] is not None else 0)[-top_refs:][::-1]
print("")
print("Most influential references:")
for r in refs:
    print("\'{title}\', {auth} {year} ({ncit}), {doi}".format(
        title=r['title'], 
        auth=", ".join([i['name'] for i in r['authors']]),
        year=r['year'], 
        ncit=r['citationCount'],
        doi=r['paperId']
    ))
  
print("")
cits = sorted(paper['citations'], key=lambda x: x['citationCount'] if x['citationCount'] is not None else 0)[-top_cits:][::-1]
print("Most influential citations:")
for r in cits:
    print("\'{title}\', {auth} {year} ({ncit}), {doi}".format(
        title=r['title'], 
        auth=", ".join([i['name'] for i in r['authors']]),
        year=r['year'], 
        ncit=r['citationCount'],
        doi=r['paperId']
    ))
