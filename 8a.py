
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Label
from bokeh.io import output_file

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a Bokeh figure
p = figure(title="Line Graph with Annotations and Legends", x_axis_label='X-axis', y_axis_label='Y-axis')

# Create a data source
source = ColumnDataSource(data={'x': x, 'y': y})

# Create a line plot
p.line('x', 'y', source=source, legend_label='Line Plot', line_color='blue',line_width=2)

# Create annotations
label = Label(x=3, y=6, x_units='data', y_units='data', text='Annotation')
p.add_layout(label)

p.legend.title = 'Legend'

# Output the plot to an HTML file
output_file('line_graph_with_annotations_and_legend.html')

# Show the plot
show(p)

'''
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.io import output_file

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a Bokeh figure
p = figure(title="Line Graph with Annotations and Legends", x_axis_label='X-axis', y_axis_label='Y-axis')

# Create a data source
source = ColumnDataSource(data={'x': x, 'y': y})

# Create a line plot
p.line('x', 'y', source=source, legend_label='Line Plot', line_color='blue',line_width=2)

# Create annotations
label = Label(x=3, y=6, x_units='data', y_units='data', text='Annotation',background_fill_color='lightgray', background_fill_alpha=0.7)
p.add_layout(label)

# Create legends
p.legend.title = 'Legend'
p.legend.label_text_font_size = '12pt'
p.legend.background_fill_alpha = 0.7

# Create a label set
labels = LabelSet(x='x', y='y', text='y', level='glyph', source=source,text_baseline='middle',text_align='center', text_font_size='12pt')
p.add_layout(labels)

# Output the plot to an HTML file
output_file('line_graph_with_annotations_and_legends.html')

# Show the plot
show(p)
'''