-- 建表: 设备燃油数据
-- Date: 2024-12-04
create table equipment_fuel
(
    id           int auto_increment,
    equipment_id int not null,
    fuel_type_id int not null,
    PRIMARY KEY (id)
);