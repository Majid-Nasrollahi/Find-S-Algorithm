D = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','Normal','Strong','Cool','Change', 'Yes']
]

def find_s(ds):
    h = ['','','','','','']
    for x in ds:
        if x[-1] == 'No':
            continue
        else:
            for i in range(len(x)-1):
                if h[i] == x[i]:
                    pass
                else:
                    if h[i] == '':
                        h[i] = x[i]
                    else:
                        h[i] = '?'
    
    return h

print(find_s(D))