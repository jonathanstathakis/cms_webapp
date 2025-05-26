from pathlib import Path
from cms_mkdwn.models import MarkdownContent
from cms.settings import BASE_DIR


def ingest_from_dir(dirpath: str):
    """
    ingest all the markdown files in `dirpath` into
    the database
    """
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


if __name__ == "__main__":
    dirpath = BASE_DIR / "samples"

    ingest_from_dir(dirpath=str(dirpath))
