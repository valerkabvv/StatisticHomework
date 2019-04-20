from scipy.stats import norm
from numpy import histogram,sort,linspace,unique,where
import matplotlib.pyplot as plt

#ввод параметров распределения и размер выборки
#mean,dispersion, size, numbins = [float(a) for a in input().split(' ')]

mean,dispersion, size, numbins = [-4, 0.5, 200, 15]
norm_distr = norm(mean,dispersion)
sample = norm_distr.rvs(int(size))
sample = sort(sample)

_,ax=plt.subplots()
x = linspace(norm_distr.ppf(0.01),norm_distr.ppf(0.99),100)
uniq,count = unique(sample,return_counts=True)
ax.hist(sample, bins=int(numbins),density=True, color='#539caf',alpha=0.75, label='histogram of frequency')
ax.plot(x,norm_distr.pdf(x),'r-', lw=5, alpha=0.6, label='norm pdf' )
ax.plot(uniq,count*(1/200))
ax.set_ylabel('frequency')
ax.set_xlabel('value')
ax.set_title('comparison')
_.show()

_,ax=plt.subplots()
sample_list = list(sample)
y = [(sample_list.index(i)+1)/200 for i in uniq]
ax.hlines(y[1:],uniq[:uniq.size-1],uniq[1:])
ax.plot(x,norm_distr.cdf(x),'r-', lw=5, alpha=0.6, label='norm cdf' )
ax.set_ylabel('propabilitygit push')
ax.set_xlabel('value')
_.show()
