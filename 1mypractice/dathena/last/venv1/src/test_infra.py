def test_user_dathena(host):
    """Check that the user dathena is in the host"""
    assert host.ansible("user", "name=dathena state=present")

def test_user_dathena_pw(host):
    """Check that the user dathena has a password set"""
    with host.sudo():   
        assert (len(host.user("dathena").password)>10)

def test_pkg_vim(host):
    """Check that the vim package is available on the host"""
    cmd = host.run("vim --version")
    assert cmd.succeeded

def test_pkg_iperf3(host):
    """Check that the iperf3 package is available on the host"""
    cmd = host.run("iperf3 --version")
    assert cmd.succeeded

def test_pkg_bindutils(host):
    """Check that the bind-utils package is available on the host"""
    cmd = host.run("yum list installed bind-utils")
    assert ("bind-utils" in cmd.stdout)


def test_pip_docker(host):
    """Check that the docker package is available on the host"""
    cmd = host.run("pip3 list | grep docker")
    assert ("docker" in cmd.stdout)

def test_pip_psutil(host):
    """Check that the docker package is available on the host"""
    cmd = host.run("pip3 list | grep psutil")
    assert ("psutil" in cmd.stdout)

def test_pip_pycryptodome(host):
    """Check that the pycryptodome package is available on the host"""
    cmd = host.run("pip3 list | grep pycryptodome")
    assert ("pycryptodome" in cmd.stdout)

def test_user_jsimon(host):
    """Check that the user jsimon is in the host"""
    assert host.ansible("user", "name=jsimon state=present")

def test_user_jsimon_pw(host):
    """Check that the user jsimon has a password set"""
    with host.sudo():   
        assert (len(host.user("jsimon").password)>10)

def test_user_jsimon_sshkey(host):
    """Check that the user jsimon has SSH privatekeys"""
    with host.sudo():   
        assert host.file("/home/jsimon/.ssh/id_rsa_jsimon").exists

def test_user_jsimon_sshkey_pub(host):
    """Check that the user jsimon has SSH privatekeys"""
    with host.sudo():   
        assert host.file("/home/jsimon/.ssh/id_rsa_jsimon.pub").exists

def test_user_tkolesn(host):
    """Check that the user tkolesn is in the host"""
    assert host.ansible("user", "name=tkolesn state=present")

def test_user_tkolesn_pw(host):
    """Check that the user tkolesn has a password set"""
    with host.sudo():   
        assert (len(host.user("tkolesn").password)>10)

def test_user_tkolesn_sshkey(host):
    """Check that the user tkolesn has SSH privatekeys"""
    with host.sudo():   
        assert host.file("/home/tkolesn/.ssh/id_rsa_tkolesn").exists

def test_user_tkolesn_sshkey_pub(host):
    """Check that the user tkolesn has SSH privatekeys"""
    with host.sudo():   
        assert host.file("/home/tkolesn/.ssh/id_rsa_tkolesn.pub").exists

def test_check_permitrootlogin(host):
    """Check if root login is disabled"""
    with host.sudo():
        cmd = host.run("cat /etc/ssh/sshd_config | grep \"PermitRootLogin no\"")
        assert ("PermitRootLogin no" in cmd.stdout)

def test_log_dathena_dtq(host):
    """Check that the file /var/log/dathena/dtq/.keep exists"""
    with host.sudo():   
        assert host.file("/var/log/dathena/dtq/.keep").exists

def test_log_dathena_dpm(host):
    """Check that the file /var/log/dathena/dpm/.keep exists"""
    with host.sudo():   
        assert host.file("/var/log/dathena/dpm/.keep").exists

def test_log_dathena_reporting(host):
    """Check that the file /var/log/dathena/reporting/.keep exists"""
    with host.sudo():   
        assert host.file("/var/log/dathena/reporting/.keep").exists

def test_check_qa_dathena(host):
    """Check if 192.168.1.206 qa.dathena.io exists in /etc/hosts"""
    with host.sudo():
        cmd = host.run("cat /etc/hosts | grep \"qa.dathena.io\"")
        assert ("192.168.1.206" in cmd.stdout)

def test_check_se_dathena(host):
    """Check if 192.168.1.212 se-01.dathena.io exists in /etc/hosts"""
    with host.sudo():
        cmd = host.run("cat /etc/hosts | grep \"se-01.dathena.io\"")
        assert ("192.168.1.212" in cmd.stdout)