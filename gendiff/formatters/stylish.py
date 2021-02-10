def deconstruct_value(item):
    if isinstance(item, tuple):
        return item[:2]
    return None, item


def convert(value):
    if value is False:
        convert_value = 'false'
    elif value is True:
        convert_value = 'true'
    elif value is None:
        convert_value = 'null'
    else:
        convert_value = value
    return convert_value


def create_content(input, lvl):
    if isinstance(input, dict):
        return render(input, lvl + 1)
    return convert(input)


def render(diff_dict, lvl=0):
    result = []
    tab = '    ' * lvl

    for key, value in diff_dict.items():
        state, data = deconstruct_value(value)
        content = create_content(data, lvl)

        if state == 'NESTED':
            result.append(tab + '    {}: {}'.format(
                key,
                render(data, lvl + 1)
            ))

        elif state == 'ADDED':
            result.append(tab + '  + {}: {}'.format(key, content))

        elif state == 'REMOVED':
            result.append(tab + '  - {}: {}'.format(key, content))

        elif state == 'CHANGED':
            old_content = content
            new_content = create_content(value[2], lvl)
            result.append(tab + '  - {}: {}'.format(key, old_content))
            result.append(tab + '  + {}: {}'.format(key, new_content))

        else:
            result.append(tab + '    {}: {}'.format(key, content))

    return '{\n' + '\n'.join(result) + '\n{}}}'.format(tab)
