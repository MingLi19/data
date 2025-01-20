-- 建表: 用户数据
-- Date: 2024-12-11
create table user
(
    id              int auto_increment
    username        varchar(255) not null comment '用户名',
    hashed_password varchar(255) not null comment '密码',
    phone           varchar(255) not null comment '手机号',
    is_admin        tinyint(1)   not null comment '是否管理员',
    is_system_admin tinyint(1)   not null comment '是否系统管理员',
    disabled        tinyint(1)   not null comment '是否禁用',
    company_id      int          not null comment '所属公司',
    created_at      datetime     not null default CURRENT_TIMESTAMP,
    
    PRIMARY KEY (id)
);