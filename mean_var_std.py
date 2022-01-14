import numpy as np

def calculate(lista):    
    try:
        calculations = {'mean':[], 
                    'variance':[],
                    'standard deviation':[],
                    'max':[],
                    'min':[],
                    'sum':[]}
        
        matrix = np.array(lista)
        matrix = matrix.reshape(3,3)
        
        calculations['mean'].extend([
            list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()
        ])
        calculations['variance'].extend([
            list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()
        ])
        calculations['standard deviation'].extend([
            list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()
        ])
        calculations['max'].extend([
            list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()
        ])
        calculations['min'].extend([
            list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()
        ])
        calculations['sum'].extend([
            list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()
        ])
    
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    
    return calculations