class Keys:
    @classmethod
    def initialise(cls):
        # Miscellaneous
        cls.backspace = 0
        cls.tab = 0
        cls.enter = 0
        cls.pausebreak = 0
        cls.escape = 0
        cls.space = 0
        cls.apostrophe = 0
        cls.comma = 0
        cls.minus = 0
        cls.fullstop = 0
        cls.forwardslash = 0
        # Numbers across the top
        cls.zero = 0
        cls.one = 0
        cls.two = 0
        cls.three = 0
        cls.four = 0
        cls.five = 0
        cls.six = 0
        cls.seven = 0
        cls.eight = 0
        cls.nine = 0
        # Miscellaneous
        cls.semicolon = 0
        cls.backslash = 0
        cls.equals = 0
        cls.opensquarebracket = 0
        cls.sharp = 0
        cls.closesquarebracket = 0
        cls.backtick = 0
        # Alphabet
        cls.a = 0
        cls.b = 0
        cls.c = 0
        cls.d = 0
        cls.e = 0
        cls.f = 0
        cls.g = 0
        cls.h = 0
        cls.i = 0
        cls.j = 0
        cls.k = 0
        cls.l = 0
        cls.m = 0
        cls.n = 0
        cls.o = 0
        cls.p = 0
        cls.q = 0
        cls.r = 0
        cls.s = 0
        cls.t = 0
        cls.u = 0
        cls.v = 0
        cls.w = 0
        cls.x = 0
        cls.y = 0
        cls.z = 0
        # Miscellaneous
        cls.delete = 0
        # Numpad
        cls.numpad0 = 0
        cls.numpad1 = 0
        cls.numpad2 = 0
        cls.numpad3 = 0
        cls.numpad4 = 0
        cls.numpad5 = 0
        cls.numpad6 = 0
        cls.numpad7 = 0
        cls.numpad8 = 0
        cls.numpad9 = 0
        cls.numpaddivide = 0
        cls.numpadmultiply = 0
        cls.numpadminus = 0
        cls.numpadplus = 0
        cls.numpadenter = 0
        # Arrow keys
        cls.uparrow = 0
        cls.downarrow = 0
        cls.rightarrow = 0
        cls.leftarrow = 0
        # Miscellaneous
        cls.insert = 0
        cls.home = 0
        cls.end = 0
        cls.pageup = 0
        cls.pagedown = 0
        # F keys
        cls.f1 = 0
        cls.f2 = 0
        cls.f3 = 0
        cls.f4 = 0
        cls.f5 = 0
        cls.f6 = 0
        cls.f7 = 0
        cls.f8 = 0
        cls.f9 = 0
        cls.f10 = 0
        cls.f11 = 0
        cls.f12 = 0
        # Key modifiers
        cls.scrolllock = 0
        cls.rightshift = 0
        cls.leftshift = 0
        cls.rightcontrol = 0
        cls.leftcontrol = 0
        cls.altgrammar = 0
        cls.alt = 0
        cls.leftwindows = 0
        cls.rightwindows = 0
        cls.menubutton = 0

        cls.backspace_held_time = 0
        cls.tab_held_time = 0
        cls.enter_held_time = 0
        cls.pausebreak_held_time = 0
        cls.escape_held_time = 0
        cls.space_held_time = 0
        cls.apostrophe_held_time = 0
        cls.comma_held_time = 0
        cls.minus_held_time = 0
        cls.fullstop_held_time = 0
        cls.forwardslash_held_time = 0
        cls.zero_held_time = 0
        cls.one_held_time = 0
        cls.two_held_time = 0
        cls.three_held_time = 0
        cls.four_held_time = 0
        cls.five_held_time = 0
        cls.six_held_time = 0
        cls.seven_held_time = 0
        cls.eight_held_time = 0
        cls.nine_held_time = 0
        cls.semicolon_held_time = 0
        cls.backslash_held_time = 0
        cls.equals_held_time = 0
        cls.opensquarebracket_held_time = 0
        cls.sharp_held_time = 0
        cls.closesquarebracket_held_time = 0
        cls.backtick_held_time = 0
        cls.a_held_time = 0
        cls.b_held_time = 0
        cls.c_held_time = 0
        cls.d_held_time = 0
        cls.e_held_time = 0
        cls.f_held_time = 0
        cls.g_held_time = 0
        cls.h_held_time = 0
        cls.i_held_time = 0
        cls.j_held_time = 0
        cls.k_held_time = 0
        cls.l_held_time = 0
        cls.m_held_time = 0
        cls.n_held_time = 0
        cls.o_held_time = 0
        cls.p_held_time = 0
        cls.q_held_time = 0
        cls.r_held_time = 0
        cls.s_held_time = 0
        cls.t_held_time = 0
        cls.u_held_time = 0
        cls.v_held_time = 0
        cls.w_held_time = 0
        cls.x_held_time = 0
        cls.y_held_time = 0
        cls.z_held_time = 0
        cls.delete_held_time = 0
        cls.numpad0_held_time = 0
        cls.numpad1_held_time = 0
        cls.numpad2_held_time = 0
        cls.numpad3_held_time = 0
        cls.numpad4_held_time = 0
        cls.numpad5_held_time = 0
        cls.numpad6_held_time = 0
        cls.numpad7_held_time = 0
        cls.numpad8_held_time = 0
        cls.numpad9_held_time = 0
        cls.numpaddivide_held_time = 0
        cls.numpadmultiply_held_time = 0
        cls.numpadminus_held_time = 0
        cls.numpadplus_held_time = 0
        cls.numpadenter_held_time = 0
        cls.uparrow_held_time = 0
        cls.downarrow_held_time = 0
        cls.rightarrow_held_time = 0
        cls.leftarrow_held_time = 0

        # Values to ensure keys are not registered as being pressed twice when they weren't
        cls.tab_allowed = 0
        cls.enter_allowed = 0
        cls.pausebreak_allowed = 0
        cls.escape_allowed = 0
        cls.space_allowed = 0
        cls.apostrophe_allowed = 0
        cls.comma_allowed = 0
        cls.minus_allowed = 0
        cls.fullstop_allowed = 0
        cls.forwardslash_allowed = 0
        cls.zero_allowed = 0
        cls.one_allowed = 0
        cls.two_allowed = 0
        cls.three_allowed = 0
        cls.four_allowed = 0
        cls.five_allowed = 0
        cls.six_allowed = 0
        cls.seven_allowed = 0
        cls.eight_allowed = 0
        cls.nine_allowed = 0
        cls.semicolon_allowed = 0
        cls.backslash_allowed = 0
        cls.equals_allowed = 0
        cls.opensquarebracket_allowed = 0
        cls.sharp_allowed = 0
        cls.closesquarebracket_allowed = 0
        cls.backtick_allowed = 0
        cls.a_allowed = 0
        cls.b_allowed = 0
        cls.c_allowed = 0
        cls.d_allowed = 0
        cls.e_allowed = 0
        cls.f_allowed = 0
        cls.g_allowed = 0
        cls.h_allowed = 0
        cls.i_allowed = 0
        cls.j_allowed = 0
        cls.k_allowed = 0
        cls.l_allowed = 0
        cls.m_allowed = 0
        cls.n_allowed = 0
        cls.o_allowed = 0
        cls.p_allowed = 0
        cls.q_allowed = 0
        cls.r_allowed = 0
        cls.s_allowed = 0
        cls.t_allowed = 0
        cls.u_allowed = 0
        cls.v_allowed = 0
        cls.w_allowed = 0
        cls.x_allowed = 0
        cls.y_allowed = 0
        cls.z_allowed = 0
        cls.delete_allowed = 0
        cls.numpad0_allowed = 0
        cls.numpad1_allowed = 0
        cls.numpad2_allowed = 0
        cls.numpad3_allowed = 0
        cls.numpad4_allowed = 0
        cls.numpad5_allowed = 0
        cls.numpad6_allowed = 0
        cls.numpad7_allowed = 0
        cls.numpad8_allowed = 0
        cls.numpad9_allowed = 0
        cls.numpaddivide_allowed = 0
        cls.numpadmultiply_allowed = 0
        cls.numpadminus_allowed = 0
        cls.numpadplus_allowed = 0
        cls.numpadenter_allowed = 0
        cls.uparrow_allowed = 0
        cls.downarrow_allowed = 0
        cls.rightarrow_allowed = 0
        cls.leftarrow_allowed = 0

    @classmethod
    def process_keydown(cls, keys, accepting_text=False):
        # Miscellaneous
        cls.backspace_held = keys[8]
        cls.tab_held = keys[9]
        cls.enter_held = keys[13]
        cls.pausebreak_held = keys[19]
        cls.escape_held = keys[27]
        cls.space_held = keys[32]
        cls.apostrophe_held = keys[39]
        cls.comma_held = keys[44]
        cls.minus_held = keys[45]
        cls.fullstop_held = keys[46]
        cls.forwardslash_held = keys[47]
        # Numbers across the top
        cls.zero_held = keys[48]
        cls.one_held = keys[49]
        cls.two_held = keys[50]
        cls.three_held = keys[51]
        cls.four_held = keys[52]
        cls.five_held = keys[53]
        cls.six_held = keys[54]
        cls.seven_held = keys[55]
        cls.eight_held = keys[56]
        cls.nine_held = keys[57]
        # Miscellaneous
        cls.semicolon_held = keys[59]
        cls.backslash_held = keys[60]
        cls.equals_held = keys[61]
        cls.opensquarebracket_held = keys[91]
        cls.sharp_held = keys[92]
        cls.closesquarebracket_held = keys[93]
        cls.backtick_held = keys[96]
        # Alphabet
        cls.a_held = keys[97]
        cls.b_held = keys[98]
        cls.c_held = keys[99]
        cls.d_held = keys[100]
        cls.e_held = keys[101]
        cls.f_held = keys[102]
        cls.g_held = keys[103]
        cls.h_held = keys[104]
        cls.i_held = keys[105]
        cls.j_held = keys[106]
        cls.k_held = keys[107]
        cls.l_held = keys[108]
        cls.m_held = keys[109]
        cls.n_held = keys[110]
        cls.o_held = keys[111]
        cls.p_held = keys[112]
        cls.q_held = keys[113]
        cls.r_held = keys[114]
        cls.s_held = keys[115]
        cls.t_held = keys[116]
        cls.u_held = keys[117]
        cls.v_held = keys[118]
        cls.w_held = keys[119]
        cls.x_held = keys[120]
        cls.y_held = keys[121]
        cls.z_held = keys[122]
        # Miscellaneous
        cls.delete_held = keys[127]
        # Numpad
        cls.numpad0_held = keys[256]
        cls.numpad1_held = keys[257]
        cls.numpad2_held = keys[258]
        cls.numpad3_held = keys[259]
        cls.numpad4_held = keys[260]
        cls.numpad5_held = keys[261]
        cls.numpad6_held = keys[262]
        cls.numpad7_held = keys[263]
        cls.numpad8_held = keys[264]
        cls.numpad9_held = keys[265]
        cls.numpaddivide_held = keys[267]
        cls.numpadmultiply_held = keys[268]
        cls.numpadminus_held = keys[269]
        cls.numpadplus_held = keys[270]
        cls.numpadenter_held = keys[271]
        # Arrow keys
        cls.uparrow_held = keys[273]
        cls.downarrow_held = keys[274]
        cls.rightarrow_held = keys[275]
        cls.leftarrow_held = keys[276]
        # Miscellaneous
        cls.insert_held = keys[277]
        cls.home_held = keys[278]
        cls.end_held = keys[279]
        cls.pageup_held = keys[280]
        cls.pagedown_held = keys[281]
        # F keys
        cls.f1_held = keys[282]
        cls.f2_held = keys[283]
        cls.f3_held = keys[284]
        cls.f4_held = keys[285]
        cls.f5_held = keys[286]
        cls.f6_held = keys[287]
        cls.f7_held = keys[288]
        cls.f8_held = keys[289]
        cls.f9_held = keys[290]
        cls.f10_held = keys[291]
        cls.f11_held = keys[292]
        cls.f12_held = keys[293]
        # Key modifiers
        cls.numlock = keys[300]
        cls.capslock = keys[301]
        cls.scrolllock_held = keys[302]
        cls.rightshift_held = keys[303]
        cls.leftshift_held = keys[304]
        cls.shift_held = cls.rightshift_held or cls.leftshift_held
        cls.rightcontrol_held = keys[305]
        cls.leftcontrol_held = keys[306]
        cls.altgrammar_held = keys[307]
        cls.alt_held = keys[308]
        cls.leftwindows_held = keys[311]    #} these might be
        cls.rightwindows_held = keys[312]   #} pointless (windows keys)
        cls.menubutton_held = keys[319]
        # Calculating the number of keys pressed (for typing)
        if accepting_text:
            cls.keys_pressed = 0
            for value in keys:
                cls.keys_pressed += value
            if cls.numlock:
                cls.keys_pressed -= 1
            if cls.capslock:
                cls.keys_pressed -= 1
            if cls.scrolllock_held:
                cls.keys_pressed -= 1
            if cls.rightshift_held:
                cls.keys_pressed -= 1
            if cls.leftshift_held:
                cls.keys_pressed -= 1
            if cls.rightcontrol_held:
                cls.keys_pressed -= 1
            if cls.leftcontrol_held:
                cls.keys_pressed -= 1
            if cls.altgrammar_held:
                if cls.leftcontrol_held:
                    cls.keys_pressed -= 1
                else:
                    cls.keys_pressed -= 2
            if cls.alt_held:
                cls.keys_pressed -= 1
            if cls.leftwindows_held:
                cls.keys_pressed -= 1
            if cls.rightwindows_held:
                cls.keys_pressed -= 1
            if cls.menubutton_held:
                cls.keys_pressed -= 1


    @classmethod
    def process_keyup(cls, keys):
        # Miscellaneous
        if cls.backspace_held and not keys[8]:
            cls.backspace = 1
            cls.backspace_held = 0
            cls.backspace_held_time = 0
            cls.backspace_allowed = 1
        if cls.tab_held and not keys[9]:
            cls.tab = 1
            cls.tab_held = 0
            cls.tab_held_time = 0
            cls.tab_allowed = 1
        if cls.enter_held and not keys[13]:
            cls.enter = 1
            cls.enter_held = 0
            cls.enter_held_time = 0
            cls.enter_allowed = 1
        if cls.pausebreak_held and not keys[19]:
            cls.pausebreak = 1
            cls.pausebreak_held = 0
            cls.pausebreak_held_time = 0
            cls.pausebreak_allowed = 1
        if cls.escape_held and not keys[27]:
            cls.escape = 1
            cls.escape_held = 0
            cls.escape_held_time = 0
            cls.escape_allowed = 1
        if cls.space_held and not keys[32]:
            cls.space = 1
            cls.space_held = 0
            cls.space_held_time = 0
            cls.space_allowed = 1
        if cls.apostrophe_held and not keys[39]:
            cls.apostrophe = 1
            cls.apostrophe_held = 0
            cls.apostrophe_held_time = 0
            cls.apostrophe_allowed = 1
        if cls.comma_held and not keys[44]:
            cls.comma = 1
            cls.comma_held = 0
            cls.comma_held_time = 0
            cls.comma_allowed = 1
        if cls.minus_held and not keys[45]:
            cls.minus = 1
            cls.minus_held = 0
            cls.minus_held_time = 0
            cls.minus_allowed = 1
        if cls.fullstop_held and not keys[46]:
            cls.fullstop = 1
            cls.fullstop_held = 0
            cls.fullstop_held_time = 0
            cls.fullstop_allowed = 1
        if cls.forwardslash_held and not keys[47]:
            cls.forwardslash = 1
            cls.forwardslash_held = 0
            cls.forwardslash_held_time = 0
            cls.forwardslash_allowed = 1
        # Numbers across the top
        if cls.zero_held and not keys[48]:
            cls.zero = 1
            cls.zero_held = 0
            cls.zero_held_time = 0
            cls.zero_allowed = 1
        if cls.one_held and not keys[49]:
            cls.one = 1
            cls.one_held = 0
            cls.one_held_time = 0
            cls.one_allowed = 1
        if cls.two_held and not keys[50]:
            cls.two = 1
            cls.two_held = 0
            cls.two_held_time = 0
            cls.two_allowed = 1
        if cls.three_held and not keys[51]:
            cls.three = 1
            cls.three_held = 0
            cls.three_held_time = 0
            cls.three_allowed = 1
        if cls.four_held and not keys[52]:
            cls.four = 1
            cls.four_held = 0
            cls.four_held_time = 0
            cls.four_allowed = 1
        if cls.five_held and not keys[53]:
            cls.five = 1
            cls.five_held = 0
            cls.five_held_time = 0
            cls.five_allowed = 1
        if cls.six_held and not keys[54]:
            cls.six = 1
            cls.six_held = 0
            cls.six_held_time = 0
            cls.six_allowed = 1
        if cls.seven_held and not keys[55]:
            cls.seven = 1
            cls.seven_held = 0
            cls.seven_held_time = 0
            cls.seven_allowed = 1
        if cls.eight_held and not keys[56]:
            cls.eight = 1
            cls.eight_held = 0
            cls.eight_held_time = 0
            cls.eight_allowed = 1
        if cls.nine_held and not keys[57]:
            cls.nine = 1
            cls.nine_held = 0
            cls.nine_held_time = 0
            cls.nine_allowed = 1
        # Miscellaneous
        if cls.semicolon_held and not keys[59]:
            cls.semicolon = 1
            cls.semicolon_held = 0
            cls.semicolon_held_time = 0
            cls.semicolon_allowed = 1
        if cls.backslash_held and not keys[60]:
            cls.backslash = 1
            cls.backslash_held = 0
            cls.backslash_held_time = 0
            cls.backslash_allowed = 1
        if cls.equals_held and not keys[61]:
            cls.equals = 1
            cls.equals_held = 0
            cls.equals_held_time = 0
            cls.equals_allowed = 1
        if cls.opensquarebracket_held and not keys[91]:
            cls.opensquarebracket = 1
            cls.opensquarebracket_held = 0
            cls.opensquarebracket_held_time = 0
            cls.opensquarebracket_allowed = 1
        if cls.sharp_held and not keys[92]:
            cls.sharp = 1
            cls.sharp_held = 0
            cls.sharp_held_time = 0
            cls.sharp_allowed = 1
        if cls.closesquarebracket_held and not keys[93]:
            cls.closesquarebracket = 1
            cls.closesquarebracket_held = 0
            cls.closesquarebracket_held_time = 0
            cls.closesquarebracket_allowed = 1
        if cls.backtick_held and not keys[96]:
            cls.backtick = 1
            cls.backtick_held = 0
            cls.backtick_held_time = 0
            cls.backtick_allowed = 1
        # Alphabet
        if cls.a_held and not keys[97]:
            cls.a = 1
            cls.a_held = 0
            cls.a_held_time = 0
            cls.a_allowed = 1
        if cls.b_held and not keys[98]:
            cls.b = 1
            cls.b_held = 0
            cls.b_held_time = 0
            cls.b_allowed = 1
        if cls.c_held and not keys[99]:
            cls.c = 1
            cls.c_held = 0
            cls.c_held_time = 0
            cls.c_allowed = 1
        if cls.d_held and not keys[100]:
            cls.d = 1
            cls.d_held = 0
            cls.d_held_time = 0
            cls.d_allowed = 1
        if cls.e_held and not keys[101]:
            cls.e = 1
            cls.e_held = 0
            cls.e_held_time = 0
            cls.e_allowed = 1
        if cls.f_held and not keys[102]:
            cls.f = 1
            cls.f_held = 0
            cls.f_held_time = 0
            cls.f_allowed = 1
        if cls.g_held and not keys[103]:
            cls.g = 1
            cls.g_held = 0
            cls.g_held_time = 0
            cls.g_allowed = 1
        if cls.h_held and not keys[104]:
            cls.h = 1
            cls.h_held = 0
            cls.h_held_time = 0
            cls.h_allowed = 1
        if cls.i_held and not keys[105]:
            cls.i = 1
            cls.i_held = 0
            cls.i_held_time = 0
            cls.i_allowed = 1
        if cls.j_held and not keys[106]:
            cls.j = 1
            cls.j_held = 0
            cls.j_held_time = 0
            cls.j_allowed = 1
        if cls.k_held and not keys[107]:
            cls.k = 1
            cls.k_held = 0
            cls.k_held_time = 0
            cls.k_allowed = 1
        if cls.l_held and not keys[108]:
            cls.l = 1
            cls.l_held = 0
            cls.l_held_time = 0
            cls.l_allowed = 1
        if cls.m_held and not keys[109]:
            cls.m = 1
            cls.m_held = 0
            cls.m_held_time = 0
            cls.m_allowed = 1
        if cls.n_held and not keys[110]:
            cls.n = 1
            cls.n_held = 0
            cls.n_held_time = 0
            cls.n_allowed = 1
        if cls.o_held and not keys[111]:
            cls.o = 1
            cls.o_held = 0
            cls.o_held_time = 0
            cls.o_allowed = 1
        if cls.p_held and not keys[112]:
            cls.p = 1
            cls.p_held = 0
            cls.p_held_time = 0
            cls.p_allowed = 1
        if cls.q_held and not keys[113]:
            cls.q = 1
            cls.q_held = 0
            cls.q_held_time = 0
            cls.q_allowed = 1
        if cls.r_held and not keys[114]:
            cls.r = 1
            cls.r_held = 0
            cls.r_held_time = 0
            cls.r_allowed = 1
        if cls.s_held and not keys[115]:
            cls.s = 1
            cls.s_held = 0
            cls.s_held_time = 0
            cls.s_allowed = 1
        if cls.t_held and not keys[116]:
            cls.t = 1
            cls.t_held = 0
            cls.t_held_time = 0
            cls.t_allowed = 1
        if cls.u_held and not keys[117]:
            cls.u = 1
            cls.u_held = 0
            cls.u_held_time = 0
            cls.u_allowed = 1
        if cls.v_held and not keys[118]:
            cls.v = 1
            cls.v_held = 0
            cls.v_held_time = 0
            cls.v_allowed = 1
        if cls.w_held and not keys[119]:
            cls.w = 1
            cls.w_held = 0
            cls.w_held_time = 0
            cls.w_allowed = 1
        if cls.x_held and not keys[120]:
            cls.x = 1
            cls.x_held = 0
            cls.x_held_time = 0
            cls.x_allowed = 1
        if cls.y_held and not keys[121]:
            cls.y = 1
            cls.y_held = 0
            cls.y_held_time = 0
            cls.y_allowed = 1
        if cls.z_held and not keys[122]:
            cls.z = 1
            cls.z_held = 0
            cls.z_held_time = 0
            cls.z_allowed = 1
        # Miscellaneous
        if cls.delete_held and not keys[127]:
            cls.delete = 1
            cls.delete_held = 0
            cls.delete_held_time = 0
            cls.delete_allowed = 1
        # Numpad
        if cls.numpad0_held and not keys[256]:
            cls.numpad0 = 1
            cls.numpad0_held = 0
            cls.numpad0_held_time = 0
            cls.numpad0_allowed = 1
        if cls.numpad1_held and not keys[257]:
            cls.numpad1 = 1
            cls.numpad1_held = 0
            cls.numpad1_held_time = 0
            cls.numpad1_allowed = 1
        if cls.numpad2_held and not keys[258]:
            cls.numpad2 = 1
            cls.numpad2_held = 0
            cls.numpad2_held_time = 0
            cls.numpad2_allowed = 1
        if cls.numpad3_held and not keys[259]:
            cls.numpad3 = 1
            cls.numpad3_held = 0
            cls.numpad3_held_time = 0
            cls.numpad3_allowed = 1
        if cls.numpad4_held and not keys[260]:
            cls.numpad4 = 1
            cls.numpad4_held = 0
            cls.numpad4_held_time = 0
            cls.numpad4_allowed = 1
        if cls.numpad5_held and not keys[261]:
            cls.numpad5 = 1
            cls.numpad5_held = 0
            cls.numpad5_held_time = 0
            cls.numpad5_allowed = 1
        if cls.numpad6_held and not keys[262]:
            cls.numpad6 = 1
            cls.numpad6_held = 0
            cls.numpad6_held_time = 0
            cls.numpad6_allowed = 1
        if cls.numpad7_held and not keys[263]:
            cls.numpad7 = 1
            cls.numpad7_held = 0
            cls.numpad7_held_time = 0
            cls.numpad7_allowed = 1
        if cls.numpad8_held and not keys[264]:
            cls.numpad8 = 1
            cls.numpad8_held = 0
            cls.numpad8_held_time = 0
            cls.numpad8_allowed = 1
        if cls.numpad9_held and not keys[265]:
            cls.numpad9 = 1
            cls.numpad9_held = 0
            cls.numpad9_held_time = 0
            cls.numpad9_allowed = 1
        if cls.numpaddivide_held and not keys[267]:
            cls.numpaddivide = 1
            cls.numpaddivide_held = 0
            cls.numpaddivide_held_time = 0
            cls.numpaddivide_allowed = 1
        if cls.numpadmultiply_held and not keys[268]:
            cls.numpadmultiply = 1
            cls.numpadmultiply_held = 0
            cls.numpadmultiply_held_time = 0
            cls.numpadmultiply_allowed = 1
        if cls.numpadminus_held and not keys[269]:
            cls.numpadminus = 1
            cls.numpadminus_held = 0
            cls.numpadminus_held_time = 0
            cls.numpadminus_allowed = 1
        if cls.numpadplus_held and not keys[270]:
            cls.numpadplus = 1
            cls.numpadplus_held = 0
            cls.numpadplus_held_time = 0
            cls.numpadplus_allowed = 1
        if cls.numpadenter_held and not keys[271]:
            cls.numpadenter = 1
            cls.numpadenter_held = 0
            cls.numpadenter_held_time = 0
            cls.numpadenter_allowed = 1
        # Arrow keys
        if cls.uparrow_held and not keys[273]:
            cls.uparrow = 1
            cls.uparrow_held = 0
            cls.uparrow_held_time = 0
            cls.uparrow_allowed = 1
        if cls.downarrow_held and not keys[274]:
            cls.downarrow = 1
            cls.downarrow_held = 0
            cls.downarrow_held_time = 0
            cls.downarrow_allowed = 1
        if cls.rightarrow_held and not keys[275]:
            cls.rightarrow = 1
            cls.rightarrow_held = 0
            cls.rightarrow_held_time = 0
            cls.rightarrow_allowed = 1
        if cls.leftarrow_held and not keys[276]:
            cls.leftarrow = 1
            cls.leftarrow_held = 0
            cls.leftarrow_held_time = 0
            cls.leftarrow_allowed = 1
        # Miscellaneous
        if cls.insert_held and not keys[277]:
            cls.insert = 1
            cls.insert_held = 0
        if cls.home_held and not keys[278]:
            cls.home = 1
            cls.home_held = 0
        if cls.end_held and not keys[279]:
            cls.end = 1
            cls.end_held = 0
        if cls.pageup_held and not keys[280]:
            cls.pageup = 1
            cls.pageup_held = 0
        if cls.pagedown_held and not keys[281]:
            cls.pagedown = 1
            cls.pagedown_held = 0
        # F keys
        if cls.f1_held and not keys[282]:
            cls.f1 = 1
            cls.f1_held = 0
        if cls.f2_held and not keys[283]:
            cls.f2 = 1
            cls.f2_held = 0
        if cls.f3_held and not keys[284]:
            cls.f3 = 1
            cls.f3_held = 0
        if cls.f4_held and not keys[285]:
            cls.f4 = 1
            cls.f4_held = 0
        if cls.f5_held and not keys[286]:
            cls.f5 = 1
            cls.f5_held = 0
        if cls.f6_held and not keys[287]:
            cls.f6 = 1
            cls.f6_held = 0
        if cls.f7_held and not keys[288]:
            cls.f7 = 1
            cls.f7_held = 0
        if cls.f8_held and not keys[289]:
            cls.f8 = 1
            cls.f8_held = 0
        if cls.f9_held and not keys[290]:
            cls.f9 = 1
            cls.f9_held = 0
        if cls.f10_held and not keys[291]:
            cls.f10 = 1
            cls.f10_held = 0
        if cls.f11_held and not keys[292]:
            cls.f11 = 1
            cls.f11_held = 0
        if cls.f12_held and not keys[293]:
            cls.f12 = 1
            cls.f12_held = 0
        # Key modifiers
        if cls.numlock and not keys[300]:
            cls.numlock = 1
            cls.numlock = 0
        if cls.capslock and not keys[301]:
            cls.capslock = 1
            cls.capslock = 0
        if cls.scrolllock_held and not keys[302]:
            cls.scrolllock = 1
            cls.scrolllock_held = 0
        if cls.rightshift_held and not keys[303]:
            cls.rightshift = 1
            cls.rightshift_held = 0
        if cls.leftshift_held and not keys[304]:
            cls.leftshift = 1
            cls.leftshift_held = 0
        if cls.rightshift or cls.leftshift:
            cls.shift = 1
            cls.shift_held = 0
        if cls.rightcontrol_held and not keys[305]:
            cls.rightcontrol = 1
            cls.rightcontrol_held = 0
        if cls.leftcontrol_held and not keys[306]:
            cls.leftcontrol = 1
            cls.leftcontrol_held = 0
        if cls.altgrammar_held and not keys[307]:
            cls.altgrammar = 1
            cls.altgrammar_held = 0
        if cls.alt_held and not keys[308]:
            cls.alt = 1
            cls.alt_held = 0
        if cls.leftwindows_held and not keys[311]:  # } these might be
            cls.leftwindows = 1
            cls.leftwindows_held = 0
        if cls.rightwindows_held and not keys[312]:  # } pointless (windows keys)
            cls.rightwindows = 1
            cls.rightwindows_held = 0
        if cls.menubutton_held and not keys[319]:
            cls.menubutton = 1
            cls.menubutton_held = 0

    @classmethod
    def process_keyheld(cls):
        if cls.backspace_held:
            cls.backspace_held_time += 1
        if cls.tab_held:
            cls.tab_held_time += 1
        if cls.enter_held:
            cls.enter_held_time += 1
        if cls.pausebreak_held:
            cls.pausebreak_held_time += 1
        if cls.escape_held:
            cls.escape_held_time += 1
        if cls.space_held:
            cls.space_held_time += 1
        if cls.apostrophe_held:
            cls.apostrophe_held_time += 1
        if cls.comma_held:
            cls.comma_held_time += 1
        if cls.minus_held:
            cls.minus_held_time += 1
        if cls.fullstop_held:
            cls.fullstop_held_time += 1
        if cls.forwardslash_held:
            cls.forwardslash_held_time += 1
        if cls.zero_held:
            cls.zero_held_time += 1
        if cls.one_held:
            cls.one_held_time += 1
        if cls.two_held:
            cls.two_held_time += 1
        if cls.three_held:
            cls.three_held_time += 1
        if cls.four_held:
            cls.four_held_time += 1
        if cls.five_held:
            cls.five_held_time += 1
        if cls.six_held:
            cls.six_held_time += 1
        if cls.seven_held:
            cls.seven_held_time += 1
        if cls.eight_held:
            cls.eight_held_time += 1
        if cls.nine_held:
            cls.nine_held_time += 1
        if cls.semicolon_held:
            cls.semicolon_held_time += 1
        if cls.backslash_held:
            cls.backslash_held_time += 1
        if cls.equals_held:
            cls.equals_held_time += 1
        if cls.opensquarebracket_held:
            cls.opensquarebracket_held_time += 1
        if cls.sharp_held:
            cls.sharp_held_time += 1
        if cls.closesquarebracket_held:
            cls.closesquarebracket_held_time += 1
        if cls.backtick_held:
            cls.backtick_held_time += 1
        if cls.a_held:
            cls.a_held_time += 1
        if cls.b_held:
            cls.b_held_time += 1
        if cls.c_held:
            cls.c_held_time += 1
        if cls.d_held:
            cls.d_held_time += 1
        if cls.e_held:
            cls.e_held_time += 1
        if cls.f_held:
            cls.f_held_time += 1
        if cls.g_held:
            cls.g_held_time += 1
        if cls.h_held:
            cls.h_held_time += 1
        if cls.i_held:
            cls.i_held_time += 1
        if cls.j_held:
            cls.j_held_time += 1
        if cls.k_held:
            cls.k_held_time += 1
        if cls.l_held:
            cls.l_held_time += 1
        if cls.m_held:
            cls.m_held_time += 1
        if cls.n_held:
            cls.n_held_time += 1
        if cls.o_held:
            cls.o_held_time += 1
        if cls.p_held:
            cls.p_held_time += 1
        if cls.q_held:
            cls.q_held_time += 1
        if cls.r_held:
            cls.r_held_time += 1
        if cls.s_held:
            cls.s_held_time += 1
        if cls.t_held:
            cls.t_held_time += 1
        if cls.u_held:
            cls.u_held_time += 1
        if cls.v_held:
            cls.v_held_time += 1
        if cls.w_held:
            cls.w_held_time += 1
        if cls.x_held:
            cls.x_held_time += 1
        if cls.y_held:
            cls.y_held_time += 1
        if cls.z_held:
            cls.z_held_time += 1
        if cls.delete_held:
            cls.delete_held_time += 1
        if cls.numpad0_held:
            cls.numpad0_held_time += 1
        if cls.numpad1_held:
            cls.numpad1_held_time += 1
        if cls.numpad2_held:
            cls.numpad2_held_time += 1
        if cls.numpad3_held:
            cls.numpad3_held_time += 1
        if cls.numpad4_held:
            cls.numpad4_held_time += 1
        if cls.numpad5_held:
            cls.numpad5_held_time += 1
        if cls.numpad6_held:
            cls.numpad6_held_time += 1
        if cls.numpad7_held:
            cls.numpad7_held_time += 1
        if cls.numpad8_held:
            cls.numpad8_held_time += 1
        if cls.numpad9_held:
            cls.numpad9_held_time += 1
        if cls.numpaddivide_held:
            cls.numpaddivide_held_time += 1
        if cls.numpadmultiply_held:
            cls.numpadmultiply_held_time += 1
        if cls.numpadminus_held:
            cls.numpadminus_held_time += 1
        if cls.numpadplus_held:
            cls.numpadplus_held_time += 1
        if cls.numpadenter_held:
            cls.numpadenter_held_time += 1
        if cls.uparrow_held:
            cls.uparrow_held_time += 1
        if cls.downarrow_held:
            cls.downarrow_held_time += 1
        if cls.rightarrow_held:
            cls.rightarrow_held_time += 1
        if cls.leftarrow_held:
            cls.leftarrow_held_time += 1

    @classmethod
    def process_multiple_character_input(cls, fps, maximum_characters, input_text):
        # -*- coding: utf-8 -*-
        if cls.backspace_held_time > fps / 2:
            input_text = input_text[:-1]

        if not len(input_text) <= maximum_characters:
            return input_text

        if cls.tab_held_time > fps / 2:
            input_text += "    "
        if cls.enter_held_time > fps / 2:
            pass
        if cls.space_held_time > fps / 2:
            input_text += " "

        if not cls.shift_held:
            if cls.apostrophe_held_time > fps / 2:
                input_text += "'"
            if cls.comma_held_time > fps / 2:
                input_text += ","
            if cls.minus_held_time > fps / 2:
                input_text += "-"
            if cls.fullstop_held_time > fps / 2:
                input_text += "."
            if cls.forwardslash_held_time > fps / 2:
                input_text += "/"
            if cls.zero_held_time > fps / 2:
                input_text += "0"
            if cls.one_held_time > fps / 2:
                input_text += "1"
            if cls.two_held_time > fps / 2:
                input_text += "2"
            if cls.three_held_time > fps / 2:
                input_text += "3"
            if cls.four_held_time > fps / 2:
                input_text += "4"
            if cls.five_held_time > fps / 2:
                input_text += "5"
            if cls.six_held_time > fps / 2:
                input_text += "6"
            if cls.seven_held_time > fps / 2:
                input_text += "7"
            if cls.eight_held_time > fps / 2:
                input_text += "8"
            if cls.nine_held_time > fps / 2:
                input_text += "9"
            if cls.semicolon_held_time > fps / 2:
                input_text += ";"
            if cls.backslash_held_time > fps / 2:
                input_text += "\\"
            if cls.equals_held_time > fps / 2:
                input_text += "="
            if cls.opensquarebracket_held_time > fps / 2:
                input_text += "["
            if cls.sharp_held_time > fps / 2:
                input_text += "#"
            if cls.closesquarebracket_held_time > fps / 2:
                input_text += "]"
            if cls.backtick_held_time > fps / 2:
                input_text += "`"

            if not cls.capslock:
                if cls.a_held_time > fps / 2:
                    input_text += "a"
                if cls.b_held_time > fps / 2:
                    input_text += "b"
                if cls.c_held_time > fps / 2:
                    input_text += "c"
                if cls.d_held_time > fps / 2:
                    input_text += "d"
                if cls.e_held_time > fps / 2:
                    input_text += "e"
                if cls.f_held_time > fps / 2:
                    input_text += "f"
                if cls.g_held_time > fps / 2:
                    input_text += "g"
                if cls.h_held_time > fps / 2:
                    input_text += "h"
                if cls.i_held_time > fps / 2:
                    input_text += "i"
                if cls.j_held_time > fps / 2:
                    input_text += "j"
                if cls.k_held_time > fps / 2:
                    input_text += "k"
                if cls.l_held_time > fps / 2:
                    input_text += "l"
                if cls.m_held_time > fps / 2:
                    input_text += "m"
                if cls.n_held_time > fps / 2:
                    input_text += "n"
                if cls.o_held_time > fps / 2:
                    input_text += "o"
                if cls.p_held_time > fps / 2:
                    input_text += "p"
                if cls.q_held_time > fps / 2:
                    input_text += "q"
                if cls.r_held_time > fps / 2:
                    input_text += "r"
                if cls.s_held_time > fps / 2:
                    input_text += "s"
                if cls.t_held_time > fps / 2:
                    input_text += "t"
                if cls.u_held_time > fps / 2:
                    input_text += "u"
                if cls.v_held_time > fps / 2:
                    input_text += "v"
                if cls.w_held_time > fps / 2:
                    input_text += "w"
                if cls.x_held_time > fps / 2:
                    input_text += "x"
                if cls.y_held_time > fps / 2:
                    input_text += "y"
                if cls.z_held_time > fps / 2:
                    input_text += "z"
            else:
                if cls.a_held_time > fps / 2:
                    input_text += "A"
                if cls.b_held_time > fps / 2:
                    input_text += "B"
                if cls.c_held_time > fps / 2:
                    input_text += "C"
                if cls.d_held_time > fps / 2:
                    input_text += "D"
                if cls.e_held_time > fps / 2:
                    input_text += "E"
                if cls.f_held_time > fps / 2:
                    input_text += "F"
                if cls.g_held_time > fps / 2:
                    input_text += "G"
                if cls.h_held_time > fps / 2:
                    input_text += "H"
                if cls.i_held_time > fps / 2:
                    input_text += "I"
                if cls.j_held_time > fps / 2:
                    input_text += "J"
                if cls.k_held_time > fps / 2:
                    input_text += "K"
                if cls.l_held_time > fps / 2:
                    input_text += "L"
                if cls.m_held_time > fps / 2:
                    input_text += "M"
                if cls.n_held_time > fps / 2:
                    input_text += "N"
                if cls.o_held_time > fps / 2:
                    input_text += "O"
                if cls.p_held_time > fps / 2:
                    input_text += "P"
                if cls.q_held_time > fps / 2:
                    input_text += "Q"
                if cls.r_held_time > fps / 2:
                    input_text += "R"
                if cls.s_held_time > fps / 2:
                    input_text += "S"
                if cls.t_held_time > fps / 2:
                    input_text += "T"
                if cls.u_held_time > fps / 2:
                    input_text += "U"
                if cls.v_held_time > fps / 2:
                    input_text += "V"
                if cls.w_held_time > fps / 2:
                    input_text += "W"
                if cls.x_held_time > fps / 2:
                    input_text += "X"
                if cls.y_held_time > fps / 2:
                    input_text += "Y"
                if cls.z_held_time > fps / 2:
                    input_text += "Z"
        else:
            if cls.apostrophe_held_time > fps / 2:
                input_text += "@"
            if cls.comma_held_time > fps / 2:
                input_text += "<"
            if cls.minus_held_time > fps / 2:
                input_text += "_"
            if cls.fullstop_held_time > fps / 2:
                input_text += ">"
            if cls.forwardslash_held_time > fps / 2:
                input_text += "?"
            if cls.zero_held_time > fps / 2:
                input_text += ")"
            if cls.one_held_time > fps / 2:
                input_text += "!"
            if cls.two_held_time > fps / 2:
                input_text += "\""
            if cls.three_held_time > fps / 2:
                input_text += chr(163)
            if cls.four_held_time > fps / 2:
                input_text += "$"
            if cls.five_held_time > fps / 2:
                input_text += "%"
            if cls.six_held_time > fps / 2:
                input_text += "^"
            if cls.seven_held_time > fps / 2:
                input_text += "&"
            if cls.eight_held_time > fps / 2:
                input_text += "*"
            if cls.nine_held_time > fps / 2:
                input_text += "("
            if cls.semicolon_held_time > fps / 2:
                input_text += ":"
            if cls.backslash_held_time > fps / 2:
                input_text += "|"
            if cls.equals_held_time > fps / 2:
                input_text += "+"
            if cls.opensquarebracket_held_time > fps / 2:
                input_text += "{"
            if cls.sharp_held_time > fps / 2:
                input_text += "~"
            if cls.closesquarebracket_held_time > fps / 2:
                input_text += "}"
            if cls.backtick_held_time > fps / 2:
                input_text += "¬"

            if cls.capslock:
                if cls.a_held_time > fps / 2:
                    input_text += "a"
                if cls.b_held_time > fps / 2:
                    input_text += "b"
                if cls.c_held_time > fps / 2:
                    input_text += "c"
                if cls.d_held_time > fps / 2:
                    input_text += "d"
                if cls.e_held_time > fps / 2:
                    input_text += "e"
                if cls.f_held_time > fps / 2:
                    input_text += "f"
                if cls.g_held_time > fps / 2:
                    input_text += "g"
                if cls.h_held_time > fps / 2:
                    input_text += "h"
                if cls.i_held_time > fps / 2:
                    input_text += "i"
                if cls.j_held_time > fps / 2:
                    input_text += "j"
                if cls.k_held_time > fps / 2:
                    input_text += "k"
                if cls.l_held_time > fps / 2:
                    input_text += "l"
                if cls.m_held_time > fps / 2:
                    input_text += "m"
                if cls.n_held_time > fps / 2:
                    input_text += "n"
                if cls.o_held_time > fps / 2:
                    input_text += "o"
                if cls.p_held_time > fps / 2:
                    input_text += "p"
                if cls.q_held_time > fps / 2:
                    input_text += "q"
                if cls.r_held_time > fps / 2:
                    input_text += "r"
                if cls.s_held_time > fps / 2:
                    input_text += "s"
                if cls.t_held_time > fps / 2:
                    input_text += "t"
                if cls.u_held_time > fps / 2:
                    input_text += "u"
                if cls.v_held_time > fps / 2:
                    input_text += "v"
                if cls.w_held_time > fps / 2:
                    input_text += "w"
                if cls.x_held_time > fps / 2:
                    input_text += "x"
                if cls.y_held_time > fps / 2:
                    input_text += "y"
                if cls.z_held_time > fps / 2:
                    input_text += "z"
            else:
                if cls.a_held_time > fps / 2:
                    input_text += "A"
                if cls.b_held_time > fps / 2:
                    input_text += "B"
                if cls.c_held_time > fps / 2:
                    input_text += "C"
                if cls.d_held_time > fps / 2:
                    input_text += "D"
                if cls.e_held_time > fps / 2:
                    input_text += "E"
                if cls.f_held_time > fps / 2:
                    input_text += "F"
                if cls.g_held_time > fps / 2:
                    input_text += "G"
                if cls.h_held_time > fps / 2:
                    input_text += "H"
                if cls.i_held_time > fps / 2:
                    input_text += "I"
                if cls.j_held_time > fps / 2:
                    input_text += "J"
                if cls.k_held_time > fps / 2:
                    input_text += "K"
                if cls.l_held_time > fps / 2:
                    input_text += "L"
                if cls.m_held_time > fps / 2:
                    input_text += "M"
                if cls.n_held_time > fps / 2:
                    input_text += "N"
                if cls.o_held_time > fps / 2:
                    input_text += "O"
                if cls.p_held_time > fps / 2:
                    input_text += "P"
                if cls.q_held_time > fps / 2:
                    input_text += "Q"
                if cls.r_held_time > fps / 2:
                    input_text += "R"
                if cls.s_held_time > fps / 2:
                    input_text += "S"
                if cls.t_held_time > fps / 2:
                    input_text += "T"
                if cls.u_held_time > fps / 2:
                    input_text += "U"
                if cls.v_held_time > fps / 2:
                    input_text += "V"
                if cls.w_held_time > fps / 2:
                    input_text += "W"
                if cls.x_held_time > fps / 2:
                    input_text += "X"
                if cls.y_held_time > fps / 2:
                    input_text += "Y"
                if cls.z_held_time > fps / 2:
                    input_text += "Z"

        if cls.delete_held_time > fps / 2:  # for if there is a cursor so you can go backwards and type there in the future
            pass
        if cls.numpad0_held_time > fps / 2:
            input_text += "0"
        if cls.numpad1_held_time > fps / 2:
            input_text += "1"
        if cls.numpad2_held_time > fps / 2:
            input_text += "2"
        if cls.numpad3_held_time > fps / 2:
            input_text += "3"
        if cls.numpad4_held_time > fps / 2:
            input_text += "4"
        if cls.numpad5_held_time > fps / 2:
            input_text += "5"
        if cls.numpad6_held_time > fps / 2:
            input_text += "6"
        if cls.numpad7_held_time > fps / 2:
            input_text += "7"
        if cls.numpad8_held_time > fps / 2:
            input_text += "8"
        if cls.numpad9_held_time > fps / 2:
            input_text += "9"
        if cls.numpaddivide_held_time > fps / 2:
            input_text += "/"
        if cls.numpadmultiply_held_time > fps / 2:
            input_text += "*"
        if cls.numpadminus_held_time > fps / 2:
            input_text += "-"
        if cls.numpadplus_held_time > fps / 2:
            input_text += "+"
        if cls.numpadenter_held_time > fps / 2:
            pass
        if cls.rightarrow_held_time > fps / 2:  # for if there is a cursor so you can go backwards and type there in the future
            pass
        if cls.leftarrow_held_time > fps / 2:  # for if there is a cursor so you can go backwards and type there in the future
            pass

        return input_text

    @classmethod
    def process_single_character_input(cls, keys_pressed, maximum_characters, input_text):
        # -*- coding: utf-8 -*-
        if cls.backspace_held and input_text != "":
            input_text = input_text[:-1]

        if not len(input_text) <= maximum_characters:
            return input_text
        if cls.tab_held and (cls.tab_allowed or keys_pressed < 2):
            input_text += "    "
            cls.tab_allowed = 0
        if cls.enter_held and (cls.enter_allowed or keys_pressed < 2):
            accepting_text = False
            cls.enter_allowed = 0
        if cls.space_held and (cls.space_allowed or keys_pressed < 2):
            input_text += " "
            cls.space_allowed = 0

        if not cls.shift_held:
            if cls.apostrophe_held and (cls.apostrophe_allowed or keys_pressed < 2):
                input_text += "'"
                cls.apostrophe_allowed = 0
            if cls.comma_held and (cls.comma_allowed or keys_pressed < 2):
                input_text += ","
                cls.comma_allowed = 0
            if cls.minus_held and (cls.minus_allowed or keys_pressed < 2):
                input_text += "-"
                cls.minus_allowed = 0
            if cls.fullstop_held and (cls.fullstop_allowed or keys_pressed < 2):
                input_text += "."
                cls.fullstop_allowed = 0
            if cls.forwardslash_held and (cls.forwardslash_allowed or keys_pressed < 2):
                input_text += "/"
                cls.forwardslash_allowed = 0
            if cls.zero_held and (cls.zero_allowed or keys_pressed < 2):
                input_text += "0"
                cls.zero_allowed = 0
            if cls.one_held and (cls.one_allowed or keys_pressed < 2):
                input_text += "1"
                cls.one_allowed = 0
            if cls.two_held and (cls.two_allowed or keys_pressed < 2):
                input_text += "2"
                cls.two_allowed = 0
            if cls.three_held and (cls.three_allowed or keys_pressed < 2):
                input_text += "3"
                cls.three_allowed = 0
            if cls.four_held and (cls.four_allowed or keys_pressed < 2):
                input_text += "4"
                cls.four_allowed = 0
            if cls.five_held and (cls.five_allowed or keys_pressed < 2):
                input_text += "5"
                cls.five_allowed = 0
            if cls.six_held and (cls.six_allowed or keys_pressed < 2):
                input_text += "6"
                cls.six_allowed = 0
            if cls.seven_held and (cls.seven_allowed or keys_pressed < 2):
                input_text += "7"
                cls.seven_allowed = 0
            if cls.eight_held and (cls.eight_allowed or keys_pressed < 2):
                input_text += "8"
                cls.eight_allowed = 0
            if cls.nine_held and (cls.nine_allowed or keys_pressed < 2):
                input_text += "9"
                cls.nine_allowed = 0
            if cls.semicolon_held and (cls.semicolon_allowed or keys_pressed < 2):
                input_text += ";"
                cls.semicolon_allowed = 0
            if cls.backslash_held and (cls.backslash_allowed or keys_pressed < 2):
                input_text += "\\"
                cls.backslash_allowed = 0
            if cls.equals_held and (cls.equals_allowed or keys_pressed < 2):
                input_text += "="
                cls.equals_allowed = 0
            if cls.opensquarebracket_held and (cls.opensquarebracket_allowed or keys_pressed < 2):
                input_text += "["
                cls.opensquarebracket_allowed = 0
            if cls.sharp_held and (cls.sharp_allowed or keys_pressed < 2):
                input_text += "#"
                cls.sharp_allowed = 0
            if cls.closesquarebracket_held and (cls.closesquarebracket_allowed or keys_pressed < 2):
                input_text += "]"
                cls.closesquarebracket_allowed = 0
            if cls.backtick_held and (cls.backtick_allowed or keys_pressed < 2):
                input_text += "`"
                cls.backtick_allowed = 0

            if not cls.capslock:
                if cls.a_held and (cls.a_allowed or keys_pressed < 2):
                    input_text += "a"
                    cls.a_allowed = 0
                if cls.b_held and (cls.b_allowed or keys_pressed < 2):
                    input_text += "b"
                    cls.b_allowed = 0
                if cls.c_held and (cls.c_allowed or keys_pressed < 2):
                    input_text += "c"
                    cls.c_allowed = 0
                if cls.d_held and (cls.d_allowed or keys_pressed < 2):
                    input_text += "d"
                    cls.d_allowed = 0
                if cls.e_held and (cls.e_allowed or keys_pressed < 2):
                    input_text += "e"
                    cls.e_allowed = 0
                if cls.f_held and (cls.f_allowed or keys_pressed < 2):
                    input_text += "f"
                    cls.f_allowed = 0
                if cls.g_held and (cls.g_allowed or keys_pressed < 2):
                    input_text += "g"
                    cls.g_allowed = 0
                if cls.h_held and (cls.h_allowed or keys_pressed < 2):
                    input_text += "h"
                    cls.h_allowed = 0
                if cls.i_held and (cls.i_allowed or keys_pressed < 2):
                    input_text += "i"
                    cls.i_allowed = 0
                if cls.j_held and (cls.j_allowed or keys_pressed < 2):
                    input_text += "j"
                    cls.j_allowed = 0
                if cls.k_held and (cls.k_allowed or keys_pressed < 2):
                    input_text += "k"
                    cls.k_allowed = 0
                if cls.l_held and (cls.l_allowed or keys_pressed < 2):
                    input_text += "l"
                    cls.l_allowed = 0
                if cls.m_held and (cls.m_allowed or keys_pressed < 2):
                    input_text += "m"
                    cls.m_allowed = 0
                if cls.n_held and (cls.n_allowed or keys_pressed < 2):
                    input_text += "n"
                    cls.n_allowed = 0
                if cls.o_held and (cls.o_allowed or keys_pressed < 2):
                    input_text += "o"
                    cls.o_allowed = 0
                if cls.p_held and (cls.p_allowed or keys_pressed < 2):
                    input_text += "p"
                    cls.p_allowed = 0
                if cls.q_held and (cls.q_allowed or keys_pressed < 2):
                    input_text += "q"
                    cls.q_allowed = 0
                if cls.r_held and (cls.r_allowed or keys_pressed < 2):
                    input_text += "r"
                    cls.r_allowed = 0
                if cls.s_held and (cls.s_allowed or keys_pressed < 2):
                    input_text += "s"
                    cls.s_allowed = 0
                if cls.t_held and (cls.t_allowed or keys_pressed < 2):
                    input_text += "t"
                    cls.t_allowed = 0
                if cls.u_held and (cls.u_allowed or keys_pressed < 2):
                    input_text += "u"
                    cls.u_allowed = 0
                if cls.v_held and (cls.v_allowed or keys_pressed < 2):
                    input_text += "v"
                    cls.v_allowed = 0
                if cls.w_held and (cls.w_allowed or keys_pressed < 2):
                    input_text += "w"
                    cls.w_allowed = 0
                if cls.x_held and (cls.x_allowed or keys_pressed < 2):
                    input_text += "x"
                    cls.x_allowed = 0
                if cls.y_held and (cls.y_allowed or keys_pressed < 2):
                    input_text += "y"
                    cls.y_allowed = 0
                if cls.z_held and (cls.z_allowed or keys_pressed < 2):
                    input_text += "z"
                    cls.z_allowed = 0
            else:
                if cls.a_held and (cls.a_allowed or keys_pressed < 2):
                    input_text += "A"
                    cls.a_allowed = 0
                if cls.b_held and (cls.b_allowed or keys_pressed < 2):
                    input_text += "B"
                    cls.b_allowed = 0
                if cls.c_held and (cls.c_allowed or keys_pressed < 2):
                    input_text += "C"
                    cls.c_allowed = 0
                if cls.d_held and (cls.d_allowed or keys_pressed < 2):
                    input_text += "D"
                    cls.d_allowed = 0
                if cls.e_held and (cls.e_allowed or keys_pressed < 2):
                    input_text += "E"
                    cls.e_allowed = 0
                if cls.f_held and (cls.f_allowed or keys_pressed < 2):
                    input_text += "F"
                    cls.f_allowed = 0
                if cls.g_held and (cls.g_allowed or keys_pressed < 2):
                    input_text += "G"
                    cls.g_allowed = 0
                if cls.h_held and (cls.h_allowed or keys_pressed < 2):
                    input_text += "H"
                    cls.h_allowed = 0
                if cls.i_held and (cls.i_allowed or keys_pressed < 2):
                    input_text += "I"
                    cls.i_allowed = 0
                if cls.j_held and (cls.j_allowed or keys_pressed < 2):
                    input_text += "J"
                    cls.j_allowed = 0
                if cls.k_held and (cls.k_allowed or keys_pressed < 2):
                    input_text += "K"
                    cls.k_allowed = 0
                if cls.l_held and (cls.l_allowed or keys_pressed < 2):
                    input_text += "L"
                    cls.l_allowed = 0
                if cls.m_held and (cls.m_allowed or keys_pressed < 2):
                    input_text += "M"
                    cls.m_allowed = 0
                if cls.n_held and (cls.n_allowed or keys_pressed < 2):
                    input_text += "N"
                    cls.n_allowed = 0
                if cls.o_held and (cls.o_allowed or keys_pressed < 2):
                    input_text += "O"
                    cls.o_allowed = 0
                if cls.p_held and (cls.p_allowed or keys_pressed < 2):
                    input_text += "P"
                    cls.p_allowed = 0
                if cls.q_held and (cls.q_allowed or keys_pressed < 2):
                    input_text += "Q"
                    cls.q_allowed = 0
                if cls.r_held and (cls.r_allowed or keys_pressed < 2):
                    input_text += "R"
                    cls.r_allowed = 0
                if cls.s_held and (cls.s_allowed or keys_pressed < 2):
                    input_text += "S"
                    cls.s_allowed = 0
                if cls.t_held and (cls.t_allowed or keys_pressed < 2):
                    input_text += "T"
                    cls.t_allowed = 0
                if cls.u_held and (cls.u_allowed or keys_pressed < 2):
                    input_text += "U"
                    cls.u_allowed = 0
                if cls.v_held and (cls.v_allowed or keys_pressed < 2):
                    input_text += "V"
                    cls.v_allowed = 0
                if cls.w_held and (cls.w_allowed or keys_pressed < 2):
                    input_text += "W"
                    cls.w_allowed = 0
                if cls.x_held and (cls.x_allowed or keys_pressed < 2):
                    input_text += "X"
                    cls.x_allowed = 0
                if cls.y_held and (cls.y_allowed or keys_pressed < 2):
                    input_text += "Y"
                    cls.y_allowed = 0
                if cls.z_held and (cls.z_allowed or keys_pressed < 2):
                    input_text += "Z"
                    cls.z_allowed = 0
        else:
            if cls.apostrophe_held and (cls.apostrophe_allowed or keys_pressed < 2):
                input_text += "@"
                cls.apostrophe_allowed = 0
            if cls.comma_held and (cls.comma_allowed or keys_pressed < 2):
                input_text += "<"
                cls.comma_allowed = 0
            if cls.minus_held and (cls.minus_allowed or keys_pressed < 2):
                input_text += "_"
                cls.minus_allowed = 0
            if cls.fullstop_held and (cls.fullstop_allowed or keys_pressed < 2):
                input_text += ">"
                cls.fullstop_allowed = 0
            if cls.forwardslash_held and (cls.forwardslash_allowed or keys_pressed < 2):
                input_text += "?"
                cls.forwardslash_allowed
            if cls.zero_held and (cls.zero_allowed or keys_pressed < 2):
                input_text += ")"
                cls.zero_allowed = 0
            if cls.one_held and (cls.one_allowed or keys_pressed < 2):
                input_text += "!"
                cls.one_allowed = 0
            if cls.two_held and (cls.two_allowed or keys_pressed < 2):
                input_text += "\""
                cls.two_allowed = 0
            if cls.three_held and (cls.three_allowed or keys_pressed < 2):
                input_text += "£"
                cls.three_allowed = 0
            if cls.four_held and (cls.four_allowed or keys_pressed < 2):
                input_text += "$"
                cls.four_allowed = 0
            if cls.five_held and (cls.five_allowed or keys_pressed < 2):
                input_text += "%"
                cls.five_allowed = 0
            if cls.six_held and (cls.six_allowed or keys_pressed < 2):
                input_text += "^"
                cls.six_allowed = 0
            if cls.seven_held and (cls.seven_allowed or keys_pressed < 2):
                input_text += "&"
                cls.seven_allowed = 0
            if cls.eight_held and (cls.eight_allowed or keys_pressed < 2):
                input_text += "*"
                cls.eight_allowed = 0
            if cls.nine_held and (cls.nine_allowed or keys_pressed < 2):
                input_text += "("
                cls.nine_allowed = 0
            if cls.semicolon_held and (cls.semicolon_allowed or keys_pressed < 2):
                input_text += ":"
                cls.semicolon_allowed = 0
            if cls.backslash_held and (cls.backslash_allowed or keys_pressed < 2):
                input_text += "|"
                cls.backslash_allowed = 0
            if cls.equals_held and (cls.equals_allowed or keys_pressed < 2):
                input_text += "+"
                cls.equals_allowed = 0
            if cls.opensquarebracket_held and (cls.opensquarebracket_allowed or keys_pressed < 2):
                input_text += "{"
                cls.opensquarebracket_allowed = 0
            if cls.sharp_held and (cls.sharp_allowed or keys_pressed < 2):
                input_text += "~"
                cls.sharp_allowed = 0
            if cls.closesquarebracket_held and (cls.closesquarebracket_allowed or keys_pressed < 2):
                input_text += "}"
                cls.closesquarebracket_allowed = 0
            if cls.backtick_held and (cls.backtick_allowed or keys_pressed < 2):
                input_text += "¬"
                cls.backtick_allowed = 0

            if cls.capslock:
                if cls.a_held and (cls.a_allowed or keys_pressed < 2):
                    input_text += "a"
                    cls.a_allowed = 0
                if cls.b_held and (cls.b_allowed or keys_pressed < 2):
                    input_text += "b"
                    cls.b_allowed = 0
                if cls.c_held and (cls.c_allowed or keys_pressed < 2):
                    input_text += "c"
                    cls.c_allowed = 0
                if cls.d_held and (cls.d_allowed or keys_pressed < 2):
                    input_text += "d"
                    cls.d_allowed = 0
                if cls.e_held and (cls.e_allowed or keys_pressed < 2):
                    input_text += "e"
                    cls.e_allowed = 0
                if cls.f_held and (cls.f_allowed or keys_pressed < 2):
                    input_text += "f"
                    cls.f_allowed = 0
                if cls.g_held and (cls.g_allowed or keys_pressed < 2):
                    input_text += "g"
                    cls.g_allowed = 0
                if cls.h_held and (cls.h_allowed or keys_pressed < 2):
                    input_text += "h"
                    cls.h_allowed = 0
                if cls.i_held and (cls.i_allowed or keys_pressed < 2):
                    input_text += "i"
                    cls.i_allowed = 0
                if cls.j_held and (cls.j_allowed or keys_pressed < 2):
                    input_text += "j"
                    cls.j_allowed = 0
                if cls.k_held and (cls.k_allowed or keys_pressed < 2):
                    input_text += "k"
                    cls.k_allowed = 0
                if cls.l_held and (cls.l_allowed or keys_pressed < 2):
                    input_text += "l"
                    cls.l_allowed = 0
                if cls.m_held and (cls.m_allowed or keys_pressed < 2):
                    input_text += "m"
                    cls.m_allowed = 0
                if cls.n_held and (cls.n_allowed or keys_pressed < 2):
                    input_text += "n"
                    cls.n_allowed = 0
                if cls.o_held and (cls.o_allowed or keys_pressed < 2):
                    input_text += "o"
                    cls.o_allowed = 0
                if cls.p_held and (cls.p_allowed or keys_pressed < 2):
                    input_text += "p"
                    cls.p_allowed = 0
                if cls.q_held and (cls.q_allowed or keys_pressed < 2):
                    input_text += "q"
                    cls.q_allowed = 0
                if cls.r_held and (cls.r_allowed or keys_pressed < 2):
                    input_text += "r"
                    cls.r_allowed = 0
                if cls.s_held and (cls.s_allowed or keys_pressed < 2):
                    input_text += "s"
                    cls.s_allowed = 0
                if cls.t_held and (cls.t_allowed or keys_pressed < 2):
                    input_text += "t"
                    cls.t_allowed = 0
                if cls.u_held and (cls.u_allowed or keys_pressed < 2):
                    input_text += "u"
                    cls.u_allowed = 0
                if cls.v_held and (cls.v_allowed or keys_pressed < 2):
                    input_text += "v"
                    cls.v_allowed = 0
                if cls.w_held and (cls.w_allowed or keys_pressed < 2):
                    input_text += "w"
                    cls.w_allowed = 0
                if cls.x_held and (cls.x_allowed or keys_pressed < 2):
                    input_text += "x"
                    cls.x_allowed = 0
                if cls.y_held and (cls.y_allowed or keys_pressed < 2):
                    input_text += "y"
                    cls.y_allowed = 0
                if cls.z_held and (cls.z_allowed or keys_pressed < 2):
                    input_text += "z"
                    cls.z_allowed = 0
            else:
                if cls.a_held and (cls.a_allowed or keys_pressed < 2):
                    input_text += "A"
                    cls.a_allowed = 0
                if cls.b_held and (cls.b_allowed or keys_pressed < 2):
                    input_text += "B"
                    cls.b_allowed = 0
                if cls.c_held and (cls.c_allowed or keys_pressed < 2):
                    input_text += "C"
                    cls.c_allowed = 0
                if cls.d_held and (cls.d_allowed or keys_pressed < 2):
                    input_text += "D"
                    cls.d_allowed = 0
                if cls.e_held and (cls.e_allowed or keys_pressed < 2):
                    input_text += "E"
                    cls.e_allowed = 0
                if cls.f_held and (cls.f_allowed or keys_pressed < 2):
                    input_text += "F"
                    cls.f_allowed = 0
                if cls.g_held and (cls.g_allowed or keys_pressed < 2):
                    input_text += "G"
                    cls.g_allowed = 0
                if cls.h_held and (cls.h_allowed or keys_pressed < 2):
                    input_text += "H"
                    cls.h_allowed = 0
                if cls.i_held and (cls.i_allowed or keys_pressed < 2):
                    input_text += "I"
                    cls.i_allowed = 0
                if cls.j_held and (cls.j_allowed or keys_pressed < 2):
                    input_text += "J"
                    cls.j_allowed = 0
                if cls.k_held and (cls.k_allowed or keys_pressed < 2):
                    input_text += "K"
                    cls.k_allowed = 0
                if cls.l_held and (cls.l_allowed or keys_pressed < 2):
                    input_text += "L"
                    cls.l_allowed = 0
                if cls.m_held and (cls.m_allowed or keys_pressed < 2):
                    input_text += "M"
                    cls.m_allowed = 0
                if cls.n_held and (cls.n_allowed or keys_pressed < 2):
                    input_text += "N"
                    cls.n_allowed = 0
                if cls.o_held and (cls.o_allowed or keys_pressed < 2):
                    input_text += "O"
                    cls.o_allowed = 0
                if cls.p_held and (cls.p_allowed or keys_pressed < 2):
                    input_text += "P"
                    cls.p_allowed = 0
                if cls.q_held and (cls.q_allowed or keys_pressed < 2):
                    input_text += "Q"
                    cls.q_allowed = 0
                if cls.r_held and (cls.r_allowed or keys_pressed < 2):
                    input_text += "R"
                    cls.r_allowed = 0
                if cls.s_held and (cls.s_allowed or keys_pressed < 2):
                    input_text += "S"
                    cls.s_allowed = 0
                if cls.t_held and (cls.t_allowed or keys_pressed < 2):
                    input_text += "T"
                    cls.t_allowed = 0
                if cls.u_held and (cls.u_allowed or keys_pressed < 2):
                    input_text += "U"
                    cls.u_allowed = 0
                if cls.v_held and (cls.v_allowed or keys_pressed < 2):
                    input_text += "V"
                    cls.v_allowed = 0
                if cls.w_held and (cls.w_allowed or keys_pressed < 2):
                    input_text += "W"
                    cls.w_allowed = 0
                if cls.x_held and (cls.x_allowed or keys_pressed < 2):
                    input_text += "X"
                    cls.x_allowed = 0
                if cls.y_held and (cls.y_allowed or keys_pressed < 2):
                    input_text += "Y"
                    cls.y_allowed = 0
                if cls.z_held and (cls.z_allowed or keys_pressed < 2):
                    input_text += "Z"
                    cls.z_allowed = 0

        if cls.delete_held and (cls.delete_allowed or keys_pressed < 2):  # for if there is a cursor so you can go backwards and type there in the future
            ###insert code here###
            cls.delete_allowed = 0
        if cls.numpad0_held and (cls.numpad0_allowed or keys_pressed < 2):
            input_text += "0"
            numpad0_allowed = 0
        if cls.numpad1_held and (cls.numpad1_allowed or keys_pressed < 2):
            input_text += "1"
            numpad1_allowed = 0
        if cls.numpad2_held and (cls.numpad2_allowed or keys_pressed < 2):
            input_text += "2"
            numpad2_allowed = 0
        if cls.numpad3_held and (cls.numpad3_allowed or keys_pressed < 2):
            input_text += "3"
            numpad3_allowed = 0
        if cls.numpad4_held and (cls.numpad4_allowed or keys_pressed < 2):
            input_text += "4"
            numpad4_allowed = 0
        if cls.numpad5_held and (cls.numpad4_allowed or keys_pressed < 2):
            input_text += "5"
            numpad4_allowed = 0
        if cls.numpad6_held and (cls.numpad6_allowed or keys_pressed < 2):
            input_text += "6"
            numpad6_allowed = 0
        if cls.numpad7_held and (cls.numpad7_allowed or keys_pressed < 2):
            input_text += "7"
            numpad7_allowed = 0
        if cls.numpad8_held and (cls.numpad8_allowed or keys_pressed < 2):
            input_text += "8"
            numpad8_allowed = 0
        if cls.numpad9_held and (cls.numpad9_allowed or keys_pressed < 2):
            input_text += "9"
            numpad9_allowed = 0
        if cls.numpaddivide_held and (cls.numpaddivide_allowed or keys_pressed < 2):
            input_text += "/"
            cls.numpaddivide_allowed = 0
        if cls.numpadmultiply_held and (cls.numpadmultiply_allowed or keys_pressed < 2):
            input_text += "*"
            numpadmultiply = 0
        if cls.numpadminus_held and (cls.numpadminus_allowed or keys_pressed < 2):
            input_text += "-"
            cls.numpadminus_allowed = 0
        if cls.numpadplus_held and (cls.numpadplus_allowed or keys_pressed < 2):
            input_text += "+"
            cls.numpadplus_allowed = 0
        if cls.numpadenter_held and (cls.numpadenter_allowed or keys_pressed < 2):
            accepting_text = False
            cls.numpadenter_allowed = 0
        if cls.rightarrow_held:  # for if there is a cursor so you can go backwards and type there in the future
            pass
        if cls.leftarrow_held:  # for if there is a cursor so you can go backwards and type there in the future
            pass

        return input_text
