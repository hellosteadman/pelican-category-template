from pelican import signals
from . import receivers

def register():
    signals.generator_init.connect(
        receivers.generator_init
    )

    signals.article_generator_write_article.connect(
        receivers.article_generator_write_article
    )
