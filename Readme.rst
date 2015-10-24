Category Template
-----------------

This plugin makes it possible to build templates for listings and single
articles, that are category-specific.

Installation
============

1. Create a directory inside your project called 'plugins/category_template'
1. Download the repo into that directory, or check it out as a submodule
2. Add 'category_template' to your `PLUGINS` setting

Defining templates
==================

Now in your theme's templates directory, you can create a subdirectory for each
category you want to make specific templates for. Use the category's slug as
the directory name.

Inside that directory, create an 'index.html' file which will act as the
category-specific verison of your post listing template, and should extend
'category.html'.

If you want a specific template for a single post within that category, create
a file inside that subdirectory called 'article.html'. This, predictably enough
should extend 'article.html'.
