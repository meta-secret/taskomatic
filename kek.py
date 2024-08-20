import kcl_lib.plugin as plugin
import kcl_lib.api as api
import subprocess

def f(x, y):
    print("kakaxa")
    subprocess.run(["ls", "-l"])
    return x + y

actions = {
    "add": f
}
plugin.register_plugin("my_plugin", actions)

def main():
    result = api.API().exec_program(
        api.ExecProgram_Args(k_filename_list=["main.k"])
    )
    assert result.yaml_result == "result: 2"
    print(result)

main()