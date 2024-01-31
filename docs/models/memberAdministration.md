# Data models: member administration

#### LogEntry
    type: str
    subject_type: str
    subject_id: int

    id: Optional[int]
    text: Optional[str]
    author_id: Optional[int]
    created: Optional[str]
    modified: Optional[str]
    author: Optional[object]
    subject: Optional[object]

#### Member
    TODO

#### MembershipStatus
    status_id: int

    id: Optional[int]
    name: Optional[str]
    member_from: Optional[str]
    member_to: Optional[str]
    archived: Optional[bool]
    deceased: Optional[bool]

#### ElasticMember
    TODO

#### MemberStatus
    name: str

    id: Optional[int]
    description: Optional[str]
    archived: Optional[bool]
    hidden: Optional[bool]
    deceased: Optional[bool]
    order: Optional[int]

#### Group
    id: int
    slug: str
    start: str

    folder_id: Optional[int]
    folder: Optional[object]
    name: Optional[str]
    address: Optional[object]
    postal_adress: Optional[object]
    description: Optional[str]
    description_short: Optional[str]
    email: Optional[str]
    url: Optional[str]
    logo: Optional[object]
    path: Optional[str]
    published: Optional[bool]
    end: Optional[str]
    memo: Optional[str]

#### GroupMembership
    member_id: int
    start: str
    group_id: int

    id: Optional[int]
    end: Optional[str]
    function: Optional[str]
    may_edit_profile: Optional[bool]
    may_manage_memberships: Optional[bool]
    may_manage_storage_objects: Optional[bool]
    is_self_enroll: Optional[bool]
    order_type: Optional[str]
    order: Optional[int]
    group: Optional[object]

#### GroupFolder
    TODO

#### Organisation
    TODO

#### OrganisationCategory
    TODO

#### OrganisationMembership
    TODO
