# GitLab 업그레이드 방법





##  1. Version Naming Convention

>  <u>(Major).(Minor).(Patch)</u> - ex:10.7.3



## 2. Package Download Locations

###  - Red Hat Enterprise Linux RHEL

```
sudo yum install gitlab-ce-10.0.1-ce.0.el7.x86_64
```



## 3. 백업

백업 및 복원 작업 `tar`은 후드 아래에서 아카이브를 생성하고 추출하는 데 사용 합니다. `tar`시스템에 버전 1.30 이상이 있는지 확인하십시오 . 버전을 확인하려면 다음을 실행하십시오.

``` shell
tar --version
```



Omnibus 패키지와 함께 GitLab을 설치 한 경우 이명령을 사용하십시오

``` sudo gitlab-backup create

sudo gitlab-backup create
```



> **참고** GitLab 12.1 및 이전 버전에서는을 사용하십시오 `gitlab-rake gitlab:backup:create`.





``` shell
## gitlab backup

$ cd /home/git/gitlab
$ sudo -u git -H bundle exec rake RAILS_ENV=production gitlab:backup:create

Dumping database ...
done
Dumping repositories ...
 * root/ini-and-script ... [SKIPPED]
 * lesstif/util-script ... [DONE]
 * lesstif/util-script.wiki ...  [SKIPPED]
done
Dumping uploads ...
done
Creating backup archive: 1387289435_gitlab_backup.tar ... done
Deleting tmp directories ... done
Deleting old backups ... skipping
```

생성된 백업 파일은 1387289435_gitlab_backup.tar 
cron과 연계하면 자동으로 백업할 수 있다.

- 백업 위치

- /var/opt/gitlab/backups/

  





## 4. 복원

먼저 2개의 서비스를 중지 시키고 상태를 확인

``` shell
sudo gitlab-ctl stop unicorn
sudo gitlab-ctl stop sidekiq
# Verify
sudo gitlab-ctl status
```

백업된 파일을 기본 Backup 폴더로 위치

```
sudo cp 1393513186_2014_02_27_gitlab_backup.tar /var/opt/gitlab/backups/
```

Restore 명령

``` sudo gitlab-rake gitlab:backup:restore BACKUP=1393513186_2014_02_27
sudo gitlab-rake gitlab:backup:restore BACKUP=1393513186_2014_02_27
```







```shell
$ cd /home/git/gitlab
$ sudo -u git -H bundle exec rake RAILS_ENV=production gitlab:backup:restore BACUP=1387289435
  
Unpacking backup ... done
Restoring database ...
Restoring MySQL database gitlabhq_production ... [DONE]
done
Restoring repositories ...
springwebdevel/spring-web ... [DONE]
lesstif/spring-web ... [DONE]
Put GitLab hooks in repositories dirs [DONE]
done
Restoring uploads ...
done
This will rebuild an authorized_keys file.
You will lose any data stored in authorized_keys file.
Do you want to continue (yes/no)? yes
..Deleting tmp directories ... done
```



## 5. 릴리즈 버전 업그레이드 단계별 진행

**릴리즈 정보 참고**

```https://about.gitlab.com/blog/archives.html
https://about.gitlab.com/blog/archives.html
```

[GitLab Security Release: 11.1.2, 11.0.5, and 10.8.7](https://about.gitlab.com/2018/07/26/security-release-gitlab-11-dot-1-dot-2-released/) 



**2019.09.19 기준 쇼핑/도서/공통 GitLab ver 10.0.1 사용 중**

> 업그레이드 계획 : 10.0.1 → 12.1.0 (5번 반복 작업 예상)
>
> 추천하는 업그레이드 경로 : 

```
10.0.1 (현재 릴리즈 버전) →  10.8.7 (10.x major 시리즈 마지막 릴리즈)
  → 11.0.0 (11.x major 시리즈 처음 릴리즈) → 11.10.8 (11.x major 시리즈 마지막 릴리즈)
    → 12.0.0 (12.x major 시리즈 처음 릴리즈) → 12.1.0 (타켓 버전) 
```



> **중요 :  5번 업그레이드 진행 예상**

``` shell
# Remove former Go installation folder
sudo rm -rf /usr/local/go

curl --remote-name --progress https://dl.google.com/go/go1.11.10.linux-amd64.tar.gz
echo 'aefaa228b68641e266d1f23f1d95dba33f17552ba132878b65bb798ffa37e6d0  go1.11.10.linux-amd64.tar.gz' | shasum -a256 -c - && \
  sudo tar -C /usr/local -xzf go1.11.10.linux-amd64.tar.gz
sudo ln -sf /usr/local/go/bin/{go,godoc,gofmt} /usr/local/bin/
rm go1.11.10.linux-amd64.tar.gz
```



### [참고] GitLab 내부 업그레이드 되면서 변경되는 패키지

> Rsync 설치

> GitLab 11.4이상 Go 1.10.x 이상만 지원하며, Go 1.9.x에 대한 지원은 중단되었습니다. 필요한 경우 설치하여 업그레이드하십시오.
>
> 사용중인 버전을 확인할 수 있습니다. `go version`



> GitLab 12.2부터는 Ruby 2.6 이상 만 지원하고 Ruby 2.5에 대한 지원은 중단했습니다. 필요한 경우 업그레이드하십시오. 
>
> 사용중인 버전 확인 `ruby -v`



> GitLab 11.8부터는 노드 8 이상 만 지원하고 Node  6에 대한 지원은 중단했습니다. 필요한 경우 업그레이드하십시오.
>
> `node -v`



> GitLab 11.11 이상은 Git 2.21.x 이상 만 [지원하며 이전 버전에 대한 지원은 중단되었습니다](https://gitlab.com/gitlab-org/gitlab-foss/issues/54255) . 필요한 경우 설치를 업그레이드하십시오.



## 6. 작업시간



1. 백업 시간
2. 복원 시간
3. 업그레이드 시간
4. 검증 시간



| 항목          | 시간 | 명령어 | 비고 |
| ------------- | ---- | ------ | ---- |
| 백업          |      |        |      |
| 복원          |      |        |      |
| 업그레이드 #1 |      |        |      |
| 업그레이드 #2 |      |        |      |
| 업그레이드 #3 |      |        |      |
| 업그레이드 #4 |      |        |      |
| 업그레이드 #5 |      |        |      |
| 검증          |      |        |      |





### 참고

[Backing up and restoring GitLab](https://docs.gitlab.com/ee/raketasks/backup_restore.html#restore-prerequisites)





