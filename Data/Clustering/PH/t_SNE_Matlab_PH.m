
clc;
clear all;
close all;
frs=500;
frd=1000;
b = load('betti_CNPbX.txt');
betti = [b];
for iter=1:6
    score=tsne(betti);
    fname = strcat('tsne_Eclassdata_new_v',num2str(iter),'.txt');
    dlmwrite(fname,score)
    figure;
    plot(score(1:frd-frs+1,1),score(1:frd-frs+1,2),'k^'); 
    hold on;
    plot(score(frd-frs+2:2*(frd-frs+1),1),score(frd-frs+2:2*(frd-frs+1),2),'b^');
    plot(score((frd-frs+1)*2+1:3*(frd-frs+1),1),score((frd-frs+1)*2+1:3*(frd-frs+1),2),'r^'); 

    plot(score((frd-frs+1)*3+1:4*(frd-frs+1),1),score((frd-frs+1)*3+1:4*(frd-frs+1),2),'mo'); 
    plot(score((frd-frs+1)*4+1:5*(frd-frs+1),1),score((frd-frs+1)*4+1:5*(frd-frs+1),2),'go'); 
    plot(score((frd-frs+1)*5+1:6*(frd-frs+1),1),score((frd-frs+1)*5+1:6*(frd-frs+1),2),'yo'); 

    plot(score((frd-frs+1)*6+1:7*(frd-frs+1),1),score((frd-frs+1)*6+1:7*(frd-frs+1),2),'square','color','[0.0 1.0 1.0]'); 
    plot(score((frd-frs+1)*7+1:8*(frd-frs+1),1),score((frd-frs+1)*7+1:8*(frd-frs+1),2),'square','color','[0.9 0.4 0.1]'); 
    plot(score((frd-frs+1)*8+1:9*(frd-frs+1),1),score((frd-frs+1)*8+1:9*(frd-frs+1),2),'square','color','[0.5 0.0 0.5]'); 
    set(gcf,'Position',[10 10 1000 1000])
end
