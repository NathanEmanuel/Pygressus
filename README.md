The `Client` class functions as a (sort of) [facade](https://refactoring.guru/design-patterns/facade) for the library. If the library is to be used _as-is_, then this is the only class that the user should instatiate and interact with.

## TODOs
| Difficulty | Task                                          |
|------------|-----------------------------------------------|
| Easy       | Implementing data models and GET requests     |
| Normal     | Implementing POST, PUT, and DELETE requests   |
| Hard       | Extending the HTTP part of the webhook server |
| Expert     | Extending the TLS part of the webhook server  |

# Project structure
```
congressus
│   client.py
│
├───api
│       base_client.py
│       paginated_response.py
│       requester.py
│
├───models
│       elastic_member.py
│       group.py
│       group_membership.py
│       log_entry.py
│       member.py
│       membership_status.py
│       member_status.py
│       webhook.py
│
└───webhook
        server.py
```


# Appendix A: Data models

### LogEntry
- id: int
- type: str
- text: str
- subject_type: str
- subject_id: int
- author_id: int
- created: str
- modified: str
- author: object
- subject: object

### Member
- id: int
- username: str

### MembershipStatus
- id: int
- name: str

### ElasticMember
- _score: int
- id: int

### Group
- id: int
- folder_id: int

### GroupMembership
- id: int
- member_id: int
- start: str
- end: str
- function: str
- may_edit_profile: bool
- may_manage_memberships: bool
- may_manage_storage_objects: bool
- is_self_enroll: bool
- order_type: str
- order: int
- group_id: int
- group: object

### Webhook
- id: int
- url: str
- headers: object
- version: str
- signal: enumerate
- technical_contact_email: str
- http_basic_auth_key: str
- http_basic_auth_enabled: bool
