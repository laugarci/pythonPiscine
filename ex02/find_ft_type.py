def all_thing_is_obj(object: any) -> int:
    type_name = type(object).__name__
    
    match type_name:
        case 'list':
            print(f'List : {type(object)}')
        case 'tuple':
            print(f'Tuple : {type(object)}')
        case 'set':
            print(f'Set : {type(object)}')
        case 'dict':
            print(f'Dict : {type(object)}')
        case 'str':
            print(f'{object} is in the kitchen : {type(object)}')
        case _:
            print('Type not found')
    
    return 42
