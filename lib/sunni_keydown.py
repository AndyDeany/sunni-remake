keys = pygame.key.get_pressed()
# Miscellaneous
backspace_held = keys[8]
tab_held = keys[9]
enter_held = keys[13]
pausebreak_held = keys[19]
escape_held = keys[27]
space_held = keys[32]            
apostrophe_held = keys[39]
comma_held = keys[44]
minus_held = keys[45]
fullstop_held = keys[46]
forwardslash_held = keys[47]               
# Numbers across the top
zero_held =  keys[48]
one_held = keys[49]
two_held = keys[50]
three_held = keys[51]
four_held = keys[52]
five_held = keys[53]
six_held = keys[54]
seven_held = keys[55]
eight_held = keys[56]
nine_held = keys[57]
# Miscellaneous
semicolon_held = keys[59]
backslash_held = keys[60]
equals_held = keys[61]
opensquarebracket_held = keys[91]
sharp_held = keys[92]
closesquarebracket_held = keys[93]
backtick_held = keys[96]
# Alphabet
a_held = keys[97]
b_held = keys[98]
c_held = keys[99]
d_held = keys[100]
e_held = keys[101]
f_held = keys[102]
g_held = keys[103]
h_held = keys[104]
i_held = keys[105]
j_held = keys[106]
k_held = keys[107]
l_held = keys[108]
m_held = keys[109]
n_held = keys[110]
o_held = keys[111]
p_held = keys[112]
q_held = keys[113]
r_held = keys[114]
s_held = keys[115]
t_held = keys[116]
u_held = keys[117]
v_held = keys[118]
w_held = keys[119]
x_held = keys[120]
y_held = keys[121]
z_held = keys[122]
# Miscellaneous
delete_held = keys[127]
# Numpad
numpad0_held = keys[256]
numpad1_held = keys[257]
numpad2_held = keys[258]
numpad3_held = keys[259]
numpad4_held = keys[260]
numpad5_held = keys[261]
numpad6_held = keys[262]
numpad7_held = keys[263]
numpad8_held = keys[264]
numpad9_held = keys[265]
numpaddivide_held = keys[267]
numpadmultiply_held = keys[268]
numpadminus_held = keys[269]
numpadplus_held = keys[270]         
numpadenter_held = keys[271]
# Arrow keys
uparrow_held = keys[273]
downarrow_held = keys[274]
rightarrow_held = keys[275]
leftarrow_held = keys[276]
# Miscellaneous
insert_held = keys[277]
home_held = keys[278]
end_held = keys[279]
pageup_held = keys[280]
pagedown_held = keys[281]           
# F keys
f1_held = keys[282]
f2_held = keys[283]
f3_held = keys[284]
f4_held = keys[285]
f5_held = keys[286]
f6_held = keys[287]
f7_held = keys[288]
f8_held = keys[289]
f9_held = keys[290]
f10_held = keys[291]
f11_held = keys[292]
f12_held = keys[293]
# Key modifiers
numlock = keys[300]
capslock = keys[301]
scrolllock_held = keys[302]
rightshift_held = keys[303]
leftshift_held = keys[304]
shift_held = rightshift_held or leftshift_held
rightcontrol_held = keys[305]
leftcontrol_held = keys[306]
altgrammar_held = keys[307]
alt_held = keys[308]
leftwindows_held = keys[311]    #} these might be
rightwindows_held = keys[312]   #} pointless (windows keys)
menubutton_held = keys[319]
# Calculating the number of keys pressed (for typing)
if accepting_text:
    keys_pressed = 0
    for value in keys:
        keys_pressed += value
    if numlock:
        keys_pressed -= 1
    if capslock:
        keys_pressed -= 1
    if scrolllock_held:
        keys_pressed -= 1
    if rightshift_held:
        keys_pressed -= 1
    if leftshift_held:
        keys_pressed -= 1
    if rightcontrol_held:
        keys_pressed -= 1
    if leftcontrol_held:
        keys_pressed -= 1
    if altgrammar_held:
        if leftcontrol_held:
            keys_pressed -= 1
        else:
            keys_pressed -= 2
    if alt_held:
        keys_pressed -= 1
    if leftwindows_held:
        keys_pressed -= 1
    if rightwindows_held:
        keys_pressed -= 1
    if menubutton_held:
        keys_pressed -= 1
            
