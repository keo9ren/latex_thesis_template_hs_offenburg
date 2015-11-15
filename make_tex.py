#!/usr/bin/env python

import apt
import sys
import getopt
import subprocess
import os
import os.path

def main(argv): 
    pdf = ''
    
    try:
        opts, args = getopt.getopt(argv,"hcp:",["pdf="])
    except getopt.GetoptError:
        print 'Error'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'usage'
            print 'make_tex -p <mydoc.tex>'
            print 'sudo make_tex -c'
            sys.exit()
        elif opt == '-c':
            print 'Checking your latex installation'
            print 'requires root'
            check_tex()
        elif opt in ("-p","pdf"):
            name = arg
                
            fileexists('./figures/titlepage_fig/hs_og_ei.pdf')
            fileexists('./figures/titlepage_fig/hs_offenburg.pdf')
            subprocess.call(['pdflatex',name])
            subprocess.call(['biber',name])
            subprocess.call(['pdflatex',name])
            subprocess.call(['pdflatex',name])


def fileexists(path):
    #there's something not working here so file converson will be executed every time
    #but that's not a real problem as it is very fast
    if os.path.isfile('path') and os.access('path',os.R_OK): 
        print 
    else:
        subprocess.call(['epstopdf','ei-fb_cmyk-schrift_neuerfarbraum.eps','--outfile=hs_og_ei.pdf'],cwd='./figures/titlepage_fig/')
        subprocess.call(['epstopdf','HS-Logo_BLAU.eps','--outfile=hs_offenburg.pdf'],cwd='./figures/titlepage_fig/')

def check_tex():
    print 'checking your install' 
    print 'depending on your internet connection this can take a while' 
    install("make") 
    install("texlive-base")
    install("texlive-lang-german")
    install("texlive-lang-english")
    install("texlive-font-utils")
    install("texlive-latex-base") 
    install("texlive-latex-recommended")
    install("texlive-latex-extra") 
    install("biber") 
    install("texlive-science") 

def install(pkg_name):

    cache = apt.cache.Cache()
    cache.update()

    pkg = cache[pkg_name]

    if pkg.is_installed:
        print "{pkg_name} already installed".format(pkg_name=pkg_name)
    else:
        pkg.mark_install()
    
        try:
            cache.commit()
        except Exception, arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]"
        
if __name__ == "__main__":
    main(sys.argv[1:])
