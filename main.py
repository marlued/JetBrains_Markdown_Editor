def headings():
    valid_levels = range(1, 7)
    level_outputs = {1: '#',
                     2: '##',
                     3: '###',
                     4: '####',
                     5: '#####',
                     6: '######'}

    while True:
        try:
            level = int(input('Level: ').strip())

            if level not in valid_levels:
                raise AttributeError('Level not in allowed range')

        except AttributeError:
            print('The level should be within the range of 1 to 6')
            continue

        text = input('Text: ').strip()
        return f'{level_outputs[level]} {text}\n\r'


def new_line():
    return '\n'


def link():
    label = input('Label: ').strip()
    url = input('URL: ').strip()
    return f'[{label}]({url}) '  # added space for printing


def plain():
    text = input('Text: ').strip()
    return '{} '.format(text)  # added space for printing


def bold():
    text = input('Text: ').strip()
    return f'**{text}** '  # added space for printing


def italic():
    text = input('Text: ').strip()
    return f'*{text}* '  # added space for printing


def inline_code():
    text = input('Text: ').strip()
    return f'`{text}` '  # added space for printing


def _help():
    print('Available formatters: plain bold italic header link inline-code'
          'ordered-list unordered-list new-line\n'
          'Special commands: !help !done')


def done():
    raise SystemExit()


def choices():
    user_input = input('Choose a formatter: ').strip()
    output_text = None
    valid_choices = ['header', 'bold', 'italic', 'plain', 'inline-code',
                     'new-line', 'link', '!help', '!done']

    if user_input not in valid_choices:
        raise RuntimeError('No valid Choice')

    if user_input == 'header':
        output_text = headings()

    if user_input == 'bold':
        output_text = bold()

    if user_input == 'italic':
        output_text = italic()

    if user_input == 'plain':
        output_text = plain()

    if user_input == 'inline-code':
        output_text = inline_code()

    if user_input == 'new-line':
        output_text = new_line()

    if user_input == 'link':
        output_text = link()

    if user_input == '!help':
        _help()
        raise IndexError('should not be appended to list')

    if user_input == '!done':
        done()

    return output_text


full_output = []

while True:

    try:
        to_output = choices()

    except IndexError:
        continue

    except RuntimeError:
        print('Unknown formatting type or command')
        continue

    full_output.append(to_output)

    print(''.join(full_output))
