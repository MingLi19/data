-- 建表: 设备燃油数据
-- Date: 2024-12-11
create table equipment_fuel
(
    id           int auto_increment,
    equipment_id int not null comment '设备ID',
    fuel_type_id int not null comment '燃油类型ID',

    PRIMARY KEY (id),
    FOREIGN KEY (equipment_id) REFERENCES equipment (id),
    FOREIGN KEY (fuel_type_id) REFERENCES fuel_type (id)
);