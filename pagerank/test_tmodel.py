def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    no_of_links = len(corpus[page])
    model = {}
    for pg in corpus.keys():
        model[pg] = round((1 - damping_factor) / len(corpus.keys()), 3)
    print("Initial model:", model)
    
    #if page has no links, then we can pretend it has links to all pages in the corpus, including itself
    if no_of_links:
        for pg in corpus[page]:
            model[pg] += damping_factor / no_of_links
    else:
        for pg in corpus.keys():
            model[pg] += damping_factor / len(corpus.keys())

    return model

print("Final model:", transition_model({"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}, "1.html", 0.85))