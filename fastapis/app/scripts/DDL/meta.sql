-- 建表: 燃油类型数据
-- Date: 2024-12-11
create table fuel_type
(
    id        int auto_increment,
    name_cn   varchar(255) not null comment '中文名称',
    name_en   varchar(255) not null comment '英文名称',
    name_abbr varchar(255) not null comment '缩写',
    cf        float        not null comment '碳排放系数',
    PRIMARY KEY (id)
);

-- 建表: 船舶类型数据
-- Date: 2024-12-11
create table ship_type
(
    id      int auto_increment,
    name_cn varchar(255) not null comment '中文名称',
    name_en varchar(255) not null comment '英文名称',
    code    varchar(255) not null comment '代码',
    PRIMARY KEY (id)
);

-- 建表: 船舶类型数据
-- Date: 2024-12-11
create table time_zone
(
    id           int auto_increment,
    name_cn      varchar(255) not null comment '中文名称',
    name_en      varchar(255) not null comment '英文名称',
    explaination varchar(255) not null comment '说明',
    PRIMARY KEY (id)
);