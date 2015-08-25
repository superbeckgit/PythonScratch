# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:16:13 2014

@author: mjbeck
"""

def make_rules(num):
    # Rules:
    #          pattern in         position k in        contribution to
    # Value    current string     new string           pattern number
    #                                                  is 0 if replaced by '.'
    #                                                  and value if replaced
    #                                                  by 'x'
    #   1       '...'               '.'                        1 * 0
    #   2       '..x'               'x'                        2 * 1
    #   4       '.x.'               'x'                        4 * 1
    #   8       '.xx'               'x'                        8 * 1
    #  16       'x..'               '.'                       16 * 0
    #  32       'x.x'               '.'                       32 * 0
    #  64       'xx.'               '.'                       64 * 0
    # 128       'xxx'               'x'                      128 * 1
    #                                                      ----------
    #                                                           142
    patterns = ['...','..x','.x.','.xx','x..','x.x','xx.','xxx']
    rules = {}
    
    for i in range(7,-1,-1):
        if num // 2**i:
            rules[patterns[i]] = 'x'
            num -= 2**i
        else:
            rules[patterns[i]] = '.'
        
    if num != 0:
        print('shit, math error')
    return rules

#print(make_rules(17))

def encrypt(my_str, rules):
    # copy input string for length
    outstr = my_str[:]
    strlen = len(my_str)
    for ix in range(strlen):
        # build new output string with slices and dictionary result. 
        # mod right character index for wrap around
        outstr = outstr[:ix] + rules[my_str[ix-1]+my_str[ix]+my_str[(ix+1)%strlen]] + outstr[ix+1:]
    #print(outstr)
    return outstr
    
def cellular_automaton(in_str, encr_key, iters):
    # get dictionary of rules
    rules  = make_rules(encr_key)
    # encrypt a number of times
    for i in range(iters):
        in_str = encrypt(in_str,rules)
    return in_str
    

#tests

print(cellular_automaton('.x.x.x.x.', 17, 2))
#>>> xxxxxxx..
print(cellular_automaton('.x.x.x.x.', 249, 3))
#>>> xxxxxxx..
print(cellular_automaton('...x....', 125, 1))
#>>> xx.xxxxx
print(cellular_automaton('...x....', 125, 2))
#>>> .xxx....
print(cellular_automaton('...x....', 125, 3))
#>>> .x.xxxxx
print(cellular_automaton('...x....', 125, 4))
#>>> xxxx...x
print(cellular_automaton('...x....', 125, 5))
#>>> ...xxx.x
print(cellular_automaton('...x....', 125, 6))
#>>> xx.x.xxx
print(cellular_automaton('...x....', 125, 7))
#>>> .xxxxx..
print(cellular_automaton('...x....', 125, 8))
#>>> .x...xxx
print(cellular_automaton('...x....', 125, 9))
#>>> xxxx.x.x
print(cellular_automaton('...x....', 125, 10))
#>>> ...xxxxx
print(cellular_automaton('.', 21, 1))
