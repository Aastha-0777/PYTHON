state = {'Guj' : 'GandhiNagar', 'Goa' : 'Panji', 'TN' : 'Chennai', 'Karnataka' : 'Benglore'}

print(state)

state['HP'] = 'Shimla';

print(state)

state.update({'UP' : 'Lucknow', 'UK' : 'Dehradun'})

print(state)

removedElem = state.pop('Goa')
print('removing', removedElem, '...')
print(state)

removedPair = state.popitem()
print('Removed Pair : ', removedPair)
print(state)