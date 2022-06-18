class TimelineSlide:
    def __init__(self, args):
        self.start_date = args['start_date']
        self.text = [args['text']]
        self.args = args

    def addText(self, additionalText):
        self.text.append(additionalText)

    def toDict(self):
        return {
                    'start_date': {
                        'year': self.start_date.year,
                        'month': self.start_date.month,
                        'day': self.start_date.day
                    },
                    'text': {
                        'text': self.wrapText()
                    }
                }

    def wrapText(self, useHtml = False):
        text = ''
        if useHtml:
            innerLines = ''
            for line in self.text:
                innerLines += '<li>%s</li>'%line
            wrapWithUl = '<ul>%s</ul>'%innerLines
            text = wrapWithUl
        else:
            text = '\n'.join(self.text)
        return text
