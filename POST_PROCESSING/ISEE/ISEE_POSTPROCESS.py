import os
import pandas as pd
import importlib
import CFG_POST_PROCESS_ISEE as cfg

                
class POST_PROCESS_1D:

    def __init__(self, pis,ISEE_RES, POST_PROCESS_RES, sep):

        self.pis=pis
        self.ISEE_RES=ISEE_RES
        self.POST_PROCESS_RES=POST_PROCESS_RES
        self.sep=sep
           
    def agg_YEAR(self, folder_space):  
        liste_files=[]
        for root, dirs, files in os.walk(folder_space):
            for name in files:
                liste_files.append(os.path.join(root, name))
        df_year=pd.DataFrame()
        print(folder_space, liste_files)
        liste_df=[]
        if len(liste_files) != 0:
            exists=True
            for feather in liste_files:
                if feather.split('.')[-1]==cfg.extension[1:]:
                    df_temp=pd.read_csv(feather, sep=';')
                    liste_df.append(df_temp)
            df_year = pd.concat(liste_df, ignore_index=True)
        else:
            df_year=0
            exists = False
        return df_year, exists
    
    def AGG_SPACE_YEAR(self, path_res, res_name, columns, AGG_TIME, AGG_SPACE, PI, space, list_var, stats, agg_year_param, path_feather_year, PI_CFG, years_list):
        dct_df_space=dict.fromkeys(tuple(columns),[])
        df_space=pd.DataFrame(dct_df_space)
        df_space[AGG_TIME]=years_list
        if not os.path.exists(path_res):
            os.makedirs(path_res)
        if AGG_SPACE == 'PLAN':               
            df_year, exists=self.agg_YEAR(agg_year_param)
            if exists:
                for stat in stats:
                    if stat=='sum':
                        df_space_sum=df_year.groupby(['YEAR'], as_index=False).sum()
                    elif stat=='mean':
                        df_space_mean=df_year.groupby(['YEAR'], as_index=False).mean()

                if len(stats)>1:
                    df_space=df_space_sum.merge(df_space_mean, on=['YEAR'], suffixes=('_sum', '_mean'), validate='one_to_one')
                elif stats[0]=='sum':
                    df_space=df_space_sum
                elif stats[0]=='mean':
                    df_space=df_space_mean
                else:
                    print('STAT value provided is unavailable')

                       
        elif AGG_SPACE == 'SECTION':
            df_space, exists=self.agg_YEAR(agg_year_param)

            if exists:
                columns=['YEAR']
                for var in list_var:
                    stats=PI_CFG.var_agg_stat[var]
                    for stat in stats:
                        var_stat=var+f'_{stat}'
                        df_space[var_stat]=df_space[var]
                        columns.append(var_stat)
                df_space=df_space[columns]

        if exists:
            df_space=df_space.reset_index()
            df_space.to_csv(os.path.join(path_res, res_name), sep=';')

    def agg_1D_space(self, PI, AGGS_TIME, AGGS_SPACE):
        '''
        PI = PI accronym (ex. Northern Pike = ESLU_2D)
        VAR = VAR1, VAR2 ... VARx which corresponds to VAR names in PI's metadata 
        AGGS_TIME = level of aggregation over time : list of values amongst ['YEAR', 'QM'] QM not available yet
        AGGS_SPACE = level of aggregation over space : list of values amongst [ 'PLAN', 'SECTION']
        stats = stat for aggregated values ['sum'], ['mean'] or ['sum', 'mean'] 
        '''
        
        pi_module_name=f'CFG_{PI}'
        PI_CFG=importlib.import_module(f'GENERAL.CFG_PIS.{pi_module_name}')
        
        for AGG_TIME in AGGS_TIME:
            for AGG_SPACE in AGGS_SPACE:  
                print(AGG_SPACE)
                list_var=list(PI_CFG.dct_var.keys())
                columns=[AGG_TIME]
                for var in list_var:
                    stats=PI_CFG.var_agg_stat[var]
                    for s in stats:
                        stat=var+'_'+s
                        columns.append(stat)
                        
                if AGG_TIME=='YEAR':
                    if AGG_SPACE=='PLAN':
                        for space in PI_CFG.available_plans+PI_CFG.available_baselines:

                            if space in PI_CFG.plans_hist:
                                years_list = PI_CFG.available_years_hist
                            else:
                                years_list = PI_CFG.available_years_future

                            print(space)
                            path_res=os.path.join(self.POST_PROCESS_RES, PI, AGG_TIME, AGG_SPACE, space)
                            print(path_res)

                            if os.path.exists(path_res):
                                print(
                                    f'AGG level of {AGG_SPACE} for plan {space} already exists skipping...')
                                continue

                            res_name=f'{PI}_{AGG_TIME}_{space}_{min(years_list)}_{max(years_list)}.csv'
                            agg_year_param=os.path.join(self.ISEE_RES, PI, space)
                            print(agg_year_param)
                            self.AGG_SPACE_YEAR(path_res, res_name, columns, AGG_TIME, AGG_SPACE, PI, space, list_var, stats, agg_year_param ,'', PI_CFG, years_list)
                              
                    elif AGG_SPACE=='SECTION':
                        for p in PI_CFG.available_plans+PI_CFG.available_baselines:

                            if p in PI_CFG.plans_hist:
                                years_list = PI_CFG.available_years_hist
                            else:
                                years_list = PI_CFG.available_years_future

                            for space in PI_CFG.available_sections:
                                print(p, space)
                                path_res=os.path.join(self.POST_PROCESS_RES, PI, AGG_TIME, AGG_SPACE, p, space)

                                if os.path.exists(path_res):
                                    print(
                                        f'AGG level of {AGG_SPACE} for plan {p} in section {space} already exists skipping...')
                                    continue

                                res_name=f'{PI}_{AGG_TIME}_{p}_{space}_{min(years_list)}_{max(years_list)}.csv'
                                agg_year_param=os.path.join(self.ISEE_RES, PI, p, space)
                                self.AGG_SPACE_YEAR(path_res, res_name, columns, AGG_TIME, AGG_SPACE, PI, space, list_var, stats, agg_year_param, '', PI_CFG, years_list)

                    else:
                        print(f'input AGG_SPACE {AGG_SPACE} is not valid !!')
                        quit()
                        
                elif AGG_TIME=='QM':
                    ### NOT coded yet!!
                    pass
                            
                else:
                    pass


# tiled=POST_PROCESS_2D_tiled(cfg.pis_2D_tiled, cfg.ISEE_RES, cfg.POST_PROCESS_RES, cfg.sep)
#
# not_tiled=POST_PROCESS_2D_not_tiled(cfg.pis_2D_not_tiled, cfg.ISEE_RES, cfg.POST_PROCESS_RES, cfg.sep)
 
pi_1D=POST_PROCESS_1D(cfg.pis_1D, cfg.ISEE_RES, cfg.POST_PROCESS_RES, cfg.sep)

# for pi in tiled.pis:
#     print(pi)
#     tiled.agg_2D_space(pi, ['YEAR'], ['PLAN', 'SECTION', 'TILE', 'PT_ID'])
#     #tiled.agg_2D_space(pi, ['YEAR'], ['PLAN'])
#     #tiled.agg_2D_space(pi, ['YEAR'], ['PT_ID'])

# for pi in not_tiled.pis:
#     print(pi)
#     not_tiled.agg_2D_space(pi, ['YEAR'], ['PLAN', 'SECTION', 'TILE', 'PT_ID'])
#     #not_tiled.agg_2D_space(pi, ['YEAR'], ['TILE', 'PT_ID'])

for pi in pi_1D.pis:
    print(pi)
    pi_1D.agg_1D_space(pi, ['YEAR'], ['PLAN', 'SECTION'])
             
quit()


               
