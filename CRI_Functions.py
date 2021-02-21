#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import math
import numpy as np


############################################################################################
# Intermidiate Parameters Function

def Inter_Para(O_v, T_v, O_x, O_y, T_x, T_y, O_ang, T_ang):
    vox = round(O_v * math.sin(math.radians(O_ang)), 3)
    voy = round(O_v * math.cos(math.radians(O_ang)), 3)

    vtx = round(T_v * math.sin(math.radians(T_ang)), 3)
    vty = round(T_v * math.cos(math.radians(T_ang)), 3)

    vx = vtx - vox
    vxr = round(vx, 3)
    vy = vty - voy
    vyr = round(vy, 3)

    xot = T_x - O_x
    yot = T_y - O_y

    result_1 = (vox, voy, vtx, vty, vxr, vyr, xot, yot)
    return result_1


############################################################################################

# function Relative Speed
def relative_Velo(V_O, V_T, theta_O, theta_T):
    vo_re = V_O
    vt_re = V_T
    angO_re = theta_O
    angT_re = theta_T
    velo_ratio_re = (V_T / V_O)
    diff_angle_re = theta_O - theta_T
    cos_diff_re = math.cos(math.radians(diff_angle_re))
    velo_Ratio_sqr_re = velo_ratio_re ** 2
    inside_f_re = (1 + velo_Ratio_sqr_re - 2 * velo_ratio_re * cos_diff_re)
    Vot_re = round(vo_re * math.sqrt(inside_f_re), 3)
    return Vot_re


############################################################################################

# function The Relative course and True course
def relative_Cor_TarS(VTx, VTy, Xot, Yot):
    tyu = VTx
    tyv = VTy
    if tyv == 0:
        tyv = 0.000001
    else:
        tyv = VTy
    vx_vy_ratio = tyu / tyv
    Vr_radio_pass = (vx_vy_ratio)

    def comp_fun(vr3):
        if tyu >= 0 and tyv >= 0:
            res = math.atan(vr3)
            #print('Option 1')
            return (res)
        elif tyu < 0 and tyv < 0:
            res = math.atan(vr3) + math.pi
            #print('Option 2')
            return (res)
        elif tyu >= 0 and tyv < 0:
            res = math.atan(vr3) + math.pi
            #print('Option 3')
            return (res)
        elif tyu < 0 and tyv >= 0:
            res = math.atan(vr3) + 2 * (math.pi)
            #print('Option 4')
            return (res)

    re_theta = comp_fun(Vr_radio_pass)

    theta_OT_Deg = ((180 / (math.pi)) * re_theta)

    xyu = Xot
    yyu = Yot
    if Yot == 0:
        yyu = 0.000001
    else:
        yyu = Yot
    xot_yot_ratio = xyu / yyu
    xotratio_deg = xot_yot_ratio

    def true_fun(vr5):
        if xyu >= 0 and yyu >= 0:
            res = float(math.atan(vr5))
            #print('Option 1', res)
            return (res)
        elif xyu < 0 and yyu < 0:
            res = float(math.atan(vr5) + math.pi)
            #print('Option 2')
            return (res)
        elif xyu >= 0 and yyu < 0:
            res = float(math.atan(vr5) + math.pi)
            #print('Option 3')
            return (res)
        elif xyu < 0 and yyu >= 0:
            res = float(math.atan(vr5) + 2 * (math.pi))
            #print('Option 4')
            return (res)

    real_theta = true_fun(xotratio_deg)
    theta_Real_Deg = float(((180 / (math.pi)) * real_theta))
    result_2 = (theta_OT_Deg, theta_Real_Deg)
    return result_2


############################################################################################

# Relative Motion Parameters
def Relat_Motion_para(Xo, Yo, Xt, Yt, theta_o, theta_ot, theta_real, Vott):
    xd1 = Xo
    yd1 = Yo
    xd2 = Xt
    yd2 = Yt
    Vot_re = Vott
    if Vot_re == 0:
        Vot_re = 0.00001
    else:
        Vot_re = Vott
    DO = theta_o
    theta_OT_Deg = theta_ot
    theta_Real_Deg = theta_real
    D_Btwn = math.sqrt(((xd2 - xd1) ** 2) + ((yd2 - yd1) ** 2))

    # DCPA and TCPA Calculations
    ang_D = math.sin(math.radians(theta_OT_Deg - theta_Real_Deg - 180))
    DCPA_1 = D_Btwn * ang_D
    DCPA_rnd = round(DCPA_1, 3)
    top_fun = math.cos(math.radians(theta_OT_Deg - theta_Real_Deg - 180))
    TCPA_1 = ((D_Btwn * top_fun) / Vot_re)
    TCPA_rnd = round(TCPA_1, 3)
    #print('alpha t : ', theta_Real_Deg)
    #print('Theat 0 : ', DO)
    if (theta_Real_Deg > 360):
        theta_Real_Deg = theta_Real_Deg -360
    else:
        pass
    alpha_OT = round((theta_Real_Deg - DO + 360), 3)
    result_3 = (DCPA_rnd, TCPA_rnd, alpha_OT, D_Btwn)
    return result_3


############################################################################################

# Calculation of d1 and d2
def d1_and_d2(alphaot, k):
    if alphaot > 360:
        aph_ot_d1 = alphaot - 360
    else:
        aph_ot_d1 = alphaot
    #print('aph_ot_d1 : ', aph_ot_d1)

    def d1_cal(alp_3):
        if alp_3 >= 0 and alp_3 < 112.5:
            res_d = (1.1 - ((0.2 * alp_3) / 180))
            #print("Here the value of Alpha OT is ", alp_3, " which lies between 0 and 112.5")
            return (res_d)
        elif alp_3 >= 112.5 and alp_3 < 180:
            res_d = (1 - ((0.4 * alp_3) / 180))
            #print("Here the value of Alpha OT is ", alp_3, " which lies between 112.5 and 180")
            return (res_d)
        elif alp_3 >= 180 and alp_3 < 247.5:
            res_d = (1 - ((0.4 * (360 - alp_3)) / 180))
            #print("Here the value of Alpha OT is ", alp_3, " which lies between 180 and 247.5")
            return (res_d)
        elif alp_3 >= 247.5 and alp_3 <= 360:
            res_d = (1.1 - ((0.2 * (360 - alp_3)) / 180))
            #print("Here the value of Alpha OT is ", alp_3, " which lies between 247.5 and 360")
            return (res_d)

    d1_u = round((d1_cal(aph_ot_d1)), 3)
    #print('d1 = ', d1_u)
    K_u = k
    d2_u = round((K_u * d1_u), 3)
    result_4 = (d1_u, d2_u)
    return result_4


############################################################################################

# Calculation of D1 D2 and t1 t2
def D1_D2_t1_t2(DC, GwSl, Votx, alphaOTx):
    dtz1 = DC
    dtz2 = DC
    vzot = Votx
    if vzot == 0:
        vzot = 0.00001
    else:
        vzot = Votx
    Lgws = GwSl
    lgws_NM = 0.000539957 * Lgws  # The length of the ship is converted to NM
    d2t_alph = alphaOTx
    d1_value = round((14 * lgws_NM), 3)
    d1_in_Meter = 14 * Lgws
    # Relative distance function
    # D2 Calculation
    angle_inside_cos = d2t_alph - 19
    inside_pt1 = 1.7 * math.cos(math.radians(angle_inside_cos))
    inside_root_prt = 4.4 + (2.89 * math.cos(math.radians(angle_inside_cos)) ** 2)
    inside_pt2 = math.sqrt(inside_root_prt)
    d2t_l = round((inside_pt1 + inside_pt2), 3)
    dz1 = d1_value
    dz2 = d2t_l
    if dz1 >= dtz1:
        fun_inside_rootz = abs((dz1) ** 2 - (dtz1) ** 2)
        t1zz = round(((math.sqrt(fun_inside_rootz)) / vzot), 3)
    else:
        fun_ontop = abs(((dz1 - dtz1)))
        t1zz = round(((fun_ontop) / vzot), 3)
    if dz2 >= dtz1:
        fun_inside_rootz = abs(((dz2) ** 2 - (dtz2) ** 2))
        t2zz = round(((math.sqrt(fun_inside_rootz)) / vzot), 3)
    else:
        fun_ontop = abs(((dz2 - dtz2)))
        t2zz = round(((fun_ontop) / vzot), 3)
    result_5 = (d1_value, d2t_l, t1zz, t2zz)
    return result_5


############################################################################################

# Membership function for Time to the closest Point of Approach (TCPA)
def MF_TCPA(TCPA_NP, t1zz, t2zz):
    if t2zz < abs(TCPA_NP):
        u_TCPA = 0
    elif t1zz < abs(TCPA_NP) and abs(TCPA_NP) < t2zz:
        u_TCPA = ((t2zz - abs(TCPA_NP)) / (t2zz - t1zz)) ** 2
    elif 0 <= abs(TCPA_NP) <= t1zz:
        u_TCPA = 1
    return round(u_TCPA, 3)


############################################################################################

# Membership function for Relative Distance
def MF_Rel_dis(dz1, d2t_l, Di):
    D1_rd = dz1
    D2_rd = d2t_l
    D_rd = Di
    #print('The D1 value is : ', D1_rd)
    #print('The D2 value is : ', D2_rd)
    #print('The D value is : ', D_rd)
    if D2_rd < D_rd:
        Drf = 0
    elif D1_rd <= D_rd and D_rd <= D2_rd:
        Drf = ((D2_rd - D_rd) / (D2_rd - D1_rd)) ** 2
    elif D_rd <= D1_rd:
        Drf = 1
    return round(Drf, 3)


############################################################################################

# Membership function for Relative bearing
def MF_realtive_bearing(alphaT):
    ang_alf = alphaT
    inside_angPT = (ang_alf - 19)
    indie_sqr_big = 440 / 289 + (math.cos(math.radians(inside_angPT))) ** 2
    u_alphaOT_f = round((0.5 * (math.cos(math.radians(inside_angPT)) + math.sqrt(indie_sqr_big)) - (5 / 17)), 3)
    return u_alphaOT_f


############################################################################################

# Calculation of DCPA memebership Function
def MF_DCPA(DCPA_rnd1, d1_1, d2_1):
    d1_u = d1_1
    d2_u = d2_1
    ppzz_1 = DCPA_rnd1
    if d2_u < abs(ppzz_1):
        u_dcpa_fz = 0
    elif d1_u < abs(ppzz_1) <= d2_u:
        iinnsin = (((math.pi) / (d2_u - d1_u)) * ((abs(ppzz_1)) - ((d1_u + d2_u) / 2)))
        u_dcpa_fz = round(0.5 - (0.5 * (math.sin(math.radians(iinnsin)))), 3)
    elif abs(ppzz_1) <= d1_u:
        u_dcpa_fz = 1
    return u_dcpa_fz


############################################################################################

# The memeber function for K

def MF_K(K_u, ang1, ang2):
    K_fg = K_u
    sin_ff = abs(math.sin(abs(math.radians(ang1 - ang2))))
    srt_inside_fun22 = (K_fg ** 2) + 1 + (2 * K_fg * sin_ff)
    down_fun221 = K_fg * (math.sqrt(srt_inside_fun22))
    u_kzs = round(((1) / (1 + (2 / down_fun221))), 3)
    return u_kzs


############################################################################################

# Function for Collision Risk Model is defined as follows :
# The Weights are set as 0.400, 0.367, 0.133, 0.067 and 0.033

def CRI_F(u_dcpa_fz, u_TCPA, Drf, u_alphaOT_f, u_kzs):
    UF = np.array([[u_dcpa_fz], [u_TCPA], [Drf], [u_alphaOT_f], [u_kzs]])
    WF = np.array([[float(0.4), float(0.367), float(0.133), float(0.067), float(0.003)]])
    CRF = WF.dot(UF)
    CRF_rn = round(CRF[0][0], 3)
    return CRF_rn

