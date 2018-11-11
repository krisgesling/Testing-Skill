from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG
# import urllib, urllib.request, json, random, re
# from urllib.request import Request

__author__ = 'krisgesling'
LOGGER = LOG(__name__)

class TestingSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testing.start.intent')
    def handle_start_intent(self, message):
        def validator(utterance):
            LOG.info('VALIDATOR')
            LOG.info(utterance)
        def on_fail(utterance):
            LOG.info('ON_FAIL')
            LOG.info(utterance)
            return "I have failed!"
        result = self.get_response(dialog='Say what')
        self.speak_dialog('result', {'result': result})

    def stop(self):
        pass

def create_skill():
    return TestingSkill()
