import matplotlib.pyplot as plt

acc = [
    0.296757703178, 0.333473947776, 0.358954645047, 0.371308303964, 0.378329954059, 0.384358231162,
    0.389370455552, 0.393053646678, 0.397716602943, 0.401438349642, 0.403722200306, 0.407679816385,
    0.412372256335, 0.415279800057, 0.419772658204, 0.423791509616, 0.426447308148, 0.429740407614,
    0.432897428583, 0.435582710781, 0.43805480335, 0.440851216322, 0.443037544062, 0.444638734295,
    0.447636997021, 0.450029710483, 0.452225110118, 0.452814783574, 0.455495529829, 0.457108059931,
    0.459491701482, 0.461691637082, 0.463476533272, 0.46556080215, 0.46700096617, 0.467967123444,
    0.470069536115, 0.470935902496, 0.473036047193, 0.474501158942, 0.47669882655, 0.47885567063,
    0.479341017239, 0.480613351121, 0.482257632882, 0.483260077752, 0.484434888718, 0.485634647409,
    0.487832315025, 0.488177047199, 0.489515152346, 0.490467701776, 0.492214042399, 0.49386059213,
    0.49420532431, 0.495597860858, 0.496246501656, 0.498135724692, 0.498666430804, 0.499575888706,
    0.501043268429, 0.502218079394, 0.50351309303, 0.502646726638, 0.504089158639, 0.505434067705,
    0.506060028759, 0.507418545695, 0.508597892603, 0.5099496056, 0.511092664927, 0.510473507786,
    0.512072430044, 0.511922743717, 0.51352620192, 0.513952581193, 0.515193163429, 0.516526732625,
    0.517422582678, 0.516356634512, 0.519062328489, 0.519134903685, 0.520792793283, 0.520835884812,
    0.520250747303, 0.521922244756, 0.522217081497, 0.5229723171, 0.523246742061, 0.52462567076,
    0.525591828045, 0.526074906674, 0.5264604624, 0.526979828643, 0.528415456702, 0.528401848859,
    0.528753384965, 0.528968842573, 0.529440581344, 0.530715183197]
val_acc = [
    0.320516280621, 0.343922483822, 0.370921907001, 0.380653764951, 0.387353347416, 0.392592357402,
    0.390655511281, 0.401668016115, 0.404488614415, 0.405652838856, 0.41017743839, 0.398815666234,
    0.419279556748, 0.419480650061, 0.422518217467, 0.424735535841, 0.429053750132, 0.424904877572,
    0.418014785651, 0.426598294947, 0.432361205926, 0.434059915229, 0.437229780861, 0.437764265725,
    0.439690527976, 0.435610450502, 0.439716987623, 0.443691226512, 0.437176861575, 0.444617314141,
    0.444638481851, 0.446114930126, 0.446226060635, 0.439944540582, 0.438743272635, 0.445982631889,
    0.448909068785, 0.448046484313, 0.449173665243, 0.449845740268, 0.450898834188, 0.448898484927,
    0.450851206831, 0.450920001906, 0.448289913054, 0.449073118588, 0.442061312293, 0.453179655714,
    0.451639704287, 0.453904650019, 0.451332772395, 0.450935877699, 0.454243333492, 0.454227457711,
    0.453756476, 0.456106092598, 0.456624701674, 0.456624701674, 0.458244032033, 0.45790005663,
    0.458889647399, 0.45591029122, 0.452957394683, 0.459048405283, 0.458688554092, 0.458244032033,
    0.454433842952, 0.457116851096, 0.459043113348, 0.459963909049, 0.455751533343, 0.458619759012,
    0.461138717343, 0.460964083683, 0.461043462621, 0.45994803326, 0.461212804358, 0.459694020654,
    0.458381622194, 0.462186519345, 0.459762815735, 0.461932506739, 0.457339112126, 0.462250022497,
    0.460122666927, 0.458969026344, 0.460265549017, 0.459799859241, 0.461069922268, 0.455725073691,
    0.461916630953, 0.463424830797, 0.465298173762, 0.464837775914, 0.461683786063, 0.462848010506,
    0.464276831411, 0.463504209736, 0.459482343485, 0.465060036944]

plt.ylabel('Acc.')
plt.xlabel('Epochs')

acc_line, = plt.plot(acc, label="Training Acc.", linewidth=2)
val_acc_line, = plt.plot(val_acc, label="Test Acc.", linewidth=2)
first_legend = plt.legend(handles=[acc_line, val_acc_line], loc=4)

# closest point between 2 line
min_diff_idx = 0
max_acc_idx = 0
for i in range(0, len(acc)):
    diff = abs(acc[i] - val_acc[i])
    if abs(acc[i] - val_acc[i]) < abs(acc[min_diff_idx] - val_acc[min_diff_idx]):
        min_diff_idx = i
    if val_acc[i] > val_acc[max_acc_idx]:
        max_acc_idx = i

plt.annotate(str(val_acc[min_diff_idx]), xy=(min_diff_idx, val_acc[min_diff_idx]),
             xytext=(min_diff_idx + 2, val_acc[min_diff_idx] - 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.annotate(str(val_acc[max_acc_idx]), xy=(max_acc_idx, val_acc[max_acc_idx]),
             xytext=(max_acc_idx - 2, val_acc[max_acc_idx] - 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.show()
