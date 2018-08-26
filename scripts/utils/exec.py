import subprocess

def exec_cmd(cmd, timeout: int=60) -> dict:
    """Execute a given command in the shell"""
    ret = {"code": 0}
    try:
        ret["out"] = subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True,
            stderr=subprocess.STDOUT,
            timeout=timeout)
    except subprocess.CalledProcessError as exc:
        ret["code"] = exc.returncode
        ret["out"] = str(exc.output)
    except Exception as exc:
        ret["code"] = 1
        ret["out"] = str(exc)
    return ret
