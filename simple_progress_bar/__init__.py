
def print_progressbar(value: int, max_value: int, char: str = '|', blank: str = ' ', show_value: bool = True, description: str = '', k: int = 100, mult: int = 1):
    char_base = char * mult
    char_blank = blank * mult
    bars = []
    limit = k 

    for i in range(limit):
        
        base = i * char_base
        blank = (limit - i) * char_blank
        bar = base + blank
        bars.append(bar)

    bars.append(k * char_base)
    
    bar_constant = 100 / k
    p = value * 100 / max_value 
    b_index = int(int(p) / bar_constant)  
    b = bars[b_index] if p/bar_constant >= b_index and p/bar_constant < (b_index + 1) else ''
    final_string = f'|{b}| -> {int(p)} % {description}' if show_value else f'|{b}|'
    
    print(f'\r {final_string}', end='')