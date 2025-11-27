import requests
from typing import List, TypedDict


class ResearchPaper(TypedDict):
    title: str
    authors: List[str]
    year: int
    citation_count: int
    url: str


def search_papers(topic: str, year_filter: str, year: int, citation_filter: str, citation_count: int) -> List[
    ResearchPaper]:
    query = topic.replace(" ", "+")
    url = "http://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": 10,
        "fields": "title,authors,year,citationCount,url"
    }

    response = requests.get(url, params=params)
    papers = response.json().get("data", [])

    filtered_papers = []
    for paper in papers:
        paper_year = paper.get("year")
        paper_citations = paper.get("citationCount", 0)

        year_match = True
        if year_filter == "in" and paper_year != year:
            year_match = False
        elif year_filter == "before" and paper_year >= year:
            year_match = False
        elif year_filter == "after" and paper_year <= year:
            year_match = False

        citation_match = True
        if citation_filter == "exactly" and paper_citations != citation_count:
            citation_match = False
        elif citation_filter == "at least" and paper_citations < citation_count:
            citation_match = False
        elif citation_filter == "at most" and paper_citations > citation_count:
            citation_match = False

        if year_match and citation_match:
            filtered_papers.append({
                "title": paper.get("title", "Unknown"),
                "authors": [author.get("name") for author in paper.get("authors", [])],
                "year": paper_year,
                "citation_count": paper_citations,
                "url": paper.get("url", "")
            })

    return filtered_papers