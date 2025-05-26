import markdown
import os
import re


def replace_src_attr_path_with_static(inp: str):
    pattern = r"src\s*=\s*\"\.\.\/attachments.(.+?)\""
    repl = "src=\"{% static 'r\1' %}\""
    subbed_html = re.sub(pattern, repl, inp)
    return subbed_html


def main():
    print(os.getcwd())

    with open("samples/test_mkdwn.md", "r") as f:
        mkdwn_str = f.read()

    html = markdown.markdown(text=mkdwn_str)

    subbed_html = re.sub("  ", "    ", html)

    # print(subbed_html)

    with open("samples/test_mkdwn.html", "w") as f:
        f.write(html)

    print(subbed_html)


if __name__ == "__main__":
    main()
