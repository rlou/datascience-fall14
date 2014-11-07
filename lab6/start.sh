#!/bin/bash
source $HOME/.profile
hdfs namenode -format CID-09bae78d-49c6-43ef-a2e5-6a8198a1ba08

hdfs namenode &  
hdfs datanode & 
yarn resourcemanager & 
yarn nodemanager & 
mapred historyserver & 
