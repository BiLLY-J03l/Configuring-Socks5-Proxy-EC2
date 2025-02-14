# Configuring-Socks5-Proxy-EC2
This repo showcases the process of launching, configuring an EC2 instance as a SOCKS5 proxy

## 1- Login into your aws account and launch a new ubuntu instance

![image](https://github.com/user-attachments/assets/35d6edd2-f85d-42c2-bca2-2b96df173552)

## 2- Create a new key pair to login into the EC2 instance without a password, which is more secure. The key will be downloaded automatically

![image](https://github.com/user-attachments/assets/5c9dca43-2b07-45cd-9d04-610cc424c204)

## 3- Navigate to EC2 > Instances > Instances, and you will find the EC2 instance running

![image](https://github.com/user-attachments/assets/b657bad8-bf1d-4fa2-9b90-842c559087f5)

## 4- Launch our favorite ssh client, Putty and paste the EC2 public address

![image](https://github.com/user-attachments/assets/ab8b78fd-4aa9-4cfa-bd47-81f7b3116dce)

## 5- Navigate to Connection > SSH > AUTH > Credentials, and add the downloaded key there.

![image](https://github.com/user-attachments/assets/822cac77-51be-4b7c-8e6a-1afed1fdc44b)

## 6- Click Open

![image](https://github.com/user-attachments/assets/34835221-348a-46a4-a47e-a46050c433d4)
![image](https://github.com/user-attachments/assets/00853355-9e09-4eb2-bcc8-7c39e8d36422)
![image](https://github.com/user-attachments/assets/5354caef-3b99-4199-a872-ed15293daab2)

## 7- Update our instance

    sudo su
    apt update ; apt full-upgrade -y ; apt autoremove -y
    systemctl daemon-reload

-----------------------------------------------------------------------------------------

## Now we're ready to configure the EC2 instance as a SOCKS5 proxy.
## There are two methods.

### A) using SSH
### B) using Dante -> https://www.inet.no/dante/

------------------------------------------------------------------------------------------

## First Method : SSH

-Most of the work will be done on your local machine
> -D : Specifies a local “dynamic” application-level port
               forwarding.  This works by allocating a socket to listen
               to port on the local side, optionally bound to the
               specified bind_address.  Whenever a connection is made to
               this port, the connection is forwarded over the secure
               channel, and the application protocol is then used to
               determine where to connect to from the remote machine.
               Currently the SOCKS4 and SOCKS5 protocols are supported,
               and ssh will act as a SOCKS server.  Only root can forward
               privileged ports.  Dynamic port forwardings can also be
               specified in the configuration file.

### using the command 
    ssh -i /path/to/your/key ubuntu@EC2-instance-ip -D 1080 -f
-f: Requests ssh to go to background just before command execution.
-i: specefies the private key path
-D 1080: means you're creating a SOCKS proxy on localhost:1080

-First, I will use puttygen to convert the .ppk file to .pem file to use it with openssh

![image](https://github.com/user-attachments/assets/b63df90e-df78-4695-b7ea-edf0f4a4b3bb)
1-Click on file > load private key > choose the file

2-Click on conversions > Export OpenSSH key
![image](https://github.com/user-attachments/assets/2400cded-6e3a-43a6-96c7-9f80a4dcb39b)




note: if you want to disconnect from that socks5 server

        ps aux | grep ssh
        kill -9 <PID>
-9: This is the option that specifies the signal to send. -9 represents SIGKILL, a signal that forcefully stops the process.

### adding config to ~/.ssh/config file

    Host your-ec2-alias
      HostName your-ec2-public-ip
      User ec2-user
      IdentityFile /path/to/your/private-key.pem
      DynamicForward 1080


------------------------------------------------------------------------------------------

## Second Method : Dante
