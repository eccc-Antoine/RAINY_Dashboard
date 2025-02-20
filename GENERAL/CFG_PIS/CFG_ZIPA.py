name='Wild rice'

type='1D'

dct_var={'VAR1':'Suitable habitat', 'VAR2':'Competition with cattail', 'VAR3':'Net habitat'}

#'normal' means higher is better
var_direction={'Suitable habitat':'normal', 'Competition with cattail': 'inverse', 'Net habitat':'normal'}


# need to be 'mean' or 'sum', values need to be a list even if there is only one item
var_agg_stat={'VAR1':['sum'], 'VAR2':['sum'], 'VAR3':['sum']}

units='ha'

multiplier=1

available_years_hist=list(range(1977, 2025))
available_years_future=list(range(2011, 2071))
divided_by_country=False

available_sections=['NAMAKAN', 'RAINY']

sect_dct={'Namakan Lake':['NAMAKAN'],
           'Rainy River':['RAINY']}

# available_plans=['OBS', 'Bv7_2014', 'Bv7_2014_ComboC', 'GERBL2_2014BOC_RCP45', 'GERBL2_2014_STO_330', 'GERBL2_2014_ComboC_RCP45', 'GERBL2_2014_ComboC_STO_330']
#
# plans_ts_dct={'hist':['OBS', 'Bv7_2014', 'Bv7_2014_ComboC'], 'sto':['GERBL2_2014_STO_330', 'GERBL2_2014_ComboC_STO_330'], 'cc':['GERBL2_2014BOC_RCP45','GERBL2_2014_ComboC_RCP45']}
#
# plans_hist=['PreProjectHistorical', 'OBS', 'Bv7_2014', 'Bv7_2014_ComboC']
#
# plan_dct={'PreProjectHistorical':'PreProjectHistorical', 'OBS':'OBS', 'Bv7_2014':'Bv7_2014', 'Bv7_2014_ComboC':'Bv7_2014_ComboC', 'GERBL2_2014BOC_RCP45':'GERBL2_2014BOC_RCP45', 'PreProject_RCP45':'PreProject_RCP45', 'GERBL2_2014_STO_330':'GERBL2_2014_STO_330', 'PreProject_STO_330': 'PreProject_STO_330', 'GERBL2_2014_ComboC_RCP45':'GERBL2_2014_ComboC_RCP45', 'GERBL2_2014_ComboC_STO_330':'GERBL2_2014_ComboC_STO_330'}
#
# available_baselines=['PreProjectHistorical', 'Bv7_2014', 'GERBL2_2014BOC_RCP45', 'GERBL2_2014_STO_330', 'PreProject_RCP45', 'PreProject_STO_330']
#
# baseline_dct={'PreProjectHistorical':'PreProjectHistorical' , 'Bv7_2014':'Bv7_2014', 'GERBL2_2014BOC_RCP45':'GERBL2_2014BOC_RCP45', 'GERBL2_2014_STO_330':'GERBL2_2014_STO_330', 'PreProject_RCP45':'PreProject_RCP45', 'PreProject_STO_330':'PreProject_STO_330'}
#
# baseline_ts_dct={'hist':['PreProjectHistorical', 'Bv7_2014'], 'sto':['GERBL2_2014_STO_330', 'PreProject_STO_330'], 'cc':['GERBL2_2014BOC_RCP45', 'PreProject_RCP45']}

available_plans=['RC1970', 'RC2000', 'RC2018', 'StateOfNature']

plans_ts_dct={'hist':['RC1970', 'RC2000', 'RC2018', 'StateOfNature']}

plans_hist=['RC1970', 'RC2000', 'RC2018', 'StateOfNature']

plan_dct={'RC1970':'RC1970', 'RC2000':'RC2000', 'RC2018':'RC2018', 'StateOfNature':'StateOfNature'}


available_baselines=['RC1970', 'RC2000', 'RC2018', 'StateOfNature']

baseline_dct={'RC1970':'RC1970', 'RC2000':'RC2000', 'RC2018':'RC2018', 'StateOfNature':'StateOfNature'}

baseline_ts_dct={'hist':['RC1970', 'RC2000', 'RC2018', 'StateOfNature']}

available_stats = ['sum', 'mean']

#id_column_name = 'PT_ID'

