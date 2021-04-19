""" 
Let’s take a look at how this code works:

1.concurrent.futures is imported to give us access to ThreadPoolExecutor.

2.A with statement is used to create a ThreadPoolExecutor instance executor that will promptly clean up threads upon completion.

3.Four jobs are submitted to the executor: one for each of the URLs in the wiki_page_urls list.

4.Each call to submit returns a Future instance that is stored in the futures list.

5. The as_completed function waits for each Future get_wiki_page_existence call to complete so we can print its result.
"""

import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
    
"""
https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/
"""    
        
        
