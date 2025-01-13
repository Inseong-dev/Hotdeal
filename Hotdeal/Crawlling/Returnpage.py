def returnList():
    import Crawl
    Page = []
    Page.extend(Crawl.crawl_website())
    return Page

