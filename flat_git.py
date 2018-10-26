area=int(input('please enter total area in feet'))
budget=int(input('please enter your budget'))
cost=int(input('please enter per sq.feet cost'))
total=area*cost
if total<=budget:
 print('in budget')
else:
 print('out of budget')