keyboard = [
    [[" "], ["QWERTY", "ASDFGH", "ZXCVBN"]],
    [["A"], ["XCVBGRD", "GRDXCVB", "ZSEFVCX"]],
    [["B"], ["WSXCFD", "RFVBHG", "QAZXDS", "YHNMKJ"]],
    [["C"], ["REDCV", "EWSXC", "TRFVB"]],
    [["D"], ["EDCVGR", "WSXCFE", "YHNMKU"]],
    [["E"], ["EDCVRF", "WSXCDE", "TGBNHY"]],
    [["F"], ["REDCF", "TRFVG", "EWSXD"]],
    [["G"], ["REDCVG", "CVGRED", "CVRGED"]],
    [["H"], ["WSXDRFV", "EDCFTGB", "RFVGYHN"]],
    [["I"], ["WSX", "EDC", "RFV"]],
    [["J"], ["UJMN", "WSXZ", "RFVC"]],
    [["K"], ["EDCFBY", "WSXDVR", "QAZSCE"]],
    [["L"], ["WSXCV", "EDCVB", "RFVBN"]],
    [["M"], ["ZAQWDRTGB", "XSWEFTYHN", "XSWEFTYNH"]],
    [["N"], ["ZAQWDVFR", "XSWEFTGB", "XSWEFTBG"]],
    [["O"], ["QAZXCDEW", "WSXCVFRE", "RFVBNHYT", "TGBNMJUY"]],
    [["P"], ["MNBVCCDERTG", "NBVCXSWERF", "NBVCXSWEFR"]],
    [["Q"], ["QAZXCDEWV", "EDCVBGTRN", "RFVBNHYTM"]],
    [["R"], ["MNBVCDRTGHU", "MNBVCDRTGHU", "MNBVCDRTGHU"]],
    [["S"], ["YTRFVCX", "IUYHNBV", "IUYHNBV"]],
    [["T"], ["WERTYFV", "RTYUIHN", "RTYUIHN"]],
    [["U"], ["WSXCVFR", "EDCVBGT", "EDCVBGT"]],
    [["V"], ["EFVGY", "WDCFT", "WDCFT"]],
    [["W"], ["EFVGYWDCFT", "EFVGYWDCFT", "EFVGYWDCFT"]],
    [["X"], ["WDVTDZ", "RGNYGC", "RGNYGC"]],
    [["Y"], ["JMYI", "EFVT", "EFVT"]],
    [["Z"], ["QWERDCVB", "ERTGVBN", "ERTGVBN"]]
]

def nliqwerty_dec(buf):
    dec_buf = buf
    result = ""
    while len(dec_buf) > 0:
        if dec_buf[:1] == '{' or dec_buf[:1] == '}' or dec_buf[:1] == '.' or dec_buf[:1] == ',':
            result += dec_buf[:1]
            dec_buf = dec_buf[1:]
            continue

        is_found = False
        for i in range(11, 2, -1):
            for count in range(0, 27):
                for j in keyboard[count][1]:
                    if dec_buf[:i] == j:
                        result += keyboard[count][0][0]
                        dec_buf = dec_buf[i:]
                        is_found = True
                        break

            if is_found:
                break


    print(result)


nliqwerty_dec("{WSXIUYHNBVTRFVBTRFVBQWERTYQAZSCEWSXCDEEFVTYHNMKJTGBNMJUYGRDXCVBMNBVCDRTGHUWSXCFEQWERTYTRFVBWSXNBVCXSWERFRFVGYHNWSXCDEMNBVCDRTGHU}")