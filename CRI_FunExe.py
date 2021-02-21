# This Module contains the function execution calls

import CRI_Functions


def CRI_call(Own_Ship_v, Trg_Ship_v, Own_Ship_Xpos, Own_Ship_Ypos, Trg_Ship_Xpos, Trg_Ship_Ypos, Own_Ship_ang,
             Trg_Ship_ang):
    ###################################################################################################
    #                             C R I    F U N C T I O N S
    ###################################################################################################

    # function test 1 - Intermidiate para

    Inter = CRI_Functions.Inter_Para(Own_Ship_v, Trg_Ship_v, Own_Ship_Xpos, Own_Ship_Ypos, Trg_Ship_Xpos, Trg_Ship_Ypos,
                                     Own_Ship_ang, Trg_Ship_ang)
    Vox = Inter[0]
    Voy = Inter[1]
    Vtx = Inter[2]
    Vty = Inter[3]
    Vx = Inter[4]
    Vy = Inter[5]
    Xot = Inter[6]
    Yot = Inter[7]
    #print('---------------------------------------------')
    #print('The intermediate parameters are : ')
    #print('Vox  is : ', Vox)
    #print('Voy  is : ', Voy)
    #print('Vtx  is : ', Vtx)
    #print('Vty  is : ', Vty)
    #print('Vx is : ', Vx)
    #print('Vy is : ', Vy)
    #print('Xot is : ', Xot)
    #print('Yot is : ', Yot)
    #print('---------------------------------------------')
    ###################################################################################################

    # function test 2 - Relative Speed

    VTO = CRI_Functions.relative_Velo(Own_Ship_v, Trg_Ship_v, Own_Ship_ang, Trg_Ship_ang)

    #print('---------------------------------------------')
    #print('The Relative Speed of the Target Ship w.r.t Own Ship is : ', VTO)
    #print('---------------------------------------------')
    ###################################################################################################
    # function test 3 - The Relative course and True course

    RC_TC = CRI_Functions.relative_Cor_TarS(Vx, Vy, Xot, Xot)
    Rc = RC_TC[0]
    Tc = RC_TC[1]
    #print('---------------------------------------------')
    #print('The Relative Course - Theta OT: ', Rc)
    #print('The True Course - Theta Real: ', Tc)
    #print('---------------------------------------------')

    ###################################################################################################

    # function test 4 - Relative Motion Parameters : DCPA TCPA and Alpha OT

    DTA = CRI_Functions.Relat_Motion_para(Own_Ship_Xpos, Own_Ship_Ypos, Trg_Ship_Xpos, Trg_Ship_Ypos, Own_Ship_ang, Rc,
                                          Tc, VTO)

    DCPA = DTA[0]
    TCPA = DTA[1]
    AlphaOT = DTA[2]
    D_btwnS = DTA[3]

    #print('---------------------------------------------')
    #print('DCPA : ', DCPA)
    #print('TCPA : ', TCPA)
    #print('Alpha OT : ', AlphaOT)
    #print('Distance Between the Ships - D : ', D_btwnS)
    #print('---------------------------------------------')

    ###################################################################################################

    # function test 5 - d1 and d2
    # For this we need to fix a K avale between 1.5 and 2.0, for this case we fixed K =2.0

    k = 2
    d1_d2 = CRI_Functions.d1_and_d2(AlphaOT, k)
    d1 = d1_d2[0]
    d2 = d1_d2[1]
    #print('---------------------------------------------')
    #print('The d1 value is : ', d1)
    #print('The d2 value is : ', d2)
    #print('---------------------------------------------')

    ###################################################################################################
    # Function test 6 - D1 D2 and t1 t2
    L = 100  # Length of the giveway ship

    dts = CRI_Functions.D1_D2_t1_t2(DCPA, L, VTO, AlphaOT)
    D1_value = dts[0]
    D2_value = dts[1]
    t1_value = dts[2]
    t2_value = dts[3]
    #print('---------------------------------------------')
    #print('The D1 value is : ', D1_value)
    #print('The D2 value is : ', D2_value)
    #print('The t1 value is : ', t1_value)
    #print('The t2 value is : ', t2_value)
    #print('---------------------------------------------')

    ###################################################################################################
    #                 M E M B E R S H I P     F U N C T I O N S
    ###################################################################################################

    # Function test for MF TCPA

    MF_TC = CRI_Functions.MF_TCPA(TCPA, t1_value, t2_value)
    print('---------------------------------------------')
    print('The Membership Function for TCPA is : ', MF_TC)

    # Function test for MF Relative Distance

    MF_RD = CRI_Functions.MF_Rel_dis(D1_value, D2_value, D_btwnS)
    #print('---------------------------------------------')
    #print('The Membership Function for relative distance : ', MF_RD)

    MF_B = CRI_Functions.MF_realtive_bearing(AlphaOT)
    #print('---------------------------------------------')
    #print('The Membership Function for relative bearing is : ', MF_B)

    MF_DCPAz = CRI_Functions.MF_DCPA(DCPA, d1, d2)
    print('---------------------------------------------')
    print('The Membership Function for DCPA is : ', MF_DCPAz)

    MF_Kz = CRI_Functions.MF_K(k, Trg_Ship_ang, Own_Ship_ang)
    #print('---------------------------------------------')
    #print('The Membership Function for K is : ', MF_Kz)

    CRI_Index = CRI_Functions.CRI_F(MF_DCPAz, MF_TC, MF_RD, MF_B, MF_Kz)
    # print('---------------------------------------------')
    # print('The CRI Index is : ', CRI_Index )

    return CRI_Index

