import numpy as np

def calculate(list):
  list_size = np.array(list)

  if list_size.size != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    matrix = np.array(list).reshape(3,3)
# matrix = list.reshape(3,3) - At first I had it like this, but it is better to just add .reshape(3,3) when creating the array.
    
  # Now let's create each operation / had to add the tolist() otherwise it would return as array[content] and the exercise requests "The values in the returned dictionary should be lists and not Numpy arrays."
    mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
    variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
    std_dev = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
    max = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
    min = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
    sum = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]

    calculations = {
    "mean": mean,
    "variance": variance,
    "standard deviation": std_dev,
    "max": max,
    "min": min,
    "sum": sum,
    }
  return calculations