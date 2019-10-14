
# First Function - replaces sign codes, keeps control characters

def MdC_Unicode_withLatinControlChars(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace(
        "£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordParsed = "".join(signsParsed)

    return wordParsed

#- - - - - - - - - - - -

# Second Function - replaces sign codes, removes control characters

def MdC_Unicode_noControlChars(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace(
        "£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordToParse = "".join(signsParsed)

    wordParsed = wordToParse.replace("-", "").replace(":", "").replace("*", "").replace("(", "").replace(")", "").replace("&", "")

    return wordParsed

#- - - - - - - - - - - -

# Third Function - replaces sign codes, removes control characters, insert the breaking-ligature character (u

def MdC_Unicode_noControlChars_WithBreakLigChar(wordToParse):

    wordToParse = wordToParse.replace("-", "£-£").replace(":", "£:£").replace("*", "£*£").replace("(", "£(£").replace("£)£", "").replace("£&£", "")

    signsToParse = wordToParse.split("£")

    signsParsed = replaceGardiner(signsToParse)

    wordToParse = "".join(signsParsed)

    wordParsed = wordToParse.replace("-", u"\u200B").replace(":", "").replace("*", "").replace("(", "").replace(")", "").replace("&", "")

    return wordParsed

# Fourth Function - analyses the word according to all the three previous functions, and output the result as an array

def MdC_Unicode_combined(wordToParse):

    parsed_1 = MdC_Unicode_keepControlChars(wordToParse)

    parsed_2 = MdC_Unicode_noControlChars(wordToParse)

    parsed_3 = MdC_Unicode_noControlChars_WithBreakLigChar(wordToParse)

    parsedArray = []
    parsedArray.append(parsed_1)
    parsedArray.append(parsed_2)
    parsedArray.append(parsed_3)

    return parsedArray





#============================

#============================


def replaceGardiner (signs):

    for i in range (0, len(signs)):
        if signs[i] == 'Z16h':
            signs[i] = '𓐌'
        elif signs[i] == 'Z16g':
            signs[i] = '𓐋'
        elif signs[i] == 'Z16f':
            signs[i] = '𓐊'
        elif signs[i] == 'Z16e':
            signs[i] = '𓐉'
        elif signs[i] == 'Z16d':
            signs[i] = '𓐈'
        elif signs[i] == 'Z16c':
            signs[i] = '𓐇'
        elif signs[i] == 'Z16b':
            signs[i] = '𓐆'
        elif signs[i] == 'Z16a':
            signs[i] = '𓐅'
        elif signs[i] == 'Z16':
            signs[i] = '𓐄'
        elif signs[i] == 'Z15i':
            signs[i] = '𓐃'
        elif signs[i] == 'Z15h':
            signs[i] = '𓐂'
        elif signs[i] == 'Z15g':
            signs[i] = '𓐁'
        elif signs[i] == 'Z15f':
            signs[i] = '𓐀'
        elif signs[i] == 'Z15e':
            signs[i] = '𓏿'
        elif signs[i] == 'Z15d':
            signs[i] = '𓏾'
        elif signs[i] == 'Z15c':
            signs[i] = '𓏽'
        elif signs[i] == 'Z15b':
            signs[i] = '𓏼'
        elif signs[i] == 'Z15a':
            signs[i] = '𓏻'
        elif signs[i] == 'Z15':
            signs[i] = '𓏺'
        elif signs[i] == 'Z14':
            signs[i] = '𓏹'
        elif signs[i] == 'Z13':
            signs[i] = '𓏸'
        elif signs[i] == 'Z12':
            signs[i] = '𓏷'
        elif signs[i] == 'Z11':
            signs[i] = '𓏶'
        elif signs[i] == 'Z10':
            signs[i] = '𓏵'
        elif signs[i] == 'Z9':
            signs[i] = '𓏴'
        elif signs[i] == 'Z8':
            signs[i] = '𓏳'
        elif signs[i] == 'Z7':
            signs[i] = '𓏲'
        elif signs[i] == 'Z6':
            signs[i] = '𓏱'
        elif signs[i] == 'Z5a':
            signs[i] = '𓏰'
        elif signs[i] == 'Z5':
            signs[i] = '𓏯'
        elif signs[i] == 'Z4a':
            signs[i] = '𓏮'
        elif signs[i] == 'Z4':
            signs[i] = '𓏭'
        elif signs[i] == 'Z3b':
            signs[i] = '𓏬'
        elif signs[i] == 'Z3a':
            signs[i] = '𓏫'
        elif signs[i] == 'Z3':
            signs[i] = '𓏪'
        elif signs[i] == 'Z2d':
            signs[i] = '𓏩'
        elif signs[i] == 'Z2c':
            signs[i] = '𓏨'
        elif signs[i] == 'Z2b':
            signs[i] = '𓏧'
        elif signs[i] == 'Z2a':
            signs[i] = '𓏦'
        elif signs[i] == 'Z2':
            signs[i] = '𓏥'
        elif signs[i] == 'Z1':
            signs[i] = '𓏤'
        elif signs[i] == 'Y8':
            signs[i] = '𓏣'
        elif signs[i] == 'Y7':
            signs[i] = '𓏢'
        elif signs[i] == 'Y6':
            signs[i] = '𓏡'
        elif signs[i] == 'Y5':
            signs[i] = '𓏠'
        elif signs[i] == 'Y4':
            signs[i] = '𓏟'
        elif signs[i] == 'Y3':
            signs[i] = '𓏞'
        elif signs[i] == 'Y2':
            signs[i] = '𓏝'
        elif signs[i] == 'Y1a':
            signs[i] = '𓏜'
        elif signs[i] == 'Y1':
            signs[i] = '𓏛'
        elif signs[i] == 'X8a':
            signs[i] = '𓏚'
        elif signs[i] == 'X8':
            signs[i] = '𓏙'
        elif signs[i] == 'X7':
            signs[i] = '𓏘'
        elif signs[i] == 'X6a':
            signs[i] = '𓏗'
        elif signs[i] == 'X6':
            signs[i] = '𓏖'
        elif signs[i] == 'X5':
            signs[i] = '𓏕'
        elif signs[i] == 'X4b':
            signs[i] = '𓏔'
        elif signs[i] == 'X4a':
            signs[i] = '𓏓'
        elif signs[i] == 'X4':
            signs[i] = '𓏒'
        elif signs[i] == 'X3':
            signs[i] = '𓏑'
        elif signs[i] == 'X2':
            signs[i] = '𓏐'
        elif signs[i] == 'X1':
            signs[i] = '𓏏'
        elif signs[i] == 'W25':
            signs[i] = '𓏎'
        elif signs[i] == 'W24a':
            signs[i] = '𓏍'
        elif signs[i] == 'W24':
            signs[i] = '𓏌'
        elif signs[i] == 'W23':
            signs[i] = '𓏋'
        elif signs[i] == 'W22':
            signs[i] = '𓏊'
        elif signs[i] == 'W21':
            signs[i] = '𓏉'
        elif signs[i] == 'W20':
            signs[i] = '𓏈'
        elif signs[i] == 'W19':
            signs[i] = '𓏇'
        elif signs[i] == 'W18a':
            signs[i] = '𓏆'
        elif signs[i] == 'W18':
            signs[i] = '𓏅'
        elif signs[i] == 'W17a':
            signs[i] = '𓏄'
        elif signs[i] == 'W17':
            signs[i] = '𓏃'
        elif signs[i] == 'W16':
            signs[i] = '𓏂'
        elif signs[i] == 'W15':
            signs[i] = '𓏁'
        elif signs[i] == 'W14a':
            signs[i] = '𓏀'
        elif signs[i] == 'W14':
            signs[i] = '𓎿'
        elif signs[i] == 'W13':
            signs[i] = '𓎾'
        elif signs[i] == 'W12':
            signs[i] = '𓎽'
        elif signs[i] == 'W11':
            signs[i] = '𓎼'
        elif signs[i] == 'W10a':
            signs[i] = '𓎻'
        elif signs[i] == 'W10':
            signs[i] = '𓎺'
        elif signs[i] == 'W9a':
            signs[i] = '𓎹'
        elif signs[i] == 'W9':
            signs[i] = '𓎸'
        elif signs[i] == 'W8':
            signs[i] = '𓎷'
        elif signs[i] == 'W7':
            signs[i] = '𓎶'
        elif signs[i] == 'W6':
            signs[i] = '𓎵'
        elif signs[i] == 'W5':
            signs[i] = '𓎴'
        elif signs[i] == 'W4':
            signs[i] = '𓎳'
        elif signs[i] == 'W3a':
            signs[i] = '𓎲'
        elif signs[i] == 'W3':
            signs[i] = '𓎱'
        elif signs[i] == 'W2':
            signs[i] = '𓎰'
        elif signs[i] == 'W1':
            signs[i] = '𓎯'
        elif signs[i] == 'V40a':
            signs[i] = '𓎮'
        elif signs[i] == 'V40':
            signs[i] = '𓎭'
        elif signs[i] == 'V39':
            signs[i] = '𓎬'
        elif signs[i] == 'V38':
            signs[i] = '𓎫'
        elif signs[i] == 'V37a':
            signs[i] = '𓎪'
        elif signs[i] == 'V37':
            signs[i] = '𓎩'
        elif signs[i] == 'V36':
            signs[i] = '𓎨'
        elif signs[i] == 'V35':
            signs[i] = '𓎧'
        elif signs[i] == 'V34':
            signs[i] = '𓎦'
        elif signs[i] == 'V33a':
            signs[i] = '𓎥'
        elif signs[i] == 'V33':
            signs[i] = '𓎤'
        elif signs[i] == 'V32':
            signs[i] = '𓎣'
        elif signs[i] == 'V31a':
            signs[i] = '𓎢'
        elif signs[i] == 'V31':
            signs[i] = '𓎡'
        elif signs[i] == 'V30a':
            signs[i] = '𓎠'
        elif signs[i] == 'V30':
            signs[i] = '𓎟'
        elif signs[i] == 'V29a':
            signs[i] = '𓎞'
        elif signs[i] == 'V29':
            signs[i] = '𓎝'
        elif signs[i] == 'V28a':
            signs[i] = '𓎜'
        elif signs[i] == 'V28':
            signs[i] = '𓎛'
        elif signs[i] == 'V27':
            signs[i] = '𓎚'
        elif signs[i] == 'V26':
            signs[i] = '𓎙'
        elif signs[i] == 'V25':
            signs[i] = '𓎘'
        elif signs[i] == 'V24':
            signs[i] = '𓎗'
        elif signs[i] == 'V23a':
            signs[i] = '𓎖'
        elif signs[i] == 'V23':
            signs[i] = '𓎕'
        elif signs[i] == 'V22':
            signs[i] = '𓎔'
        elif signs[i] == 'V21':
            signs[i] = '𓎓'
        elif signs[i] == 'V20l':
            signs[i] = '𓎒'
        elif signs[i] == 'V20k':
            signs[i] = '𓎑'
        elif signs[i] == 'V20j':
            signs[i] = '𓎐'
        elif signs[i] == 'V20i':
            signs[i] = '𓎏'
        elif signs[i] == 'V20h':
            signs[i] = '𓎎'
        elif signs[i] == 'V20g':
            signs[i] = '𓎍'
        elif signs[i] == 'V20f':
            signs[i] = '𓎌'
        elif signs[i] == 'V20e':
            signs[i] = '𓎋'
        elif signs[i] == 'V20d':
            signs[i] = '𓎊'
        elif signs[i] == 'V20c':
            signs[i] = '𓎉'
        elif signs[i] == 'V20b':
            signs[i] = '𓎈'
        elif signs[i] == 'V20a':
            signs[i] = '𓎇'
        elif signs[i] == 'V20':
            signs[i] = '𓎆'
        elif signs[i] == 'V19':
            signs[i] = '𓎅'
        elif signs[i] == 'V18':
            signs[i] = '𓎄'
        elif signs[i] == 'V17':
            signs[i] = '𓎃'
        elif signs[i] == 'V16':
            signs[i] = '𓎂'
        elif signs[i] == 'V15':
            signs[i] = '𓎁'
        elif signs[i] == 'V14':
            signs[i] = '𓎀'
        elif signs[i] == 'V13':
            signs[i] = '𓍿'
        elif signs[i] == 'V12b':
            signs[i] = '𓍾'
        elif signs[i] == 'V12a':
            signs[i] = '𓍽'
        elif signs[i] == 'V12':
            signs[i] = '𓍼'
        elif signs[i] == 'V11c':
            signs[i] = '𓍻'
        elif signs[i] == 'V11b':
            signs[i] = '𓍺'
        elif signs[i] == 'V11a':
            signs[i] = '𓍹'
        elif signs[i] == 'V11':
            signs[i] = '𓍸'
        elif signs[i] == 'V10':
            signs[i] = '𓍷'
        elif signs[i] == 'V9':
            signs[i] = '𓍶'
        elif signs[i] == 'V8':
            signs[i] = '𓍵'
        elif signs[i] == 'V7b':
            signs[i] = '𓍴'
        elif signs[i] == 'V7a':
            signs[i] = '𓍳'
        elif signs[i] == 'V7':
            signs[i] = '𓍲'
        elif signs[i] == 'V6':
            signs[i] = '𓍱'
        elif signs[i] == 'V5':
            signs[i] = '𓍰'
        elif signs[i] == 'V4':
            signs[i] = '𓍯'
        elif signs[i] == 'V3':
            signs[i] = '𓍮'
        elif signs[i] == 'V2a':
            signs[i] = '𓍭'
        elif signs[i] == 'V2':
            signs[i] = '𓍬'
        elif signs[i] == 'V1i':
            signs[i] = '𓍫'
        elif signs[i] == 'V1h':
            signs[i] = '𓍪'
        elif signs[i] == 'V1g':
            signs[i] = '𓍩'
        elif signs[i] == 'V1f':
            signs[i] = '𓍨'
        elif signs[i] == 'V1e':
            signs[i] = '𓍧'
        elif signs[i] == 'V1d':
            signs[i] = '𓍦'
        elif signs[i] == 'V1c':
            signs[i] = '𓍥'
        elif signs[i] == 'V1b':
            signs[i] = '𓍤'
        elif signs[i] == 'V1a':
            signs[i] = '𓍣'
        elif signs[i] == 'V1':
            signs[i] = '𓍢'
        elif signs[i] == 'U42':
            signs[i] = '𓍡'
        elif signs[i] == 'U41':
            signs[i] = '𓍠'
        elif signs[i] == 'U40':
            signs[i] = '𓍟'
        elif signs[i] == 'U39':
            signs[i] = '𓍞'
        elif signs[i] == 'U38':
            signs[i] = '𓍝'
        elif signs[i] == 'U37':
            signs[i] = '𓍜'
        elif signs[i] == 'U36':
            signs[i] = '𓍛'
        elif signs[i] == 'U35':
            signs[i] = '𓍚'
        elif signs[i] == 'U34':
            signs[i] = '𓍙'
        elif signs[i] == 'U33':
            signs[i] = '𓍘'
        elif signs[i] == 'U32a':
            signs[i] = '𓍗'
        elif signs[i] == 'U32':
            signs[i] = '𓍖'
        elif signs[i] == 'U31':
            signs[i] = '𓍕'
        elif signs[i] == 'U30':
            signs[i] = '𓍔'
        elif signs[i] == 'U29a':
            signs[i] = '𓍓'
        elif signs[i] == 'U29':
            signs[i] = '𓍒'
        elif signs[i] == 'U28':
            signs[i] = '𓍑'
        elif signs[i] == 'U27':
            signs[i] = '𓍐'
        elif signs[i] == 'U26':
            signs[i] = '𓍏'
        elif signs[i] == 'U25':
            signs[i] = '𓍎'
        elif signs[i] == 'U24':
            signs[i] = '𓍍'
        elif signs[i] == 'U23a':
            signs[i] = '𓍌'
        elif signs[i] == 'U23':
            signs[i] = '𓍋'
        elif signs[i] == 'U22':
            signs[i] = '𓍊'
        elif signs[i] == 'U21':
            signs[i] = '𓍉'
        elif signs[i] == 'U20':
            signs[i] = '𓍈'
        elif signs[i] == 'U19':
            signs[i] = '𓍇'
        elif signs[i] == 'U18':
            signs[i] = '𓍆'
        elif signs[i] == 'U17':
            signs[i] = '𓍅'
        elif signs[i] == 'U16':
            signs[i] = '𓍄'
        elif signs[i] == 'U15':
            signs[i] = '𓍃'
        elif signs[i] == 'U14':
            signs[i] = '𓍂'
        elif signs[i] == 'U13':
            signs[i] = '𓍁'
        elif signs[i] == 'U12':
            signs[i] = '𓍀'
        elif signs[i] == 'U11':
            signs[i] = '𓌿'
        elif signs[i] == 'U10':
            signs[i] = '𓌾'
        elif signs[i] == 'U9':
            signs[i] = '𓌽'
        elif signs[i] == 'U8':
            signs[i] = '𓌼'
        elif signs[i] == 'U7':
            signs[i] = '𓌻'
        elif signs[i] == 'U6b':
            signs[i] = '𓌺'
        elif signs[i] == 'U6a':
            signs[i] = '𓌹'
        elif signs[i] == 'U6':
            signs[i] = '𓌸'
        elif signs[i] == 'U5':
            signs[i] = '𓌷'
        elif signs[i] == 'U4':
            signs[i] = '𓌶'
        elif signs[i] == 'U3':
            signs[i] = '𓌵'
        elif signs[i] == 'U2':
            signs[i] = '𓌴'
        elif signs[i] == 'U1':
            signs[i] = '𓌳'
        elif signs[i] == 'T36':
            signs[i] = '𓌲'
        elif signs[i] == 'T35':
            signs[i] = '𓌱'
        elif signs[i] == 'T34':
            signs[i] = '𓌰'
        elif signs[i] == 'T33a':
            signs[i] = '𓌯'
        elif signs[i] == 'T33':
            signs[i] = '𓌮'
        elif signs[i] == 'T32a':
            signs[i] = '𓌭'
        elif signs[i] == 'T32':
            signs[i] = '𓌬'
        elif signs[i] == 'T31':
            signs[i] = '𓌫'
        elif signs[i] == 'T30':
            signs[i] = '𓌪'
        elif signs[i] == 'T29':
            signs[i] = '𓌩'
        elif signs[i] == 'T28':
            signs[i] = '𓌨'
        elif signs[i] == 'T27':
            signs[i] = '𓌧'
        elif signs[i] == 'T26':
            signs[i] = '𓌦'
        elif signs[i] == 'T25':
            signs[i] = '𓌥'
        elif signs[i] == 'T24':
            signs[i] = '𓌤'
        elif signs[i] == 'T23':
            signs[i] = '𓌣'
        elif signs[i] == 'T22':
            signs[i] = '𓌢'
        elif signs[i] == 'T21':
            signs[i] = '𓌡'
        elif signs[i] == 'T20':
            signs[i] = '𓌠'
        elif signs[i] == 'T19':
            signs[i] = '𓌟'
        elif signs[i] == 'T18':
            signs[i] = '𓌞'
        elif signs[i] == 'T17':
            signs[i] = '𓌝'
        elif signs[i] == 'T16a':
            signs[i] = '𓌜'
        elif signs[i] == 'T16':
            signs[i] = '𓌛'
        elif signs[i] == 'T15':
            signs[i] = '𓌚'
        elif signs[i] == 'T14':
            signs[i] = '𓌙'
        elif signs[i] == 'T13':
            signs[i] = '𓌘'
        elif signs[i] == 'T12':
            signs[i] = '𓌗'
        elif signs[i] == 'T11a':
            signs[i] = '𓌖'
        elif signs[i] == 'T11':
            signs[i] = '𓌕'
        elif signs[i] == 'T10':
            signs[i] = '𓌔'
        elif signs[i] == 'T9a':
            signs[i] = '𓌓'
        elif signs[i] == 'T9':
            signs[i] = '𓌒'
        elif signs[i] == 'T8a':
            signs[i] = '𓌑'
        elif signs[i] == 'T8':
            signs[i] = '𓌐'
        elif signs[i] == 'T7a':
            signs[i] = '𓌏'
        elif signs[i] == 'T7':
            signs[i] = '𓌎'
        elif signs[i] == 'T6':
            signs[i] = '𓌍'
        elif signs[i] == 'T5':
            signs[i] = '𓌌'
        elif signs[i] == 'T4':
            signs[i] = '𓌋'
        elif signs[i] == 'T3a':
            signs[i] = '𓌊'
        elif signs[i] == 'T3':
            signs[i] = '𓌉'
        elif signs[i] == 'T2':
            signs[i] = '𓌈'
        elif signs[i] == 'T1':
            signs[i] = '𓌇'
        elif signs[i] == 'S46':
            signs[i] = '𓌆'
        elif signs[i] == 'S45':
            signs[i] = '𓌅'
        elif signs[i] == 'S44':
            signs[i] = '𓌄'
        elif signs[i] == 'S43':
            signs[i] = '𓌃'
        elif signs[i] == 'S42':
            signs[i] = '𓌂'
        elif signs[i] == 'S41':
            signs[i] = '𓌁'
        elif signs[i] == 'S40':
            signs[i] = '𓌀'
        elif signs[i] == 'S39':
            signs[i] = '𓋿'
        elif signs[i] == 'S38':
            signs[i] = '𓋾'
        elif signs[i] == 'S37':
            signs[i] = '𓋽'
        elif signs[i] == 'S36':
            signs[i] = '𓋼'
        elif signs[i] == 'S35a':
            signs[i] = '𓋻'
        elif signs[i] == 'S35':
            signs[i] = '𓋺'
        elif signs[i] == 'S34':
            signs[i] = '𓋹'
        elif signs[i] == 'S33':
            signs[i] = '𓋸'
        elif signs[i] == 'S32':
            signs[i] = '𓋷'
        elif signs[i] == 'S31':
            signs[i] = '𓋶'
        elif signs[i] == 'S30':
            signs[i] = '𓋵'
        elif signs[i] == 'S29':
            signs[i] = '𓋴'
        elif signs[i] == 'S28':
            signs[i] = '𓋳'
        elif signs[i] == 'S27':
            signs[i] = '𓋲'
        elif signs[i] == 'S26b':
            signs[i] = '𓋱'
        elif signs[i] == 'S26a':
            signs[i] = '𓋰'
        elif signs[i] == 'S26':
            signs[i] = '𓋯'
        elif signs[i] == 'S25':
            signs[i] = '𓋮'
        elif signs[i] == 'S24':
            signs[i] = '𓋭'
        elif signs[i] == 'S23':
            signs[i] = '𓋬'
        elif signs[i] == 'S22':
            signs[i] = '𓋫'
        elif signs[i] == 'S21':
            signs[i] = '𓋪'
        elif signs[i] == 'S20':
            signs[i] = '𓋩'
        elif signs[i] == 'S19':
            signs[i] = '𓋨'
        elif signs[i] == 'S18':
            signs[i] = '𓋧'
        elif signs[i] == 'S17a':
            signs[i] = '𓋦'
        elif signs[i] == 'S17':
            signs[i] = '𓋥'
        elif signs[i] == 'S16':
            signs[i] = '𓋤'
        elif signs[i] == 'S15':
            signs[i] = '𓋣'
        elif signs[i] == 'S14b':
            signs[i] = '𓋢'
        elif signs[i] == 'S14a':
            signs[i] = '𓋡'
        elif signs[i] == 'S14':
            signs[i] = '𓋠'
        elif signs[i] == 'S13':
            signs[i] = '𓋟'
        elif signs[i] == 'S12':
            signs[i] = '𓋞'
        elif signs[i] == 'S11':
            signs[i] = '𓋝'
        elif signs[i] == 'S10':
            signs[i] = '𓋜'
        elif signs[i] == 'S9':
            signs[i] = '𓋛'
        elif signs[i] == 'S8':
            signs[i] = '𓋚'
        elif signs[i] == 'S7':
            signs[i] = '𓋙'
        elif signs[i] == 'S6a':
            signs[i] = '𓋘'
        elif signs[i] == 'S6':
            signs[i] = '𓋗'
        elif signs[i] == 'S5':
            signs[i] = '𓋖'
        elif signs[i] == 'S4':
            signs[i] = '𓋕'
        elif signs[i] == 'S3':
            signs[i] = '𓋔'
        elif signs[i] == 'S2a':
            signs[i] = '𓋓'
        elif signs[i] == 'S2':
            signs[i] = '𓋒'
        elif signs[i] == 'S1':
            signs[i] = '𓋑'
        elif signs[i] == 'R29':
            signs[i] = '𓋐'
        elif signs[i] == 'R28':
            signs[i] = '𓋏'
        elif signs[i] == 'R27':
            signs[i] = '𓋎'
        elif signs[i] == 'R26':
            signs[i] = '𓋍'
        elif signs[i] == 'R25':
            signs[i] = '𓋌'
        elif signs[i] == 'R24':
            signs[i] = '𓋋'
        elif signs[i] == 'R23':
            signs[i] = '𓋊'
        elif signs[i] == 'R22':
            signs[i] = '𓋉'
        elif signs[i] == 'R21':
            signs[i] = '𓋈'
        elif signs[i] == 'R20':
            signs[i] = '𓋇'
        elif signs[i] == 'R19':
            signs[i] = '𓋆'
        elif signs[i] == 'R18':
            signs[i] = '𓋅'
        elif signs[i] == 'R17':
            signs[i] = '𓋄'
        elif signs[i] == 'R16a':
            signs[i] = '𓋃'
        elif signs[i] == 'R16':
            signs[i] = '𓋂'
        elif signs[i] == 'R15':
            signs[i] = '𓋁'
        elif signs[i] == 'R14':
            signs[i] = '𓋀'
        elif signs[i] == 'R13':
            signs[i] = '𓊿'
        elif signs[i] == 'R12':
            signs[i] = '𓊾'
        elif signs[i] == 'R11':
            signs[i] = '𓊽'
        elif signs[i] == 'R10a':
            signs[i] = '𓊼'
        elif signs[i] == 'R10':
            signs[i] = '𓊻'
        elif signs[i] == 'R9':
            signs[i] = '𓊺'
        elif signs[i] == 'R8':
            signs[i] = '𓊹'
        elif signs[i] == 'R7':
            signs[i] = '𓊸'
        elif signs[i] == 'R6':
            signs[i] = '𓊷'
        elif signs[i] == 'R5':
            signs[i] = '𓊶'
        elif signs[i] == 'R4':
            signs[i] = '𓊵'
        elif signs[i] == 'R3b':
            signs[i] = '𓊴'
        elif signs[i] == 'R3a':
            signs[i] = '𓊳'
        elif signs[i] == 'R3':
            signs[i] = '𓊲'
        elif signs[i] == 'R2a':
            signs[i] = '𓊱'
        elif signs[i] == 'R2':
            signs[i] = '𓊰'
        elif signs[i] == 'R1':
            signs[i] = '𓊯'
        elif signs[i] == 'Q7':
            signs[i] = '𓊮'
        elif signs[i] == 'Q6':
            signs[i] = '𓊭'
        elif signs[i] == 'Q5':
            signs[i] = '𓊬'
        elif signs[i] == 'Q4':
            signs[i] = '𓊫'
        elif signs[i] == 'Q3':
            signs[i] = '𓊪'
        elif signs[i] == 'Q2':
            signs[i] = '𓊩'
        elif signs[i] == 'Q1':
            signs[i] = '𓊨'
        elif signs[i] == 'P11':
            signs[i] = '𓊧'
        elif signs[i] == 'P10':
            signs[i] = '𓊦'
        elif signs[i] == 'P9':
            signs[i] = '𓊥'
        elif signs[i] == 'P8':
            signs[i] = '𓊤'
        elif signs[i] == 'P7':
            signs[i] = '𓊣'
        elif signs[i] == 'P6':
            signs[i] = '𓊢'
        elif signs[i] == 'P5':
            signs[i] = '𓊡'
        elif signs[i] == 'P4':
            signs[i] = '𓊠'
        elif signs[i] == 'P3a':
            signs[i] = '𓊟'
        elif signs[i] == 'P3':
            signs[i] = '𓊞'
        elif signs[i] == 'P2':
            signs[i] = '𓊝'
        elif signs[i] == 'P1a':
            signs[i] = '𓊜'
        elif signs[i] == 'P1':
            signs[i] = '𓊛'
        elif signs[i] == 'O51':
            signs[i] = '𓊚'
        elif signs[i] == 'O5b':
            signs[i] = '𓊙'
        elif signs[i] == 'O5a':
            signs[i] = '𓊘'
        elif signs[i] == 'O50':
            signs[i] = '𓊗'
        elif signs[i] == 'O49':
            signs[i] = '𓊖'
        elif signs[i] == 'O48':
            signs[i] = '𓊕'
        elif signs[i] == 'O47':
            signs[i] = '𓊔'
        elif signs[i] == 'O46':
            signs[i] = '𓊓'
        elif signs[i] == 'O45':
            signs[i] = '𓊒'
        elif signs[i] == 'O44':
            signs[i] = '𓊑'
        elif signs[i] == 'O43':
            signs[i] = '𓊐'
        elif signs[i] == 'O42':
            signs[i] = '𓊏'
        elif signs[i] == 'O41':
            signs[i] = '𓊎'
        elif signs[i] == 'O40':
            signs[i] = '𓊍'
        elif signs[i] == 'O39':
            signs[i] = '𓊌'
        elif signs[i] == 'O38':
            signs[i] = '𓊋'
        elif signs[i] == 'O37':
            signs[i] = '𓊊'
        elif signs[i] == 'O36d':
            signs[i] = '𓊉'
        elif signs[i] == 'O36c':
            signs[i] = '𓊈'
        elif signs[i] == 'O36b':
            signs[i] = '𓊇'
        elif signs[i] == 'O36a':
            signs[i] = '𓊆'
        elif signs[i] == 'O36':
            signs[i] = '𓊅'
        elif signs[i] == 'O35':
            signs[i] = '𓊄'
        elif signs[i] == 'O34':
            signs[i] = '𓊃'
        elif signs[i] == 'O33a':
            signs[i] = '𓊂'
        elif signs[i] == 'O33':
            signs[i] = '𓊁'
        elif signs[i] == 'O32':
            signs[i] = '𓊀'
        elif signs[i] == 'O31':
            signs[i] = '𓉿'
        elif signs[i] == 'O3a':
            signs[i] = '𓉾'
        elif signs[i] == 'O30':
            signs[i] = '𓉽'
        elif signs[i] == 'O29a':
            signs[i] = '𓉼'
        elif signs[i] == 'O29':
            signs[i] = '𓉻'
        elif signs[i] == 'O28':
            signs[i] = '𓉺'
        elif signs[i] == 'O27':
            signs[i] = '𓉹'
        elif signs[i] == 'O26':
            signs[i] = '𓉸'
        elif signs[i] == 'O25a':
            signs[i] = '𓉷'
        elif signs[i] == 'O25':
            signs[i] = '𓉶'
        elif signs[i] == 'O24a':
            signs[i] = '𓉵'
        elif signs[i] == 'O24':
            signs[i] = '𓉴'
        elif signs[i] == 'O23':
            signs[i] = '𓉳'
        elif signs[i] == 'O22':
            signs[i] = '𓉲'
        elif signs[i] == 'O21':
            signs[i] = '𓉱'
        elif signs[i] == 'O2a':
            signs[i] = '𓉰'
        elif signs[i] == 'O20':
            signs[i] = '𓉯'
        elif signs[i] == 'O19a':
            signs[i] = '𓉮'
        elif signs[i] == 'O19':
            signs[i] = '𓉭'
        elif signs[i] == 'O18':
            signs[i] = '𓉬'
        elif signs[i] == 'O17':
            signs[i] = '𓉫'
        elif signs[i] == 'O16':
            signs[i] = '𓉪'
        elif signs[i] == 'O15':
            signs[i] = '𓉩'
        elif signs[i] == 'O14':
            signs[i] = '𓉨'
        elif signs[i] == 'O13':
            signs[i] = '𓉧'
        elif signs[i] == 'O12':
            signs[i] = '𓉦'
        elif signs[i] == 'O11':
            signs[i] = '𓉥'
        elif signs[i] == 'O10c':
            signs[i] = '𓉤'
        elif signs[i] == 'O10b':
            signs[i] = '𓉣'
        elif signs[i] == 'O10a':
            signs[i] = '𓉢'
        elif signs[i] == 'O10':
            signs[i] = '𓉡'
        elif signs[i] == 'O9':
            signs[i] = '𓉠'
        elif signs[i] == 'O8':
            signs[i] = '𓉟'
        elif signs[i] == 'O7':
            signs[i] = '𓉞'
        elif signs[i] == 'O6f':
            signs[i] = '𓉝'
        elif signs[i] == 'O6e':
            signs[i] = '𓉜'
        elif signs[i] == 'O6d':
            signs[i] = '𓉛'
        elif signs[i] == 'O6c':
            signs[i] = '𓉚'
        elif signs[i] == 'O6b':
            signs[i] = '𓉙'
        elif signs[i] == 'O6a':
            signs[i] = '𓉘'
        elif signs[i] == 'O6':
            signs[i] = '𓉗'
        elif signs[i] == 'O5a':
            signs[i] = '𓉖'
        elif signs[i] == 'O5':
            signs[i] = '𓉕'
        elif signs[i] == 'O4':
            signs[i] = '𓉔'
        elif signs[i] == 'O3':
            signs[i] = '𓉓'
        elif signs[i] == 'O2':
            signs[i] = '𓉒'
        elif signs[i] == 'O1a':
            signs[i] = '𓉑'
        elif signs[i] == 'O1':
            signs[i] = '𓉐'
        elif signs[i] == 'NU22a':
            signs[i] = '𓉏'
        elif signs[i] == 'NU22':
            signs[i] = '𓉎'
        elif signs[i] == 'NU21':
            signs[i] = '𓉍'
        elif signs[i] == 'NU20':
            signs[i] = '𓉌'
        elif signs[i] == 'NU19':
            signs[i] = '𓉋'
        elif signs[i] == 'NU18a':
            signs[i] = '𓉊'
        elif signs[i] == 'NU18':
            signs[i] = '𓉉'
        elif signs[i] == 'NU17':
            signs[i] = '𓉈'
        elif signs[i] == 'NU16':
            signs[i] = '𓉇'
        elif signs[i] == 'NU15':
            signs[i] = '𓉆'
        elif signs[i] == 'NU14':
            signs[i] = '𓉅'
        elif signs[i] == 'NU13':
            signs[i] = '𓉄'
        elif signs[i] == 'NU12':
            signs[i] = '𓉃'
        elif signs[i] == 'NU11a':
            signs[i] = '𓉂'
        elif signs[i] == 'NU11':
            signs[i] = '𓉁'
        elif signs[i] == 'NU1a':
            signs[i] = '𓉀'
        elif signs[i] == 'NU10':
            signs[i] = '𓈿'
        elif signs[i] == 'NU9':
            signs[i] = '𓈾'
        elif signs[i] == 'NU8':
            signs[i] = '𓈽'
        elif signs[i] == 'NU7':
            signs[i] = '𓈼'
        elif signs[i] == 'NU6':
            signs[i] = '𓈻'
        elif signs[i] == 'NU5':
            signs[i] = '𓈺'
        elif signs[i] == 'NU4':
            signs[i] = '𓈹'
        elif signs[i] == 'NU3':
            signs[i] = '𓈸'
        elif signs[i] == 'NU2':
            signs[i] = '𓈷'
        elif signs[i] == 'NU1':
            signs[i] = '𓈶'
        elif signs[i] == 'NL20':
            signs[i] = '𓈵'
        elif signs[i] == 'NL19':
            signs[i] = '𓈴'
        elif signs[i] == 'NL18':
            signs[i] = '𓈳'
        elif signs[i] == 'NL17a':
            signs[i] = '𓈲'
        elif signs[i] == 'NL17':
            signs[i] = '𓈱'
        elif signs[i] == 'NL16':
            signs[i] = '𓈰'
        elif signs[i] == 'NL15':
            signs[i] = '𓈯'
        elif signs[i] == 'NL14':
            signs[i] = '𓈮'
        elif signs[i] == 'NL13':
            signs[i] = '𓈭'
        elif signs[i] == 'NL12':
            signs[i] = '𓈬'
        elif signs[i] == 'NL11':
            signs[i] = '𓈫'
        elif signs[i] == 'NL10':
            signs[i] = '𓈪'
        elif signs[i] == 'NL9':
            signs[i] = '𓈩'
        elif signs[i] == 'NL8':
            signs[i] = '𓈨'
        elif signs[i] == 'NL7':
            signs[i] = '𓈧'
        elif signs[i] == 'NL6':
            signs[i] = '𓈦'
        elif signs[i] == 'NL5a':
            signs[i] = '𓈥'
        elif signs[i] == 'NL5':
            signs[i] = '𓈤'
        elif signs[i] == 'NL4':
            signs[i] = '𓈣'
        elif signs[i] == 'NL3':
            signs[i] = '𓈢'
        elif signs[i] == 'NL2':
            signs[i] = '𓈡'
        elif signs[i] == 'NL1':
            signs[i] = '𓈠'
        elif signs[i] == 'N42':
            signs[i] = '𓈟'
        elif signs[i] == 'N41':
            signs[i] = '𓈞'
        elif signs[i] == 'N40':
            signs[i] = '𓈝'
        elif signs[i] == 'N39':
            signs[i] = '𓈜'
        elif signs[i] == 'N38':
            signs[i] = '𓈛'
        elif signs[i] == 'N37a':
            signs[i] = '𓈚'
        elif signs[i] == 'N37':
            signs[i] = '𓈙'
        elif signs[i] == 'N36':
            signs[i] = '𓈘'
        elif signs[i] == 'N35a':
            signs[i] = '𓈗'
        elif signs[i] == 'N35':
            signs[i] = '𓈖'
        elif signs[i] == 'N34a':
            signs[i] = '𓈕'
        elif signs[i] == 'N34':
            signs[i] = '𓈔'
        elif signs[i] == 'N33a':
            signs[i] = '𓈓'
        elif signs[i] == 'N33':
            signs[i] = '𓈒'
        elif signs[i] == 'N32':
            signs[i] = '𓈑'
        elif signs[i] == 'N31':
            signs[i] = '𓈐'
        elif signs[i] == 'N30':
            signs[i] = '𓈏'
        elif signs[i] == 'N29':
            signs[i] = '𓈎'
        elif signs[i] == 'N28':
            signs[i] = '𓈍'
        elif signs[i] == 'N27':
            signs[i] = '𓈌'
        elif signs[i] == 'N26':
            signs[i] = '𓈋'
        elif signs[i] == 'N25a':
            signs[i] = '𓈊'
        elif signs[i] == 'N25':
            signs[i] = '𓈉'
        elif signs[i] == 'N24':
            signs[i] = '𓈈'
        elif signs[i] == 'N23':
            signs[i] = '𓈇'
        elif signs[i] == 'N22':
            signs[i] = '𓈆'
        elif signs[i] == 'N21':
            signs[i] = '𓈅'
        elif signs[i] == 'N20':
            signs[i] = '𓈄'
        elif signs[i] == 'N19':
            signs[i] = '𓈃'
        elif signs[i] == 'N18b':
            signs[i] = '𓈂'
        elif signs[i] == 'N18a':
            signs[i] = '𓈁'
        elif signs[i] == 'N18':
            signs[i] = '𓈀'
        elif signs[i] == 'N17':
            signs[i] = '𓇿'
        elif signs[i] == 'N16':
            signs[i] = '𓇾'
        elif signs[i] == 'N15':
            signs[i] = '𓇽'
        elif signs[i] == 'N14':
            signs[i] = '𓇼'
        elif signs[i] == 'N13':
            signs[i] = '𓇻'
        elif signs[i] == 'N12':
            signs[i] = '𓇺'
        elif signs[i] == 'N11':
            signs[i] = '𓇹'
        elif signs[i] == 'N10':
            signs[i] = '𓇸'
        elif signs[i] == 'N9':
            signs[i] = '𓇷'
        elif signs[i] == 'N8':
            signs[i] = '𓇶'
        elif signs[i] == 'N7':
            signs[i] = '𓇵'
        elif signs[i] == 'N6':
            signs[i] = '𓇴'
        elif signs[i] == 'N5':
            signs[i] = '𓇳'
        elif signs[i] == 'N4':
            signs[i] = '𓇲'
        elif signs[i] == 'N3':
            signs[i] = '𓇱'
        elif signs[i] == 'N2':
            signs[i] = '𓇰'
        elif signs[i] == 'N1':
            signs[i] = '𓇯'
        elif signs[i] == 'M44':
            signs[i] = '𓇮'
        elif signs[i] == 'M43':
            signs[i] = '𓇭'
        elif signs[i] == 'M42':
            signs[i] = '𓇬'
        elif signs[i] == 'M41':
            signs[i] = '𓇫'
        elif signs[i] == 'M40a':
            signs[i] = '𓇪'
        elif signs[i] == 'M40':
            signs[i] = '𓇩'
        elif signs[i] == 'M39':
            signs[i] = '𓇨'
        elif signs[i] == 'M38':
            signs[i] = '𓇧'
        elif signs[i] == 'M37':
            signs[i] = '𓇦'
        elif signs[i] == 'M36':
            signs[i] = '𓇥'
        elif signs[i] == 'M35':
            signs[i] = '𓇤'
        elif signs[i] == 'M34':
            signs[i] = '𓇣'
        elif signs[i] == 'M33b':
            signs[i] = '𓇢'
        elif signs[i] == 'M33a':
            signs[i] = '𓇡'
        elif signs[i] == 'M33':
            signs[i] = '𓇠'
        elif signs[i] == 'M32':
            signs[i] = '𓇟'
        elif signs[i] == 'M31a':
            signs[i] = '𓇞'
        elif signs[i] == 'M31':
            signs[i] = '𓇝'
        elif signs[i] == 'M30':
            signs[i] = '𓇜'
        elif signs[i] == 'M29':
            signs[i] = '𓇛'
        elif signs[i] == 'M28a':
            signs[i] = '𓇚'
        elif signs[i] == 'M28':
            signs[i] = '𓇙'
        elif signs[i] == 'M27':
            signs[i] = '𓇘'
        elif signs[i] == 'M26':
            signs[i] = '𓇗'
        elif signs[i] == 'M25':
            signs[i] = '𓇖'
        elif signs[i] == 'M24a':
            signs[i] = '𓇕'
        elif signs[i] == 'M24':
            signs[i] = '𓇔'
        elif signs[i] == 'M23':
            signs[i] = '𓇓'
        elif signs[i] == 'M22a':
            signs[i] = '𓇒'
        elif signs[i] == 'M22':
            signs[i] = '𓇑'
        elif signs[i] == 'M21':
            signs[i] = '𓇐'
        elif signs[i] == 'M20':
            signs[i] = '𓇏'
        elif signs[i] == 'M19':
            signs[i] = '𓇎'
        elif signs[i] == 'M18':
            signs[i] = '𓇍'
        elif signs[i] == 'M17a':
            signs[i] = '𓇌'
        elif signs[i] == 'M17':
            signs[i] = '𓇋'
        elif signs[i] == 'M16a':
            signs[i] = '𓇊'
        elif signs[i] == 'M16':
            signs[i] = '𓇉'
        elif signs[i] == 'M15a':
            signs[i] = '𓇈'
        elif signs[i] == 'M15':
            signs[i] = '𓇇'
        elif signs[i] == 'M14':
            signs[i] = '𓇆'
        elif signs[i] == 'M13':
            signs[i] = '𓇅'
        elif signs[i] == 'M12h':
            signs[i] = '𓇄'
        elif signs[i] == 'M12g':
            signs[i] = '𓇃'
        elif signs[i] == 'M12f':
            signs[i] = '𓇂'
        elif signs[i] == 'M12e':
            signs[i] = '𓇁'
        elif signs[i] == 'M12d':
            signs[i] = '𓇀'
        elif signs[i] == 'M12c':
            signs[i] = '𓆿'
        elif signs[i] == 'M12b':
            signs[i] = '𓆾'
        elif signs[i] == 'M12a':
            signs[i] = '𓆽'
        elif signs[i] == 'M12':
            signs[i] = '𓆼'
        elif signs[i] == 'M11':
            signs[i] = '𓆻'
        elif signs[i] == 'M10a':
            signs[i] = '𓆺'
        elif signs[i] == 'M10':
            signs[i] = '𓆹'
        elif signs[i] == 'M9':
            signs[i] = '𓆸'
        elif signs[i] == 'M8':
            signs[i] = '𓆷'
        elif signs[i] == 'M7':
            signs[i] = '𓆶'
        elif signs[i] == 'M6':
            signs[i] = '𓆵'
        elif signs[i] == 'M5':
            signs[i] = '𓆴'
        elif signs[i] == 'M4':
            signs[i] = '𓆳'
        elif signs[i] == 'M3a':
            signs[i] = '𓆲'
        elif signs[i] == 'M3':
            signs[i] = '𓆱'
        elif signs[i] == 'M2':
            signs[i] = '𓆰'
        elif signs[i] == 'M1b':
            signs[i] = '𓆯'
        elif signs[i] == 'M1a':
            signs[i] = '𓆮'
        elif signs[i] == 'M1':
            signs[i] = '𓆭'
        elif signs[i] == 'L8':
            signs[i] = '𓆬'
        elif signs[i] == 'L7':
            signs[i] = '𓆫'
        elif signs[i] == 'L6a':
            signs[i] = '𓆪'
        elif signs[i] == 'L6':
            signs[i] = '𓆩'
        elif signs[i] == 'L5':
            signs[i] = '𓆨'
        elif signs[i] == 'L4':
            signs[i] = '𓆧'
        elif signs[i] == 'L3':
            signs[i] = '𓆦'
        elif signs[i] == 'L2a':
            signs[i] = '𓆥'
        elif signs[i] == 'L2':
            signs[i] = '𓆤'
        elif signs[i] == 'L1':
            signs[i] = '𓆣'
        elif signs[i] == 'K8':
            signs[i] = '𓆢'
        elif signs[i] == 'K7':
            signs[i] = '𓆡'
        elif signs[i] == 'K6':
            signs[i] = '𓆠'
        elif signs[i] == 'K5':
            signs[i] = '𓆟'
        elif signs[i] == 'K4':
            signs[i] = '𓆞'
        elif signs[i] == 'K3':
            signs[i] = '𓆝'
        elif signs[i] == 'K2':
            signs[i] = '𓆜'
        elif signs[i] == 'K1':
            signs[i] = '𓆛'
        elif signs[i] == 'I15':
            signs[i] = '𓆚'
        elif signs[i] == 'I14':
            signs[i] = '𓆙'
        elif signs[i] == 'I13':
            signs[i] = '𓆘'
        elif signs[i] == 'I12':
            signs[i] = '𓆗'
        elif signs[i] == 'I11a':
            signs[i] = '𓆖'
        elif signs[i] == 'I11':
            signs[i] = '𓆕'
        elif signs[i] == 'I1a':
            signs[i] = '𓆔'
        elif signs[i] == 'I10':
            signs[i] = '𓆓'
        elif signs[i] == 'I9a':
            signs[i] = '𓆒'
        elif signs[i] == 'I9':
            signs[i] = '𓆑'
        elif signs[i] == 'I8':
            signs[i] = '𓆐'
        elif signs[i] == 'I7':
            signs[i] = '𓆏'
        elif signs[i] == 'I6':
            signs[i] = '𓆎'
        elif signs[i] == 'I5a':
            signs[i] = '𓆍'
        elif signs[i] == 'I5':
            signs[i] = '𓆌'
        elif signs[i] == 'I4':
            signs[i] = '𓆋'
        elif signs[i] == 'I3':
            signs[i] = '𓆊'
        elif signs[i] == 'I2':
            signs[i] = '𓆉'
        elif signs[i] == 'I1':
            signs[i] = '𓆈'
        elif signs[i] == 'H8':
            signs[i] = '𓆇'
        elif signs[i] == 'H7':
            signs[i] = '𓆆'
        elif signs[i] == 'H6a':
            signs[i] = '𓆅'
        elif signs[i] == 'H6':
            signs[i] = '𓆄'
        elif signs[i] == 'H5':
            signs[i] = '𓆃'
        elif signs[i] == 'H4':
            signs[i] = '𓆂'
        elif signs[i] == 'H3':
            signs[i] = '𓆁'
        elif signs[i] == 'H2':
            signs[i] = '𓆀'
        elif signs[i] == 'H1':
            signs[i] = '𓅿'
        elif signs[i] == 'G54':
            signs[i] = '𓅾'
        elif signs[i] == 'G53':
            signs[i] = '𓅽'
        elif signs[i] == 'G52':
            signs[i] = '𓅼'
        elif signs[i] == 'G51':
            signs[i] = '𓅻'
        elif signs[i] == 'G50':
            signs[i] = '𓅺'
        elif signs[i] == 'G49':
            signs[i] = '𓅹'
        elif signs[i] == 'G48':
            signs[i] = '𓅸'
        elif signs[i] == 'G47':
            signs[i] = '𓅷'
        elif signs[i] == 'G46':
            signs[i] = '𓅶'
        elif signs[i] == 'G45a':
            signs[i] = '𓅵'
        elif signs[i] == 'G45':
            signs[i] = '𓅴'
        elif signs[i] == 'G44':
            signs[i] = '𓅳'
        elif signs[i] == 'G43a':
            signs[i] = '𓅲'
        elif signs[i] == 'G43':
            signs[i] = '𓅱'
        elif signs[i] == 'G42':
            signs[i] = '𓅰'
        elif signs[i] == 'G41':
            signs[i] = '𓅯'
        elif signs[i] == 'G40':
            signs[i] = '𓅮'
        elif signs[i] == 'G39':
            signs[i] = '𓅭'
        elif signs[i] == 'G38':
            signs[i] = '𓅬'
        elif signs[i] == 'G37a':
            signs[i] = '𓅫'
        elif signs[i] == 'G37':
            signs[i] = '𓅪'
        elif signs[i] == 'G36a':
            signs[i] = '𓅩'
        elif signs[i] == 'G36':
            signs[i] = '𓅨'
        elif signs[i] == 'G35':
            signs[i] = '𓅧'
        elif signs[i] == 'G34':
            signs[i] = '𓅦'
        elif signs[i] == 'G33':
            signs[i] = '𓅥'
        elif signs[i] == 'G32':
            signs[i] = '𓅤'
        elif signs[i] == 'G31':
            signs[i] = '𓅣'
        elif signs[i] == 'G30':
            signs[i] = '𓅢'
        elif signs[i] == 'G29':
            signs[i] = '𓅡'
        elif signs[i] == 'G28':
            signs[i] = '𓅠'
        elif signs[i] == 'G27':
            signs[i] = '𓅟'
        elif signs[i] == 'G26a':
            signs[i] = '𓅞'
        elif signs[i] == 'G26':
            signs[i] = '𓅝'
        elif signs[i] == 'G25':
            signs[i] = '𓅜'
        elif signs[i] == 'G24':
            signs[i] = '𓅛'
        elif signs[i] == 'G23':
            signs[i] = '𓅚'
        elif signs[i] == 'G22':
            signs[i] = '𓅙'
        elif signs[i] == 'G21':
            signs[i] = '𓅘'
        elif signs[i] == 'G20a':
            signs[i] = '𓅗'
        elif signs[i] == 'G20':
            signs[i] = '𓅖'
        elif signs[i] == 'G19':
            signs[i] = '𓅕'
        elif signs[i] == 'G18':
            signs[i] = '𓅔'
        elif signs[i] == 'G17':
            signs[i] = '𓅓'
        elif signs[i] == 'G16':
            signs[i] = '𓅒'
        elif signs[i] == 'G15':
            signs[i] = '𓅑'
        elif signs[i] == 'G14':
            signs[i] = '𓅐'
        elif signs[i] == 'G13':
            signs[i] = '𓅏'
        elif signs[i] == 'G12':
            signs[i] = '𓅎'
        elif signs[i] == 'G11a':
            signs[i] = '𓅍'
        elif signs[i] == 'G11':
            signs[i] = '𓅌'
        elif signs[i] == 'G10':
            signs[i] = '𓅋'
        elif signs[i] == 'G9':
            signs[i] = '𓅊'
        elif signs[i] == 'G8':
            signs[i] = '𓅉'
        elif signs[i] == 'G7b':
            signs[i] = '𓅈'
        elif signs[i] == 'G7a':
            signs[i] = '𓅇'
        elif signs[i] == 'G7':
            signs[i] = '𓅆'
        elif signs[i] == 'G6a':
            signs[i] = '𓅅'
        elif signs[i] == 'G6':
            signs[i] = '𓅄'
        elif signs[i] == 'G5':
            signs[i] = '𓅃'
        elif signs[i] == 'G4':
            signs[i] = '𓅂'
        elif signs[i] == 'G3':
            signs[i] = '𓅁'
        elif signs[i] == 'G2':
            signs[i] = '𓅀'
        elif signs[i] == 'G1':
            signs[i] = '𓄿'
        elif signs[i] == 'F53':
            signs[i] = '𓄾'
        elif signs[i] == 'F52':
            signs[i] = '𓄽'
        elif signs[i] == 'F51c':
            signs[i] = '𓄼'
        elif signs[i] == 'F51b':
            signs[i] = '𓄻'
        elif signs[i] == 'F51a':
            signs[i] = '𓄺'
        elif signs[i] == 'F51':
            signs[i] = '𓄹'
        elif signs[i] == 'F50':
            signs[i] = '𓄸'
        elif signs[i] == 'F49':
            signs[i] = '𓄷'
        elif signs[i] == 'F48':
            signs[i] = '𓄶'
        elif signs[i] == 'F47a':
            signs[i] = '𓄵'
        elif signs[i] == 'F47':
            signs[i] = '𓄴'
        elif signs[i] == 'F46a':
            signs[i] = '𓄳'
        elif signs[i] == 'F46':
            signs[i] = '𓄲'
        elif signs[i] == 'F45a':
            signs[i] = '𓄱'
        elif signs[i] == 'F45':
            signs[i] = '𓄰'
        elif signs[i] == 'F44':
            signs[i] = '𓄯'
        elif signs[i] == 'F43':
            signs[i] = '𓄮'
        elif signs[i] == 'F42':
            signs[i] = '𓄭'
        elif signs[i] == 'F41':
            signs[i] = '𓄬'
        elif signs[i] == 'F40':
            signs[i] = '𓄫'
        elif signs[i] == 'F39':
            signs[i] = '𓄪'
        elif signs[i] == 'F38a':
            signs[i] = '𓄩'
        elif signs[i] == 'F38':
            signs[i] = '𓄨'
        elif signs[i] == 'F37a':
            signs[i] = '𓄧'
        elif signs[i] == 'F37':
            signs[i] = '𓄦'
        elif signs[i] == 'F36':
            signs[i] = '𓄥'
        elif signs[i] == 'F35':
            signs[i] = '𓄤'
        elif signs[i] == 'F34':
            signs[i] = '𓄣'
        elif signs[i] == 'F33':
            signs[i] = '𓄢'
        elif signs[i] == 'F32':
            signs[i] = '𓄡'
        elif signs[i] == 'F31a':
            signs[i] = '𓄠'
        elif signs[i] == 'F31':
            signs[i] = '𓄟'
        elif signs[i] == 'F30':
            signs[i] = '𓄞'
        elif signs[i] == 'F29':
            signs[i] = '𓄝'
        elif signs[i] == 'F28':
            signs[i] = '𓄜'
        elif signs[i] == 'F27':
            signs[i] = '𓄛'
        elif signs[i] == 'F26':
            signs[i] = '𓄚'
        elif signs[i] == 'F25':
            signs[i] = '𓄙'
        elif signs[i] == 'F24':
            signs[i] = '𓄘'
        elif signs[i] == 'F23':
            signs[i] = '𓄗'
        elif signs[i] == 'F22':
            signs[i] = '𓄖'
        elif signs[i] == 'F21a':
            signs[i] = '𓄕'
        elif signs[i] == 'F21':
            signs[i] = '𓄔'
        elif signs[i] == 'F20':
            signs[i] = '𓄓'
        elif signs[i] == 'F19':
            signs[i] = '𓄒'
        elif signs[i] == 'F18':
            signs[i] = '𓄑'
        elif signs[i] == 'F17':
            signs[i] = '𓄐'
        elif signs[i] == 'F16':
            signs[i] = '𓄏'
        elif signs[i] == 'F15':
            signs[i] = '𓄎'
        elif signs[i] == 'F14':
            signs[i] = '𓄍'
        elif signs[i] == 'F13a':
            signs[i] = '𓄌'
        elif signs[i] == 'F13':
            signs[i] = '𓄋'
        elif signs[i] == 'F12':
            signs[i] = '𓄊'
        elif signs[i] == 'F11':
            signs[i] = '𓄉'
        elif signs[i] == 'F10':
            signs[i] = '𓄈'
        elif signs[i] == 'F9':
            signs[i] = '𓄇'
        elif signs[i] == 'F8':
            signs[i] = '𓄆'
        elif signs[i] == 'F7':
            signs[i] = '𓄅'
        elif signs[i] == 'F6':
            signs[i] = '𓄄'
        elif signs[i] == 'F5':
            signs[i] = '𓄃'
        elif signs[i] == 'F4':
            signs[i] = '𓄂'
        elif signs[i] == 'F3':
            signs[i] = '𓄁'
        elif signs[i] == 'F2':
            signs[i] = '𓄀'
        elif signs[i] == 'F1a':
            signs[i] = '𓃿'
        elif signs[i] == 'F1':
            signs[i] = '𓃾'
        elif signs[i] == 'E38':
            signs[i] = '𓃽'
        elif signs[i] == 'E37':
            signs[i] = '𓃼'
        elif signs[i] == 'E36':
            signs[i] = '𓃻'
        elif signs[i] == 'E34a':
            signs[i] = '𓃺'
        elif signs[i] == 'E34':
            signs[i] = '𓃹'
        elif signs[i] == 'E33':
            signs[i] = '𓃸'
        elif signs[i] == 'E32':
            signs[i] = '𓃷'
        elif signs[i] == 'E31':
            signs[i] = '𓃶'
        elif signs[i] == 'E30':
            signs[i] = '𓃵'
        elif signs[i] == 'E29':
            signs[i] = '𓃴'
        elif signs[i] == 'E28a':
            signs[i] = '𓃳'
        elif signs[i] == 'E28':
            signs[i] = '𓃲'
        elif signs[i] == 'E27':
            signs[i] = '𓃱'
        elif signs[i] == 'E26':
            signs[i] = '𓃰'
        elif signs[i] == 'E25':
            signs[i] = '𓃯'
        elif signs[i] == 'E24':
            signs[i] = '𓃮'
        elif signs[i] == 'E23':
            signs[i] = '𓃭'
        elif signs[i] == 'E22':
            signs[i] = '𓃬'
        elif signs[i] == 'E21':
            signs[i] = '𓃫'
        elif signs[i] == 'E2a':
            signs[i] = '𓃪'
        elif signs[i] == 'E20':
            signs[i] = '𓃩'
        elif signs[i] == 'E19':
            signs[i] = '𓃨'
        elif signs[i] == 'E18':
            signs[i] = '𓃧'
        elif signs[i] == 'E17a':
            signs[i] = '𓃦'
        elif signs[i] == 'E17':
            signs[i] = '𓃥'
        elif signs[i] == 'E16a':
            signs[i] = '𓃤'
        elif signs[i] == 'E16':
            signs[i] = '𓃣'
        elif signs[i] == 'E15':
            signs[i] = '𓃢'
        elif signs[i] == 'E14':
            signs[i] = '𓃡'
        elif signs[i] == 'E13':
            signs[i] = '𓃠'
        elif signs[i] == 'E12':
            signs[i] = '𓃟'
        elif signs[i] == 'E11':
            signs[i] = '𓃞'
        elif signs[i] == 'E10':
            signs[i] = '𓃝'
        elif signs[i] == 'E9a':
            signs[i] = '𓃜'
        elif signs[i] == 'E9':
            signs[i] = '𓃛'
        elif signs[i] == 'E8a':
            signs[i] = '𓃚'
        elif signs[i] == 'E8':
            signs[i] = '𓃙'
        elif signs[i] == 'E7':
            signs[i] = '𓃘'
        elif signs[i] == 'E6':
            signs[i] = '𓃗'
        elif signs[i] == 'E5':
            signs[i] = '𓃖'
        elif signs[i] == 'E4':
            signs[i] = '𓃕'
        elif signs[i] == 'E3':
            signs[i] = '𓃔'
        elif signs[i] == 'E2':
            signs[i] = '𓃓'
        elif signs[i] == 'E1':
            signs[i] = '𓃒'
        elif signs[i] == 'D67h':
            signs[i] = '𓃑'
        elif signs[i] == 'D67g':
            signs[i] = '𓃐'
        elif signs[i] == 'D67f':
            signs[i] = '𓃏'
        elif signs[i] == 'D67e':
            signs[i] = '𓃎'
        elif signs[i] == 'D67d':
            signs[i] = '𓃍'
        elif signs[i] == 'D67c':
            signs[i] = '𓃌'
        elif signs[i] == 'D67b':
            signs[i] = '𓃋'
        elif signs[i] == 'D67a':
            signs[i] = '𓃊'
        elif signs[i] == 'D67':
            signs[i] = '𓃉'
        elif signs[i] == 'D66':
            signs[i] = '𓃈'
        elif signs[i] == 'D65':
            signs[i] = '𓃇'
        elif signs[i] == 'D64':
            signs[i] = '𓃆'
        elif signs[i] == 'D63':
            signs[i] = '𓃅'
        elif signs[i] == 'D62':
            signs[i] = '𓃄'
        elif signs[i] == 'D61':
            signs[i] = '𓃃'
        elif signs[i] == 'D60':
            signs[i] = '𓃂'
        elif signs[i] == 'D59':
            signs[i] = '𓃁'
        elif signs[i] == 'D58':
            signs[i] = '𓃀'
        elif signs[i] == 'D57':
            signs[i] = '𓂿'
        elif signs[i] == 'D56':
            signs[i] = '𓂾'
        elif signs[i] == 'D55':
            signs[i] = '𓂽'
        elif signs[i] == 'D54a':
            signs[i] = '𓂼'
        elif signs[i] == 'D54':
            signs[i] = '𓂻'
        elif signs[i] == 'D53':
            signs[i] = '𓂺'
        elif signs[i] == 'D52a':
            signs[i] = '𓂹'
        elif signs[i] == 'D52':
            signs[i] = '𓂸'
        elif signs[i] == 'D51':
            signs[i] = '𓂷'
        elif signs[i] == 'D50i':
            signs[i] = '𓂶'
        elif signs[i] == 'D50h':
            signs[i] = '𓂵'
        elif signs[i] == 'D50g':
            signs[i] = '𓂴'
        elif signs[i] == 'D50f':
            signs[i] = '𓂳'
        elif signs[i] == 'D50e':
            signs[i] = '𓂲'
        elif signs[i] == 'D50d':
            signs[i] = '𓂱'
        elif signs[i] == 'D50c':
            signs[i] = '𓂰'
        elif signs[i] == 'D50b':
            signs[i] = '𓂯'
        elif signs[i] == 'D50a':
            signs[i] = '𓂮'
        elif signs[i] == 'D50':
            signs[i] = '𓂭'
        elif signs[i] == 'D49':
            signs[i] = '𓂬'
        elif signs[i] == 'D48a':
            signs[i] = '𓂫'
        elif signs[i] == 'D48':
            signs[i] = '𓂪'
        elif signs[i] == 'D47':
            signs[i] = '𓂩'
        elif signs[i] == 'D46a':
            signs[i] = '𓂨'
        elif signs[i] == 'D46':
            signs[i] = '𓂧'
        elif signs[i] == 'D45':
            signs[i] = '𓂦'
        elif signs[i] == 'D44':
            signs[i] = '𓂥'
        elif signs[i] == 'D43':
            signs[i] = '𓂤'
        elif signs[i] == 'D42':
            signs[i] = '𓂣'
        elif signs[i] == 'D41':
            signs[i] = '𓂢'
        elif signs[i] == 'D40':
            signs[i] = '𓂡'
        elif signs[i] == 'D39':
            signs[i] = '𓂠'
        elif signs[i] == 'D38':
            signs[i] = '𓂟'
        elif signs[i] == 'D37':
            signs[i] = '𓂞'
        elif signs[i] == 'D36':
            signs[i] = '𓂝'
        elif signs[i] == 'D35':
            signs[i] = '𓂜'
        elif signs[i] == 'D34a':
            signs[i] = '𓂛'
        elif signs[i] == 'D34':
            signs[i] = '𓂚'
        elif signs[i] == 'D33':
            signs[i] = '𓂙'
        elif signs[i] == 'D32':
            signs[i] = '𓂘'
        elif signs[i] == 'D31a':
            signs[i] = '𓂗'
        elif signs[i] == 'D31':
            signs[i] = '𓂖'
        elif signs[i] == 'D30':
            signs[i] = '𓂕'
        elif signs[i] == 'D29':
            signs[i] = '𓂔'
        elif signs[i] == 'D28':
            signs[i] = '𓂓'
        elif signs[i] == 'D27a':
            signs[i] = '𓂒'
        elif signs[i] == 'D27':
            signs[i] = '𓂑'
        elif signs[i] == 'D26':
            signs[i] = '𓂐'
        elif signs[i] == 'D25':
            signs[i] = '𓂏'
        elif signs[i] == 'D24':
            signs[i] = '𓂎'
        elif signs[i] == 'D23':
            signs[i] = '𓂍'
        elif signs[i] == 'D22':
            signs[i] = '𓂌'
        elif signs[i] == 'D21':
            signs[i] = '𓂋'
        elif signs[i] == 'D20':
            signs[i] = '𓂊'
        elif signs[i] == 'D19':
            signs[i] = '𓂉'
        elif signs[i] == 'D18':
            signs[i] = '𓂈'
        elif signs[i] == 'D17':
            signs[i] = '𓂇'
        elif signs[i] == 'D16':
            signs[i] = '𓂆'
        elif signs[i] == 'D15':
            signs[i] = '𓂅'
        elif signs[i] == 'D14':
            signs[i] = '𓂄'
        elif signs[i] == 'D13':
            signs[i] = '𓂃'
        elif signs[i] == 'D12':
            signs[i] = '𓂂'
        elif signs[i] == 'D11':
            signs[i] = '𓂁'
        elif signs[i] == 'D10':
            signs[i] = '𓂀'
        elif signs[i] == 'D9':
            signs[i] = '𓁿'
        elif signs[i] == 'D8a':
            signs[i] = '𓁾'
        elif signs[i] == 'D8':
            signs[i] = '𓁽'
        elif signs[i] == 'D7':
            signs[i] = '𓁼'
        elif signs[i] == 'D6':
            signs[i] = '𓁻'
        elif signs[i] == 'D5':
            signs[i] = '𓁺'
        elif signs[i] == 'D4':
            signs[i] = '𓁹'
        elif signs[i] == 'D3':
            signs[i] = '𓁸'
        elif signs[i] == 'D2':
            signs[i] = '𓁷'
        elif signs[i] == 'D1':
            signs[i] = '𓁶'
        elif signs[i] == 'C24':
            signs[i] = '𓁵'
        elif signs[i] == 'C23':
            signs[i] = '𓁴'
        elif signs[i] == 'C22':
            signs[i] = '𓁳'
        elif signs[i] == 'C21':
            signs[i] = '𓁲'
        elif signs[i] == 'C20':
            signs[i] = '𓁱'
        elif signs[i] == 'C19':
            signs[i] = '𓁰'
        elif signs[i] == 'C18':
            signs[i] = '𓁯'
        elif signs[i] == 'C17':
            signs[i] = '𓁮'
        elif signs[i] == 'C16':
            signs[i] = '𓁭'
        elif signs[i] == 'C15':
            signs[i] = '𓁬'
        elif signs[i] == 'C14':
            signs[i] = '𓁫'
        elif signs[i] == 'C13':
            signs[i] = '𓁪'
        elif signs[i] == 'C12':
            signs[i] = '𓁩'
        elif signs[i] == 'C11':
            signs[i] = '𓁨'
        elif signs[i] == 'C10a':
            signs[i] = '𓁧'
        elif signs[i] == 'C10':
            signs[i] = '𓁦'
        elif signs[i] == 'C9':
            signs[i] = '𓁥'
        elif signs[i] == 'C8':
            signs[i] = '𓁤'
        elif signs[i] == 'C7':
            signs[i] = '𓁣'
        elif signs[i] == 'C6':
            signs[i] = '𓁢'
        elif signs[i] == 'C5':
            signs[i] = '𓁡'
        elif signs[i] == 'C4':
            signs[i] = '𓁠'
        elif signs[i] == 'C3':
            signs[i] = '𓁟'
        elif signs[i] == 'C2c':
            signs[i] = '𓁞'
        elif signs[i] == 'C2b':
            signs[i] = '𓁝'
        elif signs[i] == 'C2a':
            signs[i] = '𓁜'
        elif signs[i] == 'C2':
            signs[i] = '𓁛'
        elif signs[i] == 'C1':
            signs[i] = '𓁚'
        elif signs[i] == 'B9':
            signs[i] = '𓁙'
        elif signs[i] == 'B8':
            signs[i] = '𓁘'
        elif signs[i] == 'B7':
            signs[i] = '𓁗'
        elif signs[i] == 'B6':
            signs[i] = '𓁖'
        elif signs[i] == 'B5a':
            signs[i] = '𓁕'
        elif signs[i] == 'B5':
            signs[i] = '𓁔'
        elif signs[i] == 'B4':
            signs[i] = '𓁓'
        elif signs[i] == 'B3':
            signs[i] = '𓁒'
        elif signs[i] == 'B2':
            signs[i] = '𓁑'
        elif signs[i] == 'B1':
            signs[i] = '𓁐'
        elif signs[i] == 'Aa32':
            signs[i] = '𓐮'
        elif signs[i] == 'Aa31':
            signs[i] = '𓐭'
        elif signs[i] == 'Aa30':
            signs[i] = '𓐬'
        elif signs[i] == 'Aa29':
            signs[i] = '𓐫'
        elif signs[i] == 'Aa28':
            signs[i] = '𓐪'
        elif signs[i] == 'Aa27':
            signs[i] = '𓐩'
        elif signs[i] == 'Aa26':
            signs[i] = '𓐨'
        elif signs[i] == 'Aa25':
            signs[i] = '𓐧'
        elif signs[i] == 'Aa24':
            signs[i] = '𓐦'
        elif signs[i] == 'Aa23':
            signs[i] = '𓐥'
        elif signs[i] == 'Aa22':
            signs[i] = '𓐤'
        elif signs[i] == 'Aa21':
            signs[i] = '𓐣'
        elif signs[i] == 'Aa20':
            signs[i] = '𓐢'
        elif signs[i] == 'Aa19':
            signs[i] = '𓐡'
        elif signs[i] == 'Aa18':
            signs[i] = '𓐠'
        elif signs[i] == 'Aa17':
            signs[i] = '𓐟'
        elif signs[i] == 'Aa16':
            signs[i] = '𓐞'
        elif signs[i] == 'Aa15':
            signs[i] = '𓐝'
        elif signs[i] == 'Aa14':
            signs[i] = '𓐜'
        elif signs[i] == 'Aa13':
            signs[i] = '𓐛'
        elif signs[i] == 'Aa12':
            signs[i] = '𓐚'
        elif signs[i] == 'Aa11':
            signs[i] = '𓐙'
        elif signs[i] == 'Aa10':
            signs[i] = '𓐘'
        elif signs[i] == 'Aa9':
            signs[i] = '𓐗'
        elif signs[i] == 'Aa8':
            signs[i] = '𓐖'
        elif signs[i] == 'Aa7b':
            signs[i] = '𓐕'
        elif signs[i] == 'Aa7a':
            signs[i] = '𓐔'
        elif signs[i] == 'Aa7':
            signs[i] = '𓐓'
        elif signs[i] == 'Aa6':
            signs[i] = '𓐒'
        elif signs[i] == 'Aa5':
            signs[i] = '𓐑'
        elif signs[i] == 'Aa4':
            signs[i] = '𓐐'
        elif signs[i] == 'Aa3':
            signs[i] = '𓐏'
        elif signs[i] == 'Aa2':
            signs[i] = '𓐎'
        elif signs[i] == 'Aa1':
            signs[i] = '𓐍'
        elif signs[i] == 'A70':
            signs[i] = '𓁏'
        elif signs[i] == 'A69':
            signs[i] = '𓁎'
        elif signs[i] == 'A68':
            signs[i] = '𓁍'
        elif signs[i] == 'A67':
            signs[i] = '𓁌'
        elif signs[i] == 'A66':
            signs[i] = '𓁋'
        elif signs[i] == 'A65':
            signs[i] = '𓁊'
        elif signs[i] == 'A64':
            signs[i] = '𓁉'
        elif signs[i] == 'A63':
            signs[i] = '𓁈'
        elif signs[i] == 'A62':
            signs[i] = '𓁇'
        elif signs[i] == 'A61':
            signs[i] = '𓁆'
        elif signs[i] == 'A60':
            signs[i] = '𓁅'
        elif signs[i] == 'A59':
            signs[i] = '𓁄'
        elif signs[i] == 'A58':
            signs[i] = '𓁃'
        elif signs[i] == 'A57':
            signs[i] = '𓁂'
        elif signs[i] == 'A56':
            signs[i] = '𓁁'
        elif signs[i] == 'A55':
            signs[i] = '𓁀'
        elif signs[i] == 'A54':
            signs[i] = '𓀿'
        elif signs[i] == 'A53':
            signs[i] = '𓀾'
        elif signs[i] == 'A52':
            signs[i] = '𓀽'
        elif signs[i] == 'A51':
            signs[i] = '𓀼'
        elif signs[i] == 'A50':
            signs[i] = '𓀻'
        elif signs[i] == 'A49':
            signs[i] = '𓀺'
        elif signs[i] == 'A48':
            signs[i] = '𓀹'
        elif signs[i] == 'A47':
            signs[i] = '𓀸'
        elif signs[i] == 'A46':
            signs[i] = '𓀷'
        elif signs[i] == 'A45a':
            signs[i] = '𓀶'
        elif signs[i] == 'A45':
            signs[i] = '𓀵'
        elif signs[i] == 'A44':
            signs[i] = '𓀴'
        elif signs[i] == 'A43a':
            signs[i] = '𓀳'
        elif signs[i] == 'A43':
            signs[i] = '𓀲'
        elif signs[i] == 'A42a':
            signs[i] = '𓀱'
        elif signs[i] == 'A42':
            signs[i] = '𓀰'
        elif signs[i] == 'A41':
            signs[i] = '𓀯'
        elif signs[i] == 'A4a':
            signs[i] = '𓀮'
        elif signs[i] == 'A40':
            signs[i] = '𓀭'
        elif signs[i] == 'A39':
            signs[i] = '𓀬'
        elif signs[i] == 'A38':
            signs[i] = '𓀫'
        elif signs[i] == 'A37':
            signs[i] = '𓀪'
        elif signs[i] == 'A36':
            signs[i] = '𓀩'
        elif signs[i] == 'A35':
            signs[i] = '𓀨'
        elif signs[i] == 'A34':
            signs[i] = '𓀧'
        elif signs[i] == 'A33':
            signs[i] = '𓀦'
        elif signs[i] == 'A32a':
            signs[i] = '𓀥'
        elif signs[i] == 'A32':
            signs[i] = '𓀤'
        elif signs[i] == 'A31':
            signs[i] = '𓀣'
        elif signs[i] == 'A30':
            signs[i] = '𓀢'
        elif signs[i] == 'A29':
            signs[i] = '𓀡'
        elif signs[i] == 'A28':
            signs[i] = '𓀠'
        elif signs[i] == 'A27':
            signs[i] = '𓀟'
        elif signs[i] == 'A26':
            signs[i] = '𓀞'
        elif signs[i] == 'A25':
            signs[i] = '𓀝'
        elif signs[i] == 'A24':
            signs[i] = '𓀜'
        elif signs[i] == 'A23':
            signs[i] = '𓀛'
        elif signs[i] == 'A22':
            signs[i] = '𓀚'
        elif signs[i] == 'A21':
            signs[i] = '𓀙'
        elif signs[i] == 'A20':
            signs[i] = '𓀘'
        elif signs[i] == 'A19':
            signs[i] = '𓀗'
        elif signs[i] == 'A18':
            signs[i] = '𓀖'
        elif signs[i] == 'A17a':
            signs[i] = '𓀕'
        elif signs[i] == 'A17':
            signs[i] = '𓀔'
        elif signs[i] == 'A16':
            signs[i] = '𓀓'
        elif signs[i] == 'A15':
            signs[i] = '𓀒'
        elif signs[i] == 'A14a':
            signs[i] = '𓀑'
        elif signs[i] == 'A14':
            signs[i] = '𓀐'
        elif signs[i] == 'A13':
            signs[i] = '𓀏'
        elif signs[i] == 'A12':
            signs[i] = '𓀎'
        elif signs[i] == 'A11':
            signs[i] = '𓀍'
        elif signs[i] == 'A10':
            signs[i] = '𓀌'
        elif signs[i] == 'A9':
            signs[i] = '𓀋'
        elif signs[i] == 'A8':
            signs[i] = '𓀊'
        elif signs[i] == 'A7':
            signs[i] = '𓀉'
        elif signs[i] == 'A6b':
            signs[i] = '𓀈'
        elif signs[i] == 'A6a':
            signs[i] = '𓀇'
        elif signs[i] == 'A6':
            signs[i] = '𓀆'
        elif signs[i] == 'A5a':
            signs[i] = '𓀅'
        elif signs[i] == 'A5':
            signs[i] = '𓀄'
        elif signs[i] == 'A4':
            signs[i] = '𓀃'
        elif signs[i] == 'A3':
            signs[i] = '𓀂'
        elif signs[i] == 'A2':
            signs[i] = '𓀁'
        elif signs[i] == 'A1':
            signs[i] = '𓀀'
        else:
            if not signs[i] == "-" and not signs[i] == ":" and not signs[i] == "*" and not signs[i] == "(" and not signs[i] == ")":
                signs[i] = "[" + signs[i] + "]"


    
    return signs