import matplotlib.pyplot as plt

acc = [
    0.328148742863, 0.3767310318, 0.39309900618, 0.404520527447, 0.413696753627, 0.422169907609,
    0.427649334804, 0.434367076269, 0.438891686065, 0.442894661647, 0.449433233101, 0.454955751817,
    0.459469021737, 0.46432248789, 0.467763005708, 0.47111053657, 0.474877642764, 0.478111774878,
    0.480404697437, 0.483518626889, 0.485466817273, 0.487859530717, 0.491361283861, 0.492930722458,
    0.494985507648, 0.497682129726, 0.499632588077, 0.50106141223, 0.501642013787, 0.505679008991,
    0.506636094378, 0.509564049883, 0.510094755995, 0.513040855305, 0.514174842728, 0.515624078648,
    0.516293131218, 0.519223354704, 0.517819478287, 0.519869727531, 0.522276048832, 0.522843042544,
    0.524938651282, 0.525122357248, 0.525902540597, 0.527843927056, 0.528937090931, 0.529919124029,
    0.531413719433, 0.530656215845, 0.534128485316, 0.532779040289, 0.535001655639, 0.534402910272,
    0.536314813056, 0.536260381661, 0.539029578933, 0.538222179893, 0.539864193672, 0.540689736518,
    0.541601462401, 0.541703521263, 0.543994175853, 0.54374016267, 0.544792502993, 0.545704228872,
    0.545967313958, 0.546579667168, 0.547777157871, 0.548661668061, 0.549115263029, 0.550410276659,
    0.550482851854, 0.551913943968, 0.553308748497, 0.551315198607, 0.552401558557, 0.553968729175,
    0.554560670606, 0.554982513925, 0.555397553319, 0.556032586274, 0.556270723631, 0.556030318294,
    0.557409246992, 0.557939953109, 0.557611096754, 0.559185071287, 0.559788352593, 0.55889930646,
    0.561185425098, 0.56067286278, 0.559940306914, 0.562178798069, 0.560509568597, 0.56307238016,
    0.562274053012, 0.563163099149, 0.563160831178, 0.564120184534, 0.564396877457, 0.56540385829,
    0.56555354463, 0.565106753587, 0.565877865025, 0.56617950569, 0.567442767661, 0.56706855182,
    0.567689976911, 0.567147930938]
val_acc = [
    0.359062693493, 0.389189646877, 0.403663073448, 0.412505887272, 0.423999957665, 0.430752459425,
    0.41975053846, 0.440934131356, 0.441786131976, 0.448025316595, 0.453317245875, 0.455629818969,
    0.460413723038, 0.46115988506, 0.469251244927, 0.470637730398, 0.46989156837, 0.465917329487,
    0.469928611881, 0.475897908107, 0.476511771903, 0.471024041241, 0.472061259379, 0.479374705643,
    0.47558568428, 0.476405933317, 0.482391105332, 0.481025787577, 0.482195303948, 0.478422158373,
    0.485899654443, 0.486301841068, 0.48614308319, 0.487503109015, 0.488910762203, 0.486793990492,
    0.487159133606, 0.486084871967, 0.487656574964, 0.490096154361, 0.491884826452, 0.480337836766,
    0.490958738833, 0.492630988485, 0.492641572344, 0.492519857965, 0.488921346061, 0.491995956972,
    0.495155238751, 0.493969846587, 0.493811088715, 0.491958913467, 0.495271661196, 0.493017299323,
    0.49504940016, 0.494313821996, 0.498378023682, 0.494292654279, 0.482406981119, 0.498065799855,
    0.496896283484, 0.495081151742, 0.494197399546, 0.4948747665, 0.497383140972, 0.49575322676,
    0.49135563353, 0.494589002319, 0.498256309309, 0.497970545128, 0.493737001705, 0.497107960655,
    0.499499912689, 0.497356681332, 0.492498690253, 0.496070742517, 0.497584234291, 0.499563415841,
    0.500500087323, 0.499738049507, 0.500934025524, 0.496700482095, 0.493842840291, 0.499658670568,
    0.500314869798, 0.502193504686, 0.498642620146, 0.50243164151, 0.499769801082, 0.501399715301,
    0.499854471951, 0.500214323141, 0.502516312378, 0.501463218452, 0.501616684401, 0.50198711945,
    0.503135468104, 0.500357205232, 0.500748808, 0.497531314997, 0.501426174948, 0.500346621374,
    0.501161578483, 0.502018871026, 0.50301375373, 0.500230198929, 0.502151169258, 0.503664661032,
    0.504331444121, 0.500648261342]

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
