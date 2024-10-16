DROP TABLE IF EXISTS ui_demo;
DROP TABLE IF EXISTS ui_cts;
DROP TABLE IF EXISTS unemp;

CREATE TABLE ui_demos (
    st varchar(2) NOT NULL,
    dt_m int NOT NULL,
    dt_y int NOT NULL,
    gen_mal int,
    gen_fem int,
    gen_na int,
    eth_hisp int,
    eth_no_hisp int,
    eth_na int,
    rac_native int,
    rac_asian int,
    rac_black int,
    rac_pac int,
    rac_white int,
    age_lt_22 int,
    age_22_24 int,
    age_25_34 int,
    age_35_44 int,
    age_45_54 int,
    age_55_59 int,
    age_60_64 int,
    age_gte_65 int,
    age_na int,
    PRIMARY KEY (st, dt_m, dt_y)
);

CREATE TABLE ui_cts (
    st varchar(2) NOT NULL,
    dt_m int NOT NULL,
    dt_y int NOT NULL,
    wk_num Int,
    ct_ic Int,
    ct_fic Int,
    ct_xic Int,
    ct_wks Int,
    ct_wks_f Int,
    ct_wks_x Int,
    ct_wks_eb Int,
    rt_recip real,
    rt_emp_cv real,
    rt_unemp real,
    ind_eb varchar(1),
    dt_eb date,
    PRIMARY KEY (st, dt_m, dt_y)
);

CREATE TABLE unemp (
    st varchar(2) NOT NULL,
    dt_m int NOT NULL,
    dt_y int NOT NULL,
    ct_u3 int, 
    ct_u6 int,
    ct_lf_u3 int, 
    ct_lf_u6 int,
    PRIMARY KEY (st, dt_m, dt_y)
);
