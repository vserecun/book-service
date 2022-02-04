from flask_restx import Namespace, Resource, fields, marshal
import logging

logger = logging.getLogger(__name__)

DATA = {}

ns = Namespace("book_controller")

book_payload = ns.model("Book", {
    "example": fields.String()
})

book_response = ns.model("Response", {
    "example": fields.String()
})


@ns.route('/')
class BookList(Resource):
    def get(self):
        return {}

    @ns.expect(book_payload)
    @ns.marshal_with(book_response)
    def post(self):
        payload = marshal(book_payload, self.payload)
        logger.info(payload)

        return {"example": "example"}

    def put(self):
        pass

    def delete(self):
        pass

# some new routes
