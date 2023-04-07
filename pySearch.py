# Importing modules 
import os
import webbrowser
import time
import platform
import subprocess
import sys
import logging
from functools import wraps


# OPENS -----------------------------------------------------------
# Open URL
def open_url(url, wait_time=0):
    """
    Opens the given URL in a web browser.

    Args:
        url (str): The URL to open.
        wait_time (int): The number of seconds to wait before opening the URL. Defaults to 0 seconds.
    """
    time.sleep(wait_time)
    webbrowser.open(url, new=2)

# SEARCHES -----------------------------------------------------------
# StackOverFlow Search 
def search_stackoverflow(query):
    """Searches Stack Overflow for the given query.
Example: ast.search_stackoverflow('Raise custom error')"""
    query = query.replace(" ", "+")
    url = f"https://stackoverflow.com/search?q={query}"
    webbrowser.open(url)
    
# Youtube Search 
def search_youtube(query, search_type=None):
    """Searches YouTube for the given query.
Example1: search_youtube('How to export csv file in pandas')
Example2: search_youtube('Code With Harry', 'channel')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'videos' or search_type.lower() == 'video':
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"
        elif search_type.lower() == 'channels' or search_type.lower() == 'channel':
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAg%253D%253D"
        elif search_type.lower() == 'playlists' or search_type.lower() == 'playlist':
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAw%253D%253D"
        elif search_type.lower() == 'movies' or search_type.lower() == 'movie':
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQBA%253D%253D"
        else:
            print(f"Invalid search type: {search_type}. Searching for videos instead.")
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"
    else:
        url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# GitHub Search 
def search_github(query, search_type=None):
    """Searches GitHub for the given query.
Example1: ast.search_github('Python Projects')
Example2: ast.search_github('Python Projects', 'Issues')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'repositories' or search_type.lower() == 'repository':
            url = f"https://github.com/search?q={query}&type=repositories"
        elif search_type.lower() == 'codes' or search_type.lower() == 'code':
            url = f"https://github.com/search?q={query}&type=code"
        elif search_type.lower() == 'commits' or search_type.lower() == 'commit':
            url = f"https://github.com/search?q={query}&type=commits"
        elif search_type.lower() == 'issues' or search_type.lower() == 'issue':
            url = f"https://github.com/search?q={query}&type=issues"
        elif search_type.lower() == 'discussions' or search_type.lower() == 'discussion':
            url = f"https://github.com/search?q={query}&type=discussions"
        elif search_type.lower() == 'packages' or search_type.lower() == 'package':
            url = f"https://github.com/search?q={query}&type=registrypackages"
        elif search_type.lower() == 'marketplaces' or search_type.lower() == 'marketplace':
            url = f"https://github.com/search?q={query}&type=marketplace"
        elif search_type.lower() == 'topics' or search_type.lower() == 'topic':
            url = f"https://github.com/search?q={query}&type=topics"
        elif search_type.lower() == 'wiki' or search_type.lower() == 'wikis':
            url = f"https://github.com/search?q={query}&type=wikis"
        elif search_type.lower() == 'user' or search_type.lower() == 'users':
            url = f"https://github.com/search?q={query}&type=users"
        else:
            print(f"Invalid search type: {search_type}. Searching for repositories instead.")
            url = f"https://github.com/search?q={query}&type=repositories"
    else:
        url = f"https://github.com/search?q={query}"
    webbrowser.open(url)

# Google Search 
def search_google(query, search_type=None):
    """Searches Google for the given query.
    Example1: search_google('Google Developers')
    Example2: search_google('Google Company Inside', 'images')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'images' or search_type.lower() == 'image':
            url = f"https://www.google.com/search?q={query}&tbm=isch"
        elif search_type.lower() == 'videos' or search_type.lower() == 'video':
            url = f"https://www.google.com/search?q={query}&tbm=vid"
        elif search_type.lower() == 'books' or search_type.lower() == 'book':
            url = f"https://www.google.com/search?q={query}&tbm=bks"
        elif search_type.lower() == 'news':
            url = f"https://www.google.com/search?q={query}&tbm=nws"
        else:
            print(f"Invalid search type: {search_type}. Searching all types instead.")
            url = f"https://www.google.com/search?q={query}"
    else:
        url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    
# Microsoft Bing Search 
def search_bing(query, search_type=None):
    """Searches Microsoft Bing for the given query.
    Example1: ast.search_bing('Microsoft Developers')
    Example2: ast.search_bing('Microsoft Company Inside', 'Images')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'images' or search_type.lower() == 'image':
            url = f"https://www.bing.com/images/search?q={query}"
        elif search_type.lower() == 'videos' or search_type.lower() == 'video':
            url = f"https://www.bing.com/videos/search?q={query}"
        elif search_type.lower() == 'news':
            url = f"https://www.bing.com/news/search?q={query}"
        elif search_type.lower() == 'works' or search_type.lower() == 'work':
            url = f"https://www.bing.com/work/search?q={query}"
        else:
            print(f"Invalid search type: {search_type}. Searching for all results instead.")
            url = f"https://www.bing.com/search?q={query}"
    else:
        url = f"https://www.bing.com/search?q={query}"
        
    webbrowser.open(url)
    
# DuckDuckGo Search 
def search_duckduckgo(query, search_type=None):
    """Searches DuckDuckGo for the given query.
    Example1: search_duckduckgo('Python Projects')
    Example2: search_duckduckgo('Python Projects', 'Images')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'images' or search_type.lower() == 'image':
            url = f"https://duckduckgo.com/?q={query}&iar=images"
        elif search_type.lower() == 'videos' or search_type.lower() == 'video':
            url = f"https://duckduckgo.com/?q={query}&iar=videos"
        elif search_type.lower() == 'news' or search_type.lower() == 'new':
            url = f"https://duckduckgo.com/?q={query}&iar=news"
        else:
            print(f"Invalid search type: {search_type}. Searching all.")
            url = f"https://duckduckgo.com/?q={query}"
    else:
        url = f"https://duckduckgo.com/?q={query}"
    webbrowser.open(url)
    
# Facebook Search 
def search_facebook(query, search_type=None):
    """Searches Facebook for the given query.
    Example1: ast.search_facebook('OpenAI')
    Example2: ast.search_facebook('Elon Musk', 'people')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'posts' or search_type.lower() == 'post':
            url = f"https://www.facebook.com/search/posts/?q={query}"
        elif search_type.lower() == 'people' or search_type.lower() == 'accounts':
            url = f"https://www.facebook.com/search/people/?q={query}"
        elif search_type.lower() == 'pages' or search_type.lower() == 'page':
            url = f"https://www.facebook.com/search/pages/?q={query}"
        elif search_type.lower() == 'groups' or search_type.lower() == 'group':
            url = f"https://www.facebook.com/search/groups/?q={query}"
        else:
            print(f"Invalid search type: {search_type}. Searching all.")
            url = f"https://www.facebook.com/search/top?q={query}"
    else:
        url = f"https://www.facebook.com/search/top?q={query}"
    webbrowser.open(url)

# Instagram Search 
def search_instagram_tag(query):
    """Searches Instagram for the given query."""
    query = query.replace(" ", "+")
    url = f"https://www.instagram.com/explore/tags/{query}/"
    webbrowser.open(url)

# Twitter Search 
def search_twitter(query, search_type=None):
    """Searches Twitter for the given query.
Example1: search_twitter('AI')
Example2: search_twitter('python', 'top')"""
    query = query.replace(" ", "+")
    if search_type:
        if search_type.lower() == 'live' or search_type.lower() == 'latest':
            url = f"https://twitter.com/search?q={query}&f=live"
        elif search_type.lower() == 'people' or search_type.lower() == 'accounts':
            url = f"https://twitter.com/search?q={query}&f=user"
        elif search_type.lower() == 'image' or search_type.lower() == 'images':
            url = f"https://twitter.com/search?q={query}&f=image"
        elif search_type.lower() == 'video' or search_type.lower() == 'videos':
            url = f"https://twitter.com/search?q={query}&f=video"
        else:
            print(f"Invalid search type: {search_type}. Searching for top results instead.")
            url = f"https://twitter.com/search?q={query}&src=trend_click"
    else:
        url = f"https://twitter.com/search?q={query}&src=trend_click"
    webbrowser.open(url)

# Wikipedia Search 
def search_wikipedia(query):
    """Searches Wikipedia for the given query.
    Example: search_wikipedia('Python Programming Language')"""
    query = query.replace(" ", "+")
    url = f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=20&offset=0&ns0=1&search={query}"
    webbrowser.open(url)

# LinkedIn Search
def search_linkedin(query):
    """Searches LinkedIn for the given query.
Example: ast.search_linkedin('Data Scientist')"""
    query = query.replace(" ", "+")
    url = f"https://www.linkedin.com/search/results/all/?keywords={query}"
    webbrowser.open(url)

# Amazon Search
def search_amazon(query):
    """Searches Amazon for the given query.
Example: ast.search_amazon('iPhone')"""
    query = query.replace(" ", "+")
    url = f"https://www.amazon.com/s?k={query}"
    webbrowser.open(url) 
    
# Reddit Search
def search_reddit(query):
    """Searches Reddit for the given query.
Example: ast.search_reddit('Python')"""
    query = query.replace(" ", "+")
    url = f"https://www.reddit.com/search/?q={query}"
    webbrowser.open(url)   
    
# Quora Search
def search_quora(query):
    """Searches Quora for the given query.
Example: ast.search_quora('Python vs Java')"""
    query = query.replace(" ", "+")
    url = f"https://www.quora.com/search?q={query}"
    webbrowser.open(url)
    
# Medium Search
def search_medium(query):
    """Searches Medium for the given query.
Example: ast.search_medium('Python tips')"""
    query = query.replace(" ", "+")
    url = f"https://medium.com/search?q={query}"
    webbrowser.open(url)    