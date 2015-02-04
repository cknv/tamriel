from theme import theme


class Color:
    def __init__(self, light, medium, dark):
        self.light = light
        self.medium = medium
        self.dark = dark

# Tango colors used
butter = Color('#fce94f', '#edd400', '#c4a000')
orange = Color('#fcaf3e', '#f57900', '#ce5c00')
chocolate = Color('#e9b96e', '#c17d11', '#8f5902')
chameleon = Color('#8ae234', '#73d216', '#4e9a06')
sky_blue = Color('#729fcf', '#3465a4', '#204a87')
plum = Color('#ad7fa8', '#75507b', '#5c3566')
scarlet_red = Color('#ef2929', '#cc0000', '#a40000')
aluminium_light = Color('#eeeeec', '#d3d7cf', '#babdb6')
aluminium_dark = Color('#888a85', '#555753', '#2e3436')


if __name__ == '__main__':
    style = {
        'author': 'Esben Sonne',
        'name': 'tamriel',
        'version': '0.1.2',
        'uuid': '13E579BF-40AB-42E2-9EAB-0AD3EDD88532',
        'settings': {
            'invisibles': '#3B3A32',
            'lineHighlight': '#31221B',
            'selection': '#49483E',
            'findHighlight': '#FFE792',
            'findHighlightForeground': '#000000',
            'selectionBorder': '#222218',
            'activeGuide': '#9D550FB0',
            'bracketsForeground': '#F8F8F2A5',
            'bracketsOptions': 'underline',
            'bracketContentsForeground': '#F8F8F2A5',
            'bracketContentsOptions': 'underline',
            'tagsOptions': 'stippled_underline',
            'background': '#120F0A',
            'caret': aluminium_light.light,
            'foreground': aluminium_light.light,
            'gutterForeground': '#73797b75',
            'guide': '#73797b30',
        },
        'style': [
            {
                'name': 'comment',
                'scope': 'comment',
                'foreground': aluminium_dark.medium,
                'fontStyle': 'italic',
            },
            {
                'name': 'constant',
                'scope': 'constant',
                'foreground': scarlet_red.medium,
            },
            {
                'name': 'constant numeric',
                'scope': 'constant.numeric',
                'foreground': scarlet_red.light,
            },
            {
                'name': 'string',
                'scope': 'string',
                'foreground': '#ffd000',
            },
            {
                'name': 'name',
                'scope': 'storage.type',
                'fontStyle': 'bold'
            },
            {
                'name': 'class',
                'scope': 'entity.name.type.class',
                'fontStyle': 'bold',
                'foreground': aluminium_light.light,
            },
            {
                'name': 'function',
                'scope': 'entity.name.function',
                'fontStyle': 'bold',
            },
            {
                'name': 'inherired from',
                'scope': 'entity.other.inherited-class',
                'foreground': chameleon.dark,
            },
            {
                'name': 'keyword',
                'scope': 'keyword',
                'fontStyle': 'bold',
                'foreground': aluminium_light.medium,
            },
            {
                'name': 'variable',
                'scope': 'variable',
                'foreground': sky_blue.light,
            },
            {
                'name': 'builtin functions',
                'scope': 'support.function',
                'foreground': sky_blue.medium,
            },
            {
                'name': 'builtin types',
                'scope': 'support.type',
                'foreground': sky_blue.medium,
            },
            {
                'name': 'magic methods',
                'scope': 'support.function.magic',
                'foreground': orange.medium,
            },
            {
                'name': 'magic names',
                'scope': 'support.variable.magic',
                'foreground': sky_blue.medium,
            },
            {
                'name': 'decorators',
                'scope': 'entity.name.function.decorator',
                'foreground': aluminium_dark.light,
                'fontStyle': '',
            },
            {
                'name': 'xml-tags',
                'scope': 'entity.name.tag',
                'foreground': sky_blue.dark,
            },
            # gitgutter colors.
            {
                'name': 'gitgutter deleted',
                'scope': 'markup.deleted.git_gutter',
                'foreground': scarlet_red.medium,
            },
            {
                'name': 'gitgutter inserted',
                'scope': 'markup.inserted.git_gutter',
                'foreground': chameleon.medium,
            },
            {
                'name': 'gitgutter changed',
                'scope': 'markup.changed.git_gutter',
                'foreground': butter.medium,
            },
        ],
    }

    output = theme(style)

    from zipfile import ZipFile
    with ZipFile('tamriel.sublime-package', 'w') as fo:
        fo.writestr('tamriel.tmTheme', output.encode('utf-8'))
