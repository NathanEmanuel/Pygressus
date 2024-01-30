# Pygressus: Congressus API Python library
Interact with the [Congressus API](https://api.congressus.nl/v30/docs) using Python scripts!

## Basic usage
All you need to use this library is your API key, which you can get [from Congressus](https://api.congressus.nl/v30/docs#section/Introduction/Authentication). Use the key to instantiate a `Client` object (`client = Client("Your key")`) and you're all set to start making API requests.

API request are always made using the client you justed instantiated. All possible requests are grouped into *namespaces*, with each namespace relating to the type of data that you are working with. Each namespace has a method for each request type in that namespace. So if you want to make a request you need to know 2 things:

1. Which namespace corresponds to the data type you're working with.
2. Which type of request in that namespace you need.

You can generally $^1$ get this information from [Congressus's API documentation](https://api.congressus.nl/v30/docs). The name of each namespace is really similar to the name of the data type in the documentation, except that the data types are in `PascalCase` while the namespaces are in `underscore_case`. So data type `GroupMembership` corresponds with namespace `group_membership`.

The names of request types is even simpler to determine: just take the first word of its documentation name. So request type *Create Member* corresponds with the `create()` method of namespace `member`.

Each method can have parameters each of which is either optional or required. These are usually the same as the parameters in the Congressus documentation. If the documentation say that a parameter is required, than it is typically also required by this library.

$^1$ There are a few requests for which this isn't true.

### Example
Let's say you want look yourself up in your Congressus administration through the API. From the Congressus documentation, you learn that the data type you want to work with is `Member` and you conclude that the namespace is `member`. Looking up a member is done with the request *Search Members*, which you again got from the documentation, and now you know that you should use the `search()` method. Now you know that you can find yourself with:
```python
page = client.member.search("Your name")
```
This yields you a *page* with all members that Congressus found based on your name. You can see the data on that page with:
```python
print(page.data)
```
Did you find yourself? If so, congratulations! You know how to work with this library!

There is more to learn regarding different types of requests, pages, webhooks, et cetera. Congressus's documentation is always a good starting point for that. Remember that this library is nothing more than a simple way to interact with their API using Python and it therefore tries to mimic their documentation as much as possible.

## Advanced usage
The `Client` class functions as a (sort of) [facade](https://refactoring.guru/design-patterns/facade) for the library. If the library is to be used _as-is_, then this is the only class that the user should instatiate and interact with.

### Package structure
```
pygressus
│   client.py
│   webhook_server.py
│
├───api
│       base_client.py
│       paginated_response.py
│       requester.py
│
└───models
        elastic_member.py
        group.py
        group_membership.py
        log_entry.py
        member.py
        membership_status.py
        member_status.py
        webhook.py
```

### TODOs
| Difficulty | Task                                                 |
|------------|------------------------------------------------------|
| Easy       | Implementing data models and GET and DELETE requests |
| Normal     | Implementing POST and PUT requests                   |
| Hard       | Writing test code                                    |
| Expert     | Implementing the webhook server                      |
