function custom_plot2(filename,p,wa,vmin,vmax,ups)

%check dimension
[m,n]=size(p);
if size(p)~=size(wa)
    fprintf('matrix dimension mismatch');
end

%set up output array and scaling constant
o=zeros(m*ups,n*ups,3);
vsca = 1/(vmax-vmin);

%assemble the output array
for i = 1:m
    iu = (i-1)* ups;
    for j = 1: n
        ju = (j-1) *ups;
        if wa(i,j)==1
            o(iu+1:iu+ups,ju+1:ju+ups,:)=1;
        else
            colors = palette2(fscale(p(i,j),vmin,vsca));
            o(iu+1:iu+ups,ju+1:ju+ups,1)=colors(1);
            o(iu+1:iu+ups,ju+1:ju+ups,2)=colors(2);
            o(iu+1:iu+ups,ju+1:ju+ups,3)=colors(3);
        end
    end
end

%plot and save the image
figure(2)
h= image(o);
axis equal
axis off
saveas(h,filename);

%subfunction
%returns colors (red ->white->blue color scheme)
function colors = palette2(v)
colors=zeros(3,1);
if (v>0.5)
    vs=0;
else
    vs=sin(2*pi*v);
end
colors=[sqrt(v);v*v*v;vs];

%subfunction
function vs = fscale(v,vmin,vsca)
vs = (v-vmin)*vsca;
if vs<0
    vs=0;
end
if vs>1
    vs=1;
end



