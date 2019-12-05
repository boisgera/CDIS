k = 10000;
t_final = 1000;
pas = 0.1;
times = 0:pas:t_final;
y0 = [1;0];

A = [0,1;-k,0];

function xdot = vector_field(t, x)
  xdot = A*x;
endfunction 

y = ode(y0,0,times,vector_field);
