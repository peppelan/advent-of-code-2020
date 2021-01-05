from collections import defaultdict
from queue import Queue
from copy import copy

def sol(input_text):
    numbers = [int(i) for i in input_text.split("\n")]
    numbers.sort()
    
    pathsByOutput = {0: 1}
    val = 0
    
    for i in range(len(numbers)):
        n = numbers[i]
        paths = 0
        
        for nm in [n-1, n-2, n-3]:
            paths += pathsByOutput.get(nm, 0)
        
        pathsByOutput[n] = paths
        val = paths
            
    
    return paths
    
    

test_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

input_text = """46
63
21
115
125
35
89
17
116
90
51
66
111
142
148
60
2
50
82
20
47
24
80
101
103
16
34
72
145
141
124
14
123
27
62
61
95
138
29
7
149
147
104
152
22
81
11
96
97
30
41
98
59
45
88
37
10
114
110
4
56
122
139
117
108
91
36
146
131
109
31
75
70
140
38
121
3
28
118
54
107
84
15
76
71
102
130
132
87
55
129
83
23
42
69
1
77
135
128
94"""

print(sol(input_text))
