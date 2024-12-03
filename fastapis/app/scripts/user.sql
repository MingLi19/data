-- 建表: 用户数据
-- Date: 2024-11-26
create table user
(
    id              int auto_increment
    username        varchar(255) not null,
    hashed_password varchar(255) not null,
    phone           varchar(255) not null,
    is_admin        tinyint(1)   not null,
    is_system_admin tinyint(1)   not null,
    disabled        tinyint(1)   not null,
    created_at      datetime     not null,
    company_id      int          not null,
    PRIMARY KEY (id),
);