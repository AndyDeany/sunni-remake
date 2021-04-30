# -*- coding: utf-8 -*-
if backspace_held and input_text != "":
    input_text = input_text[:-1]
    last_character = ""
    second_last_character = ""
if tab_held and (last_character != "    " and second_last_character != "    " or keys_pressed < 2):
    input_text += "    "
    second_last_character = last_c nbharacter
    last_character = "    "
if enter_held and (last_character != "\n" and second_last_character != "\n" or keys_pressed < 2):
    input_text += "\n"
    second_last_character = last_character
    last_character = "\n"
if space_held and (last_character != " " and second_last_character != " " or keys_pressed < 2):
    input_text += " "
    second_last_character = last_character
    last_character = " "

if not shift_held: 
    if apostrophe_held and (last_character != "'" and second_last_character != "'" or keys_pressed < 2):
        input_text += "'"
        second_last_character = last_character
        last_character = "'"
    if comma_held and (last_character != "," and second_last_character != "," or keys_pressed < 2):
        input_text += ","
        second_last_character = last_character
        last_character = ","
    if minus_held and (last_character != "-" and second_last_character != "-" or keys_pressed < 2):
        input_text += "-"
        second_last_character = last_character
        last_character = "-"
    if fullstop_held and (last_character != "." and second_last_character != "." or keys_pressed < 2):
        input_text += "."
        second_last_character = last_character
        last_character = "."
    if forwardslash_held and (last_character != "/" and second_last_character != "/" or keys_pressed < 2):
        input_text += "/"
        second_last_character = last_character
        last_character = "/"
    if zero_held and (last_character != "0" and second_last_character != "0" or keys_pressed < 2):
        input_text += "0"
        second_last_character = last_character
        last_character = "0"
    if one_held and (last_character != "1" and second_last_character != "1" or keys_pressed < 2):
        input_text += "1"
        second_last_character = last_character
        last_character = "1"
    if two_held and (last_character != "2" and second_last_character != "2" or keys_pressed < 2):
        input_text += "2"
        second_last_character = last_character
        last_character = "2"
    if three_held and (last_character != "3" and second_last_character != "3" or keys_pressed < 2):
        input_text += "3"
        second_last_character = last_character
        last_character = "3"
    if four_held and (last_character != "4" and second_last_character != "4" or keys_pressed < 2):
        input_text += "4"
        second_last_character = last_character
        last_character = "4"
    if five_held and (last_character != "5" and second_last_character != "5" or keys_pressed < 2):
        input_text += "5"
        second_last_character = last_character
        last_character = "5"
    if six_held and (last_character != "6" and second_last_character != "6" or keys_pressed < 2):
        input_text += "6"
        second_last_character = last_character
        last_character = "6"
    if seven_held and (last_character != "7" and second_last_character != "7" or keys_pressed < 2):
        input_text += "7"
        second_last_character = last_character
        last_character = "7"
    if eight_held and (last_character != "8" and second_last_character != "8" or keys_pressed < 2):
        input_text += "8"
        second_last_character = last_character
        last_character = "8"
    if nine_held and (last_character != "9" and second_last_character != "9" or keys_pressed < 2):
        input_text += "9"
        second_last_character = last_character
        last_character = "9"
    if semicolon_held and (last_character != ";" and second_last_character != ";" or keys_pressed < 2):
        input_text += ";"
        second_last_character = last_character
        last_character = ";"
    if backslash_held and (last_character != "\\" and second_last_character != "\\" or keys_pressed < 2):
        input_text += "\\"
        second_last_character = last_character
        last_character = "\\"
    if equals_held and (last_character != "=" and second_last_character != "=" or keys_pressed < 2):
        input_text += "="
        second_last_character = last_character
        last_character = "="
    if opensquarebracket_held and (last_character != "[" and second_last_character != "[" or keys_pressed < 2):
        input_text += "["
        second_last_character = last_character
        last_character = "["
    if sharp_held and (last_character != "#" and second_last_character != "#" or keys_pressed < 2):
        input_text += "#"
        second_last_character = last_character
        last_character = "#"
    if closesquarebracket_held and (last_character != "]" and second_last_character != "]" or keys_pressed < 2):
        input_text += "]"
        second_last_character = last_character
        last_character = "]"
    if backtick_held and (last_character != "`" and second_last_character != "`" or keys_pressed < 2):
        input_text += "`"
        second_last_character = last_character
        last_character = "`"

    if not capslock:
        if a_held and (last_character != "a" and second_last_character != "a" or keys_pressed < 2):
            input_text += "a"
            second_last_character = last_character
            last_character = "a"
        if b_held and (last_character != "b" and second_last_character != "b" or keys_pressed < 2):
            input_text += "b"
            second_last_character = last_character
            last_character = "b"
        if c_held and (last_character != "c" and second_last_character != "c" or keys_pressed < 2):
            input_text += "c"
            second_last_character = last_character
            last_character = "c"
        if d_held and (last_character != "d" and second_last_character != "d" or keys_pressed < 2):
            input_text += "d"
            second_last_character = last_character
            last_character = "d"
        if e_held and (last_character != "e" and second_last_character != "e" or keys_pressed < 2):
            input_text += "e"
            second_last_character = last_character
            last_character = "e"
        if f_held and (last_character != "f" and second_last_character != "f" or keys_pressed < 2):
            input_text += "f"
            second_last_character = last_character
            last_character = "f"
        if g_held and (last_character != "g" and second_last_character != "g" or keys_pressed < 2):
            input_text += "g"
            second_last_character = last_character
            last_character = "g"
        if h_held and (last_character != "h" and second_last_character != "h" or keys_pressed < 2):
            input_text += "h"
            second_last_character = last_character
            last_character = "h"
        if i_held and (last_character != "i" and second_last_character != "i" or keys_pressed < 2):
            input_text += "i"
            second_last_character = last_character
            last_character = "i"
        if j_held and (last_character != "j" and second_last_character != "j" or keys_pressed < 2):
            input_text += "j"
            second_last_character = last_character
            last_character = "j"
        if k_held and (last_character != "k" and second_last_character != "k" or keys_pressed < 2):
            input_text += "k"
            second_last_character = last_character
            last_character = "k"
        if l_held and (last_character != "l" and second_last_character != "l" or keys_pressed < 2):
            input_text += "l"
            second_last_character = last_character
            last_character = "l"
        if m_held and (last_character != "m" and second_last_character != "m" or keys_pressed < 2):
            input_text += "m"
            second_last_character = last_character
            last_character = "m"
        if n_held and (last_character != "n" and second_last_character != "n" or keys_pressed < 2):
            input_text += "n"
            second_last_character = last_character
            last_character = "n"
        if o_held and (last_character != "o" and second_last_character != "o" or keys_pressed < 2):
            input_text += "o"
            second_last_character = last_character
            last_character = "o"
        if p_held and (last_character != "p" and second_last_character != "p" or keys_pressed < 2):
            input_text += "p"
            second_last_character = last_character
            last_character = "p"
        if q_held and (last_character != "q" and second_last_character != "q" or keys_pressed < 2):
            input_text += "q"
            second_last_character = last_character
            last_character = "q"
        if r_held and (last_character != "r" and second_last_character != "r" or keys_pressed < 2):
            input_text += "r"
            second_last_character = last_character
            last_character = "r"
        if s_held and (last_character != "s" and second_last_character != "s" or keys_pressed < 2):
            input_text += "s"
            second_last_character = last_character
            last_character = "s"
        if t_held and (last_character != "t" and second_last_character != "t" or keys_pressed < 2):
            input_text += "t"
            second_last_character = last_character
            last_character = "t"
        if u_held and (last_character != "u" and second_last_character != "u" or keys_pressed < 2):
            input_text += "u"
            second_last_character = last_character
            last_character = "u"
        if v_held and (last_character != "v" and second_last_character != "v" or keys_pressed < 2):
            input_text += "v"
            second_last_character = last_character
            last_character = "v"
        if w_held and (last_character != "w" and second_last_character != "w" or keys_pressed < 2):
            input_text += "w"
            second_last_character = last_character
            last_character = "w"
        if x_held and (last_character != "x" and second_last_character != "x" or keys_pressed < 2):
            input_text += "x"
            second_last_character = last_character
            last_character = "x"
        if y_held and (last_character != "y" and second_last_character != "y" or keys_pressed < 2):
            input_text += "y"
            second_last_character = last_character
            last_character = "y"
        if z_held and (last_character != "z" and second_last_character != "z" or keys_pressed < 2):
            input_text += "z"
            second_last_character = last_character
            last_character = "z"
    else:
        if a_held and (last_character != "A" and second_last_character != "A" or keys_pressed < 2):
            input_text += "A"
            second_last_character = last_character
            last_character = "A"
        if b_held and (last_character != "B" and second_last_character != "B" or keys_pressed < 2):
            input_text += "B"
            second_last_character = last_character
            last_character = "B"
        if c_held and (last_character != "C" and second_last_character != "C" or keys_pressed < 2):
            input_text += "C"
            second_last_character = last_character
            last_character = "C"
        if d_held and (last_character != "D" and second_last_character != "D" or keys_pressed < 2):
            input_text += "D"
            second_last_character = last_character
            last_character = "D"
        if e_held and (last_character != "E" and second_last_character != "E" or keys_pressed < 2):
            input_text += "E"
            second_last_character = last_character
            last_character = "E"
        if f_held and (last_character != "F" and second_last_character != "F" or keys_pressed < 2):
            input_text += "F"
            second_last_character = last_character
            last_character = "F"
        if g_held and (last_character != "G" and second_last_character != "G" or keys_pressed < 2):
            input_text += "G"
            second_last_character = last_character
            last_character = "G"
        if h_held and (last_character != "H" and second_last_character != "H" or keys_pressed < 2):
            input_text += "H"
            second_last_character = last_character
            last_character = "H"
        if i_held and (last_character != "I" and second_last_character != "I" or keys_pressed < 2):
            input_text += "I"
            second_last_character = last_character
            last_character = "I"
        if j_held and (last_character != "J" and second_last_character != "J" or keys_pressed < 2):
            input_text += "J"
            second_last_character = last_character
            last_character = "J"
        if k_held and (last_character != "K" and second_last_character != "K" or keys_pressed < 2):
            input_text += "K"
            second_last_character = last_character
            last_character = "K"
        if l_held and (last_character != "L" and second_last_character != "L" or keys_pressed < 2):
            input_text += "L"
            second_last_character = last_character
            last_character = "L"
        if m_held and (last_character != "M" and second_last_character != "M" or keys_pressed < 2):
            input_text += "M"
            second_last_character = last_character
            last_character = "M"
        if n_held and (last_character != "N" and second_last_character != "N" or keys_pressed < 2):
            input_text += "N"
            second_last_character = last_character
            last_character = "N"
        if o_held and (last_character != "O" and second_last_character != "O" or keys_pressed < 2):
            input_text += "O"
            second_last_character = last_character
            last_character = "O"
        if p_held and (last_character != "P" and second_last_character != "P" or keys_pressed < 2):
            input_text += "P"
            second_last_character = last_character
            last_character = "P"
        if q_held and (last_character != "Q" and second_last_character != "Q" or keys_pressed < 2):
            input_text += "Q"
            second_last_character = last_character
            last_character = "Q"
        if r_held and (last_character != "R" and second_last_character != "R" or keys_pressed < 2):
            input_text += "R"
            second_last_character = last_character
            last_character = "R"
        if s_held and (last_character != "S" and second_last_character != "S" or keys_pressed < 2):
            input_text += "S"
            second_last_character = last_character
            last_character = "S"
        if t_held and (last_character != "T" and second_last_character != "T" or keys_pressed < 2):
            input_text += "T"
            second_last_character = last_character
            last_character = "T"
        if u_held and (last_character != "U" and second_last_character != "U" or keys_pressed < 2):
            input_text += "U"
            second_last_character = last_character
            last_character = "U"
        if v_held and (last_character != "V" and second_last_character != "V" or keys_pressed < 2):
            input_text += "V"
            second_last_character = last_character
            last_character = "V"
        if w_held and (last_character != "W" and second_last_character != "W" or keys_pressed < 2):
            input_text += "W"
            second_last_character = last_character
            last_character = "W"
        if x_held and (last_character != "X" and second_last_character != "X" or keys_pressed < 2):
            input_text += "X"
            second_last_character = last_character
            last_character = "X"
        if y_held and (last_character != "Y" and second_last_character != "Y" or keys_pressed < 2):
            input_text += "Y"
            second_last_character = last_character
            last_character = "Y"
        if z_held and (last_character != "Z" and second_last_character != "Z" or keys_pressed < 2):
            input_text += "Z"
            second_last_character = last_character
            last_character = "Z"
else:
    if apostrophe_held and (last_character != "@" and second_last_character != "@" or keys_pressed < 2):
        input_text += "@"
        second_last_character = last_character
        last_character = "@"
    if comma_held and (last_character != "<" and second_last_character != "<" or keys_pressed < 2):
        input_text += "<"
        second_last_character = last_character
        last_character = "<"
    if minus_held and (last_character != "_" and second_last_character != "_" or keys_pressed < 2):
        input_text += "_"
        second_last_character = last_character
        last_character = "_"
    if fullstop_held and (last_character != ">" and second_last_character != ">" or keys_pressed < 2):
        input_text += ">"
        second_last_character = last_character
        last_character = ">"
    if forwardslash_held and (last_character != "?" and second_last_character != "?" or keys_pressed < 2):
        input_text += "?"
        second_last_character = last_character
        last_character = "?"
    if zero_held and (last_character != ")" and second_last_character != ")" or keys_pressed < 2):
        input_text += ")"
        second_last_character = last_character
        last_character = ")"
    if one_held and (last_character != "!" and second_last_character != "!" or keys_pressed < 2):
        input_text += "!"
        second_last_character = last_character
        last_character = "!"
    if two_held and (last_character != "\"" and second_last_character != "\"" or keys_pressed < 2):
        input_text += "\""
        second_last_character = last_character
        last_character = "\""
    if three_held and (last_character != "£" and second_last_character != "£" or keys_pressed < 2):
        input_text += "£"
        second_last_character = last_character
        last_character = "£"
    if four_held and (last_character != "$" and second_last_character != "$" or keys_pressed < 2):
        input_text += "$"
        second_last_character = last_character
        last_character = "$"
    if five_held and (last_character != "%" and second_last_character != "%" or keys_pressed < 2):
        input_text += "%"
        second_last_character = last_character
        last_character = "%"
    if six_held and (last_character != "^" and second_last_character != "^" or keys_pressed < 2):
        input_text += "^"
        second_last_character = last_character
        last_character = "^"
    if seven_held and (last_character != "&" and second_last_character != "&" or keys_pressed < 2):
        input_text += "&"
        second_last_character = last_character
        last_character = "&"
    if eight_held and (last_character != "*" and second_last_character != "*" or keys_pressed < 2):
        input_text += "*"
        second_last_character = last_character
        last_character = "*"
    if nine_held and (last_character != "(" and second_last_character != "(" or keys_pressed < 2):
        input_text += "("
        second_last_character = last_character
        last_character = "("
    if semicolon_held and (last_character != ":" and second_last_character != ":" or keys_pressed < 2):
        input_text += ":"
        second_last_character = last_character
        last_character = ":"
    if backslash_held and (last_character != "|" and second_last_character != "|" or keys_pressed < 2):
        input_text += "|"
        second_last_character = last_character
        last_character = "|"
    if equals_held and (last_character != "+" and second_last_character != "+" or keys_pressed < 2):
        input_text += "+"
        second_last_character = last_character
        last_character = "+"
    if opensquarebracket_held and (last_character != "{" and second_last_character != "{" or keys_pressed < 2):
        input_text += "{"
        second_last_character = last_character
        last_character = "{"
    if sharp_held and (last_character != "~" and second_last_character != "~" or keys_pressed < 2):
        input_text += "~"
        second_last_character = last_character
        last_character = "~"
    if closesquarebracket_held and (last_character != "}" and second_last_character != "}" or keys_pressed < 2):
        input_text += "}"
        second_last_character = last_character
        last_character = "}"
    if backtick_held and (last_character != "¬" and second_last_character != "¬" or keys_pressed < 2):
        input_text += "¬"
        second_last_character = last_character
        last_character = "¬"

    if capslock:
        if a_held and (last_character != "a" and second_last_character != "a" or keys_pressed < 2):
            input_text += "a"
            second_last_character = last_character
            last_character = "a"
        if b_held and (last_character != "b" and second_last_character != "b" or keys_pressed < 2):
            input_text += "b"
            second_last_character = last_character
            last_character = "b"
        if c_held and (last_character != "c" and second_last_character != "c" or keys_pressed < 2):
            input_text += "c"
            second_last_character = last_character
            last_character = "c"
        if d_held and (last_character != "d" and second_last_character != "d" or keys_pressed < 2):
            input_text += "d"
            second_last_character = last_character
            last_character = "d"
        if e_held and (last_character != "e" and second_last_character != "e" or keys_pressed < 2):
            input_text += "e"
            second_last_character = last_character
            last_character = "e"
        if f_held and (last_character != "f" and second_last_character != "f" or keys_pressed < 2):
            input_text += "f"
            second_last_character = last_character
            last_character = "f"
        if g_held and (last_character != "g" and second_last_character != "g" or keys_pressed < 2):
            input_text += "g"
            second_last_character = last_character
            last_character = "g"
        if h_held and (last_character != "h" and second_last_character != "h" or keys_pressed < 2):
            input_text += "h"
            second_last_character = last_character
            last_character = "h"
        if i_held and (last_character != "i" and second_last_character != "i" or keys_pressed < 2):
            input_text += "i"
            second_last_character = last_character
            last_character = "i"
        if j_held and (last_character != "j" and second_last_character != "j" or keys_pressed < 2):
            input_text += "j"
            second_last_character = last_character
            last_character = "j"
        if k_held and (last_character != "k" and second_last_character != "k" or keys_pressed < 2):
            input_text += "k"
            second_last_character = last_character
            last_character = "k"
        if l_held and (last_character != "l" and second_last_character != "l" or keys_pressed < 2):
            input_text += "l"
            second_last_character = last_character
            last_character = "l"
        if m_held and (last_character != "m" and second_last_character != "m" or keys_pressed < 2):
            input_text += "m"
            second_last_character = last_character
            last_character = "m"
        if n_held and (last_character != "n" and second_last_character != "n" or keys_pressed < 2):
            input_text += "n"
            second_last_character = last_character
            last_character = "n"
        if o_held and (last_character != "o" and second_last_character != "o" or keys_pressed < 2):
            input_text += "o"
            second_last_character = last_character
            last_character = "o"
        if p_held and (last_character != "p" and second_last_character != "p" or keys_pressed < 2):
            input_text += "p"
            second_last_character = last_character
            last_character = "p"
        if q_held and (last_character != "q" and second_last_character != "q" or keys_pressed < 2):
            input_text += "q"
            second_last_character = last_character
            last_character = "q"
        if r_held and (last_character != "r" and second_last_character != "r" or keys_pressed < 2):
            input_text += "r"
            second_last_character = last_character
            last_character = "r"
        if s_held and (last_character != "s" and second_last_character != "s" or keys_pressed < 2):
            input_text += "s"
            second_last_character = last_character
            last_character = "s"
        if t_held and (last_character != "t" and second_last_character != "t" or keys_pressed < 2):
            input_text += "t"
            second_last_character = last_character
            last_character = "t"
        if u_held and (last_character != "u" and second_last_character != "u" or keys_pressed < 2):
            input_text += "u"
            second_last_character = last_character
            last_character = "u"
        if v_held and (last_character != "v" and second_last_character != "v" or keys_pressed < 2):
            input_text += "v"
            second_last_character = last_character
            last_character = "v"
        if w_held and (last_character != "w" and second_last_character != "w" or keys_pressed < 2):
            input_text += "w"
            second_last_character = last_character
            last_character = "w"
        if x_held and (last_character != "x" and second_last_character != "x" or keys_pressed < 2):
            input_text += "x"
            second_last_character = last_character
            last_character = "x"
        if y_held and (last_character != "y" and second_last_character != "y" or keys_pressed < 2):
            input_text += "y"
            second_last_character = last_character
            last_character = "y"
        if z_held and (last_character != "z" and second_last_character != "z" or keys_pressed < 2):
            input_text += "z"
            second_last_character = last_character
            last_character = "z"
    else:
        if a_held and (last_character != "A" and second_last_character != "A" or keys_pressed < 2):
            input_text += "A"
            second_last_character = last_character
            last_character = "A"
        if b_held and (last_character != "B" and second_last_character != "B" or keys_pressed < 2):
            input_text += "B"
            second_last_character = last_character
            last_character = "B"
        if c_held and (last_character != "C" and second_last_character != "C" or keys_pressed < 2):
            input_text += "C"
            second_last_character = last_character
            last_character = "C"
        if d_held and (last_character != "D" and second_last_character != "D" or keys_pressed < 2):
            input_text += "D"
            second_last_character = last_character
            last_character = "D"
        if e_held and (last_character != "E" and second_last_character != "E" or keys_pressed < 2):
            input_text += "E"
            second_last_character = last_character
            last_character = "E"
        if f_held and (last_character != "F" and second_last_character != "F" or keys_pressed < 2):
            input_text += "F"
            second_last_character = last_character
            last_character = "F"
        if g_held and (last_character != "G" and second_last_character != "G" or keys_pressed < 2):
            input_text += "G"
            second_last_character = last_character
            last_character = "G"
        if h_held and (last_character != "H" and second_last_character != "H" or keys_pressed < 2):
            input_text += "H"
            second_last_character = last_character
            last_character = "H"
        if i_held and (last_character != "I" and second_last_character != "I" or keys_pressed < 2):
            input_text += "I"
            second_last_character = last_character
            last_character = "I"
        if j_held and (last_character != "J" and second_last_character != "J" or keys_pressed < 2):
            input_text += "J"
            second_last_character = last_character
            last_character = "J"
        if k_held and (last_character != "K" and second_last_character != "K" or keys_pressed < 2):
            input_text += "K"
            second_last_character = last_character
            last_character = "K"
        if l_held and (last_character != "L" and second_last_character != "L" or keys_pressed < 2):
            input_text += "L"
            second_last_character = last_character
            last_character = "L"
        if m_held and (last_character != "M" and second_last_character != "M" or keys_pressed < 2):
            input_text += "M"
            second_last_character = last_character
            last_character = "M"
        if n_held and (last_character != "N" and second_last_character != "N" or keys_pressed < 2):
            input_text += "N"
            second_last_character = last_character
            last_character = "N"
        if o_held and (last_character != "O" and second_last_character != "O" or keys_pressed < 2):
            input_text += "O"
            second_last_character = last_character
            last_character = "O"
        if p_held and (last_character != "P" and second_last_character != "P" or keys_pressed < 2):
            input_text += "P"
            second_last_character = last_character
            last_character = "P"
        if q_held and (last_character != "Q" and second_last_character != "Q" or keys_pressed < 2):
            input_text += "Q"
            second_last_character = last_character
            last_character = "Q"
        if r_held and (last_character != "R" and second_last_character != "R" or keys_pressed < 2):
            input_text += "R"
            second_last_character = last_character
            last_character = "R"
        if s_held and (last_character != "S" and second_last_character != "S" or keys_pressed < 2):
            input_text += "S"
            second_last_character = last_character
            last_character = "S"
        if t_held and (last_character != "T" and second_last_character != "T" or keys_pressed < 2):
            input_text += "T"
            second_last_character = last_character
            last_character = "T"
        if u_held and (last_character != "U" and second_last_character != "U" or keys_pressed < 2):
            input_text += "U"
            second_last_character = last_character
            last_character = "U"
        if v_held and (last_character != "V" and second_last_character != "V" or keys_pressed < 2):
            input_text += "V"
            second_last_character = last_character
            last_character = "V"
        if w_held and (last_character != "W" and second_last_character != "W" or keys_pressed < 2):
            input_text += "W"
            second_last_character = last_character
            last_character = "W"
        if x_held and (last_character != "X" and second_last_character != "X" or keys_pressed < 2):
            input_text += "X"
            second_last_character = last_character
            last_character = "X"
        if y_held and (last_character != "Y" and second_last_character != "Y" or keys_pressed < 2):
            input_text += "Y"
            second_last_character = last_character
            last_character = "Y"
        if z_held and (last_character != "Z" and second_last_character != "Z" or keys_pressed < 2):
            input_text += "Z"
            second_last_character = last_character
            last_character = "Z"
    
if delete_held and (last_character != "" and second_last_character != "" or keys_pressed < 2):# for if there is a cursor so you can go backwards and type there in the future
    pass
if numpad0_held and (last_character != "0" and second_last_character != "0" or keys_pressed < 2):
    input_text += "0"
    second_last_character = last_character
    last_character = "0"
if numpad1_held and (last_character != "1" and second_last_character != "1" or keys_pressed < 2):
    input_text += "1"
    second_last_character = last_character
    last_character = "1"
if numpad2_held and (last_character != "2" and second_last_character != "2" or keys_pressed < 2):
    input_text += "2"
    second_last_character = last_character
    last_character = "2"
if numpad3_held and (last_character != "3" and second_last_character != "3" or keys_pressed < 2):
    input_text += "3"
    second_last_character = last_character
    last_character = "3"
if numpad4_held and (last_character != "4" and second_last_character != "4" or keys_pressed < 2):
    input_text += "4"
    second_last_character = last_character
    last_character = "4"
if numpad5_held and (last_character != "4" and second_last_character != "5" or keys_pressed < 2):
    input_text += "5"
    second_last_character = last_character
    last_character = "5"
if numpad6_held and (last_character != "6" and second_last_character != "6" or keys_pressed < 2):
    input_text += "6"   
    second_last_character = last_character
    last_character = "6"
if numpad7_held and (last_character != "7" and second_last_character != "7" or keys_pressed < 2):
    input_text += "7"    
    second_last_character = last_character
    last_character = "7"
if numpad8_held and (last_character != "8" and second_last_character != "8" or keys_pressed < 2):
    input_text += "8"
    second_last_character = last_character
    last_character = "8"
if numpad9_held and (last_character != "9" and second_last_character != "9" or keys_pressed < 2):
    input_text += "9"    
    second_last_character = last_character
    last_character = "9"
if numpaddivide_held and (last_character != "/" and second_last_character != "/" or keys_pressed < 2):
    input_text += "/"    
    second_last_character = last_character
    last_character = "/"
if numpadmultiply_held and (last_character != "*" and second_last_character != "*" or keys_pressed < 2):
    input_text += "*"    
    second_last_character = last_character
    last_character = "*"
if numpadminus_held and (last_character != "-" and second_last_character != "-" or keys_pressed < 2):
    input_text += "-"    
    second_last_character = last_character
    last_character = "-"
if numpadplus_held and (last_character != "+" and second_last_character != "+" or keys_pressed < 2):
    input_text += "+"    
    second_last_character = last_character
    last_character = "+"
if numpadenter_held and (last_character != "\n" and second_last_character != "\n" or keys_pressed < 2):
    input_text += "\n"    
    second_last_character = last_character
    last_character = "\n"
if rightarrow_held:# for if there is a cursor so you can go backwards and type there in the future
    pass
if leftarrow_held:# for if there is a cursor so you can go backwards and type there in the future
    pass
