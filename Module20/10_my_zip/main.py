def shortest_seq_range(string, tpl):
    return min(len(string), len(tpl))

sym_str = 'abcde'
nums_tpl = (10, 20, 30, 40)

#pairs = [(sym_str[i_elem], nums_tpl[i_elem]) for i_elem in range(len(sym_str))]
#pairs = [(sym_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortest_seq_range(sym_str, nums_tpl))]
pairs = ((sym_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortest_seq_range(sym_str, nums_tpl)))
print(pairs)

for i_elem in pairs:
    print(i_elem)
print(zip(sym_str, nums_tpl))

