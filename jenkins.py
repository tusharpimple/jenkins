import jenkins

server = jenkins.Jenkins('http://13.56.11.237:8080', username='Tushar', password='Rupesh@123')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['Tushar Pimple'], version))
