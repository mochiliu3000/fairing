1. Install Tekton v0.10.x
https://github.com/tektoncd/pipeline/blob/master/docs/install.md#installing-tekton-pipelines-on-kubernetes
2. Create local PV to store build context
`kubectl apply -f pv.yaml`
3. Create configMap of docker config
`python docker_config.py`
4. Create pipelineResource of builtImage and remote_kubeconfig
`kubectl apply -f pipeline-resource.yaml`
5. Create build-push tekton task and taskrun
`kubectl apply -f task-build-push.yaml`
6. Create deploy tekton task and taskrun
`kubectl apply -f task-job-deploy.yaml`
7. To get task log
`
oc logs -f fairing-build-push-pod-xxxxx -c step-fairing-build-push
oc logs -f fairing-job-deploy-pod-xxxxx -c step-fairing-job-deploy
`
8. To clean-up tasks
`
kubectl delete taskrun fairing-build-push
kubectl delete task fairing-build-push

kubectl delete taskrun fairing-job-deploy
kubectl delete task fairing-job-deploy
`