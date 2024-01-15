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
     --------------------------------------------------------------------------------------------------------------------------------------------------------   
1.    
* **pwd** command will return the path of the current working directory.    
* **ls** command will return the unhidden files.    
* **ls -al** command will return all the files and folders in the current working directory including hidden files and folders     
2.    
* **mkdir <dirname>** will create a new folder, where **'dirname'** is the irectory name that we want to create.   
* **cd <path>** will move our current working directory to the path ***(in path base name cant be a file)***.   
* **touch <filename>** will create a file and **<filename>** will be the name of creating file.   
* **file <filename>** will give us more information of the the file.If the file doesnot exist it will create the file and redirect the content into it   
* **echo "nessage" > <filename>** will redirect the message into the file.   
* **cat <filename>** will open the contents of the file.   
3.   
* **cat > <filename>** will open the file for make changes.If the file already exists it clears all the contents of the file and opens the file in editing mode    
* **cat <filename>** will open the contents of the file     
* **tac <filename>** will open the contents of the file with lines reversed.     
4.   
* **cat <file1> <file2> > <file3>** will redirect the contents of file1 and file2 into file3     
* **cat <filename>** will open the contents of the file      
5.      
* **mkdir <dir1> <dir2>** will create two directories in the current working directory   
* **mkdir <dirname>** will create a new folder, where **'dirname'** is the irectory name that we want to create.   
* **cp -r <source -dir> <dest -dir>** will copy the source directory into destination directory. Here we -r(recursive) because we are copying directories . For coping of files recursive mode is not necessary   
* **rm -rf <dir -path>** will delete the folder in the path if basename is folder. If basename is a file it removes the file   
* **cp  f<source -filepath> <destination file/folder path>** will copy the file into the file or folder in the basename of destination path.    
6.   
* **cd <path>** will make the current working directory as the path    
* **mv <source file/folder> <destination file/folder>** will rename the filename in the source as filename in the destination. If the destination is a folder then the file from current working directory will be moved to destination directory   
7.    
* **cd <path>** will make the path as current working directory    
* **touch <path>** will create a file in the path and basename in path must be the filename of which we are creating.    
* **realpath <path>** will return the absolute path of the given path.    
8.     
* **cd <path>** will make the current working directory as the path    
* **man <command>** will return the manual page of the command and **man <command> > <filename>** will redirect the contents of manualpage into the file    
  


**9.**   
***( a.) Go to directory a and remove the directory b with a single command***  
***( b.) Remove the files starting with the word “file” with a single command***     

![answer2](https://github.com/komalrao1/bi0s/assets/147682987/662264e3-7980-4b53-bf88-3c5dd1d3c16c)   
    --------------------------------------------------------------------------------------------------------------------------------------------------------    
* **rm -rf <dir -path>** will delete the folder in the path if basename is folder. If basename is a file it removes the file   
* **rm <filename>** will delete the file from the current working directory   

**10.**   
***( a.) Go to https://blog.bi0s.in/  and download the logo.png image using wget***    
***(b.) Do the same with python script (Hint : request library)***   
***(c.) Also, display the metadata of the png.***    
![answer3](https://github.com/komalrao1/bi0s/assets/147682987/55d569a8-a270-4aac-80ab-ffbd6a9ef397)   
    --------------------------------------------------------------------------------------------------------------------------------------------------------    
10.                                                 
* ***a.*** **wget <url>** will download the contents from the given url. The url must contain the downloading link    
* ***b.***    
  - open a file in binary writing mode.    
  - The **requests** module will get the response from the web browser with requests.get() function    
  - we need to use **iter_content(chunksize)** method to add the response into the file. **chunksize** can be any value Here iam using 100000 .That means for each 100000 bytes the content will be iterated.If the data is more than 100000 bytes we need to open the file in append mode so that next iterated value can be appended into the file.    
  - Then I have written the chunks received from **iter_content()** into file    
* ***c.***    
  - I have imported Image from **PIL** ***(pillow)*** module.    
  - **Image.open('image')** will open the image and we can use the **info()** method to **image** object to get metadata      

**11.**    
***( a.) Use traceroute on google.com and find list of the IP addresses and hostnames between you and  google.com***    
***( b.) Find  Subdomains,ip addresses of google.com using nslookup command***     
![answer4](https://github.com/komalrao1/bi0s/assets/147682987/1f3b168d-8e2d-4070-9fac-4be231ea2a2c)     
    --------------------------------------------------------------------------------------------------------------------------------------------------------     
11.    
* **a.** **traceroute <domainname>** will return in detail about the each hop present between us and the domain.if it cound find details about hop then it return stars.    
* **b.** **nslookup <domainname>** is used for getting information from the DNS server. **-type=ns** will ouput the nameservers which are associated with the server    
 

**12**    
***Start a web server on port 8080 with python command*(In any directory and access the files in web browser )**    
![answer5](https://github.com/komalrao1/bi0s/assets/147682987/6056d091-0c8f-4e80-a427-e6f2c20477a2)    
![answer6](https://github.com/komalrao1/bi0s/assets/147682987/eae47a0c-ac40-44bb-8a1b-f70f9fb84e5c)     
* **python 3 — python -m http.server <port>** will open a simple http server to serve directories and files .The **port** can be any number greater than **1024**    
**13**    
***( a.) Learn about nmap and use that scanner to scan your own machine***    
***( b.) Go to https://tryhackme.com/room/furthernmap and get ip address and Scan the ip address with**(-sS,-sV,-A)**in your terminal include all ports (Hint : start machine )***    
![answer7](https://github.com/komalrao1/bi0s/assets/147682987/f023ca21-9c27-4471-a153-0853f7256fa3)   
![answer8](https://github.com/komalrao1/bi0s/assets/147682987/70e3fd7c-702d-4965-b8a4-a2c39c69cd70)   
![answer9](https://github.com/komalrao1/bi0s/assets/147682987/a683bac3-e884-4dca-bc0c-dea1839f6ccc)   
* **Nmap** is a powerful tool which gives more information about the target    
* **-sS** option is used for **STEALTH** ***(Half Open)*** scanning. It is used to bypass intrusion detection system. It decides whether the target is up or down without completing threeway handshake   
* **-sV** option is used to get version info of the active services     
* **-A** option is used to get info about **OPERATING SYSTEM,SERVICE and SCRIPTS**   
**14.**
***( a.) Create a chat application using nc on your local machine with one terminal as server and other as the client***   
![answer10(a)](https://github.com/komalrao1/bi0s/assets/147682987/ab117e55-235a-4a49-83f1-6340c688fecb)   

![answer10](https://github.com/komalrao1/bi0s/assets/147682987/ee6d671c-9523-4a7f-a4de-f8bbd8a431af)   
    --------------------------------------------------------------------------------------------------------------------------------------------------------    
**14.**    
* **nc(Netcat)** is used for reading and writing data between teo computer networks    
* **a.**    
  - I used awk with -W interactive option because it helps to add username evertime we get a message     
  - for the communication to occur between two devices ,One device must be in listening mode and other device connect to the ip and port of the listening device    
  - the **-l** option makes a device for listeing and **'-p'** option specifies the port for listeing     
  - The second should to connecting to the listening device using the ipaddress and port of listening device     

***( b.) Transfer a file from server to client (save that file with another name) and display the file.***    
![Screenshot from 2024-01-10 23-05-38](https://github.com/komalrao1/bi0s/assets/147682987/d891c21f-37bd-4384-a56c-75116f7063f8)     

![answer11](https://github.com/komalrao1/bi0s/assets/147682987/cd42f5b7-0cf3-444a-be59-62555a57e38d)     
     --------------------------------------------------------------------------------------------------------------------------------------------------------         
* **b.**     
  -Here Device1 will be in listen mode by opening a file which has to be shared     
  -And the device two will connect to device1 and while connecting it will redirect the shared file to its current working directory    


# **CODING CHALLENGES**      
**1**    
[**a.** ***h acker rank***](https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true)   
![answer 12(a)](https://github.com/komalrao1/bi0s/assets/147682987/7885acf3-d4cd-4774-9f82-6a3e434653d2)  
     --------------------------------------------------------------------------------------------------------------------------------------------------------      
* **a.** I have solved this using the for loop       
![answer 12(b)](https://github.com/komalrao1/bi0s/assets/147682987/ae9492f0-4971-4e84-8958-cbf9f9b65c7f)   

[**b.** ***hacker rank***](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true)   
![answer 13(a)](https://github.com/komalrao1/bi0s/assets/147682987/f4d4ba34-da8a-4380-9f21-8f057796bd7c)    
    --------------------------------------------------------------------------------------------------------------------------------------------------------     
* **b.** I have added two values using **'+'** operator ,subtracted two values using **'-'** operator and multiplied two number using **' * '** operator.I have used escape character to print in newlines **(\n)**   
![answer 13(b)](https://github.com/komalrao1/bi0s/assets/147682987/dd9847ba-33c5-415e-9015-87fe7a47b7d5)    

**2.**    
 ***Make a one line python program to find whether the given year is leap or not.***    
 ![Screenshot from 2024-01-11 09-25-36](https://github.com/komalrao1/bi0s/assets/147682987/a932c3de-9ccf-48a1-81d1-49f8f36ca4d6)    
    --------------------------------------------------------------------------------------------------------------------------------------------------------        
 * **2** I have written using single line **if else** statements and i seperated statements using **;**    

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
    --------------------------------------------------------------------------------------------------------------------------------------------------------          

* **3**    
  - I have written chat application using socket programming    
  - #### SERVER SIDE ####    
    -i created a socket object using ipv4 and tcp and binded it to a my ip adress and a port .Then i have kept the server in listening mode for one device    
    - accept method will a tuple of socket and address of the client.Then i used **recv()** method to receive messages from client.     
    - I used **send()** method to share message from server side. When i receive the message ***close*** from the **client** the connection to the client will be closed     
    - during the sending and receiving process i made encryption using **PyCryptodome** module .I have imported **HMAC,SHA,pad,unpad,AES** .The below is the process of encryption and decryyption and hmac    
    - ##### DURING RECEVING #####    
      -The server will receive a ***encrypted message*** and ***HMAC digest***     
       -The message is then sent to hmac function .Once the hmac function generated digest matches the received digest from the client, Then the message will be auhenticated and willbe sent for decryption     
       -If the two digests doesnot match the connection between client and server ends    
    - ##### DURING SENDING #####     
      -the server will generate a hmac digest and encrptys the message.     
      -After the both processes done the message will be sent to the client     
  - #### CLIENT SIDE ####     
    - I created a socket object using ipv4 and tcp and used **connect()** method to connect to the server IP and port.     
    - Then i have sent data from client to server using **send()** method and received data from server using **recv()** method     
    - ##### DURING SENDING ######      
      -the client will generate a hmac digest and encrptys the message.     
      -After the both processes done the encryptedmessage and digest will be sent to the client.     
    - ##### DURING RECEIVING #####     
      -The client will receive a ***encrypted message*** and ***HMAC digest***      
      -The message is then sent to hmac function .Once the hmac function generated digest matches the received digest from the server, Then the message will be auhenticated and will be sent for decryption     
      -If the two digests doesnot match the connection between client and server ends     


    -----------------------------------------------------------------------**THE END**-----------------------------------------------------------------------    

 









