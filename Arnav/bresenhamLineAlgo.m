disp ('Bresenham line algorithm');
x1=input('Enter value for x1:');
y1=input('Enter value for y1:');
x2=input('Enter value for x2:');
y2=input('Enter value for y2:');
x=x1;
y=y1;
slope=(y2-y1)/(x2-x1);
dy=y2-y1;
dx=x2-x1;
DP=2*dy-dx;
for i=1:dx-1
    x=x+1;
    X(i+1)=x; %initilze array for storing points
    Y(i+1)=y;
if DP<0
    DP=DP+2*dy ;
else
    DP=DP +2*dy - 2*dx;
      y=y+1;
  end
end
plot(X,Y,"r*",'linewidth',2)
grid on
      
