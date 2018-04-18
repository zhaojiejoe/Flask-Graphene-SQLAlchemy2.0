# Flask Graphene-SQLAlchemy 2.0 demo
This is an example project for using GraphQL with Flask using Graphene-SQLAlchemy.

## Installing Requirements
install the packages.
```
pip install -r requirements.txt
```
## Running Flask Server
Go to the root dir and run the below line in the terminal.
```
python manage.py runserver -h 0 -p 8888
```
## Testing GraphQL
Go to http://localhost:8888/graphql/ to try GraphQL. 
### Adding a New User
```
mutation {
  createUser(username: "test") {
    user {
      username
    }
    ok
  }
}
```
### Getting All Users List
```
{
  users {
    id,
    username
  }
}
```

