close all;
clear;
clc;
[num, txt, raw]=xlsread('person.xlsx','A2:B1277');
for i=1227:1276;
    temp=imread(raw{i,1});
    if raw{i,2}==1
        imwrite(temp,strcat('data/person/',raw{i,1}));
    else
        imwrite(temp,strcat('data/none/',raw{i,1}));
    end
end