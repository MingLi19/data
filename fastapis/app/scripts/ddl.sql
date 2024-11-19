-- 建表: 燃油类型数据
-- Date: 2024-11-12
create table fuel_type
(
    id        int auto_increment
        primary key,
    name_cn   varchar(255) not null,
    name_en   varchar(255) not null,
    name_abbr varchar(255) not null,
    cf        float        not null
);

-- 建表: 船舶类型数据
-- Date: 2024-11-19
create table db.ship_type
(
    id      int auto_increment
        primary key,
    name_cn varchar(255) not null,
    name_en varchar(255) not null,
    code    varchar(255) not null
);

