-- 建表: 燃油类型数据
-- Date: 2024-11-12
create table fuel_type
(
    id        int auto_increment
    name_cn   varchar(255) not null,
    name_en   varchar(255) not null,
    name_abbr varchar(255) not null,
    cf        float        not null,
    PRIMARY KEY (id)
);

-- 建表: 船舶类型数据
-- Date: 2024-11-19
create table ship_type
(
    id      int auto_increment
    name_cn varchar(255) not null,
    name_en varchar(255) not null,
    code    varchar(255) not null,
    PRIMARY KEY (id)
);

-- 建表: 船舶类型数据
-- Date: 2024-11-26
create table time_zone
(
    id           int auto_increment
    name_cn      varchar(255) not null,
    name_en      varchar(255) not null,
    explaination varchar(255) not null,
    PRIMARY KEY (id)
);

-- 建表: 公司数据
-- Date: 2024-11-26
create table company
(
    id             int auto_increment primary key,
    name           varchar(255) not null,
    contact_person varchar(255) null,
    contact_phone  varchar(255) null,
    contact_email  varchar(255) null,
    created_at     datetime     not null,
    address        varchar(255) null,
    constraint name
        unique (name)
);

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

-- 建表: 船舶数据
-- Date: 2024-11-26
create table vessel
(
    id                    int auto_increment
    name                  varchar(255) not null,
    mmsi                  varchar(255) not null,
    build_date            date         not null,
    gross_tone            float        not null,
    dead_weight           float        not null,
    new_vessel            tinyint(1)   not null,
    hull_clean_date       date         null,
    engine_overhaul_date  date         null,
    newly_paint_date      date         null,
    propeller_polish_date date         null,
    company_id            int          not null,
    created_at            datetime     not null,
    ship_type             int          not null,
    time_zone             int          not null,
    PRIMARY KEY (id),
);

-- 建表: 船舶设备数据
-- Date: 2024-11-26
create table equipment
(
    name       varchar(255) not null,
    type       varchar(255) not null,
    vessel_id  int          not null,
    id         int auto_increment
        primary key,
    created_at datetime     null,
);

-- 建表: 设备燃油数据
-- Date: 2024-11-26
create table equipment_fuel
(
    id           int auto_increment
        primary key,
    equipment_id int not null,
    fuel_type_id int not null,
    constraint equipment_fuel_ibfk_1
        foreign key (equipment_id) references equipment (id)
            on delete cascade,
    constraint equipment_fuel_ibfk_2
        foreign key (fuel_type_id) references fuel_type (id)
);

create index equipment_id
    on equipment_fuel (equipment_id);

create index fuel_type_id
    on equipment_fuel (fuel_type_id);

