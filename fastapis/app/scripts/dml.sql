-- 插入燃油类型数据
-- Date: 2024-11-12
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (1, '重燃油 (HFO) 硫含量高于0.5% m/m', 'HFO, S>0.5% m/m', 'HFO-HS', 3.114);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (2, '重燃油 (HFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m', 'HFO, 0.1% m/m<=S<=0.5% m/m', 'HFO-LS', 3.114);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (3, '重燃油 (HFO) 硫含量不高于0.1% m/m', 'HFO, S<=0.1% m/m', 'HFO-ULS', 3.114);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (4, '轻燃油 (LFO) 硫含量高于0.5% m/m', 'LFO, S>0.5% m/m', 'LFO-HS', 3.151);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (5, '轻燃油 (LFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m', 'LFO, 0.1% m/m<=S<=0.5% m/m', 'LFO-LS', 3.151);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (6, '轻燃油 (LFO) 硫含量不高于0.1% m/m', 'LFO, S<=0.1% m/m', 'LFO-ULS', 3.151);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (7, '船用柴油', 'MDO/MGO', 'MDO/MGO', 3.206);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (8, '内河船用燃料油', 'MDO/MGO for River Boat', 'MDO/MGO', 3.206);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (9, '液化石油气 (LPG) 丙烷', 'LPG-Propane', 'LPG-Propane', 3);
INSERT INTO fuel_type (id, name_cn, name_en, name_abbr, cf) VALUES (10, '液化石油气 (LPG) 丁烷', 'LPG-Butane', 'LPG-Butane', 3.03);

-- 插入船舶类型数据
-- Date: 2024-11-19
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (1, '散货船', 'Bulk carrier', 'I001');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (2, '气体运输船', 'Gas carrier', 'I002');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (3, '液货船', 'Tanker', 'I003');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (4, '集装箱船', 'Container ship', 'I004');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (5, '杂货船', 'General cargo ship', 'I005');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (6, '冷藏货船', 'Refrigerated cargo carrier', 'I006');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (7, '兼用船', 'Combination carrier', 'I007');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (8, 'LNG运输船', 'LNG carrier', 'I008');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (9, '滚装货船（车辆运输船）', 'Ro-ro cargo ship (vehicle carrier)', 'I009');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (10, '滚装货船', 'Ro-ro cargo ship', 'I010');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (11, '客滚船', 'Ro-ro passenger ship', 'I011');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (12, '客滚船(高速)', 'Ro-ro passenger ship (high-speed craft)', 'I011.1');
INSERT INTO ship_type (id, name_cn, name_en, code) VALUES (13, '豪华邮轮', 'Cruise passenger ship', 'I012');

-- 插入时区数据
-- Date: 2024-11-26
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (1, '零时区', 'UTC+0', '零时区 7.5° W～7.5° E 0°');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (2, '东一区', 'UTC+1', '东一区 7.5° E～22.5° E 15° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (3, '东二区', 'UTC+2', '东二区 22.5° E～37.5° E 30° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (4, '东三区', 'UTC+3', '东三区 37.5° E～52.5° E 45° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (5, '东四区', 'UTC+4', '东四区 52.5° E～67.5° E 60° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (6, '东五区', 'UTC+5', '东五区 67.5° E～82.5° E 75° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (7, '东六区', 'UTC+6', '东六区 82.5° E～97.5° E 90° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (8, '东七区', 'UTC+7', '东七区 97.5° E～112.5° E 105° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (9, '东八区', 'UTC+8', '东八区 112.5° E～127.5° E 120° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (10, '东九区', 'UTC+9', '东九区 127.5° E～142.5° E 135° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (11, '东十区', 'UTC+10', '东十区 142.5° E～157.5° E 150° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (12, '东十一区', 'UTC+11', '东十一区 157.5° E～172.5° E 165° E');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (13, '东十二区', 'UTC+12', '东十二区 172.5° E～180° E 180°');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (14, '西一区', 'UTC-1', '西一区 7.5° W～22.5° W 15° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (15, '西二区', 'UTC-2', '西二区 22.5° W～37.5° W 30° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (16, '西三区', 'UTC-3', '西三区 37.5° W～52.5° W 45° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (17, '西四区', 'UTC-4', '西四区 52.5° W～67.5° W 60° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (18, '西五区', 'UTC-5', '西五区 67.5° W～82.5° W 75° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (19, '西六区', 'UTC-6', '西六区 82.5° W～97.5° W 90° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (20, '西七区', 'UTC-7', '西七区 97.5° W～112.5° W 105° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (21, '西八区', 'UTC-8', '西八区 112.5° W～127.5° W 120° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (22, '西九区', 'UTC-9', '西九区 127.5° W～142.5° W 135° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (23, '西十区', 'UTC-10', '西十区 142.5° W～157.5° W 150° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (24, '西十一区', 'UTC-11', '西十一区 157.5° W～172.5° W 165° W');
INSERT INTO time_zone (id, name_cn, name_en, explaination) VALUES (25, '西十二区', 'UTC-12', '西十二区 172.5° W～180° W 180°');
