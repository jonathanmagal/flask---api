from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Bookmodel(db.Model):
    name = db.Column(db.String, primary_key=True)
    auther = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(29), nullable=False)
    stars = db.Column(db.Integer, nullable=False)


db.create_all()


def __repr__(self):
    return f"Book(auther= {auther}, category= {category}, stars= {stars}"


book_put_args = reqparse.RequestParser()
book_put_args.add_argument(
    "auther", type=str, help="Auther of the book is required", required=True)
book_put_args.add_argument(
    "category", type=str, help="Category of the book is required", required=True)
book_put_args.add_argument(
    "stars", type=int, help="stars of the book is required", required=True)

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("auther", type=str, help="name of the auther")
book_update_args.add_argument(
    "category", type=str, help="category of the book")
book_update_args.add_argument("stars", type=int, help="stars of the book")


resource_fileds = {
    'name': fields.String,
    'auther': fields.String,
    'category': fields.String,
    'stars': fields.Integer
}


class Book(Resource):
    @marshal_with(resource_fileds)
    def get(self, book_name):
        result = Bookmodel.query.filter_by(name=book_name).first()
        if not result:
            abort(404, message="book not exist. try anotehr book")
        return result

    @marshal_with(resource_fileds)
    def put(self, book_name):
        args = book_put_args.parse_args()
        result = Bookmodel.query.filter_by(name=book_name).first()
        if result:
            abort(409, message="book name already in use")
        book = Bookmodel(
            name=book_name, auther=args['auther'], category=args['category'], stars=args['stars'])
        db.session.add(book)
        db.session.commit()
        return book, 201

    @marshal_with(resource_fileds)
    def patch(self, book_name):
        args = book_update_args.parse_args()
        result = Bookmodel.query.filter_by(name=book_name).first()
        if not result:
            abort(404, message="book not exist. try anotehr book to update")
        if args["auther"]:
            result.auther = args['auther']
        if args["category"]:
            result.category = args['category']
        if args["stars"]:
            result.stars = args['stars']
        db.session.commit()

        return result

    @marshal_with(resource_fileds)
    def delete(self, book_name):
        result = Bookmodel.query.filter_by(name=book_name).first()
        if not result:
            abort(404, message="book not exist. try anotehr book to delete")
        db.session.delete(result)
        db.session.commit()
        return f"book {book_name} has been deleted"


api.add_resource(Book, "/books/<string:book_name>")

if __name__ == "__main__":
    app.run(debug=True)
