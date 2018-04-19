import angr
import monkeyhex
import time
import string

addr_account=0x601060
addr_key    =0x601070

def main():
    proj=angr.Project('./simple_crypt')#,load_options={'auto_load_libs':False})
    state=proj.factory.blank_state(addr = 0x4006C5)#addr=0x4006c9)
    
    bv_account=state.solver.BVS("addr_account", 8*16)
    bv_key    =state.solver.BVS("addr_key",     8*16)
    state.memory.store(addr_account, bv_account)
    state.memory.store(addr_key,     bv_key)
    for i in range(0x10):
        state.add_constraints(
            bv_account.get_byte(i) >= 0,
            bv_key.get_byte(i)     >= 0
        )

    @proj.hook(0x400470)
    def hook_scanf(state):
        pass
    
    sm = proj.factory.simulation_manager(state)
    sm.explore(find=0x400695,avoid=0x4006A1)
    if sm.found:
        find=sm.found[0]
    else :
        raise Exception("angr failed to find a path to the solution :(")
    #solution = state.solver.eval( 
    #    state.memory.load(addr_account, 32), 
    #    cast_to=str
    #    ).rstrip(b'\0').decode('ascii')
    account =find.solver.eval(
        state.memory.load(addr_account, 16),
        cast_to=str
    ).strip('\0')
    key=find.solver.eval(
        state.memory.load(addr_key,16),
        cast_to=str
    ).strip('\0')
    print key
    print account

        #time.sleep(1)
if __name__ == '__main__':
    main()