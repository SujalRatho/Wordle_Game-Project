import wikipedia

def search_wikipedia(query, lang='en'):
    wiki_wiki = wikipedia.Wikipedia(lang)
    search_results = wiki_wiki.search(query)
    return search_results

def get_page_summary(page_title, lang='en'):
    wiki_wiki = wikipedia.Wikipedia(lang)
    page = wiki_wiki.page(page_title)
    if page.exists():
        return page.summary
    else:
        return "Page does not exist."

def get_page_links(page_title, lang='en'):
    wiki_wiki = wikipedia.Wikipedia(lang)
    page = wiki_wiki.page(page_title)
    if page.exists():
        return list(page.links.keys())
    else:
        return "Page does not exist."

def main():
    query = input("Enter search query: ")
    lang = input("Enter language (default 'en'): ") or 'en'

    print("\nSearching for pages...")
    search_results = search_wikipedia(query, lang)
    if not search_results:
        print("No results found.")
        return

    print(f"\nSearch results for '{query}':")
    for idx, title in enumerate(search_results, start=1):
        print(f"{idx}. {title}")

    page_idx = int(input("\nEnter the number of the page you want to explore: ")) - 1
    if page_idx < 0 or page_idx >= len(search_results):
        print("Invalid selection.")
        return

    page_title = search_results[page_idx]

    print(f"\nFetching summary for '{page_title}'...")
    summary = get_page_summary(page_title, lang)
    print("\nSummary:")
    print(summary)

    print(f"\nFetching links for '{page_title}'...")
    links = get_page_links(page_title, lang)
    print("\nLinks:")
    for link in links:
        print(link)

if __name__ == "_main_":
    main()