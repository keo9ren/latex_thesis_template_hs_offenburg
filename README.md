Make Measurement Report from sources
=====================================

1. Requirements
=====================================
On a Debian machine the following is needed:

1) Basic Latex environment with ngerman package and biber for bibliographie  and biber for bibliographie. You also will need eps2to which is included in texlive-font-utils to convert logos from eps to pdf. 
   run:
   # apt-get install texlive-base texlive-lang-ngerman texlive-font-utils biber

2) Make is required as build system
   run:
   # apt-get install make

2. How to build
=====================================

1) Preperations for first start
    1.1) To convert logos from eps to pdf
         run:
         make logo

2) To generate document as pdf
   run:
   make pdf
