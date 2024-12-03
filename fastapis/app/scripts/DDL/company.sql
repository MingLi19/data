-- 建表: 公司数据
-- Date: 2024-12-11
create table company
(
    id             int auto_increment,
    name           varchar(255) not null comment '公司名称',
    contact_person varchar(255) null comment '联系人',
    contact_phone  varchar(255) null comment '联系电话',
    contact_email  varchar(255) null comment '联系邮箱',
    address        varchar(255) null comment '公司地址',
    created_at     datetime     not null default CURRENT_TIMESTAMP,
    
    PRIMARY KEY (id)
);
