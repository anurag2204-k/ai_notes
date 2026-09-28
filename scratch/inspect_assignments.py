import os, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

src_dir = r'C:\Users\anurag\Desktop\Building Agentic AI Applications with a Problem-First Approach'

def dump_assignment_details(html_name):
    p = os.path.join(src_dir, html_name)
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f, 'html.parser')
    h1 = soup.find('h1')
    title = h1.get_text(strip=True) if h1 else html_name
    
    # get main
    main = soup.find('main')
    if not main and h1:
        curr = h1
        while curr.parent and len(curr.parent.get_text()) < 500:
            curr = curr.parent
        main = curr.parent if curr.parent else curr
        
    text = main.get_text(separator='\n', strip=True) if main else ''
    print(f'==============================')
    print(f'FILE: {html_name}')
    print(f'TITLE: {title}')
    print(f'==============================')
    print(text[:2500])
    print('\n' + '='*50 + '\n')

dump_assignment_details('045 [Build] Assignment 1 - Using LangChain.html')
dump_assignment_details('049 [Build] Assignment 1 - Test Cases Sample.html')
dump_assignment_details('081 [Build] Assignment 2 - Using LangGraph.html')
dump_assignment_details('085 [Build] Assignment 2 - Test Cases.html')
dump_assignment_details('120 [Build] Assignment 3 - Using LangGraph.html')
dump_assignment_details('140 Capstone Overview.html')
dump_assignment_details('141 Getting Started Capstone Guidelines.html')
