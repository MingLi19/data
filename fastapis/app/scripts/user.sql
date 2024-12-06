create table user
(
    username        varchar(255) not null,
    hashed_password varchar(255) not null,
    phone           varchar(255) not null,
    is_admin        tinyint(1)   not null,
    is_system_admin tinyint(1)   not null,
    disabled        tinyint(1)   not null,
    created_at      datetime     not null,
    id              int auto_increment
        primary key,
    company_id      int          not null,
);