
Repository Size          |  Last Commit
:-------------------------:|:-------------------------:
 ![GitHub repo size](https://img.shields.io/github/repo-size/iconicsudip/RBR-system) | ![GitHub last commit](https://img.shields.io/github/last-commit/iconicsudip/RBR-system)


# RBR-SYSTEM
A room booking platform or you can say app where only authenticated user can user this app.

## Appendix

- [Why RBR](https://github.com/iconicsudip/RBR-system#why-rbr-)
- [Features](https://github.com/iconicsudip/RBR-system#why-rbr-)
- [Installation](https://github.com/iconicsudip/RBR-system#installation)
- [Run Locally](https://github.com/iconicsudip/RBR-system#run-locally)
- [Credits](https://github.com/iconicsudip/RBR-system#credits)
- [Acknowledgements](https://github.com/iconicsudip/RBR-system#acknowledgements)

## Why RBR ?
  Recently i watched a south indian movie __RRR__ and __RBR__ means __Room Book and Rebook__ so that's why i named this project as __RBR__.



## Features

  - Proper __Authentication__ System.
  - __Two Factor__ verification to cancel booking( for __Customer__ ) and Clear Slot( for __Manager__ ).
  - Well defined __Database__.


## Installation
  Here i will show you __two__ different method to download file locally.
  
  #### 1. Using SSH :
  - If you have __Git__ then open your __Git Bash__ where you want to download total file and then type below code :  
    ```
    git clone git@github.com:iconicsudip/RBR-system.git 
    
    ```
  - Or, If you don't have __Git__ then you have to download git first from this link [Download Git](https://git-scm.com/downloads) and then open git like previous step.The code is in below
    ```
    git clone git@github.com:iconicsudip/RBR-system.git

    ```
  #### 2. Download Zip:
  - If you are not familier with git then you can directly download zip file by clicking the below link:
  
    [Download RBR Zip ](https://github.com/iconicsudip/RBR-system/archive/refs/heads/master.zip)
    
## Run Locally

To run locally and to do experience you have to do few steps 
- ### If Already Downloaded
  + If you don't have python then download python from below link:
  
    [Download Python](https://www.python.org/downloads/)
  + Go to the project directory where you downloaded the file.
  + Open __terminal__ or __cmd__ on that directory.
  + You have to download __dependencies__ type below code in __terminal__ or __cmd__.
    ```bash
      > pip install -r requirments.txt
    ```
  + After finishing the __above all__ steps you have to start server so __open__ your __terminal__ or __cmd__ on that directory or if you already opened then just type below code:
    ```bash
      > python manage.py makemigrations
      > python manage.py migrate
      > python manage.py runserver
    ```
     It server will start on port __127.0.0.1:8000__ .
- ### If Not Downloaded Yet
  + If you don't have python then download python from below link:
  
    [Download Python](https://www.python.org/downloads/) 
    
    or you already have python then just skip this step.
  + If you don't have __Git__ then you have to download git first from this link [Download Git](https://git-scm.com/downloads) or if you already have git then skip this step and do next all steps.
  + Open __Git Bash__ where you want to download folder and do below steps :
    
     + Download folder
      ```
      $ git clone git@github.com:iconicsudip/RBR-system.git

      ```
     + Open __terminal__ or __cmd__ on that directory.
     + You have to download __dependencies__ type below code in __terminal__ or __cmd__.
      ```bash
        > pip install -r requirments.txt
    ```
    + After finishing the __above all__ steps you have to start server so __open__ your __terminal__ or __cmd__ on that directory or if you already opened then just type below code:
    ```bash
        > python manage.py makemigrations
        > python manage.py migrate
        > python manage.py runserver
    ```
    It server will start on port __127.0.0.1:8000__ .

## Passwords

You can see __passwords.txt__ in project directory where you can get __Customer's__ and __Manager's__ __username__,__email__ and __password__.
## Credits

 - I used bootstrap5.0 for templates responsive [Bootstrap5](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
 - I took search bar what you can see in customer dashboard from bbbootstrap [BBBootstrap](https://bbbootstrap.com/snippets/bootstrap-search-box-input-icons-inside-88211241)

## Acknowledgements
 Thanks to FOOSEE to giving this opertunity
