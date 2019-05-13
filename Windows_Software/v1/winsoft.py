# -*- coding: utf-8 -*-

import ruamel.yaml  # pip install ruamel.yaml
from mdstr import Markdown


setting = {'make': {'source_file_path': 'winsoft.yml',
                    'destination_file_path': 'winsoft.md',
                    'flags_filter': ['?', 'x', 'PRO']},  # ['?', 'x', 'PRO']
           'merge': {'enable': True,
                     'head_file_path': 'head.md',
                     'tail_file_path': 'tail.md',
                     'output': 'Windows_Software.md', 
                     'append_timestamp': False},
           'markdown': {'indenting_spaces': 2,
                        'style_indicator': '*'}}


class Item:
    yaml_tag = '!i'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.anchor = None
        self.link = None
        self.text = None
        self.tags = None  # List of str
        self.flags = None  # List of str
        self.ref = None  # List of Item
        return self

    def __init__(self, anchor, link=None, text=None, tags=None, flags=None,
                 ref=None):
        # type: (str, str, str, list, list, list) -> None
        self.anchor = anchor
        self.link = link
        self.text = text
        self.tags = tags  # List of str
        self.flags = flags  # List of str
        self.ref = ref  # List of Item

    def str(self, md: Markdown = None, style: list = None) -> str:
        md = Markdown() if md is None else md
        anchor_text = md.style(self.anchor, style)
        text = ""

        if self.flags is not None:
            for flag in self.flags:
                text += "`{}` ".format(flag)

        if self.link not in [None, '']:
            text += "[{}]({})".format(anchor_text, self.link)
        else:
            text += anchor_text

        if any(self.__dict__[attr] is not None
               for attr in ['tags', 'text', 'ref']):
            text += ": "

            if self.tags is not None:
                for tag in self.tags:
                    text += "`{}` ".format(tag)

            if self.text is not None:
                text += self.text

            if self.ref is not None:
                for r in self.ref:
                    text += "（{}）".format(r)

        return text

    def __str__(self):
        return self.str()


class Folder(Item):
    yaml_tag = '!fld'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.sub = None
        return self

    def __init__(self, anchor, link=None, text=None, tags=None, flags=None,
                 ref=None, sub=None):
        # type: (str, str, str, list, list, list, list) -> None
        super().__init__(anchor, link, text, tags, flags, ref)

        self.sub = sub  # List of Cls or Software


class Family(Folder):
    yaml_tag = '!fam'


class Software(Item):
    yaml_tag = '!sfw'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.editions = None
        self.extensions = None
        return self

    def __init__(self, anchor, link=None, text=None, tags=None, flags=None,
                 ref=None, editions=None, extensions=None):
        # type: (str, str, str, list, list, list, list) -> None
        super().__init__(anchor, link, text, tags, flags, ref)

        self.editions = editions  # List of Cls, Software or Family
        self.extensions = extensions  # List of Cls, Software or Family


def print_and_write(fd, content):
    print(content, end='')
    fd.write(content)


def check_flag(flags, true_list):
    return True if any(flag in true_list for flag in flags) else False


def recur(fd, md, flags_filter, items, hlv=1, llv=0, method='root'):
    for _, item in enumerate(items):
        print('[{:^10}] [{:^10}] {} {} | '
              .format(method, type(item).__name__, hlv, llv), end='')

        if item.flags is not None:
            if check_flag(item.flags, flags_filter):
                print("{{BLOCKED}}")
                continue

        if type(item) == Item:
            pass
        if type(item) == Folder:
            if method in ['editions', 'extensions']:
                print_and_write(fd, md.indents(md.unordered_lists(item.str(
                    md, ['B'])), llv))
                if item.sub is not None:
                    recur(fd, md, flags_filter, item.sub, hlv, llv + 1, 'cls')
            else:
                print_and_write(fd, md.indents(md.headers(item, hlv), llv))
                if item.sub is not None:
                    recur(fd, md, flags_filter, item.sub, hlv + 1, llv, 'cls')

        elif type(item) == Family:
            print_and_write(fd, md.indents(md.unordered_lists(
                item.str(md, ['B'])), llv))
            if item.sub is not None:
                recur(fd, md, flags_filter, item.sub, hlv, llv + 1, 'family')

        elif type(item) == Software:
            print_and_write(fd, md.indents(md.unordered_lists(item), llv))
            if item.editions is not None:
                print(' ' * 30 + '| ', end='')
                print_and_write(fd, md.indents(md.unordered_lists(md.bold(
                    'Editions')), llv + 1))
                recur(fd, md, flags_filter, item.editions, hlv, llv + 2,
                      'editions')
            if item.extensions is not None:
                print(' ' * 30 + '| ', end='')
                print_and_write(fd, md.indents(md.unordered_lists(md.bold(
                    'Extensions')), llv + 1))
                recur(fd, md, flags_filter, item.extensions, hlv, llv + 2,
                      'extensions')


def merge(_input_list, _output):
    with open(_output, 'wb') as _oup:
        for _input in _input_list:
            with open(_input, 'rb') as _inp:
                _oup.write(_inp.read())


def main():
    import sys
    yaml = ruamel.yaml.YAML()
    yaml.register_class(Item)
    yaml.register_class(Folder)
    yaml.register_class(Family)
    yaml.register_class(Software)

    yaml.dump(setting, sys.stdout)
    print()

    with open(setting['make']['source_file_path'], "r", encoding='utf-8') as fd:
        items = yaml.load(fd.read())
    print("[  STATUS  ] yaml.load() Done.")

    print("[  METHOD  ] [   TYPE   ] H L | item.__dict__")
    with open(setting['make']['destination_file_path'], "w", encoding='utf-8',
              buffering=1) as fd:
        recur(fd, Markdown(setting['markdown']['indenting_spaces'],
                           setting['markdown']['style_indicator']),
              setting['make']['flags_filter'], items, 2)
    print("[  STATUS  ] recur() Done.")

    if setting['merge']['enable'] is True:
        merge([setting['merge']['head_file_path'],
               setting['make']['destination_file_path'],
               setting['merge']['tail_file_path']], setting['merge']['output'])
        if setting['merge']['append_timestamp']:
            with open(setting['merge']['output'], 'a', encoding='utf-8') as fd:
                import time
                print_and_write(fd, "- Build: {}\n".format(time.ctime()))
            print("[  STATUS  ] append_timestamp")
        print("[  STATUS  ] merge() Done.")


if __name__ == '__main__':
    main()
