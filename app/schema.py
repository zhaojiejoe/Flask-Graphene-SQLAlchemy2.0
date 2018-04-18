# coding=utf-8
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene

from app.models import UserModel


class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    """
    for search
    """
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()


class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()

    ok = graphene.Boolean()
    user = graphene.Field(User)

    def mutate(self, info, username):
        ok = True
        user = UserModel(username=username)
        user.save()
        return CreateUser(user=user, ok=ok)


class Mutation(graphene.ObjectType):
    """
    for create
    """
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
