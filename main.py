# initialize required variables

available_formats = 'plain bold italic header link inline-code ordered-list unordered-list new-line'.split()
program_running = True
choose_format = 'Choose a formatter'
error_message = 'Unknown formatting type or command'
help_message = 'Available formatters: plain bold italic header link inline-code ordered-list unordered-list' \
               'new-line\nSpecial commands: !help !done'

while program_running:

    print(choose_format)
    user_input = input().strip()

    if user_input == '!done':
        break

    if user_input == '!help':
        print(help_message)
        continue

    if user_input not in available_formats:
        print(error_message)
        continue

    if user_input in available_formats:
        continue
