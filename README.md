# Configure a sample set of links for a site

You can replace the default index.html file with a one configured with links pointing to the site this material's repo is being used for.

## Instructions:
0) Fork this repo to your account
1) clone the repo locally and switch to the gh-pages branch
2) cd into the folder .configure_site
3) open .configure.py and replace the values specified near the top:
  
    (EXAMPLE VALUES USED BY palomar)  
    SITE = "palomar"  
    GITHUB_ACCOUNT = "https://github.com/csit128"  
    GITHUB_MATERIALS_REPO = "csit128_Intro_DS"  
  
4) Execute .configure.py from the .configure_site folder: 
    - python3 .configure.py

5) Navigate to index.html file: (most likely it is this URL):
    - https://{YOUR_GITHUB_ACCOUNT}.github.io/{REPO}/  
      (e.g. https://csit128.github.io/csit128_Intro_DS/)

NOTE: After running the above the commands, the old index.html file with
all the various demonstration links is now in this file: index_data8_example.html