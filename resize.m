close all;
clear;
clc;
Files = dir(fullfile('C:\Users\qinghua2\Pictures\personimages\DATA3\person\','*.jpg'));
size_hw=500;
mkdir('data2\person\');
mkdir('data2\none\');
for i=1:length(Files)
    temp=imread(strcat('C:\Users\qinghua2\Pictures\personimages\DATA3\person\',Files(i).name));
    temp=imresize(temp,[size_hw,size_hw]);
    imwrite(temp,strcat('C:\Users\qinghua2\Pictures\personimages\data2\person\',Files(i).name));
end
Files = dir(fullfile('C:\Users\qinghua2\Pictures\personimages\DATA3\none\','*.jpg'));
for i=1:length(Files)
    temp=imread(strcat('C:\Users\qinghua2\Pictures\personimages\DATA3\none\',Files(i).name));
    temp=imresize(temp,[size_hw,size_hw]);
    imwrite(temp,strcat('C:\Users\qinghua2\Pictures\personimages\data2\none\',Files(i).name));
end