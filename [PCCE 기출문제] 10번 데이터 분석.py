def solution(data, ext, val_ext, sort_by):
    
    diction = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
        
    valid_items = [datum for datum in data if datum[diction[ext]] < val_ext]
    valid_items = sorted(valid_items, key=lambda x: x[diction[sort_by]])
    return valid_items
