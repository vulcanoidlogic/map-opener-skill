from mycroft import MycroftSkill, intent_file_handler


class MapOpener(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('opener.map.intent')
    def handle_opener_map(self, message):
        self.speak_dialog('opener.map')


def create_skill():
    return MapOpener()

