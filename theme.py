from lxml.etree import Element, tostring


def key_node(name):
    node = Element('key')
    node.text = name
    return node


def string_node(value):
    node = Element('string')
    node.text = value
    return node


def style_node(style):
    node = Element('dict')
    node.append(key_node('name'))
    node.append(string_node(style['name']))
    node.append(key_node('scope'))
    node.append(string_node(style['scope']))
    node.append(key_node('settings'))
    settings = Element('dict')

    if 'foreground' in style:
        settings.append(key_node('foreground'))
        settings.append(string_node(style['foreground']))
    if 'fontStyle' in style:
        settings.append(key_node('fontStyle'))
        settings.append(string_node(style['fontStyle']))

    node.append(settings)
    return node


def add_node(name, style, parent):
    parent.append(key_node(name))
    parent.append(string_node(style[name]))


def general_settings(style):
    settings = Element('array')
    sub = Element('dict')
    sub.append(key_node('settings'))
    settings.append(sub)
    sub2 = Element('dict')
    for key, value in style['settings'].items():
        sub2.append(key_node(key))

        sub2.append(string_node(value))

    sub.append(sub2)
    for each in style['style']:
        settings.append(style_node(each))
    return settings


def theme(style):
    root = Element('plist', version=style['version'])

    doctype = '<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    settings = Element('dict')
    root.append(settings)

    add_node('author', style, settings)
    add_node('name', style, settings)
    add_node('uuid', style, settings)

    settings.append(key_node('settings'))
    settings.append(general_settings(style))

    return tostring(
        root,
        pretty_print=True,
        doctype=doctype,
        xml_declaration=True,
        encoding='UTF-8',
    ).decode('utf-8')
