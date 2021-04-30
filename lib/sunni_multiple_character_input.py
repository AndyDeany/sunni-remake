# -*- coding: utf-8 -*-
if backspace_held_time > fps/2:
    input_text = input_text[:-1]

if len(input_text) <= maximum_characters:
    if tab_held_time > fps/2:
        input_text += "    "
    if enter_held_time > fps/2:
        pass
    if space_held_time > fps/2:
        input_text += " "

    if not shift_held:
        if apostrophe_held_time > fps/2:
            input_text += "'"
        if comma_held_time > fps/2:
            input_text += ","
        if minus_held_time > fps/2:
            input_text += "-"
        if fullstop_held_time > fps/2:
            input_text += "."
        if forwardslash_held_time > fps/2:
            input_text += "/"
        if zero_held_time > fps/2:
            input_text += "0"
        if one_held_time > fps/2:
            input_text += "1"
        if two_held_time > fps/2:
            input_text += "2"
        if three_held_time > fps/2:
            input_text += "3"
        if four_held_time > fps/2:
            input_text += "4"
        if five_held_time > fps/2:
            input_text += "5"
        if six_held_time > fps/2:
            input_text += "6"
        if seven_held_time > fps/2:
            input_text += "7"
        if eight_held_time > fps/2:
            input_text += "8"
        if nine_held_time > fps/2:
            input_text += "9"
        if semicolon_held_time > fps/2:
            input_text += ";"
        if backslash_held_time > fps/2:
            input_text += "\\"
        if equals_held_time > fps/2:
            input_text += "="
        if opensquarebracket_held_time > fps/2:
            input_text += "["
        if sharp_held_time > fps/2:
            input_text += "#"
        if closesquarebracket_held_time > fps/2:
            input_text += "]"
        if backtick_held_time > fps/2:
            input_text += "`"

        if not capslock:
            if a_held_time > fps/2:
                input_text += "a"
            if b_held_time > fps/2:
                input_text += "b"
            if c_held_time > fps/2:
                input_text += "c"
            if d_held_time > fps/2:
                input_text += "d"
            if e_held_time > fps/2:
                input_text += "e"
            if f_held_time > fps/2:
                input_text += "f"
            if g_held_time > fps/2:
                input_text += "g"
            if h_held_time > fps/2:
                input_text += "h"
            if i_held_time > fps/2:
                input_text += "i"
            if j_held_time > fps/2:
                input_text += "j"
            if k_held_time > fps/2:
                input_text += "k"
            if l_held_time > fps/2:
                input_text += "l"
            if m_held_time > fps/2:
                input_text += "m"
            if n_held_time > fps/2:
                input_text += "n"
            if o_held_time > fps/2:
                input_text += "o"
            if p_held_time > fps/2:
                input_text += "p"
            if q_held_time > fps/2:
                input_text += "q"
            if r_held_time > fps/2:
                input_text += "r"
            if s_held_time > fps/2:
                input_text += "s"
            if t_held_time > fps/2:
                input_text += "t"
            if u_held_time > fps/2:
                input_text += "u"
            if v_held_time > fps/2:
                input_text += "v"
            if w_held_time > fps/2:
                input_text += "w"
            if x_held_time > fps/2:
                input_text += "x"
            if y_held_time > fps/2:
                input_text += "y"
            if z_held_time > fps/2:
                input_text += "z"
        else:
            if a_held_time > fps/2:
                input_text += "A"
            if b_held_time > fps/2:
                input_text += "B"
            if c_held_time > fps/2:
                input_text += "C"
            if d_held_time > fps/2:
                input_text += "D"
            if e_held_time > fps/2:
                input_text += "E"
            if f_held_time > fps/2:
                input_text += "F"
            if g_held_time > fps/2:
                input_text += "G"
            if h_held_time > fps/2:
                input_text += "H"
            if i_held_time > fps/2:
                input_text += "I"
            if j_held_time > fps/2:
                input_text += "J"
            if k_held_time > fps/2:
                input_text += "K"
            if l_held_time > fps/2:
                input_text += "L"
            if m_held_time > fps/2:
                input_text += "M"
            if n_held_time > fps/2:
                input_text += "N"
            if o_held_time > fps/2:
                input_text += "O"
            if p_held_time > fps/2:
                input_text += "P"
            if q_held_time > fps/2:
                input_text += "Q"
            if r_held_time > fps/2:
                input_text += "R"
            if s_held_time > fps/2:
                input_text += "S"
            if t_held_time > fps/2:
                input_text += "T"
            if u_held_time > fps/2:
                input_text += "U"
            if v_held_time > fps/2:
                input_text += "V"
            if w_held_time > fps/2:
                input_text += "W"
            if x_held_time > fps/2:
                input_text += "X"
            if y_held_time > fps/2:
                input_text += "Y"
            if z_held_time > fps/2:
                input_text += "Z"
    else:
        if apostrophe_held_time > fps/2:
            input_text += "@"
        if comma_held_time > fps/2:
            input_text += "<"
        if minus_held_time > fps/2:
            input_text += "_"
        if fullstop_held_time > fps/2:
            input_text += ">"
        if forwardslash_held_time > fps/2:
            input_text += "?"
        if zero_held_time > fps/2:
            input_text += ")"
        if one_held_time > fps/2:
            input_text += "!"
        if two_held_time > fps/2:
            input_text += "\""
        if three_held_time > fps/2:
            input_text += unichr(163)
        if four_held_time > fps/2:
            input_text += "$"
        if five_held_time > fps/2:
            input_text += "%"
        if six_held_time > fps/2:
            input_text += "^"
        if seven_held_time > fps/2:
            input_text += "&"
        if eight_held_time > fps/2:
            input_text += "*"
        if nine_held_time > fps/2:
            input_text += "("
        if semicolon_held_time > fps/2:
            input_text += ":"
        if backslash_held_time > fps/2:
            input_text += "|"
        if equals_held_time > fps/2:
            input_text += "+"
        if opensquarebracket_held_time > fps/2:
            input_text += "{"
        if sharp_held_time > fps/2:
            input_text += "~"
        if closesquarebracket_held_time > fps/2:
            input_text += "}"
        if backtick_held_time > fps/2:
            input_text += "¬"

        if capslock:
            if a_held_time > fps/2:
                input_text += "a"
            if b_held_time > fps/2:
                input_text += "b"
            if c_held_time > fps/2:
                input_text += "c"
            if d_held_time > fps/2:
                input_text += "d"
            if e_held_time > fps/2:
                input_text += "e"
            if f_held_time > fps/2:
                input_text += "f"
            if g_held_time > fps/2:
                input_text += "g"
            if h_held_time > fps/2:
                input_text += "h"
            if i_held_time > fps/2:
                input_text += "i"
            if j_held_time > fps/2:
                input_text += "j"
            if k_held_time > fps/2:
                input_text += "k"
            if l_held_time > fps/2:
                input_text += "l"
            if m_held_time > fps/2:
                input_text += "m"
            if n_held_time > fps/2:
                input_text += "n"
            if o_held_time > fps/2:
                input_text += "o"
            if p_held_time > fps/2:
                input_text += "p"
            if q_held_time > fps/2:
                input_text += "q"
            if r_held_time > fps/2:
                input_text += "r"
            if s_held_time > fps/2:
                input_text += "s"
            if t_held_time > fps/2:
                input_text += "t"
            if u_held_time > fps/2:
                input_text += "u"
            if v_held_time > fps/2:
                input_text += "v"
            if w_held_time > fps/2:
                input_text += "w"
            if x_held_time > fps/2:
                input_text += "x"
            if y_held_time > fps/2:
                input_text += "y"
            if z_held_time > fps/2:
                input_text += "z"
        else:
            if a_held_time > fps/2:
                input_text += "A"
            if b_held_time > fps/2:
                input_text += "B"
            if c_held_time > fps/2:
                input_text += "C"
            if d_held_time > fps/2:
                input_text += "D"
            if e_held_time > fps/2:
                input_text += "E"
            if f_held_time > fps/2:
                input_text += "F"
            if g_held_time > fps/2:
                input_text += "G"
            if h_held_time > fps/2:
                input_text += "H"
            if i_held_time > fps/2:
                input_text += "I"
            if j_held_time > fps/2:
                input_text += "J"
            if k_held_time > fps/2:
                input_text += "K"
            if l_held_time > fps/2:
                input_text += "L"
            if m_held_time > fps/2:
                input_text += "M"
            if n_held_time > fps/2:
                input_text += "N"
            if o_held_time > fps/2:
                input_text += "O"
            if p_held_time > fps/2:
                input_text += "P"
            if q_held_time > fps/2:
                input_text += "Q"
            if r_held_time > fps/2:
                input_text += "R"
            if s_held_time > fps/2:
                input_text += "S"
            if t_held_time > fps/2:
                input_text += "T"
            if u_held_time > fps/2:
                input_text += "U"
            if v_held_time > fps/2:
                input_text += "V"
            if w_held_time > fps/2:
                input_text += "W"
            if x_held_time > fps/2:
                input_text += "X"
            if y_held_time > fps/2:
                input_text += "Y"
            if z_held_time > fps/2:
                input_text += "Z"    
                
    if delete_held_time > fps/2: # for if there is a cursor so you can go backwards and type there in the future
        pass
    if numpad0_held_time > fps/2:
        input_text += "0"
    if numpad1_held_time > fps/2:
        input_text += "1"
    if numpad2_held_time > fps/2:
        input_text += "2"
    if numpad3_held_time > fps/2:
        input_text += "3"
    if numpad4_held_time > fps/2:
        input_text += "4"
    if numpad5_held_time > fps/2:
        input_text += "5"
    if numpad6_held_time > fps/2:
        input_text += "6"
    if numpad7_held_time > fps/2:
        input_text += "7"
    if numpad8_held_time > fps/2:
        input_text += "8"
    if numpad9_held_time > fps/2:
        input_text += "9"
    if numpaddivide_held_time > fps/2:
        input_text += "/"
    if numpadmultiply_held_time > fps/2:
        input_text += "*"
    if numpadminus_held_time > fps/2:
        input_text += "-"
    if numpadplus_held_time > fps/2:
        input_text += "+"
    if numpadenter_held_time > fps/2:
        pass
    if rightarrow_held_time > fps/2: # for if there is a cursor so you can go backwards and type there in the future
       pass
    if leftarrow_held_time > fps/2:  # for if there is a cursor so you can go backwards and type there in the future
        pass

