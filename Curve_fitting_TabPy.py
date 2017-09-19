SCRIPT_REAL('
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.interpolate as interpolate

X=_arg1 #assigning months dimension to x axis
y=_arg2 #assigning our KPI measure to y axis

#getting rid from Nones
X=[i for i in X if i is not None]
y=[i for i in y if i is not None]

xsmooth=list(range(min(X),max(X)+1)) #densification of X axis (can be done as well with numpy.linespace)
ysmooth=interpolate.pchip_interpolate(X,y,xsmooth) #interpolation (depending on source data, other function can be used, like spline)

result=[round(i,10) for i in ysmooth] #rounding to fit in output JSON
return result
',
attr([Month]),[ASK vFP])