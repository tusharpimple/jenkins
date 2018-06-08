import requests

def create_new_jenkins_job(http://13.56.11.237:8080, 8080, firstjob, tpimple, Rupesh@123):
url     = '{0}:{1}/createItem?name={2}'.format(j_url, j_port, new_job_name)
auth    = (j_user, j_pass)
payload = '<project><builders/><publishers/><buildWrappers/></project>'
r = requests.post(url, data=payload, auth=auth, headers=headers)
return r.status_code

"""
	Create a new jenkins job

	:param j_url: 13.56.11.237
	:param j_port: 8080
	:param new_job_name: firstjob
	:param j_user: tpimple
	:param j_pass: Rupesh@123
	:return:
	"""
