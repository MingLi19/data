-- 建表: 船舶设备数据
-- Date: 2024-12-11
create table equipment
(
    id         int auto_increment,
    name       varchar(255) not null comment '设备名称',
    type       varchar(255) not null comment '设备类型',
    vessel_id  int          not null comment '所属船舶',
    created_at datetime     null default CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
    FOREIGN KEY (vessel_id) REFERENCES vessel (id)
);