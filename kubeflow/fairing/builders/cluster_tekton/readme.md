1. Install Tekton v0.10.x
https://github.com/tektoncd/pipeline/blob/master/docs/install.md#installing-tekton-pipelines-on-kubernetes
2. Create local PV
`kubectl apply -f pv.yaml`
3. Create configMap of docker config
`python docker_config.py`
4. Create tekton task and taskrun
`kubectl apply -f task-build-push.yaml`