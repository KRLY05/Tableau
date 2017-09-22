SCRIPT_REAL('
import scipy.interpolate as interpolate

X_all=_arg1 #assigning date dimension to x axis
y_all=_arg2 #assigning our KPI measure to y axis

y=[i for i in y_all if i is not None] #getting rid from Nones for y
X=[i[0] for i in enumerate(X_all) if i[1] is not None] #getting list of indexes for X without Nones

Xsmooth=list(range(0,len(X_all))) #generation full list of indexes for X
ysmooth=interpolate.pchip_interpolate(X,y,Xsmooth) #interpolation (depending on source data, other function can be used, like spline)

result=[round(i,10) for i in ysmooth] #rounding to fit in output JSON
return result
',attr([Date]),ATTR([Value1]))