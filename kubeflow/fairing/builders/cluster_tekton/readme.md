# Simple Tekton cluster builder example
Also refer to https://github.com/kubeflow/testing/tree/master/apps-cd

## Prepare
* Install Tekton v0.10.x
  * https://github.com/tektoncd/pipeline/blob/master/docs/install.md#installing-tekton-pipelines-on-kubernetes
* Create local PV to store build context
  * `kubectl apply -f pv.yaml`
* Configure in advance
  * Container arguments in `yamls/config/fairing-job-template.yaml`
  * Parameters in `yamls/config/pipelinerun-template.yaml`
  * PipelineResource Parameters in `yamls/config/pipelineresource-template.yaml`

## Run
* Generate and apply pipelinerun with kustomization and template
  * `kustomize build yamls/ | kubectl apply -f -`

---

## Test and Clean up
* Create pipelineresource of builtImage and remote_kubeconfig
  * `kubectl apply -f yamls/config/pipelineresource.template.yaml`
* Create build-push tekton task
  * `kubectl apply -f yamls/task-build-push.yaml`
* Create deploy tekton task
  * `kubectl apply -f yamls/task-job-deploy.yaml`
* Create taskrun for testing
  * `kubectl apply -f yamls/test/taskrun.yaml`
* To get taskrun logs
  * `kubectl logs -f fairing-build-deploy-pipeline-0-fairing-build-push-xxxxx--xxxxx -c step-fairing-build-push`
  * `kubectl logs -f fairing-build-deploy-pipeline-0-fairing-job-deploy-xxxxx--xxxxx -c step-fairing-job-deploy`
* To clean-up tasks
  * `kubectl delete taskrun fairing-build-push`
  * `kubectl delete task fairing-build-push`
  * `kubectl delete taskrun fairing-job-deploy`
  * `kubectl delete task fairing-job-deploy`
* Create pipeline
  * `kubectl apply -f yamls/pipeline-build-deploy.yaml`
* Create and pipelinerun for testing
  * `kubectl apply -f yamls/test/pipelinerun.yaml`
* To clean up pipeline
  * `kubectl delete pipeline fairing-build-deploy-pipeline`
  * `kubectl delete pipelinerun fairing-build-deploy-pipeline-0`
