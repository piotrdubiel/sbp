function [mu trmx] = prepTransform(tvec, comp_count)
% tvec - maciery zawieraj�ca obrazy zbioru uczacego
% comp_count - liczba najwi�kszych sk�adowych w macierzy transformacji
% mu - warto�� �rednia zbioru ucz�cego
% trmx - macierz transformacji do comp_count-wymiarowej przestrzeni PCA
% Funkcja zapisuje w plikach wektor sredniej zbioru ucz�cego, oraz WSZYSTKIE wektory w�asne 
% w kolejno�ci od odpowiadaj�cego najwi�kszej wartosci w�asnej (w tej wersji zapis wykomentowany!)

mu = mean(tvec);
cmx = cov(tvec);
[evec eval] = eig(cmx);
eval = sum(eval);
[eval evid] = sort(eval);
eval = eval(size(eval,2):-1:1);
evec = evec(:, evid(size(eval,2):-1:1));
% save 'nist_mu.mat' mu
% save 'nist_cov.mat' evec 
trmx = evec(:, 1:comp_count);
