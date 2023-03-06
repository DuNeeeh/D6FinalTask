from django import template

register = template.Library()


@register.filter()
def censor(value):
    if type(value) is not str:
        raise ValueError
    obscene_words = ('богатырь', 'автоблоггера', 'видеокарт')
    punctuations = ',.!?;:-'
    text = value.split()
    for i in range(len(text)):
        for check in obscene_words:
            if check in text[i].lower():
                if text[i][-1] in punctuations:
                    text[i] = f'{text[i][0]}{"*" * (len(text[i]) - 2)}{text[i][-1]}'
                else:
                    text[i] = f'{text[i][0]}{"*"*(len(text[i])-1)}'
    text = ' '.join(text)

    return f'{text} '
