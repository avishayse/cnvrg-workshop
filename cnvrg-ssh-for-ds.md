**Serivce-account**
```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ds-sa-group
  namespace: cnvrg
  ```
**Role**

```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: cnvrg
  name: ds-role
rules:
- apiGroups: [""]
  resources: ["pods", "pods/portforward", "pods/exec" , "pods/log"]
  verbs: ["get", "list", "watch", "describe", "update", "patch", "create"]
```

**RoleBinding**

```
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ds-rolebinding
  namespace: cnvrg
subjects:
- kind: ServiceAccount
  name: ds-sa-group
  namespace: cnvrg
roleRef:
  kind: Role
  name: ds-role
  apiGroup: rbac.authorization.k8s.io
```

**Create kubeconfig**

***Fetch the name of the secrets used by the service account***

This can be found by running the following command:

 ``` kubectl describe serviceAccounts ds-sa-group ```
  
***output***
```
Name:                ds-sa-group
Namespace:           cnvrg
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
**Mountable secrets:  ds-sa-group-token-nwkpp**
Tokens:              ds-sa-group-token-nwkpp
Events:              <none>
```

Note down the ```Mountable secrets``` information which has the name of the secret that holds the token



**Fetch the token from the secret**

 Using the Mountable secrets value, you can get the token used by the service account. Run the following command to extract this information:

``` kubectl describe secrets ds-sa-group-token-nwkpp ```

***output***

```
Name:         ds-sa-group-token-nwkpp
Namespace:    cnvrg
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: ds-sa-group
              kubernetes.io/service-account.uid: 4b20-91fa-4b4eec5b5f0a

Type:  kubernetes.io/service-account-token

Data
====
token:      
ca.crt:     1765 bytes
namespace:  5 bytes
```
This will output the token information that looks something like above. Note down the ``token`` value


***Get the certificate info for the cluster***

Every cluster has a certificate that clients can use to encryt traffic. Fetch the certificate and write to a file by running this command. In this case, we are using a file name cluster-cert.txt

```
kubectl config view --flatten --minify > cluster-cert.txt
cat cluster-cert.txt
```
**output**
```
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: <token>
  name: aks-cicd-7687
contexts:
- context:
    cluster: aks-aks-cicd:443
    namespace: cnvrg
    user: cnvrg-app
  name: aks-aks-cicd:443
current-context: aks-cicd-7687
kind: Config
preferences: {}
users:
- name: cnvrg-app
  user:
    token: 
```
    
Copy two pieces of information from here ```certificate-authority-data``` and ```server```

****Create a kubeconfig file

From the steps above, you should have the following pieces of information

* token
* certificate-authority-data
* server

Create a file called sa-config and paste this content on to it
```
apiVersion: v1
kind: Config
users:
- name: svcs-acct-dply
  user:
    token:** <replace this with token info>**
clusters:
- cluster:
    certificate-authority-data: **<replace this with certificate-authority-data info>**
    server: <replace this with server info>
  name: self-hosted-cluster
contexts:
- context:
    cluster: self-hosted-cluster
    user: svcs-acct-dply
  name: svcs-acct-context
current-context: svcs-acct-context
```
  
Replace the placeholder above with the information gathered so far

* replace the token
* replace the certificate-authority-data
* replace the server


**Copy the file to $HOME/.kube/**

If you want your client to use this context, copy sa-config to ```$HOME/.kube``` and you can configure kubectl to use the context.

``` kubectl config --kubeconfig=$HOME/.kube/sa-config set-context svcs-acct-context ```

**CNVRG CLI**
make sure you have CNVRG client installed
if not, you can find it here, https://app.cnvrg.io/docs/cli/install.html

Next grab the relevant workspace-id, got to workspace and open the relevnat instance(you can find it on the uri address)

![image](https://user-images.githubusercontent.com/88431066/137325391-41ac26b8-fb45-4d29-bbb7-0d2dd9d57772.png)

Run the CLI:

``` cnvrg ssh start zifz2rsqpsiqjjz2vsla ```

And then in another window run:

``` ssh root@127.0.0.1 -p 2222 ```
