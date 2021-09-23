# Phylogenetic trees subtrees are within the normal brackets "(" and ")"
# Pull substrings/subtrees out of the string

# Guide 
# 1st Identify taxlabel/species (eg Felis silvestris) index in the string (eg 17)
# 2nd n = 0, assgin "(" to +1 and ")" to -1
# 3rd From each taxlabel/species search the index label for when the sum of n = -1 (eg. openbracket(+1), closedbracket(-1), closedbracket(-1))
# 4th Return the substring from the start of the taxlabel/species to the first closed squared bracket "]" after the sum of normal brackets n=-1

import re   # import regular expression to identify characters in string that matches it


# Data set phylogenetic tree string

# Find the index at which the taxlabel/species 

data = "[&R] [&R=true]((('Felis silvestris'[&length_range={0.1942546268646502,0.8249044947224048},rate_range={0.48713071263378177,2.254020365174967},height_median=8.881784197001252E-16,height=7.987699981389713E-16,rate_95%_HPD={0.5749728452561609,1.6050867815047987},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.5455417729722768,height_range={0.0,5.329070518200751E-15},rate_median=0.777077845937059,length_median=0.5730455317442351,length_95%_HPD={0.23141104109206645,0.6853836574407342},rate=0.86368313598804]:0.5455417729722768,('Lynx canadensis'[&length_range={0.12416487760390357,0.6529903723630749},rate_range={0.5846284683483233,3.371219138161746},height_median=8.881784197001252E-16,height=7.951732352154781E-16,rate_95%_HPD={0.7193463546643171,2.137409196335331},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.4288757786404431,height_range={0.0,5.329070518200751E-15},rate_median=0.9519225207058954,length_median=0.4507006930297067,length_95%_HPD={0.17998710718452576,0.5601477374580388},rate=1.0799308161855512]:0.42887577864044313,('Acinonyx jubatus'[&length_range={0.07494436962673542,0.5341230164937385},rate_range={0.7983317639133981,5.4159844533833095},height_median=8.881784197001252E-16,height=7.981483354114539E-16,rate_95%_HPD={0.8315084298655286,3.5748984382034936},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.32686653867816057,height_range={0.0,5.329070518200751E-15},rate_median=1.205835707275285,length_median=0.34524797927544526,length_95%_HPD={0.09447812698815154,0.44357523744728955},rate=1.477508785345113]:0.3268665386781608,'Puma concolor'[&length_range={0.07494436962673542,0.5341230164937385},rate_range={0.581994691432055,4.544308664405514},height_median=8.881784197001252E-16,height=7.981483354114539E-16,rate_95%_HPD={0.673451450997393,2.919800070246849},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.32686653867816057,height_range={0.0,5.329070518200751E-15},rate_median=0.9889815465826269,length_median=0.34524797927544526,length_95%_HPD={0.09447812698815154,0.44357523744728955},rate=1.2066197565100574]:0.3268665386781608)[&rate_range={0.3660011159035478,6.556720996036486},height_median=0.34524797927544615,length=0.1020092399622809,length_median=0.09983994968725368,length_95%_HPD={0.04407004534636699,0.16899714027654417},length_range={0.0072492797152948485,0.23181818155672423},height=0.32686653867816157,rate_95%_HPD={0.5230274576369115,1.6410234141724875},height_95%_HPD={0.09447812698815383,0.44357523744729077},height_range={0.07494436962673845,0.534123016493739},rate_median=0.9612252154468139,posterior=1.0,rate=1.0475356571912782]:0.10200923996228234)[&rate_range={0.4373858130022312,7.760242300323579},height_median=0.4507006930297077,length=0.11666599433183426,length_median=0.11450192277700416,length_95%_HPD={0.039059677377391966,0.19518617155539053},length_range={0.01328661146700208,0.3281629344234659},height=0.4288757786404439,rate_95%_HPD={0.5228137238199303,1.7764401007889248},height_95%_HPD={0.17998710718452848,0.5601477374580401},height_range={0.12416487760390815,0.6529903723630772},rate_median=0.9677641940853318,posterior=1.0,rate=1.0753676526225928]:0.11666599433183367)[&rate_range={0.4017398161219104,2.394452748108598},height_median=0.5730455317442367,length=0.17421812181062732,length_median=0.17157767039681987,length_95%_HPD={0.07080879180125058,0.2652916072624548},length_range={0.04428395677413219,0.4296830563270294},height=0.5455417729722776,rate_95%_HPD={0.4848563603988733,1.409522621996914},height_95%_HPD={0.23141104109206623,0.685383657440735},height_range={0.19425462686465167,0.8249044947224053},rate_median=0.8785855406961453,posterior=1.0,rate=0.9216538071750086]:0.17421812181062735,('Neofelis nebulosa'[&length_range={0.11560351155046529,0.7623080939874496},rate_range={0.6675829558306837,4.811232415894687},height_median=8.881784197001252E-16,height=8.020781319389742E-16,rate_95%_HPD={0.7121564493925345,2.7593682311154355},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.5019820498059957,height_range={0.0,7.105427357601002E-15},rate_median=1.0030970324566633,length_median=0.5277239422052145,length_95%_HPD={0.16667385839883533,0.6512791360582133},rate=1.1766104840868747]:0.5019820498059958,(('Panthera pardus'[&length_range={0.051762869859318994,0.4526257508074602},rate_range={0.49368739668785994,4.349498522520932},height_median=8.881784197001252E-16,height=7.878242936866124E-16,rate_95%_HPD={0.5875710311640657,2.388298574734536},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.2563323902942868,height_range={0.0,7.105427357601002E-15},rate_median=0.8882343696143651,length_median=0.26838332331163006,length_95%_HPD={0.08328714329516121,0.36665252761390743},rate=1.0514917777211554]:0.2563323902942867,'Uncia uncia'[&length_range={0.051762869859318994,0.4526257508074602},rate_range={0.7683197861329419,6.266173588236551},height_median=8.881784197001252E-16,height=7.878242936866124E-16,rate_95%_HPD={0.8199145379531707,3.5653026846309572},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.2563323902942868,height_range={0.0,7.105427357601002E-15},rate_median=1.2911019985361756,length_median=0.26838332331163006,length_95%_HPD={0.08328714329516121,0.36665252761390743},rate=1.5535682374566369]:0.2563323902942867)[&rate_range={0.46803883350258807,9.834507345740448},height_median=0.26838332331162995,length=0.10867247005991089,length_median=0.11061971608133951,length_95%_HPD={0.02731436483867397,0.17664826942854434},length_range={0.010944803172169004,0.24884919628325008},height=0.2563323902942875,rate_95%_HPD={0.5358805962458113,2.9939470791927274},height_95%_HPD={0.08328714329516185,0.3666525276139092},height_range={0.05176286985931888,0.45262575080746004},rate_median=1.0187285446096805,posterior=1.0,rate=1.2669921159813096]:0.10867247005991426,'Panthera tigris'[&length_range={0.08532591429406478,0.6087081028431981},rate_range={0.64104478547289,4.469496764501257},height_median=8.881784197001252E-16,height=7.974600659631312E-16,rate_95%_HPD={0.6601763098775789,2.9221020637601365},height_95%_HPD={0.0,1.7763568394002505E-15},length=0.36500486035420143,height_range={0.0,7.105427357601002E-15},rate_median=1.0331395368585283,length_median=0.384001768113435,length_95%_HPD={0.10036919430360339,0.4748998604435545},rate=1.2281864034497612]:0.365004860354201)[&rate_range={0.48509464599677854,18.082500681767065},height_median=0.3840017681134351,length=0.13697718945179724,length_median=0.13580473342718635,length_95%_HPD={0.039214318232917905,0.22065840296567502},length_range={0.0047778118156244775,0.3420132324781422},height=0.36500486035420177,rate_95%_HPD={0.49633916193835914,2.399993491859389},height_95%_HPD={0.10036919430360669,0.47489986044355526},height_range={0.08532591429406544,0.6087081028431984},rate_median=1.0278344388441993,posterior=1.0,rate=1.2363914765102544]:0.13697718945179482)[&rate_range={0.4916092720185956,3.938447196579812},height_median=0.5277239422052147,length=0.21777784497690808,length_median=0.21354683963694326,length_95%_HPD={0.11443310780200067,0.330905592113783},length_range={0.05212511948934845,0.4229082767907564},height=0.5019820498059966,rate_95%_HPD={0.642773019217055,1.6583625334999348},height_95%_HPD={0.1666738583988363,0.6512791360582142},height_range={0.11560351155046611,0.7623080939874498},rate_median=1.049440752521783,posterior=1.0,rate=1.112291954452042]:0.21777784497690833)[&rate_range={0.43851340290440743,8.387473475919357},height_median=0.7506512526826756,length=1.1628791402926324,length_median=1.2493832283251654,length_95%_HPD={0.1272704705854425,1.6596804431116017},length_range={0.08403367503938441,2.216702592836695},height=0.7197598947829049,rate_95%_HPD={0.44757538069278713,4.265733627944012},height_95%_HPD={0.3708492724650281,0.9301593356195479},height_range={0.28422983976841376,1.0131966206050502},rate_median=0.7184911912125955,posterior=1.0,rate=1.0935773283947143]:1.162879140292626,'Herpestes auropunctatus'[&length_range={0.4077442841383848,3.077593604887982},rate_range={0.5486788213718423,4.598892955320532},height_median=8.881784197001252E-16,height=8.040097268423317E-16,rate_95%_HPD={0.6360581306112283,2.88417107587848},height_95%_HPD={0.0,1.7763568394002505E-15},length=1.8826390350755302,height_range={0.0,5.329070518200751E-15},rate_median=0.8991040578710322,length_median=2.021171780673231,length_95%_HPD={0.4807096379270705,2.443946052786261},rate=1.1191694071404383]:1.88263903507553)[&rate_range={0.41309931846777115,18.082500681767065},height_median=2.021171780673232,length=1.0629176463189733,length_median=1.1321548896603348,length_95%_HPD={0.0377505419998857,1.4932788016680352},length_range={0.03364454999348404,1.9387773558192827},height=1.8826390350755309,rate_95%_HPD={0.42732676388065827,5.632839247671333},height_95%_HPD={0.4807096379270712,2.443946052786262},height_range={0.4077442841383858,3.077593604887983},rate_median=0.6630484354562965,!hilight={9,8.881784197001252E-16,#-198545},posterior=1.0,rate=1.2661885937834805]:1.095513840672626;"

x= data.find("'Felis silvestris'")
print(x)

# Function identify position index the first "]" after n=-1
def test(x):
    
    n = 0
    if (chr == '\('):
        n = n + 1
    elif (chr == "\)"):
        n = n - 1
    
    for n in range(0, -2):  # range between 0 and -2 so that it gets the first squared bracket "]" after the sum condition (n=-1) 
        mdata = "]"
        pos = x.rfind(mdata, 17)    # search starting at the beginning of the taxlabel/species index (eg Felis silvestris index = 17)
        print(pos)


test(data)



data[17-1:200+20]


### Find index
pattern = ",\(\'"

match = (re.search(pattern, data))
print(match)


### Species information metadata
### OSCAR first and second position
firstPosition = data.find(",('")
firstPosition = firstPosition + 3
secondPosition = data.find(",('", firstPosition)

print(firstPosition)
print(secondPosition)

datatest = print(data[firstPosition:secondPosition])

### Find the index of all the brackets


massive_data="C:/Users/Rocky/OneDrive/Desktop/Project/DataSet/HA_continuous_MCC.tre"


y= data.find("'Felis silvestris'")
x = y - 1

lstob=[]        #list of open bracket index
for i in range(x, len(data)):
    if (data[i] == "("):
        lstob.append(i)
print(lstob)

lstcb=[]        #list of closed bracket index
for i in range(x, len(data)):
    if (data[i] == ")"):
        lstcb.append(i)
print(lstcb)

a = data.find("]", 3158, len(data))     # first instance of squared bracket within range

b = data.find("," or ";", a, len(data))  # first instance of comma within range

data[x:b+1]

# Matching parenthesis script
def check_parentheses(s):
    """ Return True if the parentheses in string s match, otherwise False. """
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0

check_parentheses(massive_data)

def find_parentheses(s):
    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs

sp_lst= find_parentheses(small_data)
print(sp_lst)



data[1048:2081]