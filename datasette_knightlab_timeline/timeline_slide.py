class TimelineSlide:
    def __init__(self, args):
        self.start_date = args['start_date']
        self.text = [args['text']]
        self.args = args

    def addText(self, additionalText):
        self.text.append(additionalText)
