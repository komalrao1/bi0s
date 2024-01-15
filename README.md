# bi0s
**bi0s pentest challenges repository**

## challenges questions  
**1.**
***( a.) Display the path of your current directory***  
***( b.) List out the contents of your current directory***  
***( c.) List out the contents of your current directory including hidden files***  

**2.**
***( a.) Create a new directory named a***  
***( b.) Move to the newly created directory a***  
***( c.) Create a blank file named “file1”***  
***( d.) Display the file type of “file1”***  
***( e.) Add the line “Hello World” to “file1” using the command echo***  
***( f.) Display the contents of “file1”***  
***( g.) Display the file type of “file1” again***  

**3.**
***( a.) Stay in directory a. Create a file “file2” and add the contents below using the  command cat***  
      **First Line Second Line Third Line**  
***( b.) Display the contents of “file2”***  
***( c.) Display the contents of “file2” with the lines reversed***  

**4.**
***( a.) Stay in directory a. Concatenate the contents of “file1” and “file2” and save them into a new file “file3”***  
***( b.) Display the contents of “file3”***  

**5.**
***( a.) Stay in directory a. Create 2 directories b/c with a single command***  
***( b.) Create a new directory d***  
***( c.) Copy the directory d to directory c using a single command***  
***( d.) Delete the directory d in the current directory a***  
***( e.) Copy “file3” to the directory d with a single command***  

**6.**
***( a.) Go to directory d and rename “file3” to “file0”***  
****( b.) Stay in the same directory and move “file0” to directory a***  

**7.**
***( a.) Go to your home directory***  
***( b.) Create a file named “test” in the directory a/b/c/d***  
***( c.) Stay in the home directory. Find and display the path of “test”***  

  **8.**
***( a.) Go to directory a. Get the man page of grep and save its contents to a file named “grepman.txt”***  
***( b.) Print the lines containing the word “FILE” (Case sensitive) in the file “grepman.txt”***  

![answer1](https://github.com/komalrao1/bi0s/assets/147682987/0ee4ab67-b1c4-4bac-b4cd-915c84eae798)

**9.**
***( a.) Go to directory a and remove the directory b with a single command***  
***( b.) Remove the files starting with the word “file” with a single command***  

![answer2](https://github.com/komalrao1/bi0s/assets/147682987/662264e3-7980-4b53-bf88-3c5dd1d3c16c)

**10.**
***( a.) Go to https://blog.bi0s.in/  and download the logo.png image using wget***
***(b.) Do the same with python script (Hint : request library)***
***(c.) Also, display the metadata of the png.***
![answer3](https://github.com/komalrao1/bi0s/assets/147682987/55d569a8-a270-4aac-80ab-ffbd6a9ef397)

**11.**
***( a.) Use traceroute on google.com and find list of the IP addresses and hostnames between you and  google.com***
***( b.) Find  Subdomains,ip addresses of google.com using nslookup command***
![answer4](https://github.com/komalrao1/bi0s/assets/147682987/1f3b168d-8e2d-4070-9fac-4be231ea2a2c)

**12**
***Start a web server on port 8080 with python command*(In any directory and access the files in web browser )**
![answer5](https://github.com/komalrao1/bi0s/assets/147682987/6056d091-0c8f-4e80-a427-e6f2c20477a2)
![answer6](https://github.com/komalrao1/bi0s/assets/147682987/eae47a0c-ac40-44bb-8a1b-f70f9fb84e5c)
**13**
***( a.) Learn about nmap and use that scanner to scan your own machine***
***( b.) Go to https://tryhackme.com/room/furthernmap and get ip address and Scan the ip address with**(-sS,-sV,-A)**in your terminal include all ports (Hint : start machine )***
![answer7](https://github.com/komalrao1/bi0s/assets/147682987/f023ca21-9c27-4471-a153-0853f7256fa3)
![answer8](https://github.com/komalrao1/bi0s/assets/147682987/70e3fd7c-702d-4965-b8a4-a2c39c69cd70)
![answer9](https://github.com/komalrao1/bi0s/assets/147682987/a683bac3-e884-4dca-bc0c-dea1839f6ccc)
**14.**
***( a.) Create a chat application using nc on your local machine with one terminal as server and other as the client***
***( b.) Transfer a file from server to client (save that file with another name) and display the file.***
![answer10](https://github.com/komalrao1/bi0s/assets/147682987/ee6d671c-9523-4a7f-a4de-f8bbd8a431af)
![answer11](https://github.com/komalrao1/bi0s/assets/147682987/cd42f5b7-0cf3-444a-be59-62555a57e38d)



# **CODING CHALLENGES**
**1**
[**a.** ***hacker rank***](https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true)
![answer 12(a)](https://github.com/komalrao1/bi0s/assets/147682987/7885acf3-d4cd-4774-9f82-6a3e434653d2)
![answer 12(b)](https://github.com/komalrao1/bi0s/assets/147682987/ae9492f0-4971-4e84-8958-cbf9f9b65c7f)

[**b.** ***hacker rank***](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true)
![answer 13(a)](https://github.com/komalrao1/bi0s/assets/147682987/f4d4ba34-da8a-4380-9f21-8f057796bd7c)
![answer 13(b)](https://github.com/komalrao1/bi0s/assets/147682987/dd9847ba-33c5-415e-9015-87fe7a47b7d5)

**2.**
 ***Make a one line python program to find whether the given year is leap or not.***
 ![Screenshot from 2024-01-11 09-25-36](https://github.com/komalrao1/bi0s/assets/147682987/a932c3de-9ccf-48a1-81d1-49f8f36ca4d6)

**3.**
**1. Write a chat application using socket programming.**  
   ***Consider a small chat program with two processes, A and B:***  
   ***A: Establish a connection over sockets and send a message/data to the server side/receiver side.***  
   ***B: Receive the connection and send a message/response back.***  
   ***Feel free to use any library functions.***  
   ***The application should include the following security features:***  
   ***- Symmetric key encryption for confidentiality (You can use any algorithm).***  
   ***- SHA-512 for integrity.***  
   ***- HMAC for message authentication.***  

   ![answer 14](https://github.com/komalrao1/bi0s/assets/147682987/1e27c7d8-b4b4-4d30-a618-d1a3b1a4e1a4)
   ![answer 14](https://github.com/komalrao1/bi0s/assets/147682987/d1b49668-3d0a-4c28-8ea6-5e599a32434a)
   













