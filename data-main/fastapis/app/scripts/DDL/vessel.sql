-- 建表: 船舶数据
-- Date: 2024-12-11
create table vessel
(
    id                    int auto_increment,
    name                  varchar(255) not null comment '船名',
    mmsi                  varchar(255) not null comment '海事识别号',
    build_date            date         not null comment '建造日期',
    gross_tone            float        not null comment '总吨位',
    dead_weight           float        not null comment '装载吨位',
    new_vessel            tinyint(1)   not null comment '是否新船',
    hull_clean_date       date         null comment '船体清洁日期',
    engine_overhaul_date  date         null comment '发动机检修日期',
    newly_paint_date      date         null comment '新涂装日期',
    propeller_polish_date date         null comment '螺旋桨抛光日期',
    company_id            int          not null comment '公司ID',
    ship_type             int          not null comment '船舶类型',
    time_zone             int          not null comment '时区',
    created_at            datetime     not null default CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);