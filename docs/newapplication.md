## Create new application in RPAC

Go to folder `./AwsServerlessTemplate`, revise `NewAppTemplate` as your application (folder name and contents). Later, you can use this name in `resource.ini`.

Change your configurations in `resource.ini` and `application.ini`.
- resource.ini
    - application: Your application name, which is the **folder name** in `./AwsServerlessTemplate` or `./AzureServerlessTemplate`. 
    - reproduce_storage: The **S3 Bucket name**, which will store all reproduction historical files. You need to create your bucket **before** running RPAC. We recommend a name only with lowercase letters, numbers, and hyphens (-). The Bucket naming rules can be find in [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
 
- application.ini
    - experiment_docker: The **public docker image name** in DockerHub, formated in `<username>/<repository_name>`.
  
        If you provide Dockerfile, run the following commands at the folder of your docker file, such as docker/CloudRetrievalViaDask: 
        
            1. Log into the Docker public registry on your local machine: `docker login -u <Username> -p <Password>`.  
            2. Build the image: `docker build -t <username>/<repository_name>[:tagname] .`. For example: `docker build -t starlyxxx/dask-decision-tree-example:latest .`  
                If you have a Mac M1/M2 or Higher --> ARM chips use this command instead
                `docker build --platform linux/amd64 -t <username>/<repository_name>[:tagname] .` 
            3. Push your Docker image to Docker Hub: `docker push <username>/<repository_name>[:tagname]`. For example: `docker push starlyxxx/dask-decision-tree-example:latest`.  
            4. Then put your public docker image name into `application.ini`.  
    - data_address: The **S3 URI** of the data.
    - command: Command line to start docker-based execution analytics starting by `docker run` or `nvidia-docker run`. **Note: since the json format cannot convert correctly in RPAC, please using ` (back apostrophe) to replace the ' (apostrophe) symbol.** 
    - bootstrap: Command lines **before** you starting execution analytics. Like private s3 data download and unzip, program library install, and any other additional commands (mutiple commands can be chained by logical AND operator `&&`).

> Note: The serverless function provided by RPAC uses the print out contents of analytics execution as the `results.txt`. You may need advanced operations for mutiple outputs within your application. At this time, you need to develop your own serverless function, by updating `./AwsServerlessTemplate/NewAppTemplate/lambda` folder. More instructions and examples for serverless function development can be found in [link](https://github.com/serverless/examples).




--> Goto your newly created AwsserverlessTemplate folder
--> Goto `SampleEvent.json` , Update all the settings here
        1)`instancetype` (Select Instance Type)
        2)`instance_num` (Number of Instances deployed)
        3)`gpu_num` (Number of Gpus Deployed)
        4) Update all the other necessary settings 

--> Goto `deploy_config.json` Update all the required settings here as well.
        1)set `InstanceNum` Example :p3.8xlarge
        2)set `Ec2KeyName` Example: Rohan_west
        3)set `Ec2KeyPath`
        4)set `SubnetId`    
        5)set `VpcId`
        6)set `IamInstanceName`
        7)set `PythonRuntime`
        8)set `ImageId` (Search the required ami in ami catalog in aws and paste the ami ID)
        9)Set any other settings required.