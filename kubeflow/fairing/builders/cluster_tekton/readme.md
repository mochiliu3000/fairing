1. Install Tekton v0.10.x
https://github.com/tektoncd/pipeline/blob/master/docs/install.md#installing-tekton-pipelines-on-kubernetes
2. Create local PV to store build context
`$ kubectl apply -f pv.yaml`
3. Create pipelineresource of builtImage and remote_kubeconfig
`$ kubectl apply -f yamls/config/pipelineresource.template.yaml`
4. Create build-push tekton task
`$ kubectl apply -f yamls/task-build-push.yaml`
5. Create deploy tekton task
`$ kubectl apply -f yamls/task-job-deploy.yaml`
6. Create taskrun for testing
`$ kubectl apply -f yamls/test/taskrun.yaml`
7. To get taskrun logs
`$ kubectl logs -f fairing-build-deploy-pipeline-0-fairing-build-push-xxxxx--xxxxx -c step-fairing-build-push`
`$ kubectl logs -f fairing-build-deploy-pipeline-0-fairing-job-deploy-xxxxx--xxxxx -c step-fairing-job-deploy`
8. To clean-up tasks
`$ kubectl delete taskrun fairing-build-push`
`$ kubectl delete task fairing-build-push`
`$ kubectl delete taskrun fairing-job-deploy`
`$ kubectl delete task fairing-job-deploy`
9. Create pipeline
`$ kubectl apply -f yamls/pipeline-build-deploy.yaml`
10. Create and pipelinerun for testing
`$ kubectl apply -f yamls/test/pipelinerun.yaml`
11. To clean-up pipeline
`$ kubectl delete pipeline fairing-build-deploy-pipeline`
`$ kubectl delete pipelinerun fairing-build-deploy-pipeline-0`
12. Generate pipelinerun with kustomization and template
`$ kustomize build yamls/ | kubectl apply -f -`
13. Things need to set
* container args in fairing-job-template.yaml
* params in pipelinerun-template.yaml