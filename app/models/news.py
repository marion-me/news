class News:
    '''
    Sources class to define source Objects
    '''

    def __init__(self,id,name,title,description,url,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content