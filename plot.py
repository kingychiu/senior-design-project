import matplotlib.pyplot as plt

acc = [0.513904953715,0.615317448442,0.638004000718,0.649892724794,0.657714970006,0.661851756109,0.667632823956,0.671672087136,0.673815323361,0.676505141514,0.67846013581,0.68010214959,0.681716947685,0.683597098816,0.685327563621,0.68629145292,0.687187302973,0.687747492775,0.689416722236,0.690112990511,0.69286177601,0.691902422655,0.693242795776,0.693485469101,0.693235991858,0.693902776465,0.696002921168,0.69605508459,0.696116319904,0.695644581143,0.697084745157,0.696608470443,0.697874000394,0.698064510279,0.698125745612,0.698964896296,0.699679308367,0.699502406343,0.699565909626,0.700375576648,0.700835975528,0.70094257035,0.700974322004,0.701545851651,0.701854296241,0.702051610045,0.701806668757,0.702822721476,0.703133434048,0.70299508757,0.7020017146,0.702629943628,0.703795682699,0.703264976588,0.704274225377,0.704299173106,0.703893205611,0.704131342969,0.704618957559,0.704798127562,0.705288010129,0.705108840116,0.705233578749,0.705344709503,0.705637278258,0.70563047434,0.705208631021,0.705764284843,0.705673565861,0.705780160673,0.705986546389,0.706975383416,0.70614530462,0.706267775268,0.706755389845,0.706705494406,0.706927755934,0.707070638366,0.706109017031,0.706236023614,0.706768997695,0.706617043388,0.707673919649,0.706664670858,0.707574128761,0.708367919958,0.707760102705,0.707800926244,0.708263593123,0.708662756682,0.70773061903,0.70827266501,0.70712506975,0.708653684794,0.708830586826,0.708088959055,0.709095939881,0.707376814958,0.708306684645,0.708445031097,0.70857657365,0.708912233913,0.709309129522,0.708939449617,0.708349776155,0.709195730779,0.708315756533,0.709492835478,0.709379436741,0.708465442876]
val_acc = [0.621997491631,0.653166955082,0.672773553058,0.676329729534,0.678822228224,0.679536638677,0.69418999085,0.692814089237,0.702440108595,0.700101075854,0.701699238496,0.706319092756,0.706737155168,0.704916731497,0.704032979308,0.704477501367,0.709271989294,0.709155566849,0.709017976689,0.708610498134,0.710753729491,0.713807172686,0.710346250937,0.71464858944,0.715024316419,0.713500240787,0.711700984832,0.714696216804,0.715934528255,0.717463895817,0.711748612196,0.711748612196,0.716384342244,0.713071594515,0.7153100806,0.716902951312,0.715828689669,0.715802230023,0.712378351781,0.718358231865,0.719538332093,0.719750009265,0.720231574829,0.716299671375,0.715193658156,0.721025364221,0.719490704731,0.721168246312,0.71795075331,0.716215000507,0.717347473372,0.718606952541,0.722094333935,0.719824096275,0.716601311344,0.720358581132,0.718220641703,0.72205729043,0.720157487819,0.72139050734,0.720247450617,0.72109945123,0.72286695561,0.7230098377,0.719903475213,0.722448893197,0.721506929785,0.718331772218,0.719638878751,0.719797636628,0.718427026945,0.724809093655,0.721861489047,0.72462916806,0.72404176391,0.720099276597,0.723713664294,0.723290309952,0.721517513644,0.721750358532,0.724375155454,0.723057465064,0.721977911491,0.723073340852,0.721999079209,0.722152545157,0.720369164991,0.720617885667,0.724835553302,0.724666211565,0.724105267061,0.726714188196,0.719644170679,0.720628469525,0.723687204648,0.719548915952,0.719892891356,0.723586657991,0.723359105033,0.722824620176,0.724512745615,0.720623177596,0.724226981434,0.725295951149,0.722734657378,0.721787402037,0.721877364835,0.72572988935,0.725692845845,0.726174411408]

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

# plt.annotate(str(val_acc[min_diff_idx]), xy=(min_diff_idx, val_acc[min_diff_idx]),
#              xytext=(min_diff_idx + 2, val_acc[min_diff_idx] - 0.1),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              )
plt.annotate(str(val_acc[max_acc_idx]), xy=(max_acc_idx, val_acc[max_acc_idx]),
             xytext=(max_acc_idx - 50, val_acc[max_acc_idx] - 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.show()
