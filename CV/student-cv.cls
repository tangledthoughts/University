%-------------------------------------------------------------------------------
%                           CLASS NAME AND VERSION
%-------------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{studentcv}[2020/06/09 CV class]


%-------------------------------------------------------------------------------
%                            PROCESS CLASS OPTIONS
%-------------------------------------------------------------------------------
%% load some required packages first
% for easy color definitions; provides \definecolor; load before background pkg
\RequirePackage[dvipsnames, svgnames, x11names]{xcolor}
% for positioning text within the side column | use showboxes for visible frame
\RequirePackage[absolute,overlay]{textpos}
% provides key-value class options via \DeclareOptionX
\RequirePackage{xkeyval}
% provides \ifnumgreater{<int expr.>}{<int expr.>}{<true>}{<false>},
% \apptocmd{<command>}{<code>}{<success>}{<failure>} and \newtoggle{<name>}
\RequirePackage{etoolbox}
% enable simple math like +/- etc. on lengths
\RequirePackage{calc}
% change page margins
\RequirePackage[
	nohead,
	nofoot,
	nomarginpar,
]{geometry}

% Provide some pre-defined colours to choose from
% This is the Macchiato flavour of my favourite colour palette Catppuccin
\definecolor[white]{HTML}{FFFFFF}
\definecolor[black]{HTML}{000000}
\definecolor[rosewater-ma]{F4DBD6}
\definecolor[flamingo-ma]{F0C6C6}
\definecolor[pink-ma]{F5BDE6}
\definecolor[mauve-ma]{C6A0F6}
\definecolor[red-ma]{ED8796}
\definecolor[maroon-ma]{EE99A0}
\definecolor[peach-ma]{F5A97F}
\definecolor[yellow-ma]{EED49F}
\definecolor[green-ma]{A6DA95}