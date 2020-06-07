"""
Asmita Chitale
Assignment 01
ATCM 3311.0U1
06/11/2020
"""

# IMPORTS
import nltk
import newspaper
import progressbar

# CONSTS
SOURCES = [
    u"https://arstechnica.com/",
    u"https://www.mentalfloss.com/",
    u"https://www.wired.com/"
]

# SETUP
nltk.download('punkt')


def user_keyword ():
    """
    Ask user for a keyword
    :return: the keyword
    """
    print("", flush=True)
    userinput = input("Please enter any keyword (press enter to continue): ")
    return userinput


def get_articles():
    """
    Gets all of the latest articles from SOURCES
    :return: List of Articles
    """
    newspapers = [newspaper.build(url, memoize_articles=False) for url in SOURCES]
    articles = [][:]
    for i, paper in enumerate(newspapers):
        print("Scraping " + SOURCES[i] + " ...", flush=True)
        articles.extend(paper.articles)
    articles = articles[0::10]  # TODO delete
    print("Found %d articles." % len(articles), flush=True)
    return articles


def process_articles(articles):
    """
    Download, parse, and NLP articles
    :param articles: List of Articles
    :return: Processed list of Articles
    """
    print("Processing articles ...", flush=True)
    good_articles = [][:]
    failures = 0
    for article in progressbar.progressbar(articles):
        try:
            article.download()
            article.parse()
            article.nlp()
            good_articles.append(article)
        except newspaper.ArticleException:
            failures += 1
    print("%d of %d articles failed to process." % (failures, len(articles)), flush=True)
    return good_articles


def filter_articles(articles, keyword):
    """
    Filters articles by keyword
    :param articles: List of Articles
    :param keyword: Filtering keyword
    :return: Filtered list of Articles
    """
    print("Filtering ...", flush=True)

    def filter_function(article):
        keywords = [word.lower() for word in article.keywords]
        keyword_lower = keyword.lower()
        return keyword_lower in keywords

    good_articles = list(filter(filter_function, articles))
    return good_articles

if __name__ == '__main__':
    # Ask user for keyword input
    keyword = user_keyword()

    # Get articles
    articles = get_articles()
    for x in articles:  # TODO delete
        print(x.url)  # TODO delete

    # Process articles
    articles = process_articles(articles)

    # Filter by keyword
    if keyword:
        articles = filter_articles(articles, keyword)
    print(len(articles))  # TODO delete
    for x in articles:  # TODO delete
        print(x.url)  # TODO delete

    # Save article summaries

    # Extra feature

    pass