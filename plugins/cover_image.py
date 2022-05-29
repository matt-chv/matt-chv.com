#home brewed heavily influenced by
#https://github.com/peterdesmet/pelican-cover-image/blob/master/cover_image.py

def cover_image(generator):
    """
    Adds cover_image_url and cover_image_caption attributes to each article/page, based on 
    metadata or pelican settings
    """

    articles = getattr(generator, "articles", [])
    for article in articles:
        if hasattr(article, "cover_image_url") and article.cover_image_url:
            article.cover_image_url = cover_image_url
            article.cover_image_caption = "cover_image_caption"

def register():
    signals.article_generator_finalized.connect(cover_image)