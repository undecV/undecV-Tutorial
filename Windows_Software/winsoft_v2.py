from datetime import datetime
import ruamel.yaml  # pip install ruamel.yaml
from mdstr import Markdown


setting = {'make': {'source_file_path': 'winsoft_v2.yml',
                    'destination_file_path': 'winsoft_v2.md',
                    'flags_filter': ['PRO', 'HIDE', 'OLD']},  # ['?', 'x', 'PRO', 'HIDE', 'OLD', 'Family']
           'merge': {'enable': True,
                     'head_file_path': 'head.md',
                     'tail_file_path': 'tail.md',
                     'output': 'Windows_Software_v2.md', 
                     'append_timestamp': False},
           'markdown': {'indenting_spaces': 4,
                        'style_indicator': '*'}}


class A:
    yaml_tag = '!a'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.anchor = None
        self.link = None
        return self

    def __init__(self, anchor: str, link: str = None):
        self.anchor = anchor  # str
        self.link = link  # str, URL
    
    def tostr(self, md: Markdown = None, style: list = None) -> str:
        md = Markdown() if md is None else md
        anchor_text = md.style(self.anchor, style)
        if self.link not in [None, '']:
            return "[{}]({})".format(anchor_text, self.link)
        else:
            return anchor_text
    
    def __str__(self):
        return self.tostr()


class Item(A): 
    yaml_tag = '!item'

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.text = None  # str
        self.tags = None  # List of str
        self.flags = None  # List of str
        self.licenses = None  # List of str
        self.ref = None  # List of A
        self.sub = None  # List of Item
        return self

    def __init__(self, anchor: str, link: str = None, text: str=None, 
                    tags: str = None, flags: str = None, licenses: list = None, 
                    ref: list = None, sub: list = None):
        # type: (str, str, str, list, list, list) -> None
        super().__init__(anchor, link)
        self.text = text  # str
        self.tags = tags  # List of str
        self.flags = flags  # List of str
        self.licenses = licenses  # List of str
        self.ref = ref  # List of A
        self.sub = sub  # List of Folder or Software

    def tostr(self, md: Markdown = None, style: list = None) -> str:
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
               for attr in ['tags', 'text', 'ref', 'licenses']):
            text += ": "
            if self.licenses not in [None, []]:
                if self.licenses[0] is not None:
                    text += "`{}` ".format(self.licenses[0])
            if self.tags is not None:
                text += ''.join(["`{}` ".format(tag) for tag in self.tags])
            if self.text is not None:
                text += self.text
            if self.ref is not None:
                for r in self.ref:
                    text += "（{}）".format(r)

        return text

    def __str__(self):
        return self.tostr()


class Folder(Item):
    yaml_tag = '!folder'


class Software(Item):
    yaml_tag = '!software'


def print_and_write(fd, content):
    print(content, end='')
    fd.write(content)


def merge(_input_list, _output):
    with open(_output, 'wb') as _oup:
        for _input in _input_list:
            with open(_input, 'rb') as _inp:
                _oup.write(_inp.read())


def check_flag(flags, true_list):
    return True if any(flag in true_list for flag in flags) else False


def recur(fd, md, flags_filter, items, counter, hlv=1, llv=0, method='root'):
    for _, item in enumerate(items):
        item_type = type(item).__name__

        print('[{:^10}] [{:^10}] {} {} | '
              .format(method, item_type, hlv, llv), end='')

        if item.flags is not None:
            if check_flag(item.flags, flags_filter):
                counter["Blocked"][item_type] += 1
                print("{{BLOCKED}}")
                continue

        counter[item_type] += 1

        if type(item) == Folder:
            if method in ['software']:
                print_and_write(fd, md.indents(md.unordered_lists(item.tostr(
                    md, ['B'])), llv))
                if item.sub is not None:
                    recur(fd, md, flags_filter, item.sub, counter, hlv, llv + 1, 'software')
            else:
                print_and_write(fd, md.indents(md.headers(item, hlv), llv))
                if item.sub is not None:
                    recur(fd, md, flags_filter, item.sub, counter, hlv + 1, llv, 'folder')
    
        elif type(item) == Software:
            print_and_write(fd, md.indents(md.unordered_lists(item), llv))
            if item.sub is not None:
                recur(fd, md, flags_filter, item.sub, counter, hlv, llv + 1, 'software')
    
        elif type(item) == Item:
            print_and_write(fd, md.indents(md.unordered_lists(item), llv))


def main():
    import sys
    import json

    yaml = ruamel.yaml.YAML()
    yaml.register_class(A)
    yaml.register_class(Item)
    yaml.register_class(Folder)
    yaml.register_class(Software)

    yaml.dump(setting, sys.stdout)
    print()

    with open(setting['make']['source_file_path'], "r", encoding='utf-8') as fd:
        items = yaml.load(fd.read())
    print("[  STATUS  ] yaml.load() Done.")

    counter = {
        "Item": 0, 
        "Folder": 0, 
        "Software": 0, 
        "All": 0, 
        "Blocked": {
            "Item": 0, 
            "Folder": 0, 
            "Software": 0, 
            "All": 0, 
        }
    }

    print("[  METHOD  ] [   TYPE   ] H L | item.__dict__")
    with open(setting['make']['destination_file_path'], "w", encoding='utf-8',
              buffering=1) as fd:
        fd.write("\n<!-- START -->\n<!-- flags_filter: {} -->\n\n".format(json.dumps(setting['make']['flags_filter'])))
        recur(fd, Markdown(setting['markdown']['indenting_spaces'],
                           setting['markdown']['style_indicator']),
              setting['make']['flags_filter'], items, counter, 3, 0, 'root')

        counter["All"] = counter["Item"] + counter["Software"]
        counter["Blocked"]["All"] = counter["Blocked"]["Item"] + counter["Blocked"]["Software"]
        fd.write("\n<!-- END -->\n")
        fd.write("<!-- Date: {} -->\n".format(datetime.now().strftime('%Y-%m-%d')))
        fd.write("<!-- Count: {} -->\n\n".format(json.dumps(counter)))
    print("[  STATUS  ] recur() Done.")

    print("[  STATUS  ]", counter)

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
