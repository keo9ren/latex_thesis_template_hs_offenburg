ivESK Latex Template
=====================================
This is the draft of the latex template used by the institute of reliable
embedded systems and communications electronics (ivESK).

0 Requirements & Build
=====================================
In order to build you will need a full [texlive](https://www.tug.org/texlive/)
or [miktex](https://www.tug.org/texlive/) installation. Depending on the way you
install latex, you may install [biber](https://www.ctan.org/pkg/biber?lang=de)
additionally. If you want to use, our preffered build system
[scons](http://scons.org/) you have to install it to. Otherwise the templates
will also work compiled with an arbitrary PdfLatex compiler.

On a debian based os you may want to install using:

1) Basic Latex environment with ngerman package and biber for bibliographie  and
biber for bibliographie.    
   run:
   # apt-get install texlive-base texlive-lang-ngerman texlive-font-utils biber
2) Scons build system.
   run:
   # apt-get install scons
   
1 Report
=====================================
This is the official ivESK template for report, thesis and the like. 
To build,
   run:
   # scons
To clean:
   run:
   # scons -c


2 Presentation
=====================================
This is the non-official ivESK latex beamer template. 
To build,
   run:
   # scons
To clean:
   run:
   # scons -c

