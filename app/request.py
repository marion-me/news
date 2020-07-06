import urllib.request,json
from .models import source,news

news = news.news
Sources = source.Sources

# Getting api key
apiKey = None

# Getting the news base url
base_url = None

# Getting the source url
sources_url = None

def configure_request(app):
    global apiKey,base_url,sources_url 
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_news_BASE_URL']
    sources_url = app.config['NEWS_SOURCE_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news']:
            news_results_list = get_news_response['news']
            news_results = process_news(news_results_list)


    return news_results        

def get_news(id):
    get_news_details_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_detail_data = url.read()
        news_detail_response = json.loads(news_detail_data)

        news_object = None

        if news_detail_response:
            id = news_detail_response.get('id')
            name = news_detail_response.get('name')
            title = news_detail_response.get('title')
            description = news_detail_response.get('description')
            url = news_detail_response.get('url')
            publishedAt = news_detail_response.get('publishedAt')
            content = news_detail_response.get('content')

    return news_object        

     


def process_news(news_list):
    '''
    Function that processes the news result and transform them to a list of objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
       news_results: A list of news objects   
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if content:
            news_object = news(id,name,title,description,url,publishedAt,content)
            news_results.append(news_object)

    return news_results        


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
        # print(sources_results)

    return sources_results   


def get_source(id):
    get_source_details_url = sources_url.format(id,apiKey)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_detail_data = url.read()
        source_detail_response = json.loads(source_detail_data)

        source_object = None

        if source_detail_response:
            id = source_detail_response.get('id')
            name = source_detail_response.get('name')
            title = source_detail_response.get('title')
            description = source_detail_response.get('description')
            url = source_detail_response.get('url')
            publishedAt = source_detail_response.get('publishedAt')
            content = source_detail_response.get('content')

    return source_object


def process_sources(sources_list):
    '''
      Function that processes the sources result and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns:
       sources_results: A list of sources objects  
    '''
    sources_results = []

    for sources_item in sources_list:
        print(sources_results)
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        country = sources_item.get('country')

        if name:
            sources_objects = Sources(id,name,description,url,category,country)
            sources_results.append(sources_objects)

    return sources_results

def search_news(news_name):
    search_news_url = base_url.format(apiKey,news_name)

    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['news']:
            search_news_list = search_news_response['news']
            search_news_results = process_news(search_news_list)

    return search_news_results   

def search_sources(main_search):
    search_sources_url = sources_url.format(apiKey,main_search)

    with urllib.request.urlopen(search_sources_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)

        search_sources_results = None

        if search_sources_response['sources']:
            search_sourcess_list = search_sources_response['sources']
            search_sources_results = process_sources(search_sources_list)

    return search_sources_results 