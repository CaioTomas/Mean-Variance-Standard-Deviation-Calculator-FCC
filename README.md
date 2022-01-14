## English description

This is the repo of my solution to the *Mean, Variance and Standard Deviation Calculator* project from the **Data Analysis with Python** course from freeCodeCamp. The portuguese description is down below.

### Assignment

Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix. 

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix. 

The returned dictionary should follow this format:

```py
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:

```py
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

The unit tests for this project are in `test_module.py`.

### Development

For development, you can use `main.py` to test your `calculate()` function. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

----------------------------------------------------------------------

## Descrição em português

Esse é o repositório com a minha solução para o projeto *Mean, Variance and Standard Deviation Calculator* do curso **Data Analysis with Python** do freeCodeCamp. 
A tradução é livre e feita por mim.

### Tarefa

Crie uma função chamada `calculate()` em `mean_var_std.py` que usa Numpy para retornar a média, variância, desvio padrão, máximo, mínimo, soma das linhas, colunas e elementos em uma matriz 3 x 3. 

A entrada da função deve ser uma lista com 9 dígitos. A função deve converter a lista em um array 3 x 3 do Numpy e retornar um dicionário contendo todos os valores mencionados acima ao longo dos dois eixos e da matriz achatada. 

O dicionário retornado deve seguir o seguinte formato:

```py
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

Se uma lista com menos de 9 elementos for passada na função, ela deve levantar uma exceção `ValueError` com a messagem: "List must contain nine numbers." Os valores no dicionário retornado devem ser listas e não arrays do Numpy.

Por exemplo, `calculate([0,1,2,3,4,5,6,7,8])` deve retornar:

```py
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

Os testes unitários deste projeto estão em `test_module.py`.

### Desenvolvimento

Para desenvolvimento, você pode usar `main.py` para testar sua função `calculate()`. Clique em "run" para rodar `main.py`.

### Testando 

Os testes unitários para este projeto estão em `test_module.py`. Importamos os testes de `test_module.py` para `main.py` por conveniência. Os teste vão rodar automaticamente quando clicar em "run".

### Submissão

Copie a URL do projeto e submeta-a ao freeCodeCamp.
