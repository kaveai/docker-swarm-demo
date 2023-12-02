# Docker Swarm Örneği

Bu örnekte docker-swarm kullanarak Front-End Streamlit, Backend FastAPI olan, kullanıcıdan 2 girdi alıp back-end'de toplama yapıp sonucu dönen bir örnek yapacağız. 

# Docker Swarm Komutları

## AWS üzerinde Canlıya Alma
- AWS üzerinde uygulamanın canlıya alınabilmesi için öncelikle [AWS EC2](https://us-east-1.console.aws.amazon.com/ec2/) servisi üzerinden 1GB RAM 1VCPU'ya sahip bir makine açılması gerekmektedir. Makine tipi olarak ücretsiz olduğu için t2.micro tercih edilebilir. 
- Ayarlar yapılırken security group ayarında bütün portlar(önerilmez veya streamlit uygulamasının yayınlanacağı porta erişim verilmesi gerekmektedir. 
- Makine açıldıktan sonra makineye ssh veya ec2-serial-console kullanılarak erişilebilir.
- Amazon makineleri yüksek ihtimalle python3 yüklü olarak gelmektedir. Eğer gelmediyse internet üzerinden Debian/Linux makinelere nasıl python yükleneceğine bakabilirsiniz.
- Makineye gerekli kodların çekilebilmesi için git yüklenir. 


## Node Ön Koşulları
- İstediğiniz kadar node açabilirsiniz. 
- Node'larda şu portların açık olması gerekiyor.
	- 2376, 2377, 7946, 4789, 22

## Node'lara Gerekli Yüklemeler
``` bash
#!/bin/bash
sudo yum update
sudo yum -y install docker
service docker start
usermod -a -G docker ec2-user
chkconfig docker on

sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Docker-Swarm Komutları
```
docker swarm init --advertise-addr <private ip of master node> 
```
Bu şekilde master node'u oluşturmuş oluyorsunuz. Bunun sonucunda size bir token veriliyor. 

```
docker swarm join --token <TOKEN> <private ip of master node> 
```
Bu şekilde worker-node'ların girişini sağlıyorsunuz. 

```
docker stack deploy -c docker-compose.yml <uygulama-adi>
```

