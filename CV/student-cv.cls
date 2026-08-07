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
\definecolor[rosewater-ma]{HTML}{F4DBD6}
\definecolor[flamingo-ma]{HTML}{F0C6C6}
\definecolor[pink-ma]{HTML}{F5BDE6}
\definecolor[mauve-ma]{HTML}{C6A0F6}
\definecolor[red-ma]{HTML}{ED8796}
\definecolor[maroon-ma]{HTML}{EE99A0}
\definecolor[peach-ma]{HTML}{F5A97F}
\definecolor[yellow-ma]{HTML}{EED49F}
\definecolor[green-ma]{HTML}{A6DA95}
\definecolor[teal-ma]{HTML}{8BD5CA}