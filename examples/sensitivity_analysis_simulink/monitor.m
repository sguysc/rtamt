function [rob] = monitor( in, param1, param2 )
% FUNCTION: monitot the input data in using rtamt
%
% Created:  20-01-2020
% Author:   Dejan Nickovic

import py.rtamt.STLIOSpecification;
spec = STLIOSpecification(1);
declare_var(spec, 'pc', 'float');
declare_var(spec, 'lep', 'float');
declare_var(spec, 'out', 'float');
set_var_io_type(spec, 'pc', 'input');
set_var_io_type(spec, 'lep', 'output');
set_var_io_type(spec, 'out', 'output');
spec.iosem = 'output-robustness';
spec.spec = sprintf('out = always((pc >= %d ) implies (eventually[0:100] always[0:%d] (abs(pc - lep) <= 3)))',param1, param2);

display(spec.spec)

parse(spec);

pc_signal = in.get('pc');
lep_signal = in.get('lep');
for(i=1:1001)
    pc_val = pc_signal.Values.Data(i);
    lep_val = lep_signal.Values.Data(i);
    pc_tuple = py.tuple({'pc',pc_val});
    
    lep_tuple = py.tuple({'lep',lep_val});
    l = py.list;
    append(l, pc_tuple);
    append(l, lep_tuple);
    rob = update(spec, i, l);
end