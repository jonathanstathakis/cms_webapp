from pathlib import Path
from cms_mkdwn.models import MarkdownContent


def ingest_from_dir(dirpath: str):
    paths = Path(dirpath).glob("*.md")
    mcs = []

    for x in paths:
        abspath = x.absolute()
        name = x.stem[3:]
        order = x.stem[:2]

        with open(abspath) as f:
            content = f.read()

        mcs.append(
            MarkdownContent(title=name, content=content, source_fp=abspath, order=order)
        )

    for mc in mcs:
        mc.save()
