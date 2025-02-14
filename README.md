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

-All of the work will be done on your local machine
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
    ssh -i /path/to/your/key ubuntu@EC2-instance-ip -D 1080 -f -N
-i: specefies the private key path

-D 1080: means you're creating a SOCKS proxy on localhost:1080

-f: Requests ssh to go to background just before command execution.

-N: Do not execute a remote command. This is useful for just forwarding ports (protocol version 2 only).


-First, I will use puttygen to convert the .ppk file to .pem file to use it with openssh

![image](https://github.com/user-attachments/assets/b63df90e-df78-4695-b7ea-edf0f4a4b3bb)

1-Click on file > load private key > choose the file

2-Click on conversions > Export OpenSSH key

![image](https://github.com/user-attachments/assets/2400cded-6e3a-43a6-96c7-9f80a4dcb39b)

3-command execution

![image](https://github.com/user-attachments/assets/4601152e-1be6-4828-ade7-15533fdc2aee)

4-Verify that the connection is established with:
        
    netstat -antp | grep 1080

![image](https://github.com/user-attachments/assets/c11fb914-f11e-480c-b972-88a14641e1e6)

5-configure proxychains4 to forward the traffic through the SOCKS5 proxy:

    apt install proxychains4
    vim /etc/proxychains4.conf
    
![image](https://github.com/user-attachments/assets/b204a9ae-d595-4290-a280-d8b1453204d6)

6-I wrote a python3 script to get my public IP:

![image](https://github.com/user-attachments/assets/e4a19b60-9047-4b4a-8ded-b57c9e6ecbd2)

**IT WORKS**

7- You can use FoxyProxy as well
![image](https://github.com/user-attachments/assets/66e26d1e-bb9d-46f5-ac0b-c6f840be4991)
![image](https://github.com/user-attachments/assets/5769a109-71a5-48f5-9fb1-c494985ad137)


note: if you want to disconnect from that socks5 server

        ps aux | grep ssh
        kill <PID>
-9: This is the option that specifies the signal to send. -9 represents SIGKILL, a signal that forcefully stops the process.

-Disconneting execution:
![image](https://github.com/user-attachments/assets/30b04eb5-a6d3-4e96-9ca5-a344cda13da7)


### (another method) adding config to ~/.ssh/config file

    Host your-ec2-alias
      HostName your-ec2-public-ip
      User ec2-user
      IdentityFile /path/to/your/private-key.pem
      DynamicForward 1080
     
1- Configure the .ssh/config file

![image](https://github.com/user-attachments/assets/7a117bec-7151-413b-a4f6-bc3aab8f22f6)

2- Use the alias to connect

    ssh -f -N server1_proxy
    
![image](https://github.com/user-attachments/assets/a5df076c-fe37-47ba-b16b-240d3580305f)

![image](https://github.com/user-attachments/assets/a295d3e1-bba3-49d3-bdb7-16ddfc12f973)


------------------------------------------------------------------------------------------

## Second Method : Dante

-Most of the work will be done on the EC2 instance

    apt install dante-server
    systemctl daemon-reload

![image](https://github.com/user-attachments/assets/6ba78412-eda9-4a34-9e97-cb307bd133a2)

1- Configure the /etc/danted.conf file

    vim /etc/danted.conf

![image](https://github.com/user-attachments/assets/b1691b05-6ae2-400c-bf07-8f31d65752e5)
![image](https://github.com/user-attachments/assets/f854e3e8-6698-4010-ad1f-bcf135a598ed)

2- Restart the service

    systemctl restart danted
    
![image](https://github.com/user-attachments/assets/3d27455f-cf46-4d3b-823c-927c55033de1)


3- add the server to foxyproxy settings and navigate to dnsleaktest.com

-we will notice that it won't work.

-Why is that? Because the EC2 instance has a strict firewall by default.

-Let's change that

4- Navigate to the EC2 instances and open the "Security" tab:

![image](https://github.com/user-attachments/assets/1a693e4c-f083-467e-8dcd-600f973b50da)

5- Save the changes and try again:

![image](https://github.com/user-attachments/assets/b94d4e12-a2d6-46d6-b148-2125e0160e7d)

**IT WORKS**

6- Using proxychains4:

    vim /etc/proxychains4.conf
    proxychains -q /home/caretaker/Desktop/pub.py

![image](https://github.com/user-attachments/assets/0e5d397a-9568-4cff-b275-02402ece2332)

![image](https://github.com/user-attachments/assets/68fa9a1b-3ccc-4c82-9c70-b52ecd8706d4)

**IT WORKS**
