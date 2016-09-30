# name: Genevieve Laymon
# email: gml36@pitt.edu
# date: 9-30-2016
# class: CS0008-f2016
# instructor: Max Novelli (man8@pitt.edu)
# description: Assignment 1
# notes: I had the most trouble with the formatting of the output and had to correct it several times before it worked.

system = raw_input('Do you want to use USC or Metric?')
# here I am asking if the client wants Metric or USC
if system != 'USC' and system != 'Metric':
    input('System not recognized! Press enter to exit.')
    exit()
distance = float(raw_input('What was the distance driven?'))
# here I am asking for the distance the client drove
amount = float(raw_input('How much gasoline was used?'))
# here I am asking for the amount of gas the client used

metric_distance = 0
usc_distance = 0
if system == 'USC':
    usc_distance = distance
    metric_distance = usc_distance*1.60934
else:
    metric_distance = distance
    usc_distance = metric_distance*0.621371
# calculated metric vs usc distance

gallons = 0
liters = 0
if system == 'USC':
    gallons = amount
    liters = gallons*3.78541
else:
    liters = amount
    gallons = liters*0.264172
# calculated gallons and liters
mpg = usc_distance/gallons
# calculated mpg
metric_consumption = (100*liters)/metric_distance
# calculated 1/100KM

rating = ''
if metric_consumption > 20:
    rating = 'Extremely Poor'
elif metric_consumption > 15 and metric_consumption <= 20:
    rating = 'Poor'
elif metric_consumption > 10 and metric_consumption <= 15:
    rating = 'Average'
elif metric_consumption > 8 and metric_consumption <= 10:
    rating = 'Good'
else:
    rating = 'Excellent'
# calculated ratings for fuel consumption

print('                             USC                 Metric')
print('Distance _________________:  %.3f Miles          %.3f Km' % (usc_distance, metric_distance))
print('Gas_______________________:  %.3f Gallons        %.3f Liters' % (gallons, liters))
print('Consumption_______________:  %.3f mpg            %.3f 1/100Km' % (mpg, metric_consumption))
print('')
print('Gas Consumption Rating    : %s' % (rating))
# prints output