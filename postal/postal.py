import theatre_ag as theatre


class Actor(theatre.Actor):
    def __init__(self, *args, **kwargs):
        self.inbox = []

    def recieve_message(self, message):
        '''
        Recieves a message to the actor's inbox.
        TODO: work out what more needs to be done to ensure arrival ordering given our temporal model.
        '''
        self.inbox.append(message)

    def __clear_inbox(self):
        '''
        Indiscriminately remove all messages
        '''
        self.inbox = []
