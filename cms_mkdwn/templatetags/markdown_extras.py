"""
Template tags for markdown
"""

from os import replace
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
import re
import pdb

register = template.Library()


def replace_src_attr_path_with_static(inp: str):
    pattern = r"src\s*=\s*\"\.\.\/attachments.(.+?)\""
    repl = 'src="/static/cms_mkdwn/attachments/\\1"'
    subbed_html = re.sub(pattern, repl, inp)

    return subbed_html


def replace_toc(mkdwn: str):
    """
    replace the vim-generated toc with a TOC token for the python
    markdown package to generate its own toc through an extension.
    """

    mkdwn = re.sub(
        "^## TOC.*<!-- vim-markdown-toc GFM -->.*<!-- vim-markdown-toc -->",
        # pattern="## TOC",
        repl="[TOC]",
        string=mkdwn,
        flags=re.DOTALL,
    )

    return mkdwn


@register.filter()
@stringfilter
def markdown(mkdwn: str):
    """
    template filter for parsing markdown.
    """

    # re to enable correct markdown parsing

    mkdwn = re.sub("  ", "    ", mkdwn)

    # generate html

    mkdwn = replace_toc(mkdwn)

    print(mkdwn[0:1100])

    from markdown.extensions.toc import TocExtension

    html = md.markdown(mkdwn, extensions=[TocExtension(title="TOC")])
    html = replace_src_attr_path_with_static(inp=html)

    return html
