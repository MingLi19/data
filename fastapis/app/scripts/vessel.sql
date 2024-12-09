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