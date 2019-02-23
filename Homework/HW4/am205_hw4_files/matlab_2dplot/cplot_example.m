%script to generate plot

%load in data
q=load('pierce.txt');

%generate initial vector
w=zeros(100,200);
for i= 1:100
    x=0.1*i;
    for j = 1:200
        y= 0.1*j;
        w(i,j)=sin(x+0.5*y);
    end
end

%call the first custom plotting routine
custom_plot1('test1.png',w,q,-1.1,1.1,3);
%call the second custom plotting routine
custom_plot2('test2.png',w,q,-1.1,1.1,3);
