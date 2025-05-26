# README

A simple app that displays my markdown-based CMS notes.

## TODO

- [ ] get TOC on each page working
- [ ] get images working
- [ ] get links between pages working
- [ ] ingest all content.
- [ ] make publicly accessible.

## Design

The markdown files are ingested into the database through the MarkdownContent model via a shell script then processed and displayed as individual pages.

## Parsing Markdown

This project uses template tags as described [here](https://learndjango.com/tutorials/django-markdown-tutorial#markdown) to parse the markdown data.
