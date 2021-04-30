# -*- coding: utf-8 -*-
if backspace_held and input_text != "":
    input_text = input_text[:-1]

if len(input_text) <= maximum_characters:
    if tab_held and (tab_allowed or keys_pressed < 2):
        input_text += "    "
        tab_allowed = 0
    if enter_held and (enter_allowed or keys_pressed < 2):
        accepting_text = False
        enter_allowed = 0
    if space_held and (space_allowed or keys_pressed < 2):
        input_text += " "
        space_allowed = 0

    if not shift_held: 
        if apostrophe_held and (apostrophe_allowed or keys_pressed < 2):
            input_text += "'"
            apostrophe_allowed = 0
        if comma_held and (comma_allowed or keys_pressed < 2):
            input_text += ","
            comma_allowed = 0
        if minus_held and (minus_allowed or keys_pressed < 2):
            input_text += "-"
            minus_allowed = 0
        if fullstop_held and (fullstop_allowed or keys_pressed < 2):
            input_text += "."
            fullstop_allowed = 0
        if forwardslash_held and (forwardslash_allowed or keys_pressed < 2):
            input_text += "/"
            forwardslash_allowed = 0
        if zero_held and (zero_allowed or keys_pressed < 2):
            input_text += "0"
            zero_allowed = 0
        if one_held and (one_allowed or keys_pressed < 2):
            input_text += "1"
            one_allowed = 0
        if two_held and (two_allowed or keys_pressed < 2):
            input_text += "2"
            two_allowed = 0
        if three_held and (three_allowed or keys_pressed < 2):
            input_text += "3"
            three_allowed = 0
        if four_held and (four_allowed or keys_pressed < 2):
            input_text += "4"
            four_allowed = 0
        if five_held and (five_allowed or keys_pressed < 2):
            input_text += "5"
            five_allowed = 0
        if six_held and (six_allowed or keys_pressed < 2):
            input_text += "6"
            six_allowed = 0
        if seven_held and (seven_allowed or keys_pressed < 2):
            input_text += "7"
            seven_allowed = 0
        if eight_held and (eight_allowed or keys_pressed < 2):
            input_text += "8"
            eight_allowed = 0
        if nine_held and (nine_allowed or keys_pressed < 2):
            input_text += "9"
            nine_allowed = 0
        if semicolon_held and (semicolon_allowed or keys_pressed < 2):
            input_text += ";"
            semicolon_allowed = 0
        if backslash_held and (backslash_allowed or keys_pressed < 2):
            input_text += "\\"
            backslash_allowed = 0
        if equals_held and (equals_allowed or keys_pressed < 2):
            input_text += "="
            equals_allowed = 0
        if opensquarebracket_held and (opensquarebracket_allowed or keys_pressed < 2):
            input_text += "["
            opensquarebracket_allowed = 0
        if sharp_held and (sharp_allowed or keys_pressed < 2):
            input_text += "#"
            sharp_allowed = 0
        if closesquarebracket_held and (closesquarebracket_allowed or keys_pressed < 2):
            input_text += "]"
            closesquarebracket_allowed = 0
        if backtick_held and (backtick_allowed or keys_pressed < 2):
            input_text += "`"
            backtick_allowed = 0

        if not capslock:
            if a_held and (a_allowed or keys_pressed < 2):
                input_text += "a"
                a_allowed = 0
            if b_held and (b_allowed or keys_pressed < 2):
                input_text += "b"
                b_allowed = 0
            if c_held and (c_allowed or keys_pressed < 2):
                input_text += "c"
                c_allowed = 0
            if d_held and (d_allowed or keys_pressed < 2):
                input_text += "d"
                d_allowed = 0
            if e_held and (e_allowed or keys_pressed < 2):
                input_text += "e"
                e_allowed = 0
            if f_held and (f_allowed or keys_pressed < 2):
                input_text += "f"
                f_allowed = 0
            if g_held and (g_allowed or keys_pressed < 2):
                input_text += "g"
                g_allowed = 0
            if h_held and (h_allowed or keys_pressed < 2):
                input_text += "h"
                h_allowed = 0
            if i_held and (i_allowed or keys_pressed < 2):
                input_text += "i"
                i_allowed = 0
            if j_held and (j_allowed or keys_pressed < 2):
                input_text += "j"
                j_allowed = 0
            if k_held and (k_allowed or keys_pressed < 2):
                input_text += "k"
                k_allowed = 0
            if l_held and (l_allowed or keys_pressed < 2):
                input_text += "l"
                l_allowed = 0
            if m_held and (m_allowed or keys_pressed < 2):
                input_text += "m"
                m_allowed = 0
            if n_held and (n_allowed or keys_pressed < 2):
                input_text += "n"
                n_allowed = 0
            if o_held and (o_allowed or keys_pressed < 2):
                input_text += "o"
                o_allowed = 0
            if p_held and (p_allowed or keys_pressed < 2):
                input_text += "p"
                p_allowed = 0
            if q_held and (q_allowed or keys_pressed < 2):
                input_text += "q"
                q_allowed = 0
            if r_held and (r_allowed or keys_pressed < 2):
                input_text += "r"
                r_allowed = 0
            if s_held and (s_allowed or keys_pressed < 2):
                input_text += "s"
                s_allowed = 0
            if t_held and (t_allowed or keys_pressed < 2):
                input_text += "t"
                t_allowed = 0
            if u_held and (u_allowed or keys_pressed < 2):
                input_text += "u"
                u_allowed = 0
            if v_held and (v_allowed or keys_pressed < 2):
                input_text += "v"
                v_allowed = 0
            if w_held and (w_allowed or keys_pressed < 2):
                input_text += "w"
                w_allowed = 0
            if x_held and (x_allowed or keys_pressed < 2):
                input_text += "x"
                x_allowed = 0
            if y_held and (y_allowed or keys_pressed < 2):
                input_text += "y"
                y_allowed = 0
            if z_held and (z_allowed or keys_pressed < 2):
                input_text += "z"
                z_allowed = 0
        else:
            if a_held and (a_allowed or keys_pressed < 2):
                input_text += "A"
                a_allowed = 0
            if b_held and (b_allowed or keys_pressed < 2):
                input_text += "B"
                b_allowed = 0
            if c_held and (c_allowed or keys_pressed < 2):
                input_text += "C"
                c_allowed = 0
            if d_held and (d_allowed or keys_pressed < 2):
                input_text += "D"
                d_allowed = 0
            if e_held and (e_allowed or keys_pressed < 2):
                input_text += "E"
                e_allowed = 0
            if f_held and (f_allowed or keys_pressed < 2):
                input_text += "F"
                f_allowed = 0
            if g_held and (g_allowed or keys_pressed < 2):
                input_text += "G"
                g_allowed = 0
            if h_held and (h_allowed or keys_pressed < 2):
                input_text += "H"
                h_allowed = 0
            if i_held and (i_allowed or keys_pressed < 2):
                input_text += "I"
                i_allowed = 0
            if j_held and (j_allowed or keys_pressed < 2):
                input_text += "J"
                j_allowed = 0
            if k_held and (k_allowed or keys_pressed < 2):
                input_text += "K"
                k_allowed = 0
            if l_held and (l_allowed or keys_pressed < 2):
                input_text += "L"
                l_allowed = 0
            if m_held and (m_allowed or keys_pressed < 2):
                input_text += "M"
                m_allowed = 0
            if n_held and (n_allowed or keys_pressed < 2):
                input_text += "N"
                n_allowed = 0
            if o_held and (o_allowed or keys_pressed < 2):
                input_text += "O"
                o_allowed = 0
            if p_held and (p_allowed or keys_pressed < 2):
                input_text += "P"
                p_allowed = 0
            if q_held and (q_allowed or keys_pressed < 2):
                input_text += "Q"
                q_allowed = 0
            if r_held and (r_allowed or keys_pressed < 2):
                input_text += "R"
                r_allowed = 0
            if s_held and (s_allowed or keys_pressed < 2):
                input_text += "S"
                s_allowed = 0
            if t_held and (t_allowed or keys_pressed < 2):
                input_text += "T"
                t_allowed = 0
            if u_held and (u_allowed or keys_pressed < 2):
                input_text += "U"
                u_allowed = 0
            if v_held and (v_allowed or keys_pressed < 2):
                input_text += "V"
                v_allowed = 0
            if w_held and (w_allowed or keys_pressed < 2):
                input_text += "W"
                w_allowed = 0
            if x_held and (x_allowed or keys_pressed < 2):
                input_text += "X"
                x_allowed = 0
            if y_held and (y_allowed or keys_pressed < 2):
                input_text += "Y"
                y_allowed = 0
            if z_held and (z_allowed or keys_pressed < 2):
                input_text += "Z"
                z_allowed = 0
    else:
        if apostrophe_held and (apostrophe_allowed or keys_pressed < 2):
            input_text += "@"
            apostrophe_allowed = 0
        if comma_held and (comma_allowed or keys_pressed < 2):
            input_text += "<"
            comma_allowed = 0
        if minus_held and (minus_allowed or keys_pressed < 2):
            input_text += "_"
            minus_allowed = 0
        if fullstop_held and (fullstop_allowed or keys_pressed < 2):
            input_text += ">"
            fullstop_allowed = 0
        if forwardslash_held and (forwardslash_allowed or keys_pressed < 2):
            input_text += "?"
            forwardslash_allowed
        if zero_held and (zero_allowed or keys_pressed < 2):
            input_text += ")"
            zero_allowed = 0
        if one_held and (one_allowed or keys_pressed < 2):
            input_text += "!"
            one_allowed = 0
        if two_held and (two_allowed or keys_pressed < 2):
            input_text += "\""
            two_allowed = 0
        if three_held and (three_allowed or keys_pressed < 2):
            input_text += "£"
            three_allowed = 0
        if four_held and (four_allowed or keys_pressed < 2):
            input_text += "$"
            four_allowed = 0
        if five_held and (five_allowed or keys_pressed < 2):
            input_text += "%"
            five_allowed = 0
        if six_held and (six_allowed or keys_pressed < 2):
            input_text += "^"
            six_allowed = 0
        if seven_held and (seven_allowed or keys_pressed < 2):
            input_text += "&"
            seven_allowed = 0
        if eight_held and (eight_allowed or keys_pressed < 2):
            input_text += "*"
            eight_allowed = 0
        if nine_held and (nine_allowed or keys_pressed < 2):
            input_text += "("
            nine_allowed = 0
        if semicolon_held and (semicolon_allowed or keys_pressed < 2):
            input_text += ":"
            semicolon_allowed = 0
        if backslash_held and (backslash_allowed or keys_pressed < 2):
            input_text += "|"
            backslash_allowed = 0
        if equals_held and (equals_allowed or keys_pressed < 2):
            input_text += "+"
            equals_allowed = 0
        if opensquarebracket_held and (opensquarebracket_allowed or keys_pressed < 2):
            input_text += "{"
            opensquarebracket_allowed = 0
        if sharp_held and (sharp_allowed or keys_pressed < 2):
            input_text += "~"
            sharp_allowed = 0
        if closesquarebracket_held and (closesquarebracket_allowed or keys_pressed < 2):
            input_text += "}"
            closesquarebracket_allowed = 0
        if backtick_held and (backtick_allowed or keys_pressed < 2):
            input_text += "¬"
            backtick_allowed = 0

        if capslock:
            if a_held and (a_allowed or keys_pressed < 2):
                input_text += "a"
                a_allowed = 0
            if b_held and (b_allowed or keys_pressed < 2):
                input_text += "b"
                b_allowed = 0
            if c_held and (c_allowed or keys_pressed < 2):
                input_text += "c"
                c_allowed = 0
            if d_held and (d_allowed or keys_pressed < 2):
                input_text += "d"
                d_allowed = 0
            if e_held and (e_allowed or keys_pressed < 2):
                input_text += "e"
                e_allowed = 0
            if f_held and (f_allowed or keys_pressed < 2):
                input_text += "f"
                f_allowed = 0
            if g_held and (g_allowed or keys_pressed < 2):
                input_text += "g"
                g_allowed = 0
            if h_held and (h_allowed or keys_pressed < 2):
                input_text += "h"
                h_allowed = 0
            if i_held and (i_allowed or keys_pressed < 2):
                input_text += "i"
                i_allowed = 0
            if j_held and (j_allowed or keys_pressed < 2):
                input_text += "j"
                j_allowed = 0
            if k_held and (k_allowed or keys_pressed < 2):
                input_text += "k"
                k_allowed = 0
            if l_held and (l_allowed or keys_pressed < 2):
                input_text += "l"
                l_allowed = 0
            if m_held and (m_allowed or keys_pressed < 2):
                input_text += "m"
                m_allowed = 0
            if n_held and (n_allowed or keys_pressed < 2):
                input_text += "n"
                n_allowed = 0
            if o_held and (o_allowed or keys_pressed < 2):
                input_text += "o"
                o_allowed = 0
            if p_held and (p_allowed or keys_pressed < 2):
                input_text += "p"
                p_allowed = 0
            if q_held and (q_allowed or keys_pressed < 2):
                input_text += "q"
                q_allowed = 0
            if r_held and (r_allowed or keys_pressed < 2):
                input_text += "r"
                r_allowed = 0
            if s_held and (s_allowed or keys_pressed < 2):
                input_text += "s"
                s_allowed = 0
            if t_held and (t_allowed or keys_pressed < 2):
                input_text += "t"
                t_allowed = 0
            if u_held and (u_allowed or keys_pressed < 2):
                input_text += "u"
                u_allowed = 0
            if v_held and (v_allowed or keys_pressed < 2):
                input_text += "v"
                v_allowed = 0
            if w_held and (w_allowed or keys_pressed < 2):
                input_text += "w"
                w_allowed = 0
            if x_held and (x_allowed or keys_pressed < 2):
                input_text += "x"
                x_allowed = 0
            if y_held and (y_allowed or keys_pressed < 2):
                input_text += "y"
                y_allowed = 0
            if z_held and (z_allowed or keys_pressed < 2):
                input_text += "z"
                z_allowed = 0
        else:
            if a_held and (a_allowed or keys_pressed < 2):
                input_text += "A"
                a_allowed = 0
            if b_held and (b_allowed or keys_pressed < 2):
                input_text += "B"
                b_allowed = 0
            if c_held and (c_allowed or keys_pressed < 2):
                input_text += "C"
                c_allowed = 0
            if d_held and (d_allowed or keys_pressed < 2):
                input_text += "D"
                d_allowed = 0
            if e_held and (e_allowed or keys_pressed < 2):
                input_text += "E"
                e_allowed = 0
            if f_held and (f_allowed or keys_pressed < 2):
                input_text += "F"
                f_allowed = 0
            if g_held and (g_allowed or keys_pressed < 2):
                input_text += "G"
                g_allowed = 0
            if h_held and (h_allowed or keys_pressed < 2):
                input_text += "H"
                h_allowed = 0
            if i_held and (i_allowed or keys_pressed < 2):
                input_text += "I"
                i_allowed = 0
            if j_held and (j_allowed or keys_pressed < 2):
                input_text += "J"
                j_allowed = 0
            if k_held and (k_allowed or keys_pressed < 2):
                input_text += "K"
                k_allowed = 0
            if l_held and (l_allowed or keys_pressed < 2):
                input_text += "L"
                l_allowed = 0
            if m_held and (m_allowed or keys_pressed < 2):
                input_text += "M"
                m_allowed = 0
            if n_held and (n_allowed or keys_pressed < 2):
                input_text += "N"
                n_allowed = 0
            if o_held and (o_allowed or keys_pressed < 2):
                input_text += "O"
                o_allowed = 0
            if p_held and (p_allowed or keys_pressed < 2):
                input_text += "P"
                p_allowed = 0
            if q_held and (q_allowed or keys_pressed < 2):
                input_text += "Q"
                q_allowed = 0
            if r_held and (r_allowed or keys_pressed < 2):
                input_text += "R"
                r_allowed = 0
            if s_held and (s_allowed or keys_pressed < 2):
                input_text += "S"
                s_allowed = 0
            if t_held and (t_allowed or keys_pressed < 2):
                input_text += "T"
                t_allowed = 0
            if u_held and (u_allowed or keys_pressed < 2):
                input_text += "U"
                u_allowed = 0
            if v_held and (v_allowed or keys_pressed < 2):
                input_text += "V"
                v_allowed = 0
            if w_held and (w_allowed or keys_pressed < 2):
                input_text += "W"
                w_allowed = 0
            if x_held and (x_allowed or keys_pressed < 2):
                input_text += "X"
                x_allowed = 0
            if y_held and (y_allowed or keys_pressed < 2):
                input_text += "Y"
                y_allowed = 0
            if z_held and (z_allowed or keys_pressed < 2):
                input_text += "Z"
                z_allowed = 0
        
    if delete_held and (delete_allowed or keys_pressed < 2):# for if there is a cursor so you can go backwards and type there in the future
        ###insert code here###
        delete_allowed = 0
    if numpad0_held and (numpad0_allowed or keys_pressed < 2):
        input_text += "0"
        numpad0_allowed = 0
    if numpad1_held and (numpad1_allowed or keys_pressed < 2):
        input_text += "1"
        numpad1_allowed = 0
    if numpad2_held and (numpad2_allowed or keys_pressed < 2):
        input_text += "2"
        numpad2_allowed = 0
    if numpad3_held and (numpad3_allowed or keys_pressed < 2):
        input_text += "3"
        numpad3_allowed = 0
    if numpad4_held and (numpad4_allowed or keys_pressed < 2):
        input_text += "4"
        numpad4_allowed = 0
    if numpad5_held and (numpad4_allowed or keys_pressed < 2):
        input_text += "5"
        numpad4_allowed = 0
    if numpad6_held and (numpad6_allowed or keys_pressed < 2):
        input_text += "6"   
        numpad6_allowed = 0 
    if numpad7_held and (numpad7_allowed or keys_pressed < 2):
        input_text += "7"    
        numpad7_allowed = 0
    if numpad8_held and (numpad8_allowed or keys_pressed < 2):
        input_text += "8"
        numpad8_allowed = 0
    if numpad9_held and (numpad9_allowed or keys_pressed < 2):
        input_text += "9"    
        numpad9_allowed = 0
    if numpaddivide_held and (numpaddivide_allowed or keys_pressed < 2):
        input_text += "/"    
        numpaddivide_allowed = 0
    if numpadmultiply_held and (numpadmultiply_allowed or keys_pressed < 2):
        input_text += "*"    
        numpadmultiply = 0
    if numpadminus_held and (numpadminus_allowed or keys_pressed < 2):
        input_text += "-"    
        numpadminus_allowed = 0
    if numpadplus_held and (numpadplus_allowed or keys_pressed < 2):
        input_text += "+"    
        numpadplus_allowed = 0
    if numpadenter_held and (numpadenter_allowed or keys_pressed < 2):
        accepting_text = False 
        numpadenter_allowed = 0
    if rightarrow_held:# for if there is a cursor so you can go backwards and type there in the future
        pass
    if leftarrow_held:# for if there is a cursor so you can go backwards and type there in the future
        pass
