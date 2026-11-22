from gp_ir import (IRCall, IRComment, ExecutionPlan, RuntimeContext, IRExecutor, emit_python, emit_function, wrap_python_script)   

def use_print_statement(INDENT, print_name):
    rv = f"{INDENT}print({print_name})"
    return rv

def use_return_statement(INDENT, print_name):
    res = []
    res.append("{")
    it = 0
    for name in print_name:
        res.append(f"'{name}':{name}")
        if it==len(print_name)-1:
            continue
        res.append(",")
        it+=1
    res.append("}")
    print_name = "".join(res)
    rv = f"{INDENT}return({print_name})"
    return rv

def use_output_statement(INDENT,function_name,print_name):
    print_name = [f"{p}" for p in print_name]
    print_name = ",".join(print_name)
    rv = f"{INDENT}{function_name}({print_name})"
    return rv

def create_script(INDENT,function_name,args,out_args,rest_functionality_string,do_you_want_to_print):
    NEWLINE = "\n"
    results = []
    fn = emit_function(ir_nodes = [], name = function_name, args = args[:-1])
    results += [fn]
    results += [rest_functionality_string]
    rv = use_return_statement(INDENT, args)
    results += [rv]
    results += [NEWLINE]
    results += [f"if __name__ == \"__main__\":"]
    rv = use_output_statement("",function_name,out_args)
    results += [f"{INDENT}out = {rv}"]
    if do_you_want_to_print==True:
        results+=[f"{INDENT}print(out)"]
    return results

def print_script(results):
    for res in results:
        print(res)
    
def create_scripts(INDENT,function_name,args,out_args,rest_functionality_string,how_many_scripts_to_create):
    do_you_want_to_print = False
    rvs = []
    for i in range(1,how_many_scripts_to_create + 1):
        rvs+=[create_script(INDENT,function_name,args,out_args,rest_functionality_string,do_you_want_to_print)]
    return rvs

if __name__=="__main__":

    INDENT= "    "
    function_name = "luffy"
    args = ["a","b","rv"]
    out_args  = [1,10]
    rest_functionality_string = f"{INDENT}{args[len(args)-1]} = a + b"
    do_you_want_to_print = True
    results = create_script(INDENT,function_name,args,out_args,rest_functionality_string,do_you_want_to_print)
    print_script(results)
    how_many_scripts_to_create = 1000_000
    NEWLINE = "\n"
    total_scripts = create_scripts(INDENT,function_name,args,out_args,rest_functionality_string,how_many_scripts_to_create)
    print(NEWLINE)
    print(f"total scripts generated :-")
    print(len(total_scripts))
