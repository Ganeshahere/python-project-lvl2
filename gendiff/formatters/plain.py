from gendiff.formatters.stylish import deconstruct_value, convert


def create_content(input):
    if isinstance(input, dict):
        return '[complex value]'
    elif isinstance(input, str):
        return "\'{}\'".format(input)
    return convert(input)


def render(diff_dict, lvl=''):
    result = []

    for key, value in diff_dict.items():
        state, data = deconstruct_value(value)
        content = create_content(data)

        if state == 'NESTED':
            result.append(render(data, lvl + '{}.'.format(key)))

        elif state == 'ADDED':
            result.append("Property '{}' was added with value: {}".format(
                lvl + key,
                content)
            )

        elif state == 'REMOVED':
            result.append("Property '{}' was removed".format(lvl + key))

        elif state == 'CHANGED':
            old_content = content
            new_content = create_content(value[2])
            result.append("Property '{}' was updated. From {} to {}".format(
                lvl + key,
                old_content,
                new_content)
            )

        else:
            continue

    return '\n'.join(result)
