from flask_restful import Resource, request

class Door(Resource):
    def __init__(self,messageHandler):
        self.messageHandler = messageHandler

    def post(self):
        request_argument = request.get_json()
        try:
            user = request_argument['user']
            msg = request_argument['msg']
            self.messageHandler.send_to_user('line','U6a538ecc80009f40ac41e09d21ae6155','使用者'+user+'說：'+msg+', 要求開門！')

        except KeyError:
            return 'Bad Request',400
        return 'OK',200
