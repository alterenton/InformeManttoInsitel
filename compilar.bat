@echo off

lualatex ^
--aux-directory=auxiliares ^
--output-directory=construido ^
--interaction=errorstopmode ^
%*
