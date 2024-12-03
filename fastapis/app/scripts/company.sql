create table company
(
    id             int auto_increment,
    name           varchar(255) not null,
    contact_person varchar(255) null,
    contact_phone  varchar(255) null,
    contact_email  varchar(255) null,
    created_at     datetime     not null,
    address        varchar(255) null,
    PRIMARY KEY (id),
);

