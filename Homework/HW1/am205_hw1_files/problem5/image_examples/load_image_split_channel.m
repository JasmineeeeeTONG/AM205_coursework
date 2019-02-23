% 09/11/16 Jinsoo Kim

clear % erase all the variables in the workspace
close all % close all the figures
clc % clear the command window

option = 1;
% 1 - thirlmere.png, 2 - rubik.png


% Read the test image
% This image should be placed in the same folder with m-file
if option == 1
    imagename = 'thirlmere.png';
else
    imagename = 'rubik.png';
end
test_image = imread(imagename); 

% remove the extension '.png' in the name
imagename = strsplit(imagename,'.'); % output - cell
imagename = imagename{1};


% Check size
% R - test_image(:,:,1), G - test_image(:,:,2), B - test_image(:,:,3)
% pixel value: uint8 (range: 0~255)
[r,c,channel] = size(test_image); 
display([int2str(c) 'x' int2str(r) ' pixels in ' int2str(channel) ' channels'])



% Plot the image
figure()
image(test_image)


% Output each channel
for aa=1:channel
    test_image2 = zeros(size(test_image),'uint8'); % make the 3 dimensional zero matrix (uint8 type)
    test_image2(:,:,aa) = test_image(:,:,aa); % assign only one channel of test timage to the new image
    
    figure()
    image(test_image2)
    
    imwrite(test_image2,[imagename '_channel' num2str(aa) '.png']) % write the image as png file
end