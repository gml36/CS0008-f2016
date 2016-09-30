system = input('Do you want to use USC or Metric?')
# here I am asking if the client wants Metric or USC
if system != 'USC' and system != 'Metric':
    input('System not recognized! Press enter to exit.')
    exit()
distance = float(input('What was the distance driven?'))
# here I am asking for the distance the client drove
amount = float(input('How much gasoline was used?'))
# here I am asking for the amount of gas the client used

metric_distance = 0
usc_distance = 0
if system == 'USC':
    usc_distance = distance
    # TODO check conversion
    metric_distance = usc_distance*0.621371
else:
    metric_distance = distance
    #TODO check conversion
    usc_distance = metric_distance*1.60934
# calculated metric vs usc distance

gallons = 0
liters = 0
if system == 'USC':
    gallons = amount
    liters = gallons*0.264172
else:
    liters = amount
    gallons = liters*3.78541
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
