import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7,4))
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [0.23,0.49,0.58,0.72,0.83,0.97,0.91,0.85,0.82,0.79]
# plt.plot(x, y,'r', lw=1.5)
# plt.plot(x, y,'o', lw=1.5)
# plt.vlines(6,0,0.97,colors='c',linestyles='dashed')
# plt.axis('tight')
# plt.xlabel('Number of Features Selected')
# plt.ylabel('Score')
# plt.title('Recursive Feature Elimination')
# plt.show()
x = ['Azimuth',
     'Altitude', 'Velocity','Latitude', 'Inclination','Longitude ']
y = [99, 98,45, 38, 24,19]
x.reverse()
y.reverse()
plt.barh(range(6), y,tick_label=x)
plt.xlabel('Relative Importance')
plt.title('Feature Importance of 6 Features')
plt.show()