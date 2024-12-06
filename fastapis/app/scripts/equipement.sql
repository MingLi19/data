-- 建表: 船舶设备数据
-- Date: 2024-12-04
create table equipment
(
    id         int auto_increment,
    name       varchar(255) not null,
    type       varchar(255) not null,
    vessel_id  int          not null,
    created_at datetime     null,
    PRIMARY KEY (id)
);