from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request): #view-function
    #ss ---> is HTML data/code
    print("welcome/ url is requested and display() is executed")
    ss='''
        <center>
            <h2 style= "color:Blue;">
                Hello user, Welcome to Django First-Project First-Application
            </h2>
            <h3/>
        </center>
       '''
    return HttpResponse(ss)

def show(request):
    ss='''
            <!--
HTML Webpage to display "Welcome-Message" with different headings and styles
"E:\00.Full_Stack_Dev\03.Django\QEdgeTech\DailyClassPractice\23-03-23_HTML\Welcome.html"
-->
<html>
	<head>
		<title>
		***Welcome-Page***
		</title>
		<style>
			h1{
				color:Blue;
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:Violet;
			}
			h1,h3,h5{
				background-color: yellow;
			}
			h2,h4,h6{
				background-color: lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML Webpage</h1>
			<hr color="Brown" width="95%"/>
			<h2>Welcome to DJANGO HTML Webpage</h2>
			<hr color="Brown" width="85%"/>
			<h3>Welcome to DJANGO HTML Webpage</h3>
			<hr color="Brown" width="75%"/>
			<h4>Welcome to DJANGO HTML Webpage</h4>
			<hr color="Brown" width="65%"/>
			<h5>Welcome to DJANGO HTML Webpage</h5>
			<hr color="Brown" width="55%"/>
			<h6>Welcome to DJANGO HTML Webpage</h6>
			<hr color="Brown" width="45%"/>
		</center>
	</body>
</html>
       '''
    return HttpResponse(ss)
    
def hello(request):
    print("hello/ url is requested and hello() is executed")
    ss='''
        <html>
            <head>
            <title>Hello Webpage</title>
            </head>
            <style>
            h1{
                color:Blue;
                width=90%;
            }
            h2{
                color:Green;
                width=80%;
            }
            h3{
                color:Red;
                width=70%;
            }
            h1,h2,h3{
                background-color:lightblue;
                border:2px solid brown;
            }
            </style>
            <body>
                <center>
                    <h1> Hello User...!!!</h1>
                    <hr color="brown" width="80%"/>
                    <h2> Hello User...!!!</h2>
                    <hr color="brown" width="60%"/>
                    <h3> Hello User...!!!</h3>
                    <hr color="brown" width="40%"/>
                </center>
            </body>
        </html>
        '''
    return HttpResponse(ss)
    

import time

def senddatetime(request):
    print("dtime/ url is requested and senddatetime() is executed")
    ct=time.ctime()
    print("client request date & time on server::",ct)
    ss='''
        <html>
            <head>
                <title>Date-time Webpage</title>
                <style>
                    h1{
                        color:Blue;
                        width:90%;
                    }
                    h2{
                        color:Green;
                        width:80%;
                    }
                    h3{
                        color:Red;
                        width:70%
                    }
                    h1,h2,h3{
                        background-color:lightgreen;
                        border:2px solid brown;
                    }
                </style>
            </head>
            <body>
                <center>
                    <h1>Welcome to Django - User ...!!!</h1>
                    <hr color="brown" width="80%">
                    <h2>Server-Date and time</h2>
                    <hr color="brown" width="70%">
                    <h3>''',ct,'''</h3>
                    <hr color="brown" width="60%">
                </center>
            </body>
        </html>
        '''
    return HttpResponse(ss)

def demo(request):
    print("multiple-url requests for same response")
    htmldata='''
    <center>
        <h1>Welcome Demo User</h1>
        <hr/>
        <h2>This is same output for diff-multiple-url-requests</h2>
        <hr/>
        <h3>Have a great day</h3>
        <hr/>
    </center>
    '''
    return HttpResponse(htmldata)
    

#default-url-request-view-func
def homepage(request):
    htmldata='''
    <center>
        <h1>Welcome to Default Home Page!!!</h1>
        <hr/>
        <h2>Your request page is not found...</h2>
        <hr/>
        <h3>Please try other URL or links!!!</h3>
        <hr/>
    </center>
    '''
    return HttpResponse(htmldata)