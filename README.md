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

-----------------------------------------------------------------------------------------

## Now we're ready to configure the EC2 instance as a SOCKS5 proxy.
## There are two methods.

### A) using SSH
### B) using DANTE
