# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.layouts import row, column
from bokeh.models.widgets import Select
import glob
source = ColumnDataSource()

path = glob.glob('../csv/*.csv')
np.seterr(divide='ignore', invalid='ignore')
output_file('Outliers.html')
#loop and get infared outliers
for j in range(len(path)):
    df = pd.read_csv(path[j])
    path[j] = path[j].replace('../csv/', '')
    path[j] = path[j].replace('.csv', '')
    band_matrix = df.iloc[:, 2:8].as_matrix()
    
    outlier_thresh = 10
    infared = (band_matrix[:,3]+band_matrix[:,4]+band_matrix[:,5])
    infared[np.where(infared < outlier_thresh)] = 0
    infared = infared.reshape(651,651)
    
    source.add([infared],name = 'infared_' + path[j])
source.add([infared],name = 'infared')    
#plot parametes
plot_width = 600
plot_height = 600
dw = 10
dh = 10
N = 651

select = Select(title='Select Year/Date', options=path, value=path[0])
callback = CustomJS(args=dict(source=source), code="""
                    var data = source.data;
                    var s = cb_obj.value
                    x=data['infared_'+s]
                    data['infared'] = x
                    source.change.emit()
""")

select .js_on_change('value',callback)
p = figure(title='Infared outliers',
           plot_width=plot_width, plot_height=plot_height, x_range=(0, dw),
           y_range=(0, dh))

pg = p.image(image='infared', x=0, y=0, dw=dw, dh=dh, source=source,
             palette='Spectral11')
show(row(p,select))


    