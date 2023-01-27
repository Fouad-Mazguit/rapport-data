clc;
clear all;
close all;

codMD = 0.8050;
codTDa = 0.9308;

x = categorical({'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
x = reordercats(x,{'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
y = [codTDa 0.9065  codMD];
subplot(1,3,1)
b=bar(x, y, 'BarWidth', 0.6);
set(gca,'XDir','reverse')
ylim([0.5 1])
ylabel('$R^2~~~$','Interpreter','latex','Rotation',0, 'FontSize', 20);
yticks([0.5 0.6 0.7 0.8 0.9 1])
b.FaceColor = 'flat';
b.CData(1,:) = [0 0.75 0];
b.CData(2,:) = [0 0.75 0];
b.CData(3,:) = [0 0 0.5];

set(gca,'FontSize',20,'LineWidth',2)

maeMD = 0.3458;
maeTDa = 0.2114;

x = categorical({'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
x = reordercats(x,{'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
y = [maeTDa 0.2605 maeMD];
subplot(1,3,2)
b=bar(x,y, 'BarWidth', 0.7);
set(gca,'XDir','reverse')
ylim([0.1 0.45])
ylabel('MAE-(eV)','FontSize', 20);
b.FaceColor = 'flat';
b.CData(1,:) = [0 0.75 0];
b.CData(2,:) = [0 0.75 0];
b.CData(3,:) = [0 0 0.5];

set(gca,'FontSize',20,'LineWidth',2)


mseMD = 0.201;
mseTDa = 0.0787;

x = categorical({'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
x = reordercats(x,{'PH-GBT', 'PFC-GBT', 'TPD-GBT'});
y = [mseTDa 0.1071 mseMD ];
subplot(1,3,3)
b=bar(x,y, 'BarWidth', 0.7);
set(gca,'XDir','reverse')
ylim([0 0.3])
ylabel('MSE-(eV)','FontSize',20);
b.FaceColor = 'flat';
b.CData(1,:) = [0 0.75 0];
b.CData(2,:) = [0 0.75 0];
b.CData(3,:) = [0 0 0.5];

set(gca,'FontSize',20,'LineWidth',2)

set(gcf,'Position',[10 10 1000 1000])



