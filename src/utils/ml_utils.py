import itertools


def generate_params(param_grid):
    # Lặp qua tất cả các siêu tham số và giá trị của chúng
    param_lists = []
    for key, values in param_grid.items():
        param_lists.append([(key, v) for v in values])
    
    # Tạo tất cả các bộ tham số có thể có từ các giá trị cho mỗi siêu tham số
    for params in itertools.product(*param_lists):
        yield dict(params)