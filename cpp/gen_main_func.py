

main_func = '''
#include <iostream>
#include <string>

int main(int argv, char *args[])
{
    // add code here.

    return 0;
}
'''

def gen_main_func(setting, fp):
    if fp:
        fp.write(main_func)
        fp.close()


if __name__=="__main__":
    import sys
    gen_main_func(None, sys.stdout)
