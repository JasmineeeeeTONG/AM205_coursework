%%function bin_mul
function bin_mul_example

L=[1 0 0 0; 0 1 0 0;  1 1 1 0; 1 0 1 1];
U=[1 0 1 0; 0 1 1 1;  0 0 1 0; 0 0 0 1];

A=bin_mul(L,U)

function A=bin_mul(L,U)
%find matrix size
[lnr,lnz]=size(L);
[unr,unz]=size(U);

%check matrix dimension
if lnz ~= unr
    error('matrix dimension dismatch')
end

A=zeros(lnr,unz);

for i=1:lnr
    for j=1:unz
        for k=1:lnz
            A(i,j)=bitxor(A(i,j),bitand(L(i,k),U(k,j)));
        end
    end
end
