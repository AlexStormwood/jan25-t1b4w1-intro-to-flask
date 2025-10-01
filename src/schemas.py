from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from src.models.article import Article
from src.models.user import User

class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        
        model = Article  
        load_instance = True
        include_fk = True

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:

        # Define the model that this schema is based on
        model = User  

        # Allow deserialization to create class instances based on the above model
        load_instance = True

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

# Singular schema for when we return a single DB record about a user 
user_schema = UserSchema()
# Plural schema for when we return multiple DB records about users
users_schema = UserSchema(many=True)