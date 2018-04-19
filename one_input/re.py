import angr

win =0x400762
suck=0x40076E
addr_main=0x40073B
addr_key =0x601080
addr_scanf=0x40074E
len_key=0x10

def scanf_hook(state):
    return 

def main():
    proj=angr.Project('./g',load_options={'auto_load_libs':False})
    proj.hook(addr_scanf,scanf_hook,length=5)
    state=proj.factory.entry_state()#addr = addr_main)
    bv_key=state.solver.BVS('key',8 * len_key)
    state.memory.store(addr_key,bv_key)
    simgr = proj.factory.simulation_manager(state)
    
    print "start explore:"
    simgr.explore(find=win,avoid=suck)

    print "start eval :"

    if simgr.found:
        find=simgr.found[0]
    else:
        raise Exception("cannt find key :{")
    key = find.solver.eval(bv_key,cast_to=str).strip('\0')
    print key
    return

if __name__ == '__main__':
    main()