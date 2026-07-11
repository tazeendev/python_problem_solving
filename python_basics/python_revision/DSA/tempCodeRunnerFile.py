def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ['Ali', 'Ahmad', 'Safia', 'Sadia', 'Sabah', 'Ahmad']
search_name = 'Ahmad'
result = find_paper(papers, search_name)
if result:
    print(f'{search_name} found in the list')
else: