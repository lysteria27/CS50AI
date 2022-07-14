import os
import random
import re
import sys
import math

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a set of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


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
        model[pg] = (1 - damping_factor) / len(corpus.keys())
        #model[pg] = round((1 - damping_factor) / len(corpus.keys()), 7)
    # print(model)

    if no_of_links:
        for pg in corpus[page]:
            model[pg] += damping_factor / no_of_links

    # if page has no links, then we can pretend it has links to all pages in the corpus, including itself
    else:
        for pg in corpus.keys():
            model[pg] += damping_factor / len(corpus.keys())

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}

    for page in corpus:
        pagerank[page] = 0

    # choosing randomly for first sample
    sample = random.choices(list(corpus.keys()))[0]
    pagerank[sample] += 1

    # for n samples, keeping count of the no of times a page is sampled
    for i in range(n):
        model = transition_model(corpus, sample, damping_factor)

        # the next sample should be generated from the previous sample based on the previous sample’s transition model
        sample = random.choices(
            list(model.keys()), list(model.values()), k=1)[0]

        pagerank[sample] += 1

    # calculating the final probability
    for page in corpus:
        pagerank[page] /= n
    # print(pagerank)
    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    newrank = {}
    N = len(corpus.keys())
    total = 0.0

    for page in corpus:
        pagerank[page] = 1/N
        newrank[page] = 0.0

    isTrue = True

    while isTrue:

        for page in corpus:

            for i in corpus:
                if len(corpus[i]) == 0:
                    total += pagerank[i] / N
                if page in corpus[i]:
                    total += pagerank[i] / len(corpus[i])

            newrank[page] = (1 - damping_factor) / N + damping_factor * total
            total = 0.0

        isTrue = False

        for page in corpus:
            if not math.isclose(newrank[page], pagerank[page], abs_tol=0.001):
                isTrue = True
            
            if not isTrue:
                continue

            pagerank[page] = newrank[page]

    return pagerank



if __name__ == "__main__":
    main()
