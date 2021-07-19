import os
from git import Repo
# os.system("python3.8 --version");
project_dir = os.path.dirname(os.path.abspath(__file__))
full_local_path = "/mnt/d/python/repo/wager-detail"
remote = f"git@gitlab.higgstar.org:brand/wager-detail.git"
ssh_executable = os.path.join(project_dir, 'my_ssh_executable.sh')
Repo.clone_from(remote, full_local_path)
os.system("dotnet restore repo/wager-detail/All.sln -s http://proget.higgstar.org/nuget/dev/");
os.system("dotnet build repo/wager-detail/All.sln  -c Release");
