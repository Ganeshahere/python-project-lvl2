INDENT_LENGTH = 0


def stringify(value):
    if type(value) is bool:
        return str(value).lower()
    return str(value)


def render_diff(diff_data, format):
    indentation = ' ' * INDENT_LENGTH
    nodes_representation = []
    for node in diff_data:
        if node['type'] == 'removed':
            value = stringify(node['value'])
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {value}"
            )
        elif node['type'] == 'added':
            value = stringify(node['value'])
            nodes_representation.append(
                f"{indentation}  + {node['key']}: {value}"
            )
        elif node['type'] == 'unchanged':
            old_value = stringify(node['old_value'])
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {value}"
            )
        elif node['type'] == 'updated':
            old_value = stringify(node['old_value'])
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {old_value}"
            )
            new_value = stringify(node['new_value'])
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {new_value}"
            )
    content = '\n'.join(nodes_representation)
    result = f"{'{'}\n{content}\n{'}'}"
    return result
