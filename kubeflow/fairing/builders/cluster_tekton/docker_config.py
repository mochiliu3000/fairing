# Create a docker creds configmap. Only need once for one namespace!
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from os.path import expanduser

namespace = 'tk'
docker_cm_name = 'docker-config'

config.load_kube_config()
api_instance = client.CoreV1Api()

with open(expanduser('./config.json')) as f:
    contents = f.read()

configmap_body = client.V1ConfigMap(
    api_version='v1', kind='ConfigMap',
    metadata=client.V1ObjectMeta(
        name=docker_cm_name, namespace=namespace),
    data={'config.json': contents})

try:
    api_instance.create_namespaced_config_map(namespace, configmap_body)
except ApiException as e:
    print("The ConfigMap docker-config already exists in namespace %s \n" % namespace)
