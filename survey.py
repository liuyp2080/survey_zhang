
import streamlit as st
from deta import Deta
import pandas as pd     
import plotly.express as px
import streamlit_survey as ss
import json
from streamlit_option_menu import option_menu
# sidebar for navigation
with st.sidebar:
    #logo
    st.image('logo.png', use_column_width='auto')
    
    selected = option_menu('目录',

                           ['研究内容',
                            '调查问卷'
                            ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=1)
    st.header('研究团队')
    '''
    姓名：张三      性别：男  
    年龄：37岁      籍贯：江苏徐州
    毕业院校：徐州医科大学  
    学    历：博士研究生
    政治面貌：中共党员

    '''
    st.header('联系方式')


if selected=='研究内容':
    st.title('⚕️研究内容')
    st.header('一、研究背景')
    '胃癌术后低体重是术后并发症及长期预后的重要危险因素，研究进一步分析发现在体重下降过程中，瘦肉组织群的丢失是重要的预后因素，因此阻击胃癌术后瘦肉组织群丢失是改善胃癌患者预后的重要治疗措施。我们基于自主开发的机体组成自动化检测软件，通过患者CT图像多时空的追踪患者机体机组成改变，其中包含骨骼肌群、内脏、皮下脂肪群，通过定量分析，指导术后营养支持策略调整。本研究中我们给予胃癌患者术后长期ONS进行补充能量，降低患者术后摄入不足对全身营养状态的影响，同时供给益生菌改善优化肠道菌群，通过肠道菌群及其代谢产物与骨骼肌群间的互相对话，改善骨骼肌质量（前期研究已证实优化肠道菌群可以改善骨骼肌质量）。基于上述的科研思路，我们设计如下临床随机对照研究，进一步从临床层面上观察长程ONS联合益生菌是否可以改善术后骨骼肌丢失。'
    '--------'         

    st.header('二、研究目的')
    '1. 主要目的：基于机体组成变化探究长程ONS联合益生菌干预对老年III期胃癌患者行全胃切除术后骨骼肌流失的影响。'
    '2. 次要目的：探究长程ONS联合益生菌干预对老年III期胃癌患者行全胃切除术后骨骼肌流失影响的可能作用机制及患者的生存预后和营养状况。'
    st.header('三、研究设计类型、原则与试验步骤')
    '1. 研究设计'
    '本研究是多中心、平行、开放、优效的随机对照临床研究，预计5家医院参与本研究。针对主要终点指标，采用log-rank检验，按照双侧显著性水平α和检验效能1-β，采用PASS15.0软件对本试验所需的样本量进行估算，并且考虑5%左右的脱落率，最终预计纳入696例老年Ⅲ期胃癌行全胃切除术的患者。每个中心采用竞争入组的方式纳入患者，采用分层区组随机化的方法将纳入的患者按1：1：1随机分为长程ONS联合益生菌组、长程ONS组和常规饮食组，每组为232人。'
    '2. 研究步骤'
    '入选标准：年龄≥60岁，男女不限；胃癌根治术（III期，全胃切除）；出院时ECOG体力活动评分0-2分；出院时NRS 2002 ≥ 3分；自愿参加临床研究，签署知情同意书。'
    '排除标准：无法口服；无法行根治术或残胃癌或皮革胃；运动系统疾病患者无法完成握力测量和5次起坐试验；存在认知功能障碍，无法完成相关问卷调查填写；3周内服用过益生菌制剂或抗生素。'
    '终止研究标准：患者出现死亡、肿瘤复发等无法进行研究时，终止研究。'
    '治疗方案：'
    'ONS联合益生菌组: 随机后口服肠内营养补充剂安素，（150g/d）+益生菌（双歧杆菌三联活菌胶囊 厂家：上海上药信谊药厂，国药准字S10950032，0.63g/次,2次/天）3个月'
    'ONS组：随机后口服肠内营养补充剂安素，（150g/d）3个月'
    '''
    常规饮食组：按照临床实践进食
    随机分配
    按各临床试验中心、劳伦分型以及TNM分期进行分层，在层内用大棒设计（BSD）随机化分配方法，事先进行随机序列生成，进行中央随机化竞争入组的分配操作，实现三组1:1:1分配的随机化。研究者则根据指定的组别对受试者进行规定的营养治疗。
    胃癌患者术后出院时收集下述患者临床资料，包括：（1）人口学特征与疾病资料：性别、年龄、BMI、ASA评分、ECOG评分、查尔森合并症数（CCI）、吸烟、饮酒情况；（2）营养学指标：血清白蛋白、血清前白蛋白、血清血红蛋白、NRS 2002评分；（3）肌少症相关指标：握力、CT第三腰椎平面骨骼肌指数。（4）手术及病理相关资料：手术方式、TNM分期。（5）EORTC QLQ-C30 (version 3)生活质量评分量表。
    ONS联合益生菌组和ONS组
    ONS联合益生菌组：随机分配至该组的患者除了正常饮食和接受饮食建议外，还需口服营养补充剂安素，（150g/d ）+双歧杆菌三联活菌胶囊，（0.63g/次, 2次/天），每日按照最低目标量喂养：热卡25-30kcal/kg，蛋白质：1.0-1.5g/kg，一共干预3个月。
    ONS组：
    随机分配至该组的患者除了正常饮食和接受饮食建议外，还需口服营养补充剂安素，（150g/d ），余同上。
    对照组--常规饮食组
    随机分配至对照组的患者按照参与单位的临床实践决定患者出院后的饮食方案和接受饮食建议，每日按照最低目标量喂养：热卡25-30kcal/kg，蛋白质：1.0-1.5g/kg，一共3个月。当患者体重持续下降，主治医师认为需要营养支持时可口服营养补充剂治疗。
    '''
    st.header('四、观察项目与检测时点')
    '''
    主要观察指标
（1）术前1周内病人的SMI、VAT、SATI；
（2）术后第3个月病人的SMI、VATI、SATI；
（3）第3个月肌少症的发生率。
    次要观察指标
（1）术前1周内和术后第1、2、3个月白蛋白、前白蛋白、IL-2、IL-6、INF-α、IL-10的值；
（2）出院后2年总体生存率；
（3）出院后3、6个月再入院率；
（4）出院后3、6、12个月生活质量；
'''
    st.header('五、预期价值：本课题理论创新程度及实际应用价值')
    '''
1、理论创新程度
研究视角的创新：该课题将机体组成变化、长程ONS（口服营养补充剂）以及益生菌干预三个元素相结合，针对老年III期胃癌全胃切除术后患者这一特定人群，探讨其对骨骼肌流失的影响。这种跨学科的整合视角在胃癌术后康复领域是较为新颖的。
研究方法的创新：通过监测机体组成变化，尤其是骨骼肌流失的情况，能够更直观地评估长程ONS联合益生菌干预的效果。这种定量评估方法相较于传统的临床评估更为精确和客观。
理论模型的创新：课题可能提出或验证一个新的理论模型，即长程ONS联合益生菌干预能够改善老年胃癌术后患者的营养状态，进而减少骨骼肌流失，促进康复。
2、实际应用价值
指导临床实践：课题的研究成果可以为临床医生在胃癌术后康复期患者的营养干预和管理提供理论依据和实践指导。
改善患者预后：通过减少骨骼肌流失，改善患者的营养状态，有助于提高患者的生活质量，降低并发症发生率，改善患者的预后。
优化治疗方案：根据课题研究结果，医生可以针对不同患者的具体情况，制定个性化的营养干预方案，提高治疗的针对性和有效性。

             '''
             
if selected=='调查问卷':
# Data to be written to Deta Base
    st.title('⚕️调查问卷📋')
    st.write('''
            填写注意事项：\n
            ID是患者的唯一标识，同一患者请保证相同的ID号，多次随访请填写相同的ID。
            ''')


    '***'  
    #首先建立一个问卷调查的界面
    survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
    #构建页面
    pages = survey.pages(3, on_submit=lambda: st.success("  "))
    with pages:
        if pages.current == 0:#第一页，患者基本信息
            
            st.subheader("1.患者的基本信息")#问题1
            
            survey.number_input("识别号（ID）", min_value=0, max_value=1000,value=0,id="id")
            
            survey.selectbox("患者的治疗方案？",options=["常规饮食组", "ONS组",'ONS联合益生菌组'],id="treatment")
            
            survey.slider("患者的年龄?",min_value=0, max_value=100,step=1,  id="age")
            
            survey.radio("患者的性别",options=["男", "女"],id="gender",horizontal=True)
            
            survey.slider('患者的身高(cm)',min_value=0, max_value=200,step=1, id="height")
            
            survey.slider('患者的体重(kg)',min_value=0, max_value=200,step=1, id="weight")
            
        
        elif pages.current == 1:#第二页，患者术前和术中信息
            st.subheader("2.患者的术前和术中信息")
            
            survey.radio('手术类型？',options=["全胃切除","非全胃切除"],id="operation_type",horizontal=True)
            
            survey.slider('ASA评分？',min_value=0, max_value=10,step=1,id="asa")
            
            survey.slider('ECOG评分？',min_value=0, max_value=10,step=1,id="ecog")
            
            survey.slider('查尔森合并症数？',min_value=0, max_value=100,step=1, id="cci")
            
            survey.slider('是否吸烟？',min_value=0, max_value=100,step=1,  id="smoking")
            
            survey.radio('是否饮酒？',options=["Yes","No"],id="alcohol",horizontal=True)
            
            survey.radio('TNM分期？',options=["I期","II期",'III期',"IV期"],id="tnm_stage",horizontal=True)
            
            survey.slider('术前生活质量评分？',min_value=0, max_value=10,step=1,id="pre_life_quality")
            
            survey.slider('术前握力？',min_value=0, max_value=10,step=1,id="pre_hand_strength")
            
            survey.slider('术前骨骼肌指数？',min_value=0, max_value=100,step=1,id="pre_smi")
            
            survey.slider('术前皮下脂肪指数？',min_value=0, max_value=100,step=1,id="pre_sati")
            
            survey.slider('术前内脏脂肪指数？',min_value=0, max_value=100,step=1,id="pre_vati")
            
            survey.dateinput('出院日期',id="discharge_date")
            
            
        if pages.current == 2:#第三页，患者随访信息
            
            st.subheader('3.患者随访信息')
            survey.dateinput('随访日期',id="follow_up_timepoint")

            survey.radio('随访时间',options=[3,6,12],id="follow_up_time",horizontal=True)
            
            survey.slider('随访骨骼肌指数？',min_value=0, max_value=100,step=1, id="post_smi")
            
            survey.slider('随访皮下脂肪指数？',min_value=0, max_value=100,step=1, id="post_sati")
            
            survey.slider('随访内脏脂肪指数？',min_value=0, max_value=100,step=1, id="post_vati")
            
            survey.slider('随访生活质量评分？',min_value=0, max_value=100,step=1,id="post_life_quality")
            
            survey.radio('是否发生死亡',options=["Yes","No"],id="death",horizontal=True)
            
            
    '***'       
    st.subheader("数据预览:")        
    data=survey.to_json()# string形式
    #string to json
    data=json.loads(data)
    st.table(data)

    submit=st.button("提交",type="primary",use_container_width=True)
    '*请再次检查数据，确认数据正确无误！'

    #josn to dataframe

    data_df=pd.DataFrame(data)
    data_df_value=data_df[data_df.index=='value']
    data_dict=data_df_value.to_dict(orient='index')
    submit_value=data_dict['value']
    # st.write(submit_value)

    # Connect to Deta Base with your Data Key
    deta = Deta(st.secrets["data_key"])# data_key was stored in secret.toml file 

    # Create a new database "example-db"
    # If you need a new database, just use another name.
    db = deta.Base("survey_zhang")#my database
    if submit:
        st.balloons()   
        db.put(submit_value)

    "***"
    with st.container():
        st.subheader("数据展示:")
        # This reads all items from the database and displays them to your app.
        # db_content is a list of dictionaries. You can do everything you want with it.
        db_content = db.fetch().items
        df_plot=st.dataframe(db_content)
    #bubble chart
    #creat dataframe for json data
    df_plot=pd.DataFrame(db_content)
    interested_var = st.selectbox("choose variable", df_plot.columns)

    var_count_plot = df_plot[interested_var].value_counts().rename_axis(interested_var).reset_index(name='count')

    '***'   
    with st.container():
        st.write("Showing data with interested variable:", interested_var)
        col1, col2 = st.columns(2)
        with col2:
            st.write(var_count_plot) 
        
        with col1:
            fig = px.pie(var_count_plot, values='count', names=f'{interested_var}', title=f'{interested_var} Count')
            st.plotly_chart(fig)
        
        fig_density = px.density_contour(df_plot, x=f'{interested_var}',title=f'{interested_var} Density')
        st.plotly_chart(fig_density)
