from pelican.generators import PelicanTemplateNotFound
from operator import attrgetter

def generate_categories(instance, writer):
    """
    Monkeypatched instance method for `ArticlesGenerator.generate_categories`,
    that chooses the template based on the category slug
    """

    for cat, articles in instance.categories:
        try:
            category_template = instance.get_template(
                'category/%s/index' % cat.slug
            )
        except PelicanTemplateNotFound:
            category_template = instance.get_template('category')

        articles.sort(key = attrgetter('date'), reverse = True)
        dates = [article for article in instance.dates if article in articles]
        writer(
            cat.save_as,
            category_template,
            instance.context,
            category = cat,
            articles = articles,
            dates = dates,
            paginated = {
                'articles': articles,
                'dates': dates
            },
            blog = True,
            page_name = cat.page_name,
            all_articles = instance.articles
        )
