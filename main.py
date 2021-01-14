someElements=[
  'a','b','c','b','d','m','n','n'
];

set1=set(someElements);
for i in set1:
  if someElements.count(i) > 1:
    print(i+' has duplicated.')
  else:
    print(i+' has not duplicated.');