import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from html import unescape


def enabled():
    """Whether internet search is allowed for the current process."""
    value = os.environ.get("ENABLE_WEB_SEARCH", "").strip().lower()
    return value in {"1", "true", "yes", "on"}


def provider_name(provider=None):
    return (provider or os.environ.get("WEB_SEARCH_PROVIDER", "brave") or "brave").lower()


def search_web(query, limit=5, provider=None):
    """Search the internet for current information. Retourne a list of {title, url, snippet} dicts."""
    if not enabled():
        raise RuntimeError("Web search is disabled. Set ENABLE_WEB_SEARCH=1 to enable it.")
    provider = provider_name(provider)
    if provider == "brave":
        return _brave_search(query, limit)
    if provider == "duckduckgo":
        return _duckduckgo_search(query, limit)
    raise RuntimeError(f"Unsupported web search provider: {provider}. Use 'brave' or 'duckduckgo'.")


def _brave_search(query, limit):
    api_key = os.environ.get("BRAVE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("BRAVE_API_KEY is required when using the Brave web search provider.")
    url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode({
        "q": query,
        "count": str(limit),
    })
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "X-Subscription-Token": api_key,
            "User-Agent": "Survival-LLM/0.1",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as resp:
        data = json.load(resp)
    results = []
    for item in (data.get("web") or {}).get("results") or []:
        title = (item.get("title") or "").strip()
        url = (item.get("url") or "").strip()
        snippet = (item.get("description") or item.get("snippet") or "").strip()
        if title and url:
            results.append({"title": title, "url": url, "snippet": snippet})
    return results[:limit]


def _duckduckgo_search(query, limit):
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=20) as resp:
        html = resp.read().decode("utf-8", "replace")
    matches = re.findall(
        r'<a rel="nofollow" class="result-link" href="(.*?)".*?>(.*?)</a>.*?<a class="result-snippet".*?>(.*?)</a>',
        html,
        re.DOTALL,
    )
    results = []
    for href, title, snippet in matches:
        text = unescape(re.sub(r"<.*?>", "", title)).strip()
        desc = unescape(re.sub(r"<.*?>", "", snippet)).strip()
        if text and href:
            results.append({"title": text, "url": href, "snippet": desc})
    return results[:limit]
