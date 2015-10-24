from pelican.generators import PelicanTemplateNotFound, ArticlesGenerator
from types import MethodType
from . import helpers

def generator_init(generator):
    """
    Monkeypatches the `ArticlesGenerator` class, replacing the
    `generate_categories` method with one that picks the template based on the
    category slug
    """

    if isinstance(generator, ArticlesGenerator):
        generator.generate_categories = MethodType(
            helpers.generate_categories, generator
        )

def article_generator_write_article(article_generator, content):
    """
    Looks for a category-specific template at
    'category/<category-slug>/article.html' and assigns that template to the
    article if found. Otherwise it defaults to the original template.
    """

    if content.category:
        template = 'category/%s/article' % content.category.slug

        try:
            article_generator.get_template(template)
        except PelicanTemplateNotFound:
            pass
        else:
            content.template = template
