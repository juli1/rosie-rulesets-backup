import sys

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://api.codiga.io/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query getRuleSet($ruleset: String!) {
      ruleSet(name: $ruleset){
        id
        name
        description
        languages
        owner{
          username
        }
        creationTimestamp
        updatedTimestamp
        rules(howmany:100, skip:0) {
          id
          name
          message
          language
          content
          category
          creationTimestamp
          updatedTimestamp
          severity
          description
          elementChecked
          ruleType
          cwe
          cve
          pattern
          patternMultiline
          owner
          {
            username
          }
          tests{
            id
            name
            description
            shouldFail
            content
          }
        }
      }
    }
"""
)

if len(sys.argv) != 2:
    print("pass a parameter")
    sys.exit(1)

ruleset_name = sys.argv[1]


params = {"ruleset": ruleset_name}

# Execute the query on the transport
result = client.execute(query, variable_values=params)
print(result)