HS Offenburg Latex Template
=====================================

1 How to
=====================================
On Linux based machine use:

1.1 Check your latex configuration 
=====================================
sudo ./make_tex.py -c 
    
1.1 Make a pdf 
=====================================
./make_tex.py -p yourfile.tex





3 Requirements (old)
=====================================
On a Debian machine the following is needed:

1) Basic Latex environment with ngerman package and biber for bibliographie  and biber for bibliographie. You also will need eps2to which is included in texlive-font-utils to convert logos from eps to pdf. 
   run:
   # apt-get install texlive-base texlive-lang-ngerman texlive-font-utils biber

2) Make is required as build system
   run:
   # apt-get install make

4 How to build (old)
=====================================

1) Preperations for first start
    1.1) To convert logos from eps to pdf
         run:
         make logo

2) To generate document as pdf
   run:
   make pdf
