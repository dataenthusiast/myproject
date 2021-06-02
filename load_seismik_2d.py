import numpy as np
import segyio
import matplotlib.pyplot as plt
import scipy
filename = 'arbitrary_line.sgy'
with segyio.open(filename, 'r', iline=73, xline=21) as segyfile:
    data = segyio.tools.cube(segyfile)
    ntraces = segyfile.tracecount
    sr = segyio.tools.dt(segyfile)
    nsamples = segyfile.samples.size
    twt = segyfile.samples + 1000
    size_mb= data.nbytes/1024**2
    inlines = segyfile.ilines
    crosslines = segyfile.xlines
    header = segyio.tools.wrap(segyfile.text[0])
print(header)
# slice = data[39,:,:]
# dt = 2
# t = np.arange(0, (len(slice[0, :])))*dt
# x = np.arange(0, (len(slice[:, 0])))*1
# sclip = abs(np.percentile(slice, 0.999))
# plt.imshow(slice.T, vmin=-sclip, vmax=sclip, aspect='auto', cmap='RdBu')
# plt.xlabel('Inline')
# plt.ylabel('TWT')
# plt.savefig('Seismic.png', dpi=1000)
# plt.show()

# arms = []
# for i in range(735):
#     a = np.square(slice[i])
#     mask = np.ones(11)/11
#     RMS_amp = np.sqrt(np.convolve(a, mask, 'same'))
#     arms.append(RMS_amp)
# arms = np.array(arms)
# arms = np.reshape(arms, (735, 1252))
# sclip = abs(np.percentile(slice, 0.999))
# fig = plt.figure(figsize=(20,15))
# ax1 = plt.subplot(121)
# extent = [crosslines[0], crosslines[-1], twt[-1], twt[0]]
# ax1.imshow(slice.T, vmin=-sclip, vmax=sclip, aspect='auto', extent=extent, cmap='RdBu')
# ax1.set_xlabel('Inlines')
# ax1.set_ylabel('TWT [ms]')
# ax1.set_title('Seismic');
# aclip = abs(np.percentile(arms, 0.999))
# ax2 = plt.subplot(122)
# im = ax2.imshow(np.transpose(arms), aspect='auto', extent=extent, cmap='inferno')
# # fig.colorbar(im, ax=ax2, aspect='auto')
# ax2.set_xlabel('Inlines')
# ax2.set_ylabel('TWT [ms]')
# ax2.set_title('RMS Attribute');
# plt.show()
