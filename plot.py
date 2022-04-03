
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import streamlit as st
dicp ={'inter': 6.03,
 'Vc': -0.121,
 'Ap': 26.86,
 'feed': 0.332,
 'Vcfeed': -2.133333333535634e-05,
 'VcAp': -0.04,
 'Apfeed': 0.06,
 'VcVc': 1.7579304830668278e-04,
 'feedfeed': -0.0014212908471364984,
 'ApAp': -3.01}


X,Y = np.meshgrid( np.linspace( 200, 500, 50), np.linspace( 40, 200, 50) )


Ap = st.slider('Ap',0.0,2.0,1.15,0.1)
Z=dicp["inter"]+dicp["Vc"]*X+dicp["Ap"]*Ap+dicp["feed"]*Y+dicp["Vcfeed"]*X*Y+dicp["VcAp"]*X*Ap+dicp["Apfeed"]*Y*Ap+dicp["VcVc"]*X*X+dicp["feedfeed"]*Y*Y+dicp["ApAp"]*Ap*Ap

fig, ax = plt.subplot(111, projection='3d')
ax.view_init(15, 40)
#surf = ax.plot_surface( X, Y, Zm,cmap=cm.coolwarm,
#linewidth=0, antialiased=False)
# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
N = Z/50  # normalize 0..1
surf = ax.plot_surface( X,  Y ,  Z, rstride=1, cstride=1, facecolors=cm.jet(N), linewidth=0, antialiased=False, shade=False)



# Customize the z axis.
ax.set_zlim(0, 50)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('Vc (m/min)')
ax.set_ylabel('feed (mm/min)')
ax.set_zlabel('Resultante (N)')

cNorm = cm.colors.Normalize(vmin=0, vmax=50)

m = cm.ScalarMappable(norm=cNorm,cmap=cm.jet)

m.set_array(Z)
# Add a color bar which maps values to colors.
plt.colorbar(m, shrink=0.5, aspect=5,label="Résultant (N)")



# Or even better, call Streamlit functions inside a "with" block:

st.pyplot(fig)



#plt.show()