## Models

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
