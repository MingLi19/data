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
