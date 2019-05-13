class Markdown:
    """
    Format string as markdown.
    """

    def __init__(self, indenting_spaces: int = 2, style_indicator: str = '*'):
        self.tab = " " * indenting_spaces
        self.style_indicator = style_indicator

    def bold(self, content: str):
        return "{b}{c}{b}".format(c=content, b=self.style_indicator * 2)

    def italic(self, content: str):
        return "{i}{c}{i}".format(c=content, i=self.style_indicator)

    def style(self, content: str = "", styles: str = None):
        if styles is None:
            styles = ['DEFAULT']

        method = dict.fromkeys(['DEFAULT', 'D', ''], lambda _: content)
        method.update(dict.fromkeys(['BOLD', 'B', 'STRONG'], self.bold))
        method.update(dict.fromkeys(['ITALIC', 'I', 'EM'], self.italic))

        t = content
        for s in styles:
            if s.upper() in method:
                t = method[s](t)
        return t

    def indents(self, content: str = "", indent_level: int = 1):
        lines = content.strip('\n').split('\n')
        text = ""
        for line in lines:
            text += "{0}{1}\n".format(self.tab * indent_level, line)
        return text

    @staticmethod
    def headers(header: str, level: int = 1):
        return "{} {}\n".format(("#" * level), header)

    @staticmethod
    def unordered_lists(item: str) -> str:
        return "- {}\n".format(item)

    def unordered_lists_from_a_list(self, a_list: list) -> str:
        text = ""
        for i in a_list:
            text += self.unordered_lists(i)
        return text

    @staticmethod
    def link(text: str, url: str, title: str = "") -> str:
        title_str = " {}".format(title) if title != "" else ""
        return "[{}]({}{})".format(text, url, title_str)

    def img(self, alt, url, title=""):
        return "!{}".format(self.link(alt, url, title))

    @staticmethod
    def quotes(content):
        lines = content.strip('\n').split('\n')
        text = ""
        for line in lines:
            text += "> {}\n".format(line)
        return text


def is_single_line(text: str):
    text.strip('\n')
    if text.find('\n') == -1:
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
