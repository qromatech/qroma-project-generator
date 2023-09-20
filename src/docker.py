import subprocess


def do_docker_container_cmd(cmd_args: list[str]) -> list[str]:
    docker_command_args: list[str] = ["docker", "container"]
    docker_command_args.extend(cmd_args)

    p = subprocess.run(docker_command_args,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       )

    if p.returncode != 0:
        raise Exception(f"Error running docker command: {p.stdout}")

    result_lines = p.stdout.decode("utf-8").splitlines()
    return result_lines


def docker_container_run(image_name: str, container_name: str, arg_list: list[str]) -> list[str]:
    docker_command_args = ["run", "-i",
                           *arg_list,
                           "--name", container_name,
                           image_name]

    result = do_docker_container_cmd(docker_command_args)
    return result


def docker_container_rm(container_name: str) -> list[str]:
    docker_command_args = ["rm", container_name]
    result = do_docker_container_cmd(docker_command_args)
    return result
