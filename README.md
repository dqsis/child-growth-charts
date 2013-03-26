growthcharts.py
===============

What is it
----------
`growthcharts.py` is a python script that allows the (graphical) assessment of a child's development according to the [World Health Organization (WHO) growth standards](http://www.cdc.gov/growthcharts/who_charts.htm).

Main features
-------------

The script, using as input data the child's:
* age
* weight
* length
* head circumference, 
 
 generates a series plots showing:
 * the curve and rate of child's growth, and
 * in which [percentile](http://en.wikipedia.org/wiki/Percentile) of population the child lies.

 An example of the output plots is shown in [this figure](https://github.com/dqsis/child-growth-charts/blob/master/data/growth.png).

Where to get it
---------------

The source code is hosted on GitHub at: [http://github.com/dqsis/child-growth-charts](http://github.com/dqsis/child-growth-charts).

Dependencies
------------

* [NumPy](http://www.numpy.org) - for array objects 
* [matplotlib](http://matplotlib.org) - for plots

Documentation
-------------

The only input required by `growthcharts.py` is the population of the file `child_data.csv` which contains the child's:

* weight
* length
* head circumference

at different ages. 
The structure of the file is as following:

<table>
  <tr>
      <th>age</th><th>weight</th><th>lenght</th><th>head circumference</th>
  </tr>
</table>

An example can be found [here](http://github.com/dqsis/child-growth-charts/data/child_data.csv). 


Background
----------
 
`growthcharts.py` is a rather simple script. 

My primary goal developing `growthcharts.py` -besides following my baby girl's development- was to get acquainted with: 
* python (and in particular NumPy and matplotlib) for data analysis - as an alternative to Matlab, and
* Git 

Without doubt, more simplistic approaches (e.g., spreadsheets) can be used to address this topic. 

Discussion and development
--------------------------

Future features for implementation and development ideas are listed in the [TODO.md](http://github.com/dqsis/child-growth-charts/TODO.md) file.

Licence
-------
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US).
