import graphene

import graphql_jwt
import links.schema
import users.schema


# Combinar la consulta de links con la consulta principal
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
# Crear el esquema
schema = graphene.Schema(query=Query, mutation=Mutation)

